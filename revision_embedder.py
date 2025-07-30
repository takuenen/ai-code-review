# revision_embedder.py

import os
from typing import List
from langchain.docstore.document import Document
from langchain_community.vectorstores import Chroma
from langchain_openai import AzureOpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# 👉 环境变量
VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "./vector_store")

# ✅ 函数：生成 Document 列表
def build_revision_documents(files: List, descriptions: List[str]) -> List[Document]:
    docs = []
    for file, desc in zip(files, descriptions):
        content = file.read().decode("utf-8")
        doc = Document(
            page_content=f"""【版本说明】{desc}
【代码内容】
{content}
""",
            metadata={
                "filename": file.name,
                "revision_desc": desc
            }
        )
        docs.append(doc)
    return docs

# ✅ 函数：向量化并写入 Chroma 向量数据库
def embed_documents_into_chroma(documents: List[Document]):
    embedding_model = AzureOpenAIEmbeddings(
        deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_EMBEDDING"),
        openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        openai_api_base=os.getenv("AZURE_OPENAI_ENDPOINT"),
        openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION")
    )

    db = Chroma.from_documents(
        documents=documents,
        embedding=embedding_model,
        persist_directory=VECTOR_DB_PATH
    )
    db.persist()
    return db
