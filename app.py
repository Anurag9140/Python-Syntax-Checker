import streamlit as st

# Function to check Python syntax
def check_syntax(code: str):
    try:
        compile(code, '<string>', 'exec')
        return True, "✅ No syntax errors found. The code is valid.", None
    except SyntaxError as e:
        error_msg = f"Syntax Error at line {e.lineno}: {e.msg}\\n➡️ Code: {e.text.strip() if e.text else 'N/A'}"
        suggestion = suggest_fix(e)
        return False, error_msg, suggestion
    except Exception as e:
        return False, f"⚠️ Unexpected Error: {str(e)}", None

# Suggest fix based on error
def suggest_fix(error):
    msg = error.msg.lower()
    if "unexpected eof" in msg:
        return "Missing closing bracket, parenthesis, or quote."
    elif "eol while scanning string literal" in msg:
        return "String is not properly closed."
    elif "invalid syntax" in msg:
        return "There's likely a typo or structural error."
    elif "expected ':'" in msg:
        return "You might be missing a colon like in 'if', 'for', 'def', etc."
    elif "unexpected indent" in msg:
        return "Check your indentation levels."
    else:
        return "Check the line mentioned for syntax issues."

# Set page configuration
st.set_page_config(page_title="Python Syntax Checker", layout="centered")
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #e0f7fa, #e1bee7);
        font-family: 'Inter', sans-serif;
    }
    .stTextArea > div > textarea {
        background-color: #fce4ec !important;
        color: #4a0072;
        font-family: 'Fira Code', monospace;
        font-size: 14px;
    }
    .css-1aumxhk {
        background-color: #ffffffcc;
        border-radius: 20px;
        padding: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("Python Syntax Checker")

# Upload or paste code
uploaded_file = st.file_uploader(" Upload your .py file", type=["py"])

# Initialize code variable
code_input = ""

if uploaded_file is not None:
    try:
        code_input = uploaded_file.read().decode("utf-8")
        st.success(" File uploaded and code loaded below.")
    except Exception as e:
        st.error(f"Error reading file: {e}")

# Code input area
code_input = st.text_area(" Paste or edit your code below:", value=code_input, height=250)

# Check button
if st.button("✅ Check Syntax"):
    if not code_input.strip():
        st.warning(" No code provided.")
    else:
        valid, result, suggestion = check_syntax(code_input)
        if valid:
            st.success(result)
        else:
            st.error(result)
            if suggestion:
                st.info(f"💡 Suggestion: {suggestion}")
