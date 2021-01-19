from googleapiclient.http import MediaFileUpload
from Google import Create_Service

CLIENT_SECRET_FILE='Client_secret_GoogleCloudDemo.json'
API_NAME='drive'
API_VERSION='v3'
SCOPES=['https://www.googleapis.com/auth/drive']

service=Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)
folder_id='1MB2ASh7R7d0vPr5SHAZKt1SeJN3sFWUR'

file_names=['file.xlsx','task1.py']
mime_types=['application/vnd.openxmlformats-officedocument.spreadsheetml.sheet','application/x-python-code']

for file_name in file_names:
    file_metadata={
        'name':file_name,
        'parents':[folder_id]
    }
    media= MediaFileUpload('./googledrive/{0}'.format(file_name),mimetype=mime_type)

    service.files().creates(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()