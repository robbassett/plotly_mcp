import axios from 'axios'
const API_URL = "http://127.0.0.1:8000/"

import type { ChatInterface } from '../Interfaces/ChatInterface';

const client = axios.create({
    baseURL: API_URL,
    headers:{
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Content-Type":"application/json",
        "Access-Control-Allow-Origin": "*"
    },
});

export const chatBot = async (messages: ChatInterface[]) => {
    try {
        const response = await client.post("/chat/query", {messages:messages});
        return response.data;
    } catch (e) {
        throw e;
    }
}
