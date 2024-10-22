import streamlit as st
import requests
import time


@st.dialog('Delete Worker')
def delete_worker(worker):
    st.warning('Are you sure about deleting this worker? This will delete all tasks and comments related to this '
               'worker!')
    war_col1, war_col2 = st.columns(2)
    if war_col1.button(':red[Yes]', use_container_width=True):
        response_delete = requests.delete(f'http://127.0.0.1:8000/app/workers/{worker.get('worker_id')}/')
        if response_delete.status_code == 204:
            st.toast(':green[Worker deleted]')
            time.sleep(1)
            st.rerun()
        else:
            st.toast(':red[There was an error while deleting worker]')
    if war_col2.button(':green[No]', use_container_width=True):
        st.rerun()


@st.dialog('Edit Worker')
def edit_worker(worker):
    name = st.text_input('Name', worker.get('name'))
    surname = st.text_input('Surname', worker.get('surname'))
    email = st.text_input('Email', worker.get('email'))

    war_col1, war_col2 = st.columns(2)
    if war_col1.button(':green[Submit]', use_container_width=True):
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

    if war_col2.button(':red[Cancel]', use_container_width=True):
        st.rerun()
