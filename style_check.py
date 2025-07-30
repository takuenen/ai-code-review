from utils import run_pylint, run_checkstyle, get_chat_completion, get_llm

def analyze_style(code, language):
    llm = get_llm()
    if language == "Python":
        pylint_report = run_pylint(code)
        prompt = f"""
根据下面的Pylint报告，结合代码风格最佳实践，请用中日双语指出代码风格和命名规范的问题及改进建议：

Pylint报告：
{pylint_report}
"""
    else:
        checkstyle_report = run_checkstyle(code)
        prompt = f"""
根据下面的Checkstyle报告，结合代码风格最佳实践，请用中日双语指出代码风格和命名规范的问题及改进建议：

Checkstyle报告：
{checkstyle_report}
"""
    return get_chat_completion(llm, prompt)
