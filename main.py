from flask import Flask, render_template
import os

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app")

app = Flask(__name__,
            template_folder=os.path.join(BASE_DIR, "templates"),
            static_folder=os.path.join(BASE_DIR, "static"))

# Página inicial
@app.route('/')
def home():
    return render_template('about.html')

@app.route('/skills')
def skills():
    skills = [
        {"name": "Python", "level": "90%", "years": "5 anos"},
        {"name": "Java", "level": "75%", "years": "4 anos"},
        {"name": "HTML/CSS", "level": "75%", "years": "4 anos"},
        {"name": "Javascript", "level": "50%", "years": "4 anos"},
        {"name": "C/C++", "level": "50%", "years": "4 anos"},
        {"name": "SQL Server", "level": "50%","years": "4 anos"},
        {"name": "MySQL", "level": "50%", "years": "4 anos"},
        {"name": "Git", "level": "50%", "years": "4 anos"},
        {"name": "Anaconda", "level": "50%", "years": "2 anos"},
        {"name": "Linux", "level": "50%", "years": "3 anos"},
        {"name": "Typescript", "level": "50%", "years": "2 anos"},
        {"name": "REST APIs", "level": "50%", "years": "2 anos"},
        {"name": "FastAPI", "level": "50%", "years": "2 anos"},
        {"name": "Scrum", "level": "50%", "years": "2 anos"},
        {"name": "Agile", "level": "50%", "years": "2 anos"},
        {"name": "CI/CD", "level": "50%", "years": "2 anos"},
        {"name": "Playwright", "level": "50%", "years": "2 anos"},
        {"name": "Flask", "level": "50%", "years": "2 anos"},
        {"name": "Django", "level": "40%", "years": "2 anos"},
        {"name": "Docker", "level": "40%", "years": "2 anos"},
        {"name": "Kubernetes", "level": "45%", "years": "2 anos"},
        {"name": "Data Science", "level": "40%", "years": "1 ano"},
        {"name": "Machine Learning", "level": "40%", "years": "1 ano"},
        {"name": "AWS", "level": "40%", "years": "1 ano"},
        {"name": "OCI", "level": "40%", "years": "1 ano"},
        {"name": "MongoDB", "level": "30%", "years": "2 anos"},
        {"name": "React", "level": "30%", "years": "1 ano"},
        {"name": "Angular", "level": "20%", "years": "1 ano"},
        {"name": "Haskell",  "level": "20%", "years": "1 ano"},
        {"name": "PostgreSQL", "level": "20%", "years": "1 ano"},
        {"name": "Selenium", "level": "20%", "years": "6 meses"},
        {"name": "Cypress", "level": "20%", "years": "6 meses"}
    ]
    return render_template('skills.html', skills=skills)

@app.route('/projects')
def projects():
    projects = [
        {
            'title': 'Liver Cancer',
            'description': 'This is a project that uses Multiple Linear Regression to predict what is the probability of patients to develop Liver Cancer\nbased on conditions such as smoking habits, sanitary conditions, living conditions, eating habits, drinking habits and etc',
            'tech': 'Python, Pandas, Numpy, Sckit Learn, Matplotlib, Seaborn',
            'link': 'https://github.com/PBelle451/LiverCancer'
        },
        
        {
            'title': 'Spotify Dataframe',
            'description': 'A Python project that uses Spotipy to extract data from Spotify API and creates a dataframe using Pandas.\nThe dataframe can be used to analyze the data and create visualizations using Matplotlib and Seaborn.',
            'tech': 'Python, Spotipy, Pandas, Matplotlib, Seaborn',
            'link': 'https://github.com/PBelle451/SpotifyDataframe'
        },
        
        {
            'title': 'House Prices',
            'description': 'A Data Science project that uses Linear Regression and Random Forest Regressor.\nThe model predicts the average increase of housing prices based of previous data analyzed using the Random Forest to classify large amount o data.',
            'tech': 'Python, Pandas, Numpy, Sckit Learn, Seaborn, Matplotlib',
            'link': 'https://github.com/PBelle451/HousePrices'
        },
        
        {
            'title': 'Youtube AI Transcript',
            'description': 'A Python project using Whisper AI from OpenAI which extracts the audio from the video and transcripts it to text format.',
            'tech': 'Python, OpenAI',
            'link': 'https://github.com/PBelle451/YoutubeAItranscript'
        },
        
        {
            'title': 'Covid Dashboard',
            'description': 'This small project is a mix between my knowledge in Flask and Data Science.\nI used Python, Flask, Pandas and Plotly for this project.',
            'tech': 'Python, Flask, Pandas, Plotly',
            'link': 'https://github.com/PBelle451/CovidDashboardBR'
        },
        
        {
            'title': 'Análise Ancestralidade no estado de Goiás',
            'description': 'Projeto de Ciência de Dados que analisa a ancestralidade genética da população brasileira utilizando dados de DNA.\nO projeto utiliza bibliotecas como Pandas, NumPy, Matplotlib e Seaborn para análise e visualização dos dados.',
            'tech': 'Python, Pandas, Numpy, Matplotlib, Seaborn',
            'link': 'https://github.com/PBelle451/Analise-Ancestralidade-Goias'
        },
        
        {
            'title': 'Flask Portfolio',
            'description': 'A simple portfolio website made using Flask, HTML, CSS, Javascript and Python',
            'tech': 'Python, Flask, HTML, CSS, Javascript, Docker',
            'link': 'https://github.com/PBelle451/MyPortfolio'
        },
        
        {
            'title': 'AI Chatbot Java',
            'description': 'A simple chatbot made using Java and OpenAI API\nIt offers real-time responses to user queries by leveraging advanced natural language processing capabilities.',
            'tech': 'Java, OpenAI API, Maven',
            'link': 'https://github.com/PBelle451/ChatAIJava'
        }
    ]
    return render_template('projects.html', projects=projects)

# Página de contato
@app.route('/contact')
def contact():
    contact_info = [
        {'name': 'E-Mail', 'link': 'pedrocastro451@protonmail.com'},
        {'name': 'LinkedIn', 'link': 'https://www.linkedin.com/in/pedro-castro-075020233/'},
        {'name': 'Github', 'link': 'https://github.com/PBelle451'},
        {'name': 'Whatsapp', 'link': 'https://api.whatsapp.com/send?phone=56199948985'}
    ]
    return render_template('contact.html', contact=contact_info)

print("MAIN.PY INICIADO")