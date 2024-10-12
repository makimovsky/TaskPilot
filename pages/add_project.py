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
    owners = requests.get('http://127.0.0.1:8000/app/workers/').json()
    owner_emails = []
    for owner in owners:
        owner_emails.append(f'{owner['name']} {owner['surname']} ({owner['email']})')
    owner = st.selectbox('Owner', owner_emails)

    clients = requests.get('http://127.0.0.1:8000/app/clients/').json()
    client_emails = []
    for client in clients:
        client_emails.append(f'{client['name']} ({client['email']})')
    client = st.selectbox('Client', client_emails)

    start_date = st.date_input('Start Date')
    end_date = st.date_input('End Date')

    st.markdown('')
    submit = st.form_submit_button(':blue[Add project]')

    if submit:
        data = {
            'name': name,
            'description': description,
            'owner': owner.split('(')[1][:-1],
            'client': client.split('(')[0][:-1],
            'start_date': start_date.isoformat(),
            'end_date': end_date.isoformat()
        }

        response = requests.post('http://127.0.0.1:8000/app/projects/', json=data)
        if response.status_code == 201:
            st.toast(':green[New project added]')
            time.sleep(2)
            st.switch_page('taskpilot_app.py')
        else:
            st.toast(':red[There was an error while creating project]')
