from utils import get_chat_completion, get_llm

def build_comment_prompt(code, language):
    return f"""
请为以下{language}函数生成合适的注释。
- Python请使用Docstring格式
- Java请使用JavaDoc格式
- 注释需用中日双语输出

代码如下：
{code}
"""

def generate_comment(code, language):
    llm = get_llm()
    prompt = build_comment_prompt(code, language)
    return get_chat_completion(llm, prompt)
