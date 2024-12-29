from flask import Flask
from flask import request
from random import choice
from flask import abort, jsonify

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
       "rating": 4,
       "author": "Rick_Cook",
       "text": "Программирование сегодня — это гонка разработчиков программ, стремящихся писать программы с большей и лучшей идиотоустойчивостью, и вселенной, которая пытается создать больше отборных идиотов. Пока вселенная побеждает."
    },
    {
       "id": 5,
       "rating": 6,
       "author": "Waldi Ravens",
       "text": "Программирование на С похоже на быстрые танцы на только что отполированном полу людей с острыми бритвами в руках."
    },
    {
        "author": "Rick_Cook",
        "id": 3,
        "rating": 4,
        "text": "Программирование сегодня — это гонка разработчиков программ, стремящихся писать программы с большей и лучшей идиотоустойчивостью, и вселенной, которая пытается создать больше отборных идиотов. Пока вселенная побеждает."
    },
    {
        "id": 6,
        "rating": 7,
        "author": "Mosher’s Law of Software Engineering",
        "text": "Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили."
    },
    {
       "id": 8,
       "rating": 9,
       "author": "Yoggi Berra",
       "text": "В теории, теория и практика неразделимы. На практике это не так."
    }
]


def get_new_quote_id():
    return quotes_text[-1]['id'] + 1


def exist_post_id(post_id):
    quotes_block_id = -1
    for block in quotes_text:
        quotes_block_id += 1
        if block['id'] == post_id:
            return quotes_block_id
    return False


def quotes_count():
   count = {'count': len(quotes_text) }
   return count


@app.route("/about")
def about():
   return jsonify(about_me), 200


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
    for block in quotes_text:
        if block['id'] == post_id:
            return block, 200
    return f"Quote with id={post_id} not found", 404


@app.route("/")  # Первый URL для обработки
def hello_world():  # Функция обработчик для этоо URL
   return jsonify(data="Hello, World!"), 200



# @app.route("/quotes", methods=['POST'])
# def create_quote():
#    data = request.json
#    print("data = ", data)
#    return {}, 201


@app.route('/quotes/filter', methods=['GET'])
def search():
    args = request.args
    author_value = args.get('author', default=None, type=str)
    rating_value = args.get('rating', default=None, type=int)
    result = []
    if None not in (author_value, rating_value):
        for block in quotes_text:
            if block['author'] == author_value and block['rating'] == rating_value:
                result.append(block)
    elif author_value is not None:
        for block in quotes_text:
            if block['author'] == author_value:
                result.append(block)
    elif rating_value is not None:
        for block in quotes_text:
            if  block['rating'] == rating_value:
                result.append(block)
    return result



@app.route("/quotes", methods=['POST'])
def create_quote():
    error = None
    if request.method == 'POST':
        data = request.json
        quote_rating = 1
        if 'rating' in data:
            quote_rating=data['rating']
            if quote_rating < 1 or quote_rating > 10:
                quote_rating = 1
        new_quote = {
            "id": get_new_quote_id(),
            "rating": quote_rating,
            "author": data['author'],
            "text":  data['text']
            }
        quotes_text.append(new_quote)
        return new_quote, 201
    return f'ERROR: {error}'



@app.route("/quotes/<int:id>", methods=['PUT'])
def edit_quote(id):
   # global quotes_text
   if request.method == 'PUT':
       new_data = request.json
       quotes_block_id = exist_post_id(id)
       if quotes_block_id:
           if 'author' in new_data:
               quotes_text[quotes_block_id]['author'] = new_data['author']
           if 'text' in new_data:
               quotes_text[quotes_block_id]['text'] = new_data['text']
           if 'rating' in new_data:
                if 0 < new_data['rating'] < 10:
                    quotes_text[quotes_block_id]['rating'] = new_data['rating']
       else:
           abort(404)
       return quotes_text[quotes_block_id], 201


@app.route("/quotes/<int:id>", methods=['DELETE'])
def delete(id):
   # global quotes_text
   # delete quote with id
   if request.method == 'DELETE':
       quotes_block_id = exist_post_id(id)
       if quotes_block_id:
           quotes_text.pop(quotes_block_id)
       else:
           abort(404)
       return f"Quote with id {id} is deleted.", 200






if __name__ == "__main__":
   app.run(debug=True)



