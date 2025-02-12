import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant designed by laavanjan. Please respond to the question asked"),
        ("user","Question:{question}")
    ]
)

## streamlit framework
st.title("Langchain Demo With Gemma2b Model")
input_text=st.text_input("What question you have in mind?")


## Ollama Llama2 model
llm=Ollama(model="gemma:2b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))

custom_footer = """
    <style>
    .footer {
        position: scroll;
        bottom: 0;
        width: 100%;
        background-color: black;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        color: white;
        border:2px solid white;
        border-radius:10px;
    }
    </style>
    <div class="footer">
        Developed by <b>Laavanjan</b> | © Faculty of IT B22
    </div>
"""
st.markdown(custom_footer, unsafe_allow_html=True)
