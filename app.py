from flask import Flask

app = Flask(__name__)


@app.route("/")  # Первый URL для обработки
def hello_world():  # Функция обработчик для этоо URL
   return "Hello, World!"


if __name__ == "__main__":
   app.run(debug=True)

