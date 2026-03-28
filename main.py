import os
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("📊 Regulatory Monitoring Agent (India - EdTech)")

if st.button("Run Weekly Analysis"):
    prompt = """
    Find latest regulatory updates in India related to:
    - UGC
    - AICTE
    - Data Protection (DPDP Act)
    - ASCI

    Then provide:

    1. What changed
    2. Why it matters
    3. What an EdTech company like upGrad should do

    Keep it crisp and actionable.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    st.write(response.choices[0].message.content)
