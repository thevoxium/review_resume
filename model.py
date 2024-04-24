import os
import streamlit as st
from groq import Groq

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"],
)

#Always return a response in JSON format. No additonal response should be there apart from JSON. JSON should have Review, Score, Suggestions, Good, & Bad fields. 

def model_call(prompt, job_role):

    sys_prompt = "You are a career counsellor. Your sole job is to review a resume which will be provided to you. Give the Feedback in extreme detail. Suggest good/bad, improvements to the resume. Score the resume out of 100. Keep the job role in mind. Also give a score breakdown. The use is applying for "+job_role
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": sys_prompt,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        model = "llama3-70b-8192"
    )

    return chat_completion.choices[0].message.content