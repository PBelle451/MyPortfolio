from app import app

# Render e Gunicorn procuram pela variável "app" aqui
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
