from llama_index.llms.ollama import Ollama
from llama_index.core.agent import ReActAgent
from stock_reader import stock_reader_func
from dotenv import load_dotenv
from prompts import context

import streamlit as st
import os
import time

load_dotenv()

llm = Ollama(model="mistral-openorca:7b", request_timeout=3600.0)
tools = [stock_reader_func]
agent = ReActAgent.from_tools(tools, llm=llm, verbose=False)

def handle_conversation():
    context = ""
    print("Welcome to the AI Chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = agent.chat(user_input)
        print("Bot: ", result)
        context += f"\nUser: {user_input}\nAI: {result}"

handle_conversation()

if __name__ == "__main__":
    # main()
    handle_conversation()