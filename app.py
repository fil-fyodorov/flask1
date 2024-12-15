from flask import Flask

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

about_me = {
   "name": "Фдоров",
   "surname": "Филипп",
   "email": "fil-fyodorov@yandex.ru"
}


@app.route("/about")
def about():
   return about_me


@app.route("/")  # Первый URL для обработки
def hello_world():  # Функция обработчик для этоо URL
   return "Hello, World!"


if __name__ == "__main__":
   app.run(debug=True)

