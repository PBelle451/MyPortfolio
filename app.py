from flask import Flask, render_template

app = Flask(__name__)

# Página inicial
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/skills')
def skills():
    skills = [
        {"name": "Python", "level": "90%", "years": "5 anos"},
        {"name": "HTML/CSS", "level": "75%", "years": "4 anos"},
        {"name": "Javascript", "level": "50%", "years": "4 anos"},
        {"name": "C++", "level": "50%", "years": "4 anos"},
        {"name": "SQL Server", "level": "50%","years": "4 anos"},
        {"name": "Java", "level": "50%", "years": "3 anos"},
        {"name": "Bootstrap", "level": "50%", "years": "2 anos"},
        {"name": "Django", "level": "40%", "years": "2 anos"},
        {"name": "Docker", "level": "40%", "years": "2 anos"},
        {"name": "Typescript", "level": "30%", "years": "1 ano"},
        {"name": "Angular", "level": "20%", "years": "1 ano"},
        {"name": "Haskell",  "level": "20%", "years": "1 ano"},
        {"name": "PostgresSQL", "level": "20%", "years": "1 ano"},
        {"name": "Flask", "level": "20%", "years": "1 ano"}
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
            'title': 'ECommerce',
            'description': 'A small ecommerce website I made in order to practice my knowledge in HTML, CSS, Javascript and Bootstrap',
            'tech': 'HTML, CSS, Bootstrap, Javascript',
            'link': 'https://github.com/PBelle451/ECommerce'
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
        }
    ]
    return render_template('projects.html', projects=projects)

# Página de contato
@app.route('/contact')
def contact():
    contact_info = [
        {'name': 'E-Mail', 'link': 'lordbelle7@gmail.com'},
        {'name': 'LinkedIn', 'link': 'https://www.linkedin.com/in/pedro-belle-5b4b8b1b7/'},
        {'name': 'Github', 'link': 'https://github.com/PBelle451'},
        {'name': 'Whatsapp', 'link': 'https://api.whatsapp.com/send?phone=56199948985'}
    ]
    return render_template('contact.html', contact=contact_info)


if __name__ == '__main__':
    app.run(debug=True)