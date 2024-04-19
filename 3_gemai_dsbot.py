import streamlit as st
import google.generativeai as genai


st.title("🤖Conversational Gem-AI Data Science Tutor")

genai.configure(api_key="api_key")

st.snow()

st.subheader("Ask your Data Science questions and get answers from latest helpful Gem-AI tutor.")

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                            system_instruction="""You are a helpful AI tutor who can answer only Data Science questions and provide explanations and examples where ever required.
                            If the question is not related to Data Science, very politely, inform the user that you are limited to data science related queries only and to ask the question only related to Data Science.""")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []



st.chat_message("ai").write("Hi, My name is Gem-AI. How may I help you?")

chat = model.start_chat(history=st.session_state["chat_history"])

for msg in chat.history:
    st.chat_message(msg.role).write(msg.parts[0].text)

user_prompt = st.chat_input()

if user_prompt:
    st.chat_message("user").write(user_prompt)
    response = chat.send_message(user_prompt)
    st.chat_message("ai").write(response.text)
    st.balloons()
    st.session_state["chat_history"] = chat.history
    


