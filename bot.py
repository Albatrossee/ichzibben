# coding=utf-8
import telebot
from emoji import emojize
import redis
from redis import StrictRedis

r = redis.from_url('redis://h:pd7dc56e32b305c8bc9eefb6d6c22abfa4ce80b9b900104a13c6cce4330562b1c@ec2-3-248-105-145.eu'
                   '-west-1.compute.amazonaws.com:9059')

TOKEN = '1009563255:AAE6UK73KQHeZSeRjIlm7xky5a9b0MwFaJk'
bot = telebot.TeleBot(TOKEN)

heart = emojize(':heart:', use_aliases=True)
right = emojize(':right_arrow:', use_aliases=True)
left = emojize(':left_arrow:', use_aliases=True)

r.set(int(0), "Лиза\nhttps://telegra.ph/file/910f197fa35c0089c5d7d.png\nhttps://telegra.ph/Liza-11-15-2" +
      "\nЧерная пантера, которая никого не оставит равнодушным, она может повиноваться и может командовать."
      "\nВозраст: 28 года"
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
      "\n\nStatus: ")

r.set(int(1), "Виктория\nhttps://telegra.ph/file/23cc6900ea637a352acc4.jpg\nhttps://telegra.ph/Viktoriya-11-15-3" +
      "\nЛюбительница экспериментов , анальный секс приносит ей массу удовольствия им она всегда готова принять достойного мужчину и довести его до невероятного наслаждения ."
      "\nВозраст: 20 года"
      "\nВес: 49 кг"
      "\nРост: 172 см"
      "\nГрудь: 2 размер"
      "\nНациональность: украинка"
      "\nЦена: 2800грн час| 120$"
      "\n   Минет в презервативе"
      "\n   минет без презерватива"
      "\n   Классический секс"
      "\n   анальный секс +500 uah"
      "\n\nStatus: ")

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
      "\n\nStatus: ")

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
      "\n\nStatus: ")

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
      "\n\nStatus: ")

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

r.set(str('statuse' + '0'), "Busy")
r.set(str('statuse' + '1'), "Busy")
r.set(str('statuse' + '2'), "Busy")
r.set(str('statuse' + '3'), "Busy")
r.set(str('statuse' + '4'), "Busy")

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
    r.set('language' + str(message.chat.id), 'ukr')
    menu(message)


def menu(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.clear_step_handler_by_chat_id(message.chat.id)
    language = r.get('language' + str(message.chat.id)).decode('utf-8')
    user = r.get(str('Username') + str(message.chat.id)).decode('utf-8')
    centum = telebot.types.InlineKeyboardMarkup()
    if str(language) == 'ukr':
        centum.row(
            telebot.types.InlineKeyboardButton("Відкрити каталог", callback_data="kataloog")
        )
        centum.row(
            telebot.types.InlineKeyboardButton("Зв'язок", callback_data="support")
        )
        centum.row(
            telebot.types.InlineKeyboardButton("F.A.Q", callback_data="faq")
        )
        centum.row(
            telebot.types.InlineKeyboardButton("Language", callback_data="language")
        )
        bot.send_message(message.chat.id,
                         "Ласкаво просимо " + str(user) + "\n\n" + heart + "Раді бачити тебе в нашому оазисі "
                                                                           "задоволення" + heart,
                         reply_markup=centum)
    else:
        centum.row(
            telebot.types.InlineKeyboardButton("Open catalog", callback_data="kataloog")
        )
        centum.row(
            telebot.types.InlineKeyboardButton("Support", callback_data="support")
        )
        centum.row(
            telebot.types.InlineKeyboardButton("F.A.Q", callback_data="faq")
        )
        centum.row(
            telebot.types.InlineKeyboardButton("Мова", callback_data="language")
        )
        bot.send_message(message.chat.id,
                         "Welcome " + str(
                             user) + "\n\n" + heart + "We are glad to see you in our oasis pleasure" + heart,
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
    if data.startswith('language'):
        bot.answer_callback_query(query.id)
        language = r.get('language' + str(query.message.chat.id)).decode('utf-8')
        if str(language) == 'ukr':
            r.set('language' + str(query.message.chat.id), 'eng')
        else:
            r.set('language' + str(query.message.chat.id), 'ukr')
        menu(query.message)

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
        r.set(str('statuse' + number_of_whore), "Busy")
        katalog(query.message)
    if data.startswith('whorestatus2'):
        bot.answer_callback_query(query.id)
        number_of_whore = r.get((str('nomershluhi') + str(query.message.chat.id))).decode('utf-8')
        r.set(str('status' + number_of_whore), "Вільна")
        r.set(str('statuse' + number_of_whore), "Free")
        katalog(query.message)
    if data.startswith('whorestatus3'):
        bot.answer_callback_query(query.id)
        number_of_whore = r.get((str('nomershluhi') + str(query.message.chat.id))).decode('utf-8')
        r.set(str('status' + number_of_whore), "Не працює")
        r.set(str('statuse' + number_of_whore), "Does not work")
        katalog(query.message)


def katalog(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    number_of_whore = r.get((str('nomershluhi') + str(message.chat.id))).decode('utf-8')
    whore = r.get(number_of_whore).decode('utf-8')
    status = r.get('status' + str(number_of_whore)).decode('utf-8')
    statuse = r.get('statuse' + str(number_of_whore)).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id)
    katalogarrows = telebot.types.InlineKeyboardMarkup()
    language = r.get('language' + str(message.chat.id)).decode('utf-8')
    if str(language) == 'ukr':
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
                telebot.types.InlineKeyboardButton("Вільна", callback_data='whorestatus2'),
                telebot.types.InlineKeyboardButton("Не працює", callback_data='whorestatus3')

            )
        bot.send_message(message.chat.id, str(whore) + status, reply_markup=katalogarrows)
    else:
        katalogarrows.row(
            telebot.types.InlineKeyboardButton(left, callback_data="back"),
            telebot.types.InlineKeyboardButton(right, callback_data="go")
        )
        if str(statuse) == 'Free':
            katalogarrows.row(
                telebot.types.InlineKeyboardButton(heart + "Order" + heart, callback_data="pay")
            )
        katalogarrows.row(
            telebot.types.InlineKeyboardButton("Main page", callback_data="menu")
        )
        if str(message.chat.id) == "697601461":
            katalogarrows.row(
                telebot.types.InlineKeyboardButton("Busy", callback_data='whorestatus1'),
                telebot.types.InlineKeyboardButton("Free", callback_data='whorestatus2'),
                telebot.types.InlineKeyboardButton("Does not work", callback_data='whorestatus3')
            )
        if str(message.chat.id) == "854450608":
            katalogarrows.row(
                telebot.types.InlineKeyboardButton("Busy", callback_data='whorestatus1'),
                telebot.types.InlineKeyboardButton("Free", callback_data='whorestatus2'),
                telebot.types.InlineKeyboardButton("Does not work", callback_data='whorestatus3')
            )
        bot.send_message(message.chat.id, str(whore) + statuse, reply_markup=katalogarrows)


def adress(message):
    bot.delete_message(message.chat.id, message.message_id)
    language = r.get('language' + str(message.chat.id)).decode('utf-8')
    if str(language) == 'ukr':
        bot.send_message(message.chat.id, "Відправте боту вашу адресу")
    else:
        bot.send_message(message.chat.id, "Enter your adress")
    bot.register_next_step_handler(message, numphone)


def numphone(message):
    r.set('adress' + str(message.chat.id), str(message.text))
    bot.delete_message(message.chat.id, message.message_id - 1)
    bot.delete_message(message.chat.id, message.message_id)
    language = r.get('language' + str(message.chat.id)).decode('utf-8')
    if str(language) == 'ukr':
        bot.send_message(message.chat.id,
                         "Введіть номер телефону для зв'язку з вами\nНа нього буде звонити дівчина по приїзду на адресу")
    else:
        bot.send_message(message.chat.id,
                         "Enter the phone number to contact you \nThe girl on arrival will call to you")
    bot.register_next_step_handler(message, amounthourses)


def amounthourses(message):
    bot.delete_message(message.chat.id, message.message_id - 1)
    bot.delete_message(message.chat.id, message.message_id)
    r.set('numphone' + str(message.chat.id), str(message.text))
    language = r.get('language' + str(message.chat.id)).decode('utf-8')
    if str(language) == 'ukr':
        bot.send_message(message.chat.id, "Введіть кількість годин")
    else:
        bot.send_message(message.chat.id, "Enter the number of hours")
    bot.register_next_step_handler(message, price)


def price(message):
    language = r.get('language' + str(message.chat.id)).decode('utf-8')
    if str(language) == 'ukr':
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
    else:
        try:
            amount = int(message.text)
        except:
            bot.delete_message(message.chat.id, message.message_id - 1)
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(message.chat.id, "Please enter a number")
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
    language = r.get('language' + str(message.chat.id)).decode('utf-8')
    if str(language) == 'ukr':
        keyboard.row(
            telebot.types.InlineKeyboardButton("Оплатити UAH", url='https://telegra.ph/Oplata-11-15'),
            telebot.types.InlineKeyboardButton("Оплатити Bitcoin", callback_data='bitcoin')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton("Відмінити замовлення", callback_data='kataloog')
        )
    else:
        keyboard.row(
            telebot.types.InlineKeyboardButton("Pay UAH", url='https://telegra.ph/Oplata-11-15'),
            telebot.types.InlineKeyboardButton("Pay Bitcoin", callback_data='bitcoin')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton("Cancel order", callback_data='kataloog')
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
    bot.send_message(854450608,
                     "Заявка создана\n"
                     "\nМамонт: @" + str(mamont) +
                     "\nШлюха: " + name +
                     "\nНомер телефона: " + str(phone) +
                     "\nАдрес: " + str(adres))
    bot.register_next_step_handler(message, pay)


def pay(message):
    language = r.get('language' + str(message.chat.id)).decode('utf-8')
    if str(language) == 'ukr':
        if str(message.text) == 'back':
            menu(message)
        else:
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(message.chat.id, "Транзакція в обробці")
            bot.register_next_step_handler(message, pay)
    else:
        if str(message.text) == 'back':
            menu(message)
        else:
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(message.chat.id, "Transaction in progress")
            bot.register_next_step_handler(message, pay)


def support(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    language = r.get('language' + str(message.chat.id)).decode('utf-8')
    if str(language) == 'ukr':
        keyboard.row(
            telebot.types.InlineKeyboardButton("Повернутись", callback_data='menu')
        )
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "Контакт оператора: @girlslviv", reply_markup=keyboard)
    else:
        keyboard.row(
            telebot.types.InlineKeyboardButton("Back", callback_data='menu')
        )
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "Contact to support: @girlslviv", reply_markup=keyboard)



def faq(message):
    bot.delete_message(message.chat.id, message.message_id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    language = r.get('language' + str(message.chat.id)).decode('utf-8')
    if str(language) == 'ukr':
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
                                          "Залишились питання?\nПишіть: @girlslviv"

                         , reply_markup=keyboard)
    else:
        keyboard.row(
            telebot.types.InlineKeyboardButton("Back", callback_data='menu')
        )
        bot.send_message(message.chat.id, "🍓 Frequently Asked Questions 🍓\n\n"
                                            "🔥 How to place an order?"                                          
                                          "Choose the girl you are interested in, if she is free then there will be an active press 'Order' \nAfter pressing this, follow the instructions in the bot.\n\n"
                                          "🔥 How is payment made?\n"
                                          "We only work on a full prepayment for Easypay / bitcoint / This is a forced step through the complaints of the girls themselves, because clients often have no serious intentions, refused to pay or even beat and threatened.\n\n"
                                          "🔥 Why can't you give it a hand\n"
                                          "This is a forced move that the girls went through when they were called young without money / lied to pay after / threatened. Therefore, we have to work on a different principle.\n\n"
                                          "🔥 Do you have a place?\n"
                                          " Yes, every girl can take (apartments in the city.) Traveling outside the city is discussed\n\n"
                                          "Any questions left? \nWrite: @girlslviv"

                         , reply_markup=keyboard)


def bitcoin(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Оплатитb", url="https://24paybank.net/privat24-uah-to-bitcoin.html"),
        telebot.types.InlineKeyboardButton('Відмінити замовлення', callback_data='kataloog')
    )
    price = r.get((str("price") + str(message.chat.id))).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id)
    language = r.get('language' + str(message.chat.id)).decode('utf-8')
    if str(language) == 'ukr':
        bot.send_message(message.chat.id, "💳 Сумма до оплати: " + str(price) + "UAH" + "\n\n"
                                                                                    "⚠️ ВАЛЮТА BITCOIN  \n\n"
                                                                                    "👉  Для оплати перейдіть по посиланю и слідуйте інструкціям.\n\n "
                                                                                    "📨  Післе оплати провірте свій E-mail и пришліть боту TXid \n\n"
                                                                                    "👇 BTC АДРЕС 👇\n" + "1CmxR3gLFUpkZXcrk2QrzoGvRHKe1f5ToM",
                                                                        reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "💳 Amount to be paid: " + str(price) + "UAH" + "\n\n"
                                                                                        "⚠️  BITCOIN  \n\n"
                                                                                        "👉  To pay, follow the link and follow the instructions.\n\n "
                                                                                        "📨  After payment, check your E-mail and send a TXid bot \n\n"
                                                                                        "👇 BTC ADRESS 👇\n" + "1CmxR3gLFUpkZXcrk2QrzoGvRHKe1f5ToM",
                         reply_markup=keyboard)
    bot.register_next_step_handler(message, pay)



bot.polling(none_stop=True)
