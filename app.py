import streamlit as st 
# import google.generativeai as genai
from dotenv import load_dotenv
import os


import requests

load_dotenv()

EURON_API_KEY = os.getenv("EURON_API_KEY")


def generate_completion(content):
    url = "https://api.euron.one/api/v1/euri/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {EURON_API_KEY}"
    }
    payload = {
        "messages": [
            {
                "role": "user",
                "content": content
            }
        ],
        "model": "gpt-4.1-nano",
        "max_tokens": 1000,
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    # print(data)
    return data

# generate_completion()
# df = load_dotenv()
# load_dotenv()

# genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))

# model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(layout="wide")

#title
st.title("✍🌝 BlogCraft: Your AI Writing Companion")

st.subheader("Now you can craft your perfect blogs with the help of AI")

with st.sidebar:
    st.title("Input your blog details")
    st.subheader("Enter details of blog you want to generate:")
    
    blog_title=st.text_input("Blog Title")
    keywords = st.text_area("Keywords (comma separated)")
    num_of_words = st.slider("Number of words", min_value=200, max_value=1000, step=100)
    # num_of_imgs = st.slider("Number of images", min_value=1, max_value=5, step=1)
    
    # submit_btn = st.button("Generate Blog")
    if st.button("Generate Blog Post"):
        if blog_title and keywords:
            
            #use krenge STREAMLIT'S SESSION STATE to store data
            st.session_state['generated_blog'] = ""
            st.session_state['generation_error'] = None
            
            with st.spinner("Generating your blog post..."):
                
                prompt = f"Generate a comprehensive, engaging blog post relevant to the given title '{blog_title}' including the keywords '{keywords}' and with a target length of {num_of_words} words. This should be suitable for an online audience. Ensure the content is engaging, informative, original, unique, humanized and maintains a consistent tone throughout"
                
                try:
                    # response = model.generate_content(prompt)
                    response = generate_completion(prompt)
                    generated_text  = response.get("choices", [{}])[0].get("message", {}).get("content", "")
                    #display kaise krenge
                    # st.subheader("Your Generated Blog Post:")
                    # st.write(response.text)
                    st.session_state['generated_blog'] = generated_text
                
                except Exception as e:
                    # st.error(f"An error occurred: {e}")
                    st.session_state['generation_error'] = f"An error occurred: {e}"
        else:
            st.warning("Please enter a blog topic and keywords.")
    
st.markdown("-----")
st.subheader("Your Generated Blog Post:")
st.write(st.session_state['generated_blog'] if 'generated_blog' in st.session_state else "")
st.markdown("-----")