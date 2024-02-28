import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Load configurations from settings.yaml
gauth = GoogleAuth()
gauth.settings['client_config_file'] = 'D:/Playground/Python/itesm/client_secrets.json'
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

#Folder ID de alguna carpeta en nuestra cuenta de google drive donde subiremos el archivo.
folder = '1Qd6Tqh4EKJngfIQO4OGmxO2WyEbruukK'


#file1 = drive.CreateFile({'parents': [{'id': folder}], 'title': 'hello.txt'})
#file1.SetContentString("Hello World")
#file1.Upload()

directory = "D:/Playground/Python/itesm/datos/"
for f in os.listdir(directory):
    filename = os.path.join(directory, f)
    # Revisa si el archivo ya existe en Google Drive
    file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(folder)}).GetList()
    for file in file_list:
        if file['title'] == f:
            # If the file exists, update its content
            file.SetContentFile(filename)
            file.Upload()
            break
    else:
        # Si el archivo no existe crea uno nuevo.
        gfile = drive.CreateFile({'parents': [{'id': folder}], 'title': f})
        gfile.SetContentFile(filename)
        gfile.Upload()
