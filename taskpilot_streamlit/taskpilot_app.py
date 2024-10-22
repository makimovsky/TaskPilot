import os
from pages.worker_management import *
from pages.client_management import *

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
resource = st.sidebar.selectbox('Resource', ['Projects', 'Workers', 'Clients'], label_visibility='collapsed')

if resource == 'Projects':
    project_search = st.text_input('Search Project')
    project_search_by = st.multiselect('Search By', ['name', 'description'])

    add_project_button = st.button(':green[Add project]')
    if add_project_button:
        st.switch_page('pages/add_project.py')

    if not project_search_by:
        project_search_by = ['name', 'description']

    projects = requests.get('http://127.0.0.1:8000/app/projects/').json()
    for project in projects:
        if any(project_search in project.get(field) for field in project_search_by):
            st.markdown('***')
            st.write(f'<p class="big-font">Project {project.get('project_id')} - {project.get('name')}</p>',
                     unsafe_allow_html=True)
            if st.button(label=':blue[Details]', key=hash(project.get('description'))):
                os.environ['project_id'] = str(project.get('project_id'))
                st.switch_page('pages/project_management.py')

elif resource == 'Workers':
    worker_search = st.text_input('Search Worker')
    worker_search_by = st.multiselect('Search By', ['name', 'surname', 'email'])

    add_worker_button = st.button(':green[Add worker]')
    if add_worker_button:
        st.switch_page('pages/add_worker.py')

    if not worker_search_by:
        worker_search_by = ['name', 'surname', 'email']

    workers = requests.get('http://127.0.0.1:8000/app/workers/').json()
    for worker in workers:
        if any(worker_search in worker.get(field) for field in worker_search_by):
            st.markdown('***')
            st.write(f'<p class="big-font">{worker.get('name')} {worker.get('surname')}</p>\n<ul><li>Email: '
                     f'{worker.get('email')}</li></ul>', unsafe_allow_html=True)
            if st.button(label=':blue[Edit]',
                         key=hash(f'{worker.get('worker_id')}{worker.get('name')}edit')):
                edit_worker(worker)
            if st.button(label=':red[Delete]',
                         key=hash(f'{worker.get('worker_id')}{worker.get('surname')}delete')):
                delete_worker(worker)


elif resource == 'Clients':
    client_search = st.text_input('Search Client')
    client_search_by = st.multiselect('Search By', ['name', 'email'])

    add_client_button = st.button(':green[Add client]')
    if add_client_button:
        st.switch_page('pages/add_client.py')

    if not client_search_by:
        client_search_by = ['name', 'email']

    clients = requests.get('http://127.0.0.1:8000/app/clients/').json()
    for client in clients:
        if any(client_search in client.get(field) for field in client_search_by):
            st.markdown('***')
            st.write(f'<p class="big-font">{client.get('name')}</p>\n<ul><li>Email: {client.get('email')}</li></ul>',
                     unsafe_allow_html=True)
            if st.button(label=':blue[Edit]',
                         key=hash(f'{client.get('client_id')}{client.get('name')}edit')):
                edit_client(client)
            if st.button(label=':red[Delete]',
                         key=hash(f'{client.get('worker_id')}{client.get('name')}delete')):
                delete_client(client)
