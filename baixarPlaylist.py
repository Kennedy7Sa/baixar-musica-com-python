import yt_dlp

def baixar_playlist(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        # 'noplaylist': False, # Garante que ele veja a playlist inteira
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        # Organização: Pasta com nome da playlist / Número - Título.mp3
        'outtmpl': '%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print("Iniciando o download da playlist... Isso pode demorar dependendo do tamanho.")
            ydl.download([url])
            print("\nDownload da playlist concluído!")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

url_input = input("Cole o link do vídeo ou da playlist: ")
baixar_playlist(url_input)