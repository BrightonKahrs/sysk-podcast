# sysk-podcast repo
Stuff You Should Know Podcast Similarity with LangChain

### Desired Future State Objectives
- Chat with sysk episodes
- Analyze and group semantically similar episodes
- Application to interact with the analysis of the podcast

### Short Term Objectives
- Manually pull in 10 .mp3 files from the SYSK RSS feed
- Use Whisper to convert those to .txt files
- Use LangChain + OpenAI to create embeddings and chat experience using retrieval-augmented generation
- Use Streamlit as lightweight start to application

### TODOs for Desired Future State
- Automate process of pulling in and converting all .mp3 files from the RSS feed
- Speaker diarization of transcripts
- Identify and take out ads of transcripts
- Use automated process for newly created episodes
- Convert streamlit app to web application
- T-SNE visualization of all episodes
- Vector store for embedding chunks
- Convert project to Azure hosting