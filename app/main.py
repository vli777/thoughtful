import re
import streamlit as st
from knowledge import load_knowledge_base, normalize
from classifier import classify_question
from llm_client import generic_fallback


st.title("Thoughtful AI Support Agent")
question = st.text_input("Your question:")

if question:
    kb = load_knowledge_base() 
    user_norm = normalize(question)
    st.write("User asked:", user_norm)    
    
    if user_norm in kb:
        answer = kb[user_norm]
    else:
        match = classify_question(question)
        match_norm = normalize(match)
        
        if match_norm in kb:
            answer = kb[match_norm]
        else:
            answer = generic_fallback(question)

    st.markdown(f"**Answer:** {answer}")