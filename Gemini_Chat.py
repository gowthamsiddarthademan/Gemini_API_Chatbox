#for bard api you need to go to bard website and take the Secure-1PSID (bard website ->inspect->applications->cookies->Secure-1PSID)

from bardapi import Bard
import streamlit as st
from streamlit_chat import message 
import os

os.environ["_BARD_API_KEY"] = "bQiG3qgqgH_5BN2cHb9HP0oe-D-Aw5t9SWzJl-kq16JRfcO5TXZ-8d8wEYp_daiM0avm4A."

#message = input("enter your prompt:")

#print(Bard().get_answer(str(message))['content'])

st.title("Gowtham AI")

def response_api(promot):
    message=Bard().get_answer(str(promot))['content']
    return message

def user_input():
    input_text = st.text_input("Enter Your Prompt: ")
    return input_text

if 'generate' not in st.session_state:
    st.session_state['generate']=[]
if 'past' not in st.session_state:
    st.session_state['past']=[]
    
user_text = user_input()

if user_text:
    output = response_api(user_text)
    st.session_state.generate.append(output)
    st.session_state.past.append(user_text)
    

if st.session_state['generate']:
    
    for i in range(len(st.session_state['generate'])-1,-1,-1):
        message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generate"][i], key=str(i))
        
#use streamlit run bard.py for runnig the code