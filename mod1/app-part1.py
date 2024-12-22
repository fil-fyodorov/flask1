from flask import Flask
from random import choice

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

about_me = {
   "name": "Федоров",
   "surname": "Филипп",
   "email": "fil-fyodorov@yandex.ru"
}


quotes_text = [
   {
       "id": 3,
       "author": "Rick Cook",
       "text": "Программирование сегодня — это гонка разработчиков программ, стремящихся писать программы с большей и лучшей идиотоустойчивостью, и вселенной, которая пытается создать больше отборных идиотов. Пока вселенная побеждает."
   },
   {
       "id": 5,
       "author": "Waldi Ravens",
       "text": "Программирование на С похоже на быстрые танцы на только что отполированном полу людей с острыми бритвами в руках."
   },
   {
       "id": 6,
       "author": "Mosher’s Law of Software Engineering",
       "text": "Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили."
   },
   {
       "id": 8,
       "author": "Yoggi Berra",
       "text": "В теории, теория и практика неразделимы. На практике это не так."
   },

]


@app.route("/about")
def about():
   return about_me


@app.route("/quotes")
def quotes():
   return quotes_text


@app.route("/quotes/rnd")
def show_random_post():
        return choice(quotes_text)


@app.route("/quotes/count")
def quotes_count():
   count = {'count': len(quotes_text) }
   return count


@app.route("/quotes/<int:post_id>")
def show_post(post_id):
    not_found = True
    for block in quotes_text:
        if block['id'] == post_id:
            not_found = False
            return block
    if not_found:
        return f"Quote with id={post_id} not found", 404


@app.route("/")  # Первый URL для обработки
def hello_world():  # Функция обработчик для этоо URL
   return "Hello, World!"


if __name__ == "__main__":
   app.run(debug=True)

