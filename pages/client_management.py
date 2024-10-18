import streamlit as st
import requests
import time


@st.dialog('Delete Client')
def delete_client(client):
    st.warning('Are you sure about deleting this client? This will delete all projects related to this client!')
    war_col1, war_col2 = st.columns(2)
    if war_col1.button(':red[Yes]', use_container_width=True):
        response_delete = requests.delete(f'http://127.0.0.1:8000/app/clients/{client.get('client_id')}/')
        if response_delete.status_code == 204:
            st.toast(':green[Client deleted]')
            time.sleep(1)
            st.rerun()
        else:
            st.toast(':red[There was an error while deleting client]')
    if war_col2.button(':green[No]', use_container_width=True):
        st.rerun()


@st.dialog('Edit Client')
def edit_client(client):
    name = st.text_input('Name', client.get('name'))
    email = st.text_input('Email', client.get('email'))

    war_col1, war_col2 = st.columns(2)
    if war_col1.button(':green[Submit]', use_container_width=True):
        data = {
            'name': name,
            'email': email
        }

        response_put = requests.put(f'http://127.0.0.1:8000/app/clients/{client.get('client_id')}/', json=data)
        if response_put.status_code == 200:
            st.toast(':green[Client updated]')
            time.sleep(1)
            st.rerun()
        else:
            st.toast(':red[There was an error while updating client]')

    if war_col2.button(':red[Cancel]', use_container_width=True):
        st.rerun()
