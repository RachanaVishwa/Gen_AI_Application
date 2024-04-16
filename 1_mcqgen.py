import streamlit as st
import google.generativeai as genai

genai.configure(api_key="API_KEY")

st.snow()
st.title("💬AI MCQ Generator")
st.subheader("MCQ Generating bot using Gemini AI🤖")


model = genai.GenerativeModel('gemini-pro')

# User input
topic = st.text_input("Please enter the Data Science Topic...")


if st.button("Generate"):
    st.balloons()
    # System Instructions
    system_role = """You are a friendly AI Assistant who has very good knowledge about Data Science.
                     You are given with a Data Science topic, your job is to generate 3 data science MCQ questions and answers for MCQ test."""

    prompt = f"{system_role} {topic}"
    response = model.generate_content(prompt)


    # Prompt for the model
    prompt = f"{system_role} {topic}"

    # Generate content
    response = model.generate_content(prompt)

    # Check if response is not None
    if response:
        # Extract and display the generated content
        content = response.candidates[0].content.parts[0].text
        st.write(content)
    else:
        st.write("No response received. Please try again.")


        
    





