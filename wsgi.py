from main import app

app.debug = False

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
