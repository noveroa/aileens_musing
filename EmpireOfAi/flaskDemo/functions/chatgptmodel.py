"""
Step 5: Deploying the Model

Deployment makes your model accessible for real-world applications through APIs or web interfaces.
Deployment Options:

Vercel: Easy-to-use platform for deploying apps with minimal configuration.
Hugging Face Spaces: Free hosting for machine learning apps using Streamlit or Gradio.
AWS: Scalable cloud platform for deploying models with high availability.

Using flask
Flask is a lightweight framework for creating web APIs. Here’s how to deploy a text generation model with Flask:

"""

from transformers import pipeline

model = pipeline("text-generation", model="gpt2")
