import os
import streamlit as st
import requests
import time


@st.dialog('Edit Project')
def edit_project():
    name = st.text_input('Name', proj.get('name'))
    description = st.text_input('Description', proj.get('description'))
    proj_client = st.selectbox('Client', clients_emails.keys())

    if st.button(':green[Submit]'):
        data = {
            'name': name,
            'description': description,
            'client': clients_emails.get(proj_client),
        }

        response_put = requests.put(f'http://127.0.0.1:8000/app/projects/{proj.get('project_id')}/', json=data)
        if response_put.status_code == 200:
            st.toast(':green[Project updated]')
            time.sleep(1)
            st.rerun()
        else:
            st.toast(':red[There was an error while updating project]')

    if st.button(':red[Cancel]'):
        st.rerun()


@st.dialog('Delete Project')
def delete_project():
    st.warning('Are you sure about deleting this project?')
    if st.button(':red[Yes]'):
        response_delete = requests.delete(f'http://127.0.0.1:8000/app/projects/{proj.get('project_id')}/')
        if response_delete.status_code == 204:
            st.toast(':green[Project deleted]')
            time.sleep(1)
            st.switch_page('taskpilot_app.py')
        else:
            st.toast(':red[There was an error while deleting project]')
    if st.button(':green[No]'):
        st.rerun()


@st.dialog('Delete Task')
def delete_task(task_to_delete):
    st.warning('Are you sure about deleting this task?')
    if st.button(':red[Yes]'):
        response_delete = requests.delete(f'http://127.0.0.1:8000/app/tasks/{task_to_delete.get('task_id')}/')
        if response_delete.status_code == 204:
            st.toast(':green[Task deleted]')
            time.sleep(1)
            st.rerun()
        else:
            st.toast(':red[There was an error while deleting project]')
    if st.button(':green[No]'):
        st.rerun()


@st.dialog('Add Comment')
def add_comment():
    author = st.selectbox('Author', workers_emails.keys())
    content = st.text_input('Content')
    if st.button(':green[Add]'):
        data = {
            'project_id': proj.get('project_id'),
            'author': workers_emails.get(author),
            'comment': content
        }

        response_post = requests.post('http://127.0.0.1:8000/app/comments/', json=data)
        if response_post.status_code == 201:
            st.toast(':green[Comment added]')
            time.sleep(1)
            st.rerun()
        else:
            st.toast(':red[There was an error while adding comment]')
    if st.button(':red[Cancel]'):
        st.rerun()


@st.dialog('Edit Task')
def edit_task(task_to_edit):
    task_worker = st.selectbox('Worker', workers_emails.keys())
    name = st.text_input('Name', task_to_edit.get('name'))
    description = st.text_input('Description', task_to_edit.get('description'))
    status = st.selectbox('Status', ['not started', 'in progress', 'finished'])
    start_date = st.date_input('Start Date')
    end_date = st.date_input('End Date')

    if st.button(':green[Submit]'):
        data = {
            'project_id': proj.get('project_id'),
            'worker': workers_emails.get(task_worker),
            'name': name,
            'description': description,
            'status': status,
            'start_date': start_date.isoformat(),
            'end_date': end_date.isoformat()
        }

        response_put = requests.put(f'http://127.0.0.1:8000/app/tasks/{task_to_edit.get('task_id')}/', json=data)
        if response_put.status_code == 200:
            st.toast(':green[Task updated]')
            time.sleep(1)
            st.rerun()
        else:
            st.toast(':red[There was an error while updating task]')

    if st.button(':red[Cancel]'):
        st.rerun()


@st.dialog('Add Task')
def add_task():
    task_worker = st.selectbox('Worker', workers_emails.keys())
    name = st.text_input('Name')
    description = st.text_input('Description')
    status = st.selectbox('Status', ['not started', 'in progress', 'finished'])
    start_date = st.date_input('Start Date')
    end_date = st.date_input('End Date')

    if st.button(':green[Submit]'):
        data = {
            'project_id': proj.get('project_id'),
            'worker': workers_emails.get(task_worker),
            'name': name,
            'description': description,
            'status': status,
            'start_date': start_date.isoformat(),
            'end_date': end_date.isoformat()
        }

        response_put = requests.post(f'http://127.0.0.1:8000/app/tasks/', json=data)
        if response_put.status_code == 201:
            st.toast(':green[Task added]')
            time.sleep(1)
            st.rerun()
        else:
            st.toast(':red[There was an error while adding task]')

    if st.button(':red[Cancel]'):
        st.rerun()


def find_with_id(provided_id, where):
    for key in where.keys():
        if where.get(key) == provided_id:
            return key

    return None


project_id = os.environ.get('project_id')
proj = requests.get(f'http://127.0.0.1:8000/app/projects/{project_id}/').json()

workers = requests.get('http://127.0.0.1:8000/app/workers/').json()
workers_emails = {}
for worker in workers:
    workers_emails[f'{worker.get('name')} {worker.get('surname')} ({worker.get('email')})'] = worker.get('worker_id')

clients = requests.get('http://127.0.0.1:8000/app/clients/').json()
clients_emails = {}
for client in clients:
    clients_emails[f'{client.get('name')} ({client.get('email')})'] = client.get('client_id')

comments = requests.get('http://127.0.0.1:8000/app/comments/').json()
proj_comments = []
for comment in comments:
    if comment.get('project_id') == proj.get('project_id'):
        proj_comments.append(comment)

tasks = requests.get('http://127.0.0.1:8000/app/tasks/').json()
proj_tasks = []
for task in tasks:
    if task.get('project_id') == proj.get('project_id'):
        proj_tasks.append(task)

st.set_page_config(f'TaskPilot - Project {proj.get('project_id')}', page_icon="💼", layout='wide')

st.markdown("""
<style>
.project-title {
    font-size:50px;
    font-weight: bold;
}
.ul-items li {
    font-size:30px;
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
.task-label {
    font-size:18px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([6, 1])

if col1.button(':red[< Back]'):
    st.switch_page('taskpilot_app.py')

col1.write(f'<center><p class="project-title">Project {proj.get('project_id')} - {proj.get('name')}</p></center><br>'
           f'<br><ul class="ul-items"><li>Client: {find_with_id(proj.get('client'), clients_emails)}</li><li>'
           f'Description: {proj.get('description')}</li></ul><br>', unsafe_allow_html=True)

col2.write('<br><br><br><br><br><br><br><br>', unsafe_allow_html=True)
if col2.button(':blue[Edit project]', use_container_width=True):
    edit_project()

if col2.button(':red[Delete project]', use_container_width=True):
    delete_project()

with st.expander(f'Comments ({len(proj_comments)})'):
    if st.button(':green[Add Comment]'):
        add_comment()

    for proj_comm in reversed(proj_comments):
        st.markdown('***')
        st.write(f'<p class="author">{find_with_id(proj_comm.get('author'), workers_emails)}</p>'
                 f'{proj_comm.get('comment')}<p class="date">{proj_comm.get('add_date')}</p>', unsafe_allow_html=True)

with (st.expander(f'Tasks ({len(proj_tasks)})')):
    col3, col4 = st.columns(2, vertical_alignment='center')
    if col3.button(':green[Add Task]'):
        add_task()
    task_search = col4.text_input('Search Task By Name')

    for proj_task in reversed(proj_tasks):
        if task_search in proj_task.get('name'):
            st.markdown('***')
            st.write(f'<p class="author">Task {proj_task.get('name')}</p><strong>Description:</strong> '
                     f'{proj_task.get('description')}<br><strong>Worker:</strong> '
                     f'{find_with_id(proj_task.get('worker'), workers_emails)}<br><strong>'
                     f'Task status:</strong> {proj_task.get('status')}<br><p class="date">Start date: '
                     f'{proj_task.get('start_date')}<br>End date: {proj_task.get('end_date')}</p>',
                     unsafe_allow_html=True)
            if st.button(label=':blue[Edit]', key=f'edit{proj_task.get('task_id')}'):
                edit_task(proj_task)
            if st.button(label=':red[Delete]', key=f'delete{proj_task.get('task_id')}'):
                delete_task(proj_task)
