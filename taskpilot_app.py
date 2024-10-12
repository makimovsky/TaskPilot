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
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown('<center><p class="app-title">TaskPilot</p></center>', unsafe_allow_html=True)
st.sidebar.header('Choose resource')
resource = st.sidebar.selectbox('Resource', ['Projects', 'Workers', 'Clients'])

if resource == 'Projects':
    project_search = st.text_input('Search Project')
    project_search_by = st.multiselect('Search By', ['name', 'description', 'owner', 'client'],
                                       ['name', 'description', 'owner', 'client'])

    st.markdown('***')
    add_project_button = st.button(':blue[Add project]')
    if add_project_button:
        st.switch_page('pages/add_project.py')

    projects = requests.get('http://127.0.0.1:8000/app/projects/').json()
    for project in projects:
        if any(project_search in project[field] for field in project_search_by if field in project):
            st.write(f'<p class="big-font">Project {project['project_id']} - {project['name']}</p>\n<ul><li>Owner: '
                     f'{project['owner']}</li><li>Client: {project['client']}</li><li>Description: '
                     f'{project['description']}</li><li>Start date: {project['start_date']}</li><li>End date: '
                     f'{project['end_date']}</li></ul><br>', unsafe_allow_html=True)

if resource == 'Workers':
    worker_search = st.text_input('Search Worker')
    worker_search_by = st.multiselect('Search By', ['name', 'surname', 'email'], ['name', 'surname', 'email'])

    st.markdown('***')

    add_worker_button = st.button(':blue[Add worker]')
    if add_worker_button:
        st.switch_page('pages/add_worker.py')

    workers = requests.get('http://127.0.0.1:8000/app/workers/').json()
    for worker in workers:
        if any(worker_search in worker[field] for field in worker_search_by if field in worker):
            st.write(f'<p class="big-font">{worker['name']} {worker['surname']}</p>\n<ul><li>Email: '
                     f'{worker['email']}</li></ul>', unsafe_allow_html=True)

if resource == 'Clients':
    client_search = st.text_input('Search Client')
    client_search_by = st.multiselect('Search By', ['name', 'email'], ['name', 'email'])

    st.markdown('***')

    add_client_button = st.button(':blue[Add client]')
    if add_client_button:
        st.switch_page('pages/add_client.py')

    clients = requests.get('http://127.0.0.1:8000/app/clients/').json()
    for client in clients:
        if any(client_search in client[field] for field in client_search_by if field in client):
            st.write(f'<p class="big-font">{client['name']}</p>\n<ul><li>Email: {client['email']}</li></ul>',
                     unsafe_allow_html=True)
