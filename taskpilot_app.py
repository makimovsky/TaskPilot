from pages.project_management import *
import streamlit as st
import requests

st.set_page_config('TaskPilot', page_icon="💼", layout='wide')

st.markdown("""
<style>
.big-font {
    font-size:30px;
}
.app-title {
    font-size:80px;
    font-weight: bold;
}
.author {
    font-size:17px;
    font-weight: bold;
}
.date {
    font-size:12px;
    font-style: italic;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown('<center><p class="app-title">TaskPilot</p></center>', unsafe_allow_html=True)
st.sidebar.header('Choose resource')
resource = st.sidebar.selectbox('Resource', ['Projects', 'Workers', 'Clients'])

if resource == 'Projects':
    project_search = st.text_input('Search Project')
    project_search_by = st.multiselect('Search By', ['name', 'description', 'owner', 'client'],
                                       ['name', 'description', 'owner', 'client'])

    add_project_button = st.button(':green[Add project]')
    if add_project_button:
        st.switch_page('pages/add_project.py')

    projects = requests.get('http://127.0.0.1:8000/app/projects/').json()
    for project in projects:
        if any(project_search in project[field] for field in project_search_by if field in project):
            st.markdown('***')
            st.write(f'<p class="big-font">Project {project.get('project_id')} - {project.get('name')}</p>',
                     unsafe_allow_html=True)
            if st.button(label=':blue[Details]', key=project.get('project_id')):
                show_project(project)

if resource == 'Workers':
    worker_search = st.text_input('Search Worker')
    worker_search_by = st.multiselect('Search By', ['name', 'surname', 'email'], ['name', 'surname', 'email'])

    add_worker_button = st.button(':green[Add worker]')
    if add_worker_button:
        st.switch_page('pages/add_worker.py')

    workers = requests.get('http://127.0.0.1:8000/app/workers/').json()
    for worker in workers:
        if any(worker_search in worker[field] for field in worker_search_by if field in worker):
            st.markdown('***')
            st.write(f'<p class="big-font">{worker.get('name')} {worker.get('surname')}</p>\n<ul><li>Email: '
                     f'{worker.get('email')}</li></ul>', unsafe_allow_html=True)

if resource == 'Clients':
    client_search = st.text_input('Search Client')
    client_search_by = st.multiselect('Search By', ['name', 'email'], ['name', 'email'])

    add_client_button = st.button(':green[Add client]')
    if add_client_button:
        st.switch_page('pages/add_client.py')

    clients = requests.get('http://127.0.0.1:8000/app/clients/').json()
    for client in clients:
        if any(client_search in client[field] for field in client_search_by if field in client):
            st.markdown('***')
            st.write(f'<p class="big-font">{client.get('name')}</p>\n<ul><li>Email: {client.get('email')}</li></ul>',
                     unsafe_allow_html=True)
