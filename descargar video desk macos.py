from pytube import YouTube
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
carpeta_destino = os.path.join(desktop, "VideosDescargados")


os.makedirs(carpeta_destino, exist_ok=True)

# URL del video de YouTube
url_video = ''


yt = YouTube(url_video)
stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
stream.download(output_path=carpeta_destino)
print(f'El video ha sido descargado en: {carpeta_destino}')
