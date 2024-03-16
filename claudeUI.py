import gradio as gr
from dotenv import load_dotenv 
import os 
import anthropic

# Load environment variables
load_dotenv()

# Create Anthropics client
client = anthropic.Anthropic()

# Function to fetch response from Anthropics Claude 3
def fetch_anthropic_response(user_input):
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        system="You are a helpful assistant.",
        messages=[{"role":"user", "content":user_input}],
    )
    return response.content[0].text

# Create Gradio interface
iface = gr.Interface(
    fn=fetch_anthropic_response,
    inputs="text",
    outputs="text",
    title="Anthropic Claude 3 Chatbot",
    description="Claude 3 is an AI chatbot that can help with a question you have in mind, help with writing, and more. Try it out by entering a prompt!"
)

# Launch the interface
iface.launch()
