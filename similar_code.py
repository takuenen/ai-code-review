from utils import get_llm, get_chat_completion
from vector_db import get_vectorstore, query_similar_code

def build_similar_code_prompt(query, similar_codes):
    context = "\n---\n".join(similar_codes)
    return f"""
你是一名资深代码导师，帮忙根据下面查询给出相似代码示例，并用中日双语解释它们的作用和改进点。

查询：
{query}

相似代码示例：
{context}
"""

def recommend_similar_code(query):
    vectordb = get_vectorstore()
    similar_docs = query_similar_code(vectordb, query)
    similar_texts = [doc.page_content for doc in similar_docs]

    llm = get_llm()
    prompt = build_similar_code_prompt(query, similar_texts)
    return get_chat_completion(llm, prompt)
