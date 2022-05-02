from pytube import YouTube
from pytube.cli import on_progress
import datetime
import math


def end_progress(stream, path):
    print("Baixado! Obrigado por usar nosso downloader")
    input("Pressione qualquer tecla para fechar")
    quit()


print("Bem-Vindo ao nosso Youtube Downloader :D")
dLink = input("Qual vídeo deseja baixar? ")
yt = YouTube(dLink, on_progress_callback=on_progress,
             on_complete_callback=end_progress)
print('Coletando informações...')
print("Título:", yt.title)
print("Número de views:", yt.views)
print("Tamanho do vídeo:", str(datetime.timedelta(seconds=yt.length)))
type = input("Deseja baixar o vídeo [1] ou áudio [2]? ")


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def downloadVideo():
    print("Carregando links...")
    allVideos = yt.streams.order_by('resolution').filter(
        file_extension='mp4', type='video')
    for i in allVideos:
        if i.is_progressive:
            print("[", i.itag, "] ->",
                  "Tipo:", i.mime_type,
                  "| Qualidade:", i.resolution,
                  "| Fps:", i.fps,
                  "| Tamanho:", convert_size(i.filesize),
                  " - Vídeo e Áudio"
                  )
        else:
            print("[", i.itag, "] ->",
                  "Tipo:", i.mime_type,
                  "| Qualidade:", i.resolution,
                  "| Fps:", i.fps,
                  "| Tamanho:", convert_size(i.filesize),
                  " - Somente Vídeo"
                  )

    itagDown = input(
        "Qual deseja baixar? (utilize o número entre [] para identificar) ")
    stream = yt.streams.get_by_itag(itagDown)
    stream.download('Downloads')


def downloadAudio():
    print("Carregando links...")
    allVideos = yt.streams.filter(
        only_audio=True)
    for i in allVideos:
        print("[", i.itag, "] ->",
              "Tipo:", i.mime_type,
              "| Qualidade:", i.abr,
              "| Tamanho:", convert_size(i.filesize),
              "- Somente Áudio"
              )

    itagDown = input(
        "Qual deseja baixar? (utilize o número entre [] para identificar) ")
    stream = yt.streams.get_by_itag(itagDown)
    stream.download('Downloads')


if type == "1":
    downloadVideo()
elif type == "2":
    downloadAudio()
