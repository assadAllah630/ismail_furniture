import os
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

# Set up PyDrive2 to use service account

def get_drive():
    gauth = GoogleAuth()
    gauth.settings["client_config_file"] = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON")
    gauth.ServiceAuth()
    return GoogleDrive(gauth)

def upload_file_to_drive(filepath, filename, folder_id):
    drive = get_drive()
    file_drive = drive.CreateFile({'title': filename, 'parents': [{'id': folder_id}]})
    file_drive.SetContentFile(filepath)
    file_drive.Upload()
    # Make file public
    file_drive.InsertPermission({
        'type': 'anyone',
        'value': 'anyone',
        'role': 'reader'
    })
    return file_drive['alternateLink'] 