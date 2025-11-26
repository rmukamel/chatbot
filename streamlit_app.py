import streamlit as st

user_id = st.text_input("Username")

prompt = st.chat_input("Say something")
        
if st.button("Clear chat", type="primary"):
    with open("log",'w') as log:
        pass

if prompt:

    if user_id:
        prompt = user_id +": "+prompt
    else:
        prompt = "Anonymous: "+prompt

    with open("log",'a') as log:
        print(prompt,file=log)

    with open("log",'r') as log:
        for line in log:
            st.write(line)