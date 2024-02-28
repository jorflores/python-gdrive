import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


gauth = GoogleAuth()
#Path completo donde se encuentra el archivo client_secrets.json
gauth.settings['client_config_file'] = 'D:/Playground/Python/itesm/client_secrets.json'
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

#Folder ID de alguna carpeta en nuestra cuenta de google drive donde subiremos el archivo.
folder = ''

# ejemplo de como subir un archivo nuevo 
#file1 = drive.CreateFile({'parents': [{'id': folder}], 'title': 'hello.txt'})
#file1.SetContentString("Hello World")
#file1.Upload()

# Directorio donde leeremos el archivo que vamos a subir.
directory = ""
for f in os.listdir(directory):
    filename = os.path.join(directory, f)
    gfile = drive.CreateFile({'parents': [{'id': folder}], 'title': f})
    gfile.SetContentFile(filename)
    gfile.Upload()
