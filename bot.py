# coding=utf-8
import telebot
from emoji import emojize
import redis
from redis import StrictRedis

r = redis.from_url('redis://h:p1c62240a1b9b67829bd2100ae0da826cb3c2e4af6c91d1bcd057ab618daa6663@ec2-3-248-105-145.eu-west-1.compute.amazonaws.com:9639')

TOKEN = '1009563255:AAE6UK73KQHeZSeRjIlm7xky5a9b0MwFaJk'
bot = telebot.TeleBot(TOKEN)

heart = emojize(':heart:', use_aliases=True)
right = emojize(':right_arrow:', use_aliases=True)
left = emojize(':left_arrow:', use_aliases=True)

r.set(int(0), "Лиза\nhttps://telegra.ph/file/910f197fa35c0089c5d7d.png\nhttps://telegra.ph/Liza-11-15-2" +
      "\nЧерная пантера, которая никого не оставит равнодушным, она может повиноваться и может командовать."
      "\nВозраст: 28 лет"
      "\nВес: 60 кг"
      "\nРост: 170 см"
      "\nГрудь: 2 размер"
      "\nНациональность: украинка"
      "\nЦена: 2500грн час| 100$"
      "\n   Минет в презервативе"
      "\n   Классический секс"
      "\n   Легкая доминация"
      "\n   Страпон + 1000 грн"
      "\n   Золотой дождь  выдача"
      "\n   Кунилингус "
      "\n\nСтатус: ")

r.set(int(1), "Виктория\nhttps://telegra.ph/file/23cc6900ea637a352acc4.jpg\nhttps://telegra.ph/Viktoriya-11-15-3" +
      "\nЛюбительница экспериментов , анальный секс приносит ей массу удовольствия им она всегда готова принять достойного мужчину и довести его до невероятного наслаждения ."
      "\nВозраст: 20 лет"
      "\nВес: 49 кг"
      "\nРост: 172 см"
      "\nГрудь: 2 размер"
      "\nНациональность: украинка"
      "\nЦена: 2800грн час| 120$"
      "\n   Минет в презервативе"
      "\n   минет без презерватива"
      "\n   Классический секс"
      "\n   анальный секс +500 uah"
      "\n\nСтатус: ")

r.set(int(2), "Лера\nhttps://telegra.ph/file/edb9b4926ad16859127ba.jpg\nhttps://telegra.ph/Lera-11-15-5" +
      "\nНежная хрупкая девочка , может подарить любовь ту которую не подарит никто , будет заботливой и любящей , есть риски влюбиться"
      "\nВозраст: 22 года"
      "\nВес: 55 кг"
      "\nРост: 167 см"
      "\nГрудь: 1 размер"
      "\nНациональность: украинка"
      "\nЦена: 1800грн час| 65$"
      "\n   Минет в презервативе"
      "\n   Классический секс"
      "\n\nСтатус: ")

r.set(int(3), "Анастасия\nhttps://telegra.ph/file/b386cd099e3f30e944c2f.jpg\nhttps://telegra.ph/Anastasiya-11-15-3" +
      "\nОбожает секс , ее перед ее упругой попкой не сможет устоят даже самый ценитель женской красоты , любит подчинение и анальный секс."
      "\nВозраст: 23 года"
      "\nВес: 56 кг"
      "\nРост: 169 см"
      "\nГрудь: 2 размер"
      "\nНациональность: украинка"
      "\nЦена: 2500грн час| 100$"
      "\n   Минет в презервативе"
      "\n   минет без презерватива"
      "\n   Классический секс"
      "\n   анальный секс +1000 uah"
      "\n   Кунилингус "
      "\n   Подчинение ( легкая доминация , наручники ) + 1000 uah"
      "\n\nСтатус: ")

r.set(int(4), "Власта\nhttps://telegra.ph/file/806d69ba6efd591b9bcb4.jpg\nhttps://telegra.ph/Vlasta-11-15" +
      "\nНастоящая Госпожа , может подарить обычный секс , а может покорять под себя любого мужчину , любит управлять "
      "и подчинять под себя , может доставить наслаждение БДСМ . Есть большой набор игрушек , начиная от обычного "
      "страпона , заканчивая клипсами на соски , кляпом , плеткой . Так же есть костюмы из латекса .Если тебе "
      "нравиться БДСМ ты обязательно будешь у ее ног "
      "\nВозраст: 22 года"
      "\nВес: 53 кг"
      "\nРост: 169 см"
      "\nГрудь: 3 размер"
      "\nНациональность: украинка"
      "\nЦена: 2500грн час| 100$"
      "\n   Минет в презервативе"
      "\n   Классический секс"
      "\n   Госпожа (СТРАПОН , БДСМ , Золотой дождь  )+ 1000 UAH"
      "\n   Кунилингус "
      "\n\nСтатус: ")

r.set(int(100), "Лиза\nhttps://telegra.ph/file/c9bddef82a056c7d3b25f.jpg")
r.set(int(101), "Виктория\nhttps://telegra.ph/file/23cc6900ea637a352acc4.jpg")
r.set(int(102), "Лера\nhttps://telegra.ph/file/edb9b4926ad16859127ba.jpg")
r.set(int(103), "Анастасия\nhttps://telegra.ph/file/b386cd099e3f30e944c2f.jpg")
r.set(int(104), "Лиза\nhttps://telegra.ph/file/c9bddef82a056c7d3b25f.jpg")

r.set(str('status' + '0'), "На виклику")
r.set(str('status' + '1'), "На виклику")
r.set(str('status' + '2'), "На виклику")
r.set(str('status' + '3'), "На виклику")
r.set(str('status' + '4'), "На виклику")

r.set('price0', int(2500))
r.set('price1', int(2800))
r.set('price2', int(1800))
r.set('price3', int(2500))
r.set('price4', int(2500))


@bot.message_handler(commands=['start'])
def start_command(message):
    r.set(str('Username') + str(message.chat.id), str(message.from_user.username))
    r.set(str('ChatID') + str(message.chat.id), str(message.chat.id))
    r.set((str('nomershluhi') + str(message.chat.id)), int(0))
    r.set((str('Nomerokna') + str(message.chat.id)), int(0))
    menu(message)


def menu(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.clear_step_handler_by_chat_id(message.chat.id)
    centum = telebot.types.InlineKeyboardMarkup()
    centum.row(
        telebot.types.InlineKeyboardButton("Відкрити каталог", callback_data="kataloog")
    )
    centum.row(
        telebot.types.InlineKeyboardButton("Зв'язок", callback_data="support")
    )
    centum.row(
        telebot.types.InlineKeyboardButton("F.A.Q", callback_data="faq")
    )
    user = r.get(str('Username') + str(message.chat.id)).decode('utf-8')
    bot.send_message(message.chat.id,
                     "Ласкаво просимо " + str(user) + "\n\n" + heart + "Раді бачити тебе в нашому оазисі "
                                                                        "задоволення" + heart,
                     reply_markup=centum)


@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    if data.startswith('kataloog'):
        bot.answer_callback_query(query.id)
        katalog(query.message)
    if data.startswith('menu'):
        bot.answer_callback_query(query.id)
        menu(query.message)
    if data.startswith('pay'):
        bot.answer_callback_query(query.id)
        adress(query.message)
    if data.startswith('support'):
        bot.answer_callback_query(query.id)
        support(query.message)
    if data.startswith('faq'):
        bot.answer_callback_query(query.id)
        faq(query.message)
    if data.startswith('bitcoin'):
        bot.answer_callback_query(query.id)
        bitcoin(query.message)

    if data.startswith('back'):
        bot.answer_callback_query(query.id)
        if int(r.get((str("nomershluhi") + str(query.message.chat.id)))) > 0:
            r.decr((str("nomershluhi") + str(query.message.chat.id)), 1)
        else:
            r.set((str("nomershluhi") + str(query.message.chat.id)), int(4))
        katalog(query.message)
    if data.startswith('go'):
        bot.answer_callback_query(query.id)
        if int(r.get((str("nomershluhi") + str(query.message.chat.id)))) < 4:
            r.incr((str("nomershluhi") + str(query.message.chat.id)), 1)
        else:
            r.set((str("nomershluhi") + str(query.message.chat.id)), int(0))
        katalog(query.message)
    if data.startswith('whorestatus1'):
        bot.answer_callback_query(query.id)
        number_of_whore = r.get((str('nomershluhi') + str(query.message.chat.id))).decode('utf-8')
        r.set(str('status' + number_of_whore), "На виклику")
        katalog(query.message)
    if data.startswith('whorestatus2'):
        bot.answer_callback_query(query.id)
        number_of_whore = r.get((str('nomershluhi') + str(query.message.chat.id))).decode('utf-8')
        r.set(str('status' + number_of_whore), "Вільна")
        katalog(query.message)


def katalog(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    number_of_whore = r.get((str('nomershluhi') + str(message.chat.id))).decode('utf-8')
    whore = r.get(number_of_whore).decode('utf-8')
    status = r.get('status' + str(number_of_whore)).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id)
    katalogarrows = telebot.types.InlineKeyboardMarkup()
    katalogarrows.row(
        telebot.types.InlineKeyboardButton(left, callback_data="back"),
        telebot.types.InlineKeyboardButton(right, callback_data="go")
    )
    if str(status) == 'Вільна':
        katalogarrows.row(
            telebot.types.InlineKeyboardButton(heart + "Замовити" + heart, callback_data="pay")
        )
    katalogarrows.row(
        telebot.types.InlineKeyboardButton("На головну", callback_data="menu")
    )
    if str(message.chat.id) == "697601461":
        katalogarrows.row(
            telebot.types.InlineKeyboardButton("На виклику", callback_data='whorestatus1'),
            telebot.types.InlineKeyboardButton("Вільна", callback_data='whorestatus2')
        )
    bot.send_message(message.chat.id, str(whore) + status, reply_markup=katalogarrows)


def adress(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Відправте боту вашу адресу")
    bot.register_next_step_handler(message, numphone)


def numphone(message):
    r.set('adress' + str(message.chat.id), str(message.text))
    bot.delete_message(message.chat.id, message.message_id - 1)
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id,
                     "Введіть номер телефону для зв'язку з вами\nНа нього буде звонити дівчина по приїзду на адресу")
    bot.register_next_step_handler(message, amounthourses)


def amounthourses(message):
    bot.delete_message(message.chat.id, message.message_id - 1)
    bot.delete_message(message.chat.id, message.message_id)
    r.set('numphone' + str(message.chat.id), str(message.text))
    bot.send_message(message.chat.id, "Введіть кількість годин")
    bot.register_next_step_handler(message, price)


def price(message):
    try:
        amount = int(message.text)
    except:
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "Введіть числом")
        bot.register_next_step_handler(message, price)
    else:
        number_of_whore = r.get((str('nomershluhi') + str(message.chat.id))).decode('utf-8')
        pricebefore = r.get('price' + str(number_of_whore))
        priceuah = int(pricebefore) * int(amount)
        r.set('price' + str(message.chat.id), priceuah)
        order(message)


def order(message):
    number_of_whore = r.get((str('nomershluhi') + str(message.chat.id))).decode('utf-8')
    phone = r.get('numphone' + str(message.chat.id)).decode('utf-8')
    adres = r.get('adress' + str(message.chat.id)).decode('utf-8')
    name = r.get(int(number_of_whore) + int(100)).decode('utf-8')
    priceuah = r.get('price' + str(message.chat.id)).decode('utf-8')
    mamont = r.get(str('Username') + str(message.chat.id)).decode('utf-8')
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Оплатити UAH", url='https://telegra.ph/Oplata-11-15'),
        telebot.types.InlineKeyboardButton("Оплатити Bitcoin", callback_data='bitcoin')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Відмінити замовлення", callback_data='kataloog')
    )
    bot.delete_message(message.chat.id, message.message_id - 1)
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id,
                     "Звірте данні и оплатіть послугу\nДівчина приїде на протязі 30-40 хвилин після оплати и повідомить "
                     "вас дзвінком\n\nДівчина: " +
                     str(name) +
                     "\nАдреса: " + str(adres) +
                     "\nНомер телефону: " + str(phone) +
                     "\nЦіна: " + str(priceuah) + "UAH", reply_markup=keyboard)
    bot.send_message(697601461,
                     "Заявка создана\n"
                     "\nМамонт: @" + str(mamont) +
                     "\nШлюха: " + name +
                     "\nНомер телефона: " + str(phone) +
                     "\nАдрес: " + str(adres))
    bot.register_next_step_handler(message, pay)
    bot.register_next_step_handler(message, pay)


def pay(message):
    if str(message.text) == 'back':
        menu(message)
    else:

        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "Транзакція в обробці")
        bot.register_next_step_handler(message, pay)


def support(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Повернутись", callback_data='menu')
    )
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Контакт оператора: @MrPhotoshops", reply_markup=keyboard)


def faq(message):
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Повернутись", callback_data='menu')
    )
    bot.send_message(message.chat.id, "🍓 Відповіді на часті запитання 🍓\n\n"
                                      "🔥 Як зробити замовлення?"
                                      "Виберіть дівчину яка вас зацікавить, якщо вона вільна то буде активний натиск 'Замовити'\nПісля натиску слідуйте інструкціям в боті.\n\n"
                                      "🔥 Як відбувається оплата?\n"
                                      "Ми працюємо тільки за повною передоплатою на рахунок Easypay/bitcoint / Цевимушений крок через скарги самих дівчат, тому що клієнти часто не маютьсерйозних намірів, відмовлялися платити або навіть били та погрожували.\n\n"
                                      "🔥 Чому не можна дати на руки\n"
                                      "Це вимушений крок, на який дівчата пішли через випадки, коли їх викликалимолодики без грошей/брехали що заплатять після/погрожували. Тому ми змушеніпрацювати за іншим принципом.\n\n"
                                      "🔥 Я оплатив, що далі?\n"
                                      "Уточнюємо адрес, дівчина через 40-60 хв. приїжджає.\n\n"
                                      "🔥 Чи є у вас своє місце?\n"
                                      " Так, кожна дівчина може прийняти у себе (квартири по місті.) Виїзд за межі міста обговорюється\n\n"
                                      "Залишились питання?\nПишіть: @MrPhotoshops"

                     , reply_markup=keyboard)


def bitcoin(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Оплатитb", url="https://24paybank.net/privat24-uah-to-bitcoin.html"),
        telebot.types.InlineKeyboardButton('Відмінити замовлення', callback_data='kataloog')
    )
    price = r.get((str("price") + str(message.chat.id))).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "💳 Сумма до оплати: " + str(price) + "UAH" + "\n\n"
                                                                                   "⚠️ ВАЛЮТА BITCOIN  \n\n"
                                                                                   "👉  Для оплати перейдіть по посиланю и слідуйте інструкціям.\n\n "
                                                                                   "📨  Післе оплати провірте свій E-mail и пришліть боту TXid \n\n"
                                                                                   "👇 BTC АДРЕС 👇\n" + "1CmxR3gLFUpkZXcrk2QrzoGvRHKe1f5ToM",
                     reply_markup=keyboard)
    bot.register_next_step_handler(message, pay)


def lol(message):
    bot.send_message(697601461,
                     "Заявка создана\n"
                     "\nМамонт: @" + str(mamont) +
                     "\nШлюха: " + name)
    bot.register_next_step_handler(message, pay)
    return


bot.polling(none_stop=True)
