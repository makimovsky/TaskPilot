import time
import streamlit as st
import requests

st.set_page_config('TaskPilot - Add Worker', page_icon="💼")

st.markdown("""
<style>
.add-worker {
    font-size:100px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<center><p class="add-worker">Add Worker</p></center>', unsafe_allow_html=True)

with st.form(':blue[Add worker]'):
    name = st.text_input('Name')
    surname = st.text_input('Surname')
    email = st.text_input('Email')

    st.markdown('')
    submit = st.form_submit_button(':blue[Add worker]')

    if submit:
        data = {
            'name': name,
            'surname': surname,
            'email': email
        }

        response = requests.post('http://127.0.0.1:8000/app/workers/', json=data)
        if response.status_code == 201:
            st.toast(':green[New worker added]')
            time.sleep(2)
            st.switch_page('taskpilot_app.py')
        else:
            st.toast(':red[There was an error while creating worker]')
