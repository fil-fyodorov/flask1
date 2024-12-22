from flask import Flask
from flask import request
from random import choice
from flask import abort

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


def get_new_quote_id():
    return quotes_text[-1]['id'] + 1


def exist_post_id(post_id):
    not_found = True
    quotes_block_id = -1
    for block in quotes_text:
        quotes_block_id += 1
        if block['id'] == post_id:
            not_found = False
            return quotes_block_id
    if not_found:
        return False


def quotes_count():
   count = {'count': len(quotes_text) }
   return count


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



# @app.route("/quotes", methods=['POST'])
# def create_quote():
#    data = request.json
#    print("data = ", data)
#    return {}, 201


@app.route("/quotes", methods=['POST'])
def create_quote():
    global quotes_text
    error = None
    if request.method == 'POST':
        data = request.json
        new_quote = {
            "id": get_new_quote_id(),
            "author": data['author'],
            "text":  data['text']
            }
        quotes_text.append(new_quote)
        return new_quote, 201
    return f'ERROR: {error}'



@app.route("/quotes/<id>", methods=['PUT'])
def edit_quote(id):
   global quotes_text
   if request.method == 'PUT':
       new_data = request.json
       quotes_block_id = exist_post_id(int(id))
       if quotes_block_id:
           if 'author' in new_data:
               quotes_text[quotes_block_id]['author'] = new_data['author']
           if 'text' in new_data:
               quotes_text[quotes_block_id]['text'] = new_data['text']
       else:
           abort(404)
       return quotes_text[quotes_block_id], 201


@app.route("/quotes/<id>", methods=['DELETE'])
def delete(id):
   global quotes_text
   # delete quote with id
   if request.method == 'DELETE':
       quotes_block_id = exist_post_id(int(id))
       if quotes_block_id:
           quotes_text.pop(quotes_block_id)
       else:
           abort(404)
       return f"Quote with id {id} is deleted.", 200








if __name__ == "__main__":
   app.run(debug=True)



