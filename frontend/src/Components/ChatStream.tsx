import { useState, useEffect, useRef } from 'react';
import { Box, Input, Flex, Button } from "@chakra-ui/react";

import { chatBot } from '../api/endpoints';
import ChatMessage from './ChatMessage';
import type { ChatInterface } from '../Interfaces/ChatInterface';

const ChatStream = () => {
    const [messages,setMessages] = useState<ChatInterface[]>([]);
    const [chatStream,setChatStream] = useState<ChatInterface[]>([]);
    const [chatInput,setChatInput] = useState<string>("");
    const [chatSubmitLoading,setChatSubmitLoading] = useState<boolean>(false);
    const messagesContainerRef = useRef<HTMLDivElement>(null);

    const scrollToBottom = () => {
        if (messagesContainerRef.current) {
            messagesContainerRef.current.scrollTop = messagesContainerRef.current.scrollHeight;
        }
    };

    useEffect(() => {
        scrollToBottom();
    }, [chatStream]);


    const handleSubmitMessage = async () => {
        if (chatInput !== "") {
            setChatSubmitLoading(true);
            const new_message: ChatInterface = {
                role:'user',
                content:chatInput
            }
            
            // Add user message to both states
            const updatedChatStream = [...chatStream, new_message];
            const updatedMessages = [...messages, new_message];
            
            // Update states - show user message and placeholder immediately
            setChatStream([...updatedChatStream, {role:"placeholder", content:""}]);
            setMessages(updatedMessages);
            setChatInput('');
            
            try {
                console.log('Sending messages (excluding charts):', updatedMessages)
                let response = await chatBot(updatedMessages);
                
                // Filter out chart messages for the messages state (for future API calls)
                const responseWithoutCharts = response.filter((msg: ChatInterface) => msg.role !== 'chart');
                setMessages(responseWithoutCharts);
                
                // Update chatStream by combining existing chatStream (with charts) + new response
                // The response contains the complete conversation for this turn, so we need to extract just the new messages
                // Find where the new conversation starts in the response (after the user message we just sent)
                const userMessageIndex = response.findIndex((msg: ChatInterface, index: number) => 
                    msg.role === 'user' && msg.content === new_message.content && index >= response.length - 10
                );
                
                if (userMessageIndex !== -1) {
                    // Get only the new messages from this interaction (user message + any new assistant/chart messages)
                    const newMessages = response.slice(userMessageIndex);
                    setChatStream([...chatStream, ...newMessages]);
                } else {
                    // Fallback: append the full response if we can't find the user message
                    setChatStream([...chatStream, ...response]);
                }
                
            } catch (error) {
                console.error('Error submitting chat:', error);
                // Revert chatStream to show user message even if API fails
                setChatStream(updatedChatStream);
            }
            setChatSubmitLoading(false);
        }
    }

    const handleEnterPress = (event: React.KeyboardEvent<HTMLInputElement>) => {
        if (event.key === 'Enter') {
            handleSubmitMessage();
        }
    };

    return (
        <Flex direction="column" height='90vh' width="90vw">
            <Box 
                ref={messagesContainerRef}
                style={{
                    flex: 1,
                    overflow: 'auto', 
                    border:"1px solid black", 
                    borderRadius: 5,
                    marginBottom: '10px'
                }}
            >
                <Flex direction="column" gap="sm" p="10">
                    {chatStream?.map(function(message: ChatInterface, index:number) {
                        return (<ChatMessage key={index} role={message.role} content={message.content}/>)
                    })}
                </Flex>
            </Box>
            
            {/* Input area - fixed at bottom */}
            <Box style={{ flexShrink: 0 }}>
                <Flex gap='5'>
                    <Input
                        placeholder='Enter your prompt...'
                        flex='10'
                        onChange={(e) => setChatInput(e.currentTarget.value)}
                        value={chatInput}
                        onKeyDown={handleEnterPress}
                    />
                    <Button
                        flex='2'
                        onClick={handleSubmitMessage}
                        loading={chatSubmitLoading}
                    >
                        Submit
                    </Button>
                </Flex>
            </Box>
        </Flex>
  );
}


export default ChatStream;
