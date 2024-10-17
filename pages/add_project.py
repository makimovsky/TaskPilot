import time
import streamlit as st
import requests

st.set_page_config('TaskPilot - Add Project', page_icon="💼")

st.markdown("""
<style>
.add-project {
    font-size:100px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<center><p class="add-project">Add Project</p></center>', unsafe_allow_html=True)

with st.form(':blue[Add project]'):
    name = st.text_input('Name')
    description = st.text_input('Description')
    clients = requests.get('http://127.0.0.1:8000/app/clients/').json()
    clients_emails = {}
    for client in clients:
        clients_emails[f'{client.get('name')} ({client.get('email')})'] = client.get('client_id')
    client = st.selectbox('Client', clients_emails.keys())

    st.markdown('')
    submit = st.form_submit_button(':blue[Add project]')

    if submit:
        data = {
            'name': name,
            'description': description,
            'client': clients_emails.get(client),
        }

        response = requests.post('http://127.0.0.1:8000/app/projects/', json=data)
        if response.status_code == 201:
            st.toast(':green[New project added]')
            time.sleep(2)
            st.switch_page('taskpilot_app.py')
        else:
            st.toast(':red[There was an error while creating project]')
