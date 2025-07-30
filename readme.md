✍🌝 BlogCraft: Your AI Writing Companion
Project Overview
BlogCraft is a Streamlit-based web application that leverages Google's Gemini AI model to help users generate engaging and comprehensive blog posts. Simply provide a blog title and relevant keywords, and BlogCraft will craft a unique, humanized, and informative article for you.

This project demonstrates the power of generative AI for content creation and provides a user-friendly interface for interacting with large language models.

Features
AI-Powered Text Generation: Utilizes Google Gemini's gemini-1.5-flash model to generate high-quality blog post content.

Customizable Length: Users can specify the desired word count for the generated blog post using a slider.

Keyword Integration: Incorporates user-provided keywords into the blog content for better relevance.

User-Friendly Interface: Built with Streamlit for an intuitive and interactive web application experience.

Responsive Design: Adapts to various screen sizes for a seamless experience on desktop and mobile.

Demo
Experience BlogCraft live! Click the link below to try it out:

Live Demo Link: https://blogcraftai-001.streamlit.app/



Technologies Used
Frontend: Streamlit (Python framework for web apps)

Backend/AI: Google Gemini API (google-generativeai Python library)

Environment Management: python-dotenv

Deployment: Streamlit

Getting Started
Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
Python 3.9+ installed on your system.

pip (Python package installer).

A Google Gemini API Key (obtainable for free from Google AI Studio).

Installation
Clone the repository:

git clone https://github.com/YOUR_USERNAME/AI-Blog-Companion.git
cd AI-Blog-Companion

(Replace YOUR_USERNAME with your GitHub username and AI-Blog-Companion with your repository name if different).

Create and activate a virtual environment:

macOS/Linux:

python -m venv venv
source venv/bin/activate

Windows (Command Prompt):

python -m venv venv
venv\Scripts\activate.bat

Windows (PowerShell):

python -m venv venv
.\venv\Scripts\Activate.ps1

Install the required Python packages:

pip install -r requirements.txt

Set up your Google Gemini API Key:

Create a file named .env in the root of your project directory.

Add your Gemini API key to this file in the following format:

GOOGLE_API_KEY='YOUR_ACTUAL_GEMINI_API_KEY'

(Replace YOUR_ACTUAL_GEMINI_API_KEY with the key you obtained from Google AI Studio).

Running the Application Locally
Once the setup is complete, you can run the Streamlit application:

streamlit run app.py

This will open the application in your default web browser, usually at http://localhost:8501.

Usage
Enter Blog Details: In the sidebar, fill in the Blog Title and Keywords (comma-separated).

Adjust Word Count: Use the slider to set your desired number of words for the blog post.

Generate Blog Post: Click the "Generate Blog Post" button.

View Results: The generated blog post will appear in the main content area of the application.

Future Enhancements
Image Generation Integration: Implement a free image generation API (e.g., a Stable Diffusion variant with a free tier) to automatically generate images based on the blog title.

Blog Post Editing: Add functionality for users to edit the generated text directly within the application.

Export Options: Allow users to export the generated blog post to various formats (e.g., Markdown, PDF, HTML).

Topic Suggestions: Implement AI-powered topic suggestions based on user interests or trending topics.

Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please feel free to:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeature).

Make your changes.

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature/YourFeature).

Open a Pull Request.

License
This project is open-source and available under the MIT License.