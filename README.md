# 🎵 YouTube to MP3 Automation Tool

Este é um projeto de automação em **Python** desenvolvido para facilitar o download e a conversão de áudios do YouTube (vídeos individuais ou playlists completas) diretamente para o formato **MP3**.

Diferente de ferramentas convencionais, este script foca em **resiliência e qualidade**, utilizando bibliotecas modernas e processamento de sinal via FFmpeg.

---

## 🚀 Funcionalidades

* ✅ **Download Individual:** Baixa áudios de vídeos específicos com um clique.
* ✅ **Suporte a Playlists:** Faz o download de álbuns ou listas inteiras automaticamente.
* ✅ **Conversão Inteligente:** Converte arquivos nativos (WebM/M4A) para **MP3 (192kbps)**.
* ✅ **Organização Automática:** Cria pastas com o nome da playlist e numera as faixas na ordem correta.

---

## 🛠️ Pré-requisitos

Para rodar este projeto, você precisará de:

1. **Python 3.x** instalado.
2. **yt-dlp**: A biblioteca principal de extração.
   ```bash
   pip install yt-dlp
    ```

   FFmpeg: O motor de conversão de mídia.

Importante: Os arquivos ffmpeg.exe e ffprobe.exe devem estar no seu PATH do sistema ou na mesma pasta do script para que a conversão para MP3 funcione.

## 🖥️ Como Usar
Clone este repositório ou baixe o código fonte.

Certifique-se de que as dependências e o FFmpeg estão configurados.

Execute o script:

Bash
python nome_do_seu_arquivo.py
Cole a URL do vídeo ou da playlist quando solicitado e aguarde o processamento.

⚙️ Tecnologias Utilizadas
Python - Linguagem base.

yt-dlp - Extração de conteúdo de alta performance.

### FFmpeg - Framework líder para processamento de áudio e vídeo.

## 📝 Notas de Automação
Este projeto demonstra conceitos de:

Integração de subprocessos (Python + Software Externo).

Manipulação de sistemas de arquivos (criação dinâmica de diretórios).

Tratamento de fluxos de dados de mídia.

## ⚖️ Licença e Uso Ético
Este projeto foi criado para fins estritamente educacionais e de automação pessoal. Lembre-se de respeitar os Termos de Serviço do YouTube e os Direitos Autorais dos criadores.

Desenvolvido por https://github.com/Kennedy7Sa
