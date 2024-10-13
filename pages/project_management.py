import streamlit as st
import requests
import time


@st.dialog("Project Information Window", width='large')
def show_project(proj):
    st.write(f'<p class="big-font">Project {proj.get('project_id')} - {proj.get('name')}</p>\n<ul><li>'
             f'Owner: {proj.get('owner')}</li><li>Client: {proj.get('client')}</li><li>Description: '
             f'{proj.get('description')}</li><li>Start date: {proj.get('start_date')}</li><li>End date: '
             f'{proj.get('end_date')}</li></ul><br>', unsafe_allow_html=True)

    comments = requests.get('http://127.0.0.1:8000/app/comments/').json()
    proj_comments = []
    for comment in comments:
        if comment.get('project_id') == proj.get('project_id'):
            proj_comments.append(comment)

    if len(proj_comments) > 0:
        with st.expander(f'Comments ({len(proj_comments)})'):
            for proj_comm in proj_comments:
                st.markdown('***')
                st.write(f'<p class="author">{proj_comm.get('author')}</p>{proj_comm.get('comment')}'
                         f'<p class="date">{proj_comm.get('add_date')}</p>',
                         unsafe_allow_html=True)

    with st.popover(':blue[Edit project]'):
        name = st.text_input('Name', proj.get('name'))
        description = st.text_input('Description', proj.get('description'))
        owners = requests.get('http://127.0.0.1:8000/app/workers/').json()
        owner_emails = []
        for owner in owners:
            owner_emails.append(f'{owner['name']} {owner['surname']} ({owner['email']})')
        owner = st.selectbox('Owner', owner_emails)

        proj_clients = requests.get('http://127.0.0.1:8000/app/clients/').json()
        client_emails = []
        for proj_client in proj_clients:
            client_emails.append(f'{proj_client['name']} ({proj_client['email']})')
        proj_client = st.selectbox('Client', client_emails)
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

            response = requests.put(f'http://127.0.0.1:8000/app/projects/{proj.get('project_id')}/', json=data)
            if response.status_code == 200:
                st.toast(':green[Project updated]')
                time.sleep(1)
                st.rerun()
            else:
                st.toast(':red[There was an error while updating project]')

    with st.popover(':red[Delete project]'):
        st.warning('Are you sure about deleting this project?')
        if st.button(':red[Yes]'):
            response = requests.delete(f'http://127.0.0.1:8000/app/projects/{proj.get('project_id')}/')
            if response.status_code == 204:
                st.toast(':green[Project deleted]')
                time.sleep(1)
                st.rerun()
            else:
                st.toast(':red[There was an error while deleting project]')

    if st.button('Close'):
        st.rerun()
