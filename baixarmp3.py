import yt_dlp

def baixar_mp3(url):
    ydl_opts = {
        'format': 'bestaudio/best',  # Escolhe o melhor áudio disponível
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',   # Define o formato de saída
            'preferredquality': '192', # Qualidade do áudio
        }],
        'outtmpl': '%(title)s.%(ext)s', # Nome do arquivo será o título do vídeo
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print("Iniciando o download...")
        ydl.download([url])
        print("\nDownload concluído com sucesso!")

# Exemplo de uso
url_do_video = input("Cole o link do YouTube aqui: ")
baixar_mp3(url_do_video)