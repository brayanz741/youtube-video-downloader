import pytube
from tkinter import messagebox
from tkinter import simpledialog
import os

# Variables
prompt = "¿Cúal será el nombre del "
route = ""
extension = ""

video = messagebox.askyesno(message="¿Desea descargar un video?", title="Mensaje del sistema")
if video:
    prompt += "video?"
    route += "C:/Users/Brayan Zambrano/Videos/Reveled King/"
    extension += ".mp4"
else:
    prompt += "audio?"
    route += "C:/Users/Brayan Zambrano/Videos/Expansion sin limites/"
    extension += ".mp3"

os.makedirs(route, exist_ok=True)
link = simpledialog.askstring("Mensaje del sistema","¿Cuál es el url de YouTube que desea obtener?")
yt = pytube.YouTube(link)
file_name = simpledialog.askstring("Mensaje del sistema",prompt)
filename = file_name + extension
if video:
    yt.streams.filter(file_extension="mp4").first().download(route,filename)
else:
    yt.streams.filter(only_audio=True).first().download(route,filename)

messagebox.showinfo(message="Archivo descargado con Éxito", title="Mensaje del sistema")
