from random import choice

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


# print(quotes_text[3])
# print(quotes_text[1]['id'])

id = 2
for block in quotes_text:
    if block['id'] == id:
        print(block)

# : /quotes/count
# print(len(quotes_text))
#
# print(quotes_text[-1]['id'] + 1)


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

print(exist_post_id(5))




# {
#     "author": "Tom",
#     "text": "Tom qoute"
# }




