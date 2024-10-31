import streamlit as st
from send_email import send_email

st.header("Contact me")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address")
    raw_message = st.text_area("Your Message")
    # message = message + "\n" + user_email
    message = f"""
    Subject: Message from {user_email}
    
    From: {user_email}
    
    {raw_message}
    """
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your Email was sent successfully!")
        
        
        
        
