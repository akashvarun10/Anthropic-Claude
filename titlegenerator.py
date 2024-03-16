from dotenv import load_dotenv 
import anthropic
import streamlit as st

load_dotenv()

def get_claude_response(user_input): 
    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        system="Generate 5 attention-grabbing blog titles based on user-provived keywords",
        messages=[{"role":"user", "content":user_input}],
    )
    return response.content[0].text

st.title("Claude 3 Blog Title Generator")
user_input = st.text_input("Enter the keyword for blog titles:")

if st.button("Generate Titles"):
    if not user_input:
        st.warning("Please enter a keyword before generating titles.", icon = "⚠️")
    generated_titles = get_claude_response(user_input)
    st.success("Titles generated successfully!")
    st.text_area("", value=generated_titles, height=300)




