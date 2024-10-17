import streamlit as st
import requests
import time


@st.dialog('Delete Worker')
def delete_worker(worker):
    st.warning('Are you sure about deleting this worker?')
    if st.button(':red[Yes]'):
        response_delete = requests.delete(f'http://127.0.0.1:8000/app/workers/{worker.get('worker_id')}/')
        if response_delete.status_code == 204:
            st.toast(':green[Worker deleted]')
            time.sleep(1)
            st.rerun()
        else:
            st.toast(':red[There was an error while deleting worker]')
    if st.button(':green[No]'):
        st.rerun()


@st.dialog('Edit Worker')
def edit_worker(worker):
    name = st.text_input('Name', worker.get('name'))
    surname = st.text_input('Surname', worker.get('surname'))
    email = st.text_input('Email', worker.get('email'))

    if st.button(':green[Submit]'):
        data = {
            'name': name,
            'surname': surname,
            'email': email
        }

        response_put = requests.put(f'http://127.0.0.1:8000/app/workers/{worker.get('worker_id')}/', json=data)
        if response_put.status_code == 200:
            st.toast(':green[Worker updated]')
            time.sleep(1)
            st.rerun()
        else:
            st.toast(':red[There was an error while updating worker]')

    if st.button(':red[Cancel]'):
        st.rerun()
