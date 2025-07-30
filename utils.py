import os
from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
import subprocess
import json

def load_env():
    load_dotenv()
    return os.getenv("AZURE_OPENAI_API_KEY") is not None

def get_llm():
    return AzureChatOpenAI(
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_CHAT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        temperature=0.3
    )

def get_chat_completion(llm, prompt: str) -> str:
    try:
        messages = [
            SystemMessage(content="你是一位严格但友善的代码审查专家"),
            HumanMessage(content=prompt)
        ]
        response = llm.invoke(messages)
        return response.content
    except Exception as e:
        return f"❌ 调用失败：{str(e)}"

def run_pylint(code: str, filename="temp.py") -> str:
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)
    result = subprocess.run(
        ["pylint", filename, "--disable=all", "--enable=C,R,W,E"], capture_output=True, text=True
    )
    return result.stdout

def run_checkstyle(code: str, filename="Temp.java") -> str:
    return "Checkstyle report placeholder"

def get_language_code(language):
    return "python" if language == "Python" else "java"

def get_learning_resources(language):
    if language == "Python":
        return (
            "- [PEP8 官方文档](https://peps.python.org/pep-0008/)\n"
            "- [Python 基础练习](https://www.w3resource.com/python-exercises/)\n"
            "- [Python 入门教程](https://docs.python.org/zh-cn/3/tutorial/index.html)\n"
            "- [Python 官方编程练习](https://www.learnpython.org/)\n"
        )
    elif language == "Java":
        return (
            "- [Java 命名规范](https://www.oracle.com/java/technologies/javase/codeconventions-namingconventions.html)\n"
            "- [Java 编程练习](https://www.w3resource.com/java-exercises/)\n"
            "- [Java 官方教程](https://docs.oracle.com/javase/tutorial/)\n"
            "- [Codecademy Java 课程](https://www.codecademy.com/learn/learn-java)\n"
        )
    else:
        return ""
