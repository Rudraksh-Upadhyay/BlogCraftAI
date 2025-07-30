import streamlit as st 
import google.generativeai as genai
from dotenv import load_dotenv
import os


load_dotenv()

try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except KeyError:
    api_key = os.getenv("GOOGLE_API_KEY")
    
if not api_key:
    st.error("Google API Key not found. Please set it as a secret in Streamlit Cloud (GOOGLE_API_KEY) or in your local .env file.")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

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
                    response = model.generate_content(prompt)
                    
                    #display kaise krenge
                    # st.subheader("Your Generated Blog Post:")
                    # st.write(response.text)
                    st.session_state['generated_blog'] = response.text
                
                except Exception as e:
                    # st.error(f"An error occurred: {e}")
                    st.session_state['generation_error'] = f"An error occurred: {e}"
        else:
            st.warning("Please enter a blog topic and keywords.")
    
st.markdown("-----")
st.subheader("Your Generated Blog Post:")
st.write(st.session_state['generated_blog'] if 'generated_blog' in st.session_state else "")
st.markdown("-----")