heroku git:remote -a pidoras-nerealny
import random

import telebot
from telebot import types
from random import choice

kinospis = []
TOKEN = '5220484316:AAH8hWz7oGmQsfTCZuRZHPnjfu4saHZezUU'
bot = telebot.TeleBot(TOKEN)
joke = ['''– Пап, расскажи сказку?
        – В тридесятом царстве, однатретьем государстве...
        – Обычно, говорят "тридевятом государстве".
        – Я сократил''',
        '''Как называется травля со стороны подъездных бабок?

        Бабуллинг''',
        '''В солдатской столовой рядовой говорит прапорщику:
        - Товарищ прапорщик, мне же мясо положено!?
        - Положено - ешь
        Солдат показывает в тарелку:
        - Так оно ведь не положено
        - Не положено - не ешь.''',
        '''Ебет один клоун другого, а тот смеется.
        - Ты чего смеешься?
        - Да чет смешно стало хз''',
        'Потерпевший кораблекрушение отправляет в бутылке записку: '
        '"Я на необитаемом острове помогите'
        ' выбратся вы моя единственная надежда"   Бутылка возвращается через 3 года '
        'с ответом: "-ться"']
status = [1]

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет котик, МЯУ, надеюсь я тебе помогу с этим '
                                      'КиноПоиском :3')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    joker = types.KeyboardButton('Анекдот')
    cinema_info = types.KeyboardButton('Статус кино')

    markup.add(joker, cinema_info)

    bot.send_message(message.chat.id, 'По этому могу только повторять, МЯУ, за тобой и '
                                      'рассказывать анекдоты, хотяяяяя и анекдотов не '
                                      'так что бы много))00) <3', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Анекдот':
            bot.send_message(message.chat.id, choice(joke))
        elif message.text == '+':
            status.append(1)
            bot.send_message(message.chat.id, 'Надеюсь просмотр был замурчательным!')
        elif message.text == 'Хорошо':
            markup = types.InlineKeyboardMarkup(row_width=2)
            stand_up = types.InlineKeyboardButton('Закончить просмотр', callback_data='up')

            markup.add(stand_up)

            bot.send_message(message.chat.id, 'Как закончишь, ответь пожалуйста', reply_markup=markup)
        elif message.text == 'Статус кино':
            if status:

                markup = types.InlineKeyboardMarkup(row_width=2)
                sit = types.InlineKeyboardButton("Хорошо", callback_data='lock')
                go_away = types.InlineKeyboardButton("Нет, спасибо", callback_data='go')
                markup.add(sit, go_away)

                bot.send_message(message.chat.id, 'Котозал свободен, МЯУ, можешь занять место 8)', reply_markup=markup)


            elif not status:
                bot.send_message(message.chat.id, 'Извинииите, МЯУ, ваше золотце расселось на все МЯУста,'
                                                  'это же не позволительно!!!, советую провести беседу!')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'lock':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton('Закончить', callback_data='end')
                markup.add(item1)

                status.remove(1)
                bot.send_message(call.message.chat.id, '''Уважаемы коть, вы заняли место,
НО ФТО ЭТО ЗА УВАФФФ!
Никогда не видел такой наглости...
Один коть, а занял все места 🤦
как закончишь, не забудь нажать на кнопочку, пожалуйста''', reply_markup=markup)

            elif call.data == 'end':
                bot.send_message(call.message.chat.id, 'Я знаю у нас котиков 9 жизней, но все же, МУРдачи!')
                status.append(1)
    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
