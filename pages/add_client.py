import time
import streamlit as st
import requests

st.set_page_config('TaskPilot - Add Client', page_icon="💼")

st.markdown("""
<style>
.add-client {
    font-size:100px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<center><p class="add-client">Add Client</p></center>', unsafe_allow_html=True)

with st.form(':blue[Add client]'):
    name = st.text_input('Name')
    email = st.text_input('Email')

    st.markdown('')
    submit = st.form_submit_button(':blue[Add client]')

    if submit:
        data = {
            'name': name,
            'email': email
        }

        response = requests.post('http://127.0.0.1:8000/app/clients/', json=data)
        if response.status_code == 201:
            st.toast(':green[New client added]')
            time.sleep(2)
            st.switch_page('taskpilot_app.py')
        else:
            st.toast(':red[There was an error while creating client]')
