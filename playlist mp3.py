from pytube import Playlist
from pytube import YouTube
import os
import ssl
from moviepy.editor import VideoFileClip

# Deshabilita la verificación del certificado SSL
ssl._create_default_https_context = ssl._create_unverified_context

# URL de la playlist de YouTube
url_playlist = 'https://youtube.com/playlist?list=PL8mMC-lMg9QPuI3FAEneLD32ygL3bIR7d&si=G-vZo06n8sQsHJJ4'  # Reemplaza con la URL de tu playlist

# Crea un objeto de Playlist
playlist = Playlist(url_playlist)

# Define la ruta de destino en el escritorio con una carpeta específica para la playlist
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
carpeta_playlist = os.path.join(desktop, f"PlaylistDescargada_{playlist.title}")

# Crea la carpeta si no existe
os.makedirs(carpeta_playlist, exist_ok=True)

# Itera sobre cada video en la playlist
for video_url in playlist.video_urls:
    try:
        # Crea un objeto de YouTube para el video actual
        yt = YouTube(video_url)

        # Selecciona el stream deseado con la resolución máxima
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        # Descarga el video en la carpeta de la playlist especificada
        video_path = stream.download(output_path=carpeta_playlist)

        # Convierte el video a MP3
        mp3_file_path = os.path.join(carpeta_playlist, f"{yt.title}.mp3")
        video_clip = VideoFileClip(video_path)
        video_clip.audio.write_audiofile(mp3_file_path)
        video_clip.close()

        # Elimina el archivo de video descargado (opcional, dependiendo de tus necesidades)
        os.remove(video_path)

        print(f'Video convertido a MP3: {yt.title}')
    except Exception as e:
        print(f'Error al procesar el video {video_url}: {e}')

print(f'Todos los videos de la playlist han sido convertidos a MP3 en: {carpeta_playlist}')
