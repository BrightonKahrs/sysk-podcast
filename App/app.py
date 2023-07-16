import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


def main():
    st.set_page_config(page_title="Stuff You Should Know")
    st.header("Ask about the podcast")
    st.write('Welcome to the page')
   
    folder_path = 'Transcripts'
    transcripts = []

    # for filename in os.listdir(folder_path):
    #     if filename.endswith('.txt'):
    file_path = os.path.join(folder_path, 'Playing_Cards_You_Got_That_Right!.mp3.txt')

    with open(file_path, 'r') as file:
        text = file.read()
        transcripts.append(text)

    # split into chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    
    # create embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    knowledge_base = FAISS.from_texts(chunks, embeddings)
    
    # show user input
    user_question = st.text_input("Ask a question about SYSK Playing Cards Episode: ")
    if user_question:
        docs = knowledge_base.similarity_search(user_question)
    
    llm = OpenAI(openai_api_key=OPENAI_API_KEY)
    chain = load_qa_chain(llm, chain_type="stuff")
    with get_openai_callback() as cb:
        response = chain.run(input_documents=docs, question=user_question)
        print(cb)
        
    st.write(response)
    

if __name__ == '__main__':
    main()
