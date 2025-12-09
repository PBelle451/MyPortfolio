📁 Meu Portfólio — Desenvolvido em Flask

Este é meu portfólio pessoal, desenvolvido com Python (Flask), estilizado com um tema inspirado em Matrix, e estruturado para rodar tanto localmente quanto em produção usando Docker + Gunicorn.

O site contém:

✔ Página inicial (Sobre Mim)
✔ Projetos
✔ Habilidades
✔ Contato
✔ Estilo animado customizado (CSS / JS)
✔ Arquitetura otimizada para deploy

🚀 Tecnologias Utilizadas

Python 3.11 / 3.12  compatível

Flask 3

HTML + CSS + JavaScript

Gunicorn (produção)

Docker + Docker Compose

Templates Jinja2

Arquitetura limpa com static/ e templates/

📂 Estrutura do Projeto

/app
│── main.py              # Arquivo principal da aplicação Flask
│── wsgi.py              # Entry point usado pelo Gunicorn
│── requirements.txt     # Dependências
│── Dockerfile           
│── docker-compose.yml
│── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── fonts/
│── templates/
    ├── base.html
    ├── about.html
    ├── projects.html
    ├── skills.html
    └── contact.html


▶️ Como rodar localmente (sem Docker)

Instale as dependências:
  pip install -r requirements.txt

Execute:
  python main.py

Acesse:
  http://127.0.0.1:8000


🐳 Rodando com Docker
1. Build + Run
   docker-compose up --build
2. Acesse:
   http://localhost:8000
3. Parar e remover contêiner
   docker-compose down

🌐 Deploy em Produção

Este projeto está preparado para:

* Render.com
* Railway
* Fly.io
* Azure Web App Containers
* AWS ECS Fargate
* Google Cloud Run

Execute:
  gunicorn wsgi:app --bind 0.0.0.0:8000

🙋 Sobre Mim

Você pode me encontrar em:

LinkedIn: https://www.linkedin.com/in/pedro-castro-075020233/

GitHub: https://github.com/PBelle451

Email: pedrocastro451@protonmail.com

📝 Licença

Este projeto é de código aberto sob a MIT License.
