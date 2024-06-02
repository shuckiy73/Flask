from flask_bootstrap import Bootstrap4
from flask import Flask, render_template

app = Flask(__name__)
bootstrap = Bootstrap4(app)

@app.route("/")
def index():
    return render_template("index.html", h1 = "Главная страница")

@app.route("/about")
def get_page_about():
    return render_template("about.html", h1 = "О приложении")

if __name__ == "__main__":
    app.run(debug=True)