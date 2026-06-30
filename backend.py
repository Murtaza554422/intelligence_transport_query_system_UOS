import json
import os
from dotenv import load_dotenv


from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from langchain_groq import ChatGroq
from langchain_classic.memory import ConversationBufferMemory
#from langchain.memory import ConversationBufferMemory
#from langchain.chains import ConversationalRetrievalChain
from langchain_classic.chains import ConversationalRetrievalChain
load_dotenv()
def load_text():

    with open(
        "data/knowledge_base.json",
        "r",
        encoding="utf-8"
    ) as f:

        data = json.load(f)

    return data["content"]


def create_vectorstore():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    if os.path.exists(
        "faiss_index/index.faiss"
    ):

        return FAISS.load_local(
            "faiss_index",
            embeddings,
            allow_dangerous_deserialization=True
        )

    text = load_text()

    chunks = []

    chunk_size = 1000

    for i in range(
        0,
        len(text),
        chunk_size
    ):

        chunks.append(
            text[i:i + chunk_size]
        )

    vectorstore = FAISS.from_texts(
        chunks,
        embeddings
    )

    vectorstore.save_local(
        "faiss_index"
    )

    return vectorstore


def get_chain():

    vectorstore = create_vectorstore()

    llm = ChatGroq(
        model_name="llama-3.3-70b-versatile",
        temperature=0,
        api_key=os.getenv("GROQ_API_KEY")
    )

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": 10,
                "fetch_k": 20
            }
        ),
        memory=memory
    )

    return chain