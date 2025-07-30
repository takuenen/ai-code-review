from utils import get_chat_completion, get_llm

def build_review_prompt(code, language):
    return f"""
你是一位经验丰富的高级代码审查专家，请根据以下目标严格审查代码，并用中日双语给出反馈：
1. 找出代码中的问题（命名、注释、结构、逻辑、可维护性）
2. 指出原因（为什么不好）
3. 提供改进建议（怎么做更好）
4. 对代码整体给出评分（A/B/C）
5. 请只输出中日双语建议和评分，格式清晰。

语言：{language}
代码：
{code}
"""

def run_code_review(code, language):
    llm = get_llm()
    prompt = build_review_prompt(code, language)
    return get_chat_completion(llm, prompt)
