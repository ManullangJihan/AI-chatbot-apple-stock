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


def stream_data(text, delay:float=0.02):
    for word in text.split():
        yield word + " "
        time.sleep(delay)

def main():
    prompt = st.chat_input("Ask me Anything")

    if prompt:
        with st.chat_message("user"):
            st.write(prompt)
        
        with st.spinner("Thinking ..."):
            result = agent.chat(prompt)
            result_text = result.text if hasattr(result, 'text') else str(result)
            st.write_stream(stream_data(result_text))

if __name__ == "__main__":
    main()