import React from "react";
import { Box, Text, Flex, Spinner } from "@chakra-ui/react";
import Plotly from 'plotly.js-dist';
import createPlotlyComponent from 'react-plotly.js/factory';

import type { ChatInterface } from "../Interfaces/ChatInterface"

const UserMessage: React.FC<ChatInterface> = ({ role, content }) => {
    return (
        <Box
            marginLeft="20%"
            padding="15px"
            marginTop="10px"
            border="1px solid gray"
            background="#d8a953ff"
            minHeight="40px"
            rounded="md"
        >
            <Text>{content}</Text>
        </Box>
    )
}

const AssistantMessage: React.FC<ChatInterface> = ({ role, content }) => {
    return (
        <Box
            marginRight="20%"
            padding="15px"
            marginTop="10px"
            border="1px solid gray"
            background="#53acd8ff"
            minHeight="40px"
            rounded="md"
        >
            <Text>{content}</Text>
        </Box>
    )
}

const Chart: React.FC<ChatInterface> = ({role, content}) => {
    const Plot = createPlotlyComponent(Plotly);
    const plotInput = JSON.parse(content);
    return (
        <Flex justify='center' width='100%'>
            <Plot 
                data={plotInput.data}
                layout={plotInput.layout}
                style={{width:'94%',  marginTop:'10px', height:'600px'}}
            />
        </Flex>
    )
}

const MessageLoading = () => {
    return (
        <Box 
            marginRight="60%"
            marginTop="10px"
            padding="15px"
            border="1px solid gray"
            background="#53acd8ff"
            minHeight="40px"
            rounded="md"
        >
            <Flex justify='center'>
                <Spinner size="md"/>
            </Flex>
        </Box>
    )
}


const ChatMessage: React.FC<ChatInterface> = ({ role, content }) => {
    let component = <></>
    switch(role) {
        case "user":
            component = <UserMessage role={role} content={content}/>;
            break;
        case "chart":
            component = <Chart role={role} content={content}/>;
            break;
        case "loading":
            component = <MessageLoading/>;
            break;
        default:
            component = <AssistantMessage role={role} content={content}/>;
            break;
    }
    return (
        component
    )
}

export default ChatMessage;
