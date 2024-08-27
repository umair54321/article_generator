import os
# from anthropic import Anthropic
import openai
import google.generativeai as genai

import streamlit as st


from dotenv import load_dotenv

load_dotenv()


# Initialize OpenAI API key
# openai.api_key = os.getenv("OPEN_AI_API_KEY")


def generate_article_with_openai(topic, word_count, tone, language):
    prompt = f"Write a {tone} article on '{topic}' in {language} with around {word_count} words."
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=word_count
    )
    
    return response.choices[0].text.strip()

# Initialize GEMINI API key
# gemini_api_key = os.getenv("GEMINI_API_KEY")
api_key = st.secrets["claude_api_key"]
genai.configure(api_key=api_key)

def generate_article_with_Gemini(topic, word_count, tone, language):
    prompt = f"Write a {tone} article on '{topic}' in {language} with around {word_count} words."
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    
    return response.text

st.sidebar.title("Article Generator Settings")

topic = st.sidebar.text_input("Enter the Topic:")
word_count = st.sidebar.slider("Word Count", 100, 2000, 500)
tone = st.sidebar.selectbox("Select Tone", ["Formal", "Casual", "Technical"])
language = st.sidebar.selectbox("Select Language", ["English", "Urdu", "Hindi","French","Arabic","Chinese"])

generate_button = st.sidebar.button("Generate Article")


st.title("AI-Powered Article Generator")
st.write("Generate high-quality articles with just a few clicks!")

if generate_button:
    if topic:
        st.subheader(f"Generating Article on: {topic}")
        st.write(f"**Word Count:** {word_count}")
        st.write(f"**Tone:** {tone}")
        st.write(f"**Language:** {language}")

        # Placeholder for the article generation logic
        article =generate_article_with_Gemini(topic, word_count, tone, language)
        st.write(article)
    else:
        st.error("Please enter a topic to generate an article.")
