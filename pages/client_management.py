import streamlit as st
import requests
import time


@st.dialog('Delete Client')
def delete_client(client):
    st.warning('Are you sure about deleting this client?')
    if st.button(':red[Yes]'):
        response_delete = requests.delete(f'http://127.0.0.1:8000/app/clients/{client.get('client_id')}/')
        if response_delete.status_code == 204:
            st.toast(':green[Client deleted]')
            time.sleep(1)
            st.rerun()
        else:
            st.toast(':red[There was an error while deleting client]')
    if st.button(':green[No]'):
        st.rerun()


@st.dialog('Edit Client')
def edit_client(client):
    name = st.text_input('Name', client.get('name'))
    email = st.text_input('Email', client.get('email'))

    if st.button(':green[Submit]'):
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

    if st.button(':red[Cancel]'):
        st.rerun()
