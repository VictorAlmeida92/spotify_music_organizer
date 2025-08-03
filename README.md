# Organizador de Músicas por Gênero no Spotify

Este projeto é um script Python que se conecta à sua conta do Spotify, lê suas músicas curtidas e organiza automaticamente suas músicas em playlists separadas por gênero.

---

## Funcionalidades

- Conecta via API do Spotify com OAuth 2.0.
- Lê todas as músicas curtidas (Liked Songs).
- Agrupa músicas pelo gênero principal do primeiro artista da faixa.
- Cria playlists privadas para cada gênero (com nomes personalizados).
- Evita duplicação de músicas nas playlists.
- Agrupa gêneros similares automaticamente (ex: "Brazilian Trap" e "Trap" juntos).
- Exclui playlists antigas antes de recriar, para manter a organização limpa.

---

## Pré-requisitos

- Python 3.9+
- Conta Spotify com acesso à API e app cadastrado em https://developer.spotify.com
- Bibliotecas Python:
    - spotipy
    - (outros, caso tenha)

---

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/victoralmeida92/spotify-music-organizer.git
cd spotify-genre-organizer
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Configure suas credenciais do Spotify (crie um arquivo `.env` ou exporte variáveis de ambiente):

```env
SPOTIPY_CLIENT_ID="seu-client-id"
SPOTIPY_CLIENT_SECRET="seu-client-secret"
SPOTIPY_REDIRECT_URI="http://127.0.0.1:8888/callback"
```

---

## Uso

Para rodar o script de organização de músicas:

```bash
python3 -m app.main
```

Ao executar, você será redirecionado para autenticar na sua conta do Spotify e autorizar o app.

---

## Estrutura do Projeto

- `src/app/interface/cli/` - Scripts CLI (linha de comando).
- `src/app/infrastructure/spotify/` - Client e integração com API Spotify.
- `src/app/infrastructure/playlist/` - Gerenciamento de playlists.
- `src/app/domain/services/` - Lógica de negócio (ex: normalização de gêneros).

---

## Contribuições

Contribuições são bem-vindas!  
Abra issues para bugs ou sugestões e envie pull requests.

---

## Licença

Projeto licenciado sob a MIT License. Veja o arquivo LICENSE para detalhes.

---

## Contato

Victor Almeida - victoralmeida92  
Projeto no GitHub: https://github.com/victoralmeida92/spotify-genre-organizer
