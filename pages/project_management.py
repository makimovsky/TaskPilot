import os
import streamlit as st
import requests
import time


@st.dialog('Edit Project')
def edit_project():
    name = st.text_input('Name', proj.get('name'))
    description = st.text_input('Description', proj.get('description'))
    owner = st.selectbox('Owner', workers_emails)
    proj_client = st.selectbox('Client', clients_emails)
    start_date = st.date_input('Start Date')
    end_date = st.date_input('End Date')

    if st.button(':green[Submit]'):
        data = {
            'name': name,
            'description': description,
            'owner': owner.split('(')[1][:-1],
            'client': proj_client.split('(')[0][:-1],
            'start_date': start_date.isoformat(),
            'end_date': end_date.isoformat()
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
    author = st.selectbox('Author', workers_emails)
    content = st.text_input('Content')
    if st.button(':green[Add]'):
        data = {
            'project_id': proj.get('project_id'),
            'author': author.split('(')[1][:-1],
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
    task_worker = st.selectbox('Worker', workers_emails)
    name = st.text_input('Name', task_to_edit.get('name'))
    description = st.text_input('Description', task_to_edit.get('description'))
    status = st.selectbox('Status', ['not started', 'in progress', 'finished'])
    start_date = st.date_input('Start Date')
    end_date = st.date_input('End Date')

    if st.button(':green[Submit]'):
        data = {
            'project_id': proj.get('project_id'),
            'worker': task_worker.split('(')[1][:-1],
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
    task_worker = st.selectbox('Worker', workers_emails)
    name = st.text_input('Name')
    description = st.text_input('Description')
    status = st.selectbox('Status', ['not started', 'in progress', 'finished'])
    start_date = st.date_input('Start Date')
    end_date = st.date_input('End Date')

    if st.button(':green[Submit]'):
        data = {
            'project_id': proj.get('project_id'),
            'worker': task_worker.split('(')[1][:-1],
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


project_id = os.environ.get('project_id')
proj = requests.get(f'http://127.0.0.1:8000/app/projects/{project_id}/').json()

workers = requests.get('http://127.0.0.1:8000/app/workers/').json()
workers_emails = []
for worker in workers:
    workers_emails.append(f'{worker['name']} {worker['surname']} ({worker['email']})')

clients = requests.get('http://127.0.0.1:8000/app/clients/').json()
clients_emails = []
for client in clients:
    clients_emails.append(f'{client['name']} ({client['email']})')

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
           f'<br><ul class="ul-items"><li>Owner: {proj.get('owner')}</li><li>Client: {proj.get('client')}</li><li>'
           f'Description: {proj.get('description')}</li><li>Start date: {proj.get('start_date')}</li><li>End date: '
           f'{proj.get('end_date')}</li></ul><br>', unsafe_allow_html=True)

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
        st.write(f'<p class="author">{proj_comm.get('author')}</p>{proj_comm.get('comment')}'
                 f'<p class="date">{proj_comm.get('add_date')}</p>',
                 unsafe_allow_html=True)

with st.expander(f'Tasks ({len(proj_tasks)})'):
    col3, col4 = st.columns(2, vertical_alignment='center')
    if col3.button(':green[Add Task]'):
        add_task()
    task_search = col4.text_input('Search Task By Name')

    for proj_task in reversed(proj_tasks):
        if task_search in proj_task.get('name'):
            st.markdown('***')
            st.write(f'<p class="author">Task {proj_task.get('name')}</p><strong>Description:</strong> '
                     f'{proj_task.get('description')}<br><strong>Worker:</strong> {proj_task.get('worker')}<br><strong>'
                     f'Task status:</strong> {proj_task.get('status')}<br><p class="date">Start date: '
                     f'{proj_task.get('start_date')}<br>End date: {proj_task.get('end_date')}</p>', unsafe_allow_html=True)
            if st.button(label=':blue[Edit]', key=f'edit{proj_task.get('task_id')}'):
                edit_task(proj_task)
            if st.button(label=':red[Delete]', key=f'delete{proj_task.get('task_id')}'):
                delete_task(proj_task)
