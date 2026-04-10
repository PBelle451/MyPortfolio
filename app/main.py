from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("about.html")

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
        {"name": "MongoDB", "level": "30%", "years": "1 ano"},
        {"name": "React", "level": "30%", "years": "1 ano"},
        {"name": "Angular", "level": "20%", "years": "1 ano"},
        {"name": "Haskell",  "level": "20%", "years": "1 ano"},
        {"name": "PostgreSQL", "level": "20%", "years": "1 ano"},
        {"name": "Selenium", "level": "20%", "years": "6 meses"},
        {"name": "Cypress", "level": "20%", "years": "6 meses"},
        {"name": "Behave", "level": "20%", "years": "6 meses"}
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
            'title': 'Youtube AI Transcript',
            'description': 'A Python project using Whisper AI from OpenAI which extracts the audio from the video and transcripts it to text format.',
            'tech': 'Python, OpenAI',
            'link': 'https://github.com/PBelle451/YoutubeAItranscript'
        },
        
        {
            'title': 'AI Chatbot Java',
            'description': 'A simple chatbot made using Java and OpenAI API\nIt offers real-time responses to user queries by leveraging advanced natural language processing capabilities.',
            'tech': 'Java, OpenAI API, Maven',
            'link': 'https://github.com/PBelle451/ChatAIJava'
        },
        
        {
            'title': 'Projeto Padaria',
            'description': 'Project of an API for a bakery, which allows to manage the inventory, sales and customers.\nI used Java and Spring Boot to create the API, and PostgreSQL to create the database.',
            'tech': 'Java, Spring Boot, PostgreSQL',
            'link': 'https://github.com/PBelle451/projeto-padaria-melhorado'
        },
        
        {
            'title': 'Projeto TDD',
            'description': 'Project for an a Test Driven Development (TDD) course I made, which consists in creating a simple API for a library, which allows to manage the inventory, sales and customers.\nI used Java and Spring Boot to create the API, and PostgreSQL to create the database.',
            'tech': 'Java, Spring Boot, PostgreSQL',
            'link': 'https://github.com/PBelle451/projeto_tdd'
        },
        
        {
            'title': 'Store Microservices',
            'description': 'Project for a Microservices course I made, which consists in creating a simple API for a store, which allows to manage the inventory, sales and customers.\nI used Java and Spring Boot to create the API, and PostgreSQL to create the database.',
            'tech': 'Java, Spring Boot, PostgreSQL',
            'link': 'https://github.com/PBelle451/store-microservices'
        },
        
        {
            'title': 'Middleware',
            'description': 'A simple middleware made using Java and Spring Boot which allows to log the requests and responses of an API.\nIt uses the public API of the Brazilian government to get the data of the cities and states of Brazil.',
            'tech': 'Java, Spring Boot',
            'link': 'https://github.com/PBelle451/MiddlewareProject'
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
print("Acesse http://localhost:8000 para visualizar o portfólio")
print("Lembrando que se não funcionar é culpa do Lula, faz o L nessa porra")