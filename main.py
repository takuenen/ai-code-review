import streamlit as st
from utils import load_env, get_language_code
from review import run_code_review
from comment_gen import generate_comment
from similar_code import recommend_similar_code

# 环境变量加载
if not load_env():
    st.error("环境变量加载失败，请检查 .env 文件！")
    st.stop()

# 页面配置
st.set_page_config(page_title="CodeSensei AI代码审查", layout="wide")
st.title("🤖 CodeSensei｜AI 代码审查工具（中日双语）")

st.markdown("让 AI 帮你发现代码问题，提升代码质量 🚀")

# 初始化 session_state
if "review_result" not in st.session_state:
    st.session_state.review_result = ""
if "comment_result" not in st.session_state:
    st.session_state.comment_result = ""
if "similar_code_result" not in st.session_state:
    st.session_state.similar_code_result = ""
if "learning_links" not in st.session_state:
    st.session_state.learning_links = ""

# 输入区域
code_input = st.text_area("📥 请输入代码", height=300, placeholder="粘贴 Python 或 Java 代码...")
language = st.selectbox("🧪 选择语言", ["Python", "Java"])

st.header("🌐 选择功能模块")
col1, col2, col3 = st.columns(3)

# 按钮功能块
def handle_review():
    if not code_input.strip():
        st.warning("请输入代码内容！")
        return
    with st.spinner("AI 正在审查中，请稍候..."):
        try:
            st.session_state.review_result = run_code_review(code_input, language)
            st.session_state.learning_links = generate_learning_resources(language)
        except Exception as e:
            st.error(f"审查失败: {e}")
            st.session_state.review_result = ""
            st.session_state.learning_links = ""

def handle_comment():
    if not code_input.strip():
        st.warning("请输入代码内容！")
        return
    with st.spinner("AI 正在生成注释..."):
        try:
            st.session_state.comment_result = generate_comment(code_input, language)
        except Exception as e:
            st.error(f"注释生成失败: {e}")
            st.session_state.comment_result = ""

def handle_similar_code():
    if not code_input.strip():
        st.warning("请输入查询代码片段！")
        return
    with st.spinner("AI 正在检索相似代码..."):
        try:
            st.session_state.similar_code_result = recommend_similar_code(code_input)
        except Exception as e:
            st.error(f"相似代码推荐失败: {e}")
            st.session_state.similar_code_result = ""

def generate_learning_resources(language):
    if language == "Python":
        return "- [PEP8 官方文档](https://peps.python.org/pep-0008/)\n- [Python 基础练习](https://www.w3resource.com/python-exercises/)"
    elif language == "Java":
        return "- [Java 命名规范](https://www.oracle.com/java/technologies/javase/codeconventions-namingconventions.html)\n- [Java 编程练习](https://www.w3resource.com/java-exercises/)"
    else:
        return ""

with col1:
    if st.button("🚀 AI审查建议"):
        handle_review()
with col2:
    if st.button("✍️ 自动注释生成"):
        handle_comment()
with col3:
    if st.button("🔍 相似代码推荐"):
        handle_similar_code()

# 结果展示
st.header("🗒️ 结果展示区域")

if st.session_state.review_result:
    st.markdown("### 审查建议（中日双语）")
    st.markdown(st.session_state.review_result)
    if st.session_state.learning_links:
        st.markdown("### 新手学习参考")
        st.markdown(st.session_state.learning_links)

if st.session_state.comment_result:
    st.markdown("### 自动注释")
    st.code(st.session_state.comment_result, language=get_language_code(language))

if st.session_state.similar_code_result:
    st.markdown("### 相似代码推荐")
    st.code(st.session_state.similar_code_result, language=get_language_code(language))
