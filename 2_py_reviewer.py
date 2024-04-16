import streamlit as st
import google.generativeai as genai

# API key
genai.configure(api_key="API_KEY")

# Initialize Generative Model
model = genai.GenerativeModel('gemini-pro')

# System instruction
sys_instruction = '''
You are a friendly AI Code Reviewer who is an expert in Python programming.
You take a Python code as input from the user.
Your job here is to identify potential bugs and provide suggestions for fixes.'''

# Function to review code
def review_code(code):
    prompt = sys_instruction + 'Instruction: Review the following code' + code
    response = model.generate_content(prompt)
    return response

st.snow()
# Title
st.title('💬AI Code Reviewer')

# User Input
st.header('User Input')
code = st.text_area('✍🏻Please Enter your Python code here...✍🏻')
st.button("Review👀")

# Review the code
if st.text_area=='code':
    st.balloons()

    # Generate prompt for the model
    prompt = f"{sys_instruction} {code}"

    # Generate review
    response = review_code(code)

    # Check if response is not None
    if response:
        # Extract and display the generated content
        content = response.candidates[0].content.parts[0].text
        st.write(content)
    else:
        st.write("🔄Please try again.")

else:
    st.write("Please enter your query first")