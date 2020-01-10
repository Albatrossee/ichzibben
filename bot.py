import telebot
from emoji import emojize
import redis
from redis import StrictRedis

r = redis.from_url(
    'redis://h:pd7dc56e32b305c8bc9eefb6d6c22abfa4ce80b9b900104a13c6cce4330562b1c@ec2-108-128-193-168.eu-west-1.compute.amazonaws.com:17559')

TOKEN = '884177238:AAFzd-8864_z5vsdCKqJxZ64OK240nf8rEY'
bot = telebot.TeleBot(TOKEN)
value = 0
price = 0

mushroom = emojize(":mushroom:", use_aliases=True)
snowflake = emojize(":snowflake:", use_aliases=True)
lemon = emojize(":lemon:", use_aliases=True)
heart = emojize(":heart:", use_aliases=True)
rainbow = emojize(':rainbow:', use_aliases=True)
candy = emojize(":candy:", use_aliases=True)
ak = emojize(":skull:", use_aliases=True)
kokos = emojize(":coconut:", use_aliases=True)
syringe = emojize(":syringe:", use_aliases=True)


@bot.message_handler(commands=['start'])
def start_command(message):
    r.set(str(message.chat.id), str(message.from_user.username))
    r.set('messageid' + str(message.chat.id), message.message_id)
    bot.delete_message(message.chat.id, message.message_id)
    firstmenu(message)


def firstmenu(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Тульчин', callback_data='warsaw'),
        telebot.types.InlineKeyboardButton('Вапнярка', callback_data='lodz')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Немирів', callback_data='poznan'),
        telebot.types.InlineKeyboardButton('Брацлав', callback_data='gdansk')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Отзывы', url='https://t.me/draghoney')
    )
    if str(message.chat.id) == '697601461':
        keyboard.row(
            telebot.types.InlineKeyboardButton('Отправить сообщение мамонтам', callback_data='sentmamont')
        )

    bot.send_photo(message.chat.id, 'https://telegra.ph/file/5e33ec112ea474d53ea66.png', reply_markup=keyboard)


def secondmenu(message):
    bot.delete_message(message.chat.id, message.message_id)
    city = r.get('city' + str(message.chat.id)).decode('utf-8')
    if str(city) == 'Тульчин':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 1г', callback_data='amf1'),
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 3г', callback_data='amf2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Сатива 1г', callback_data='weed1'),
            telebot.types.InlineKeyboardButton(ak + 'Голландия 1г', callback_data='ak1')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu')
        )
        bot.send_photo(message.chat.id, 'https://nyc3.digitaloceanspaces.com/ur-media2/photos/images/000/005/795'
                                        '/34aecddd56db6db9f3274bf29adf240915fca30f_big.jpg?1339084603',
                       reply_markup=keyboard)
    if str(city) == 'Вапнярка':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 1г', callback_data='amf1'),
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 2г', callback_data='amf2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Шишки 1г', callback_data='weed1'),
            telebot.types.InlineKeyboardButton(ak + 'Голландия 1г', callback_data='ak1')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu')
        )
        bot.send_photo(message.chat.id, 'https://photos.wikimapia.org/p/00/04/06/96/27_big.jpg', reply_markup=keyboard)
    if str(city) == 'Немирів':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 1г', callback_data='amf1'),
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 2г', callback_data='amf2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Шишки 1г', callback_data='weed1'),
            telebot.types.InlineKeyboardButton(ak + 'Голландия 1г', callback_data='ak1')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu')
        )
        bot.send_photo(message.chat.id, 'https://kompromat1.live/foto/articles_foto/2019/03/26/112568.jpg', reply_markup=keyboard)
    if str(city) == 'Брацлав':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 1г', callback_data='amf1'),
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 2г', callback_data='amf2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Шишки 1г', callback_data='weed1'),
            telebot.types.InlineKeyboardButton(ak + 'Голландия 1г', callback_data='ak1')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu')
        )
        bot.send_photo(message.chat.id, 'http://pimg.mycdn.me/getImage?disableStub=true&type=VIDEO_S_720&url=https%3A'
                                        '%2F%2Fvdp.mycdn.me%2FgetImage%3Fid%3D96100092575%26idx%3D1%26thumbType%3D32'
                                        '%26f%3D1&signatureToken=LKw2iVzkfMfg8AmJb2b43g',
                       reply_markup=keyboard)


def rajonwars(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('BTC', callback_data='online'),
        telebot.types.InlineKeyboardButton('EasyPay', callback_data='pszelew')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Отменить заказ", callback_data='backmenu')
    )
    city = r.get('city' + str(message.chat.id)).decode('utf-8')
    stuff = r.get((str("Staff") + str(message.chat.id))).decode('utf-8')
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, 'Заявка создана'
                                      '\nГород: ' + str(city) +
                     '\nПродукт: ' + str(stuff) +
                     '\nЦена: ' + str(price) + 'UAH', reply_markup=keyboard
                     )


def online(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Отменить заказ', callback_data='cancleorder')
    )
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "💳 Сумма к оплате: " + str(price) + "UAH" + "\n\n"
                                                                                  "⚠️ ВАЛЮТА BITCOIN  \n\n"
                                                                                  "👉  Получено 0 BTC\n\n "
                                                                                  "🔗 Список поступивших платежей обновляется раз в пять минут, пожалуйста, подождите...\n"
                                                                                  "⚠️ Переведите на BTC кошелек в течении 24 часов\n"
                                                                                  
                                                                                  "👇 BTC АДРЕС 👇\n" + "19zCSTupegnk3vQEkZYN6ExY5TzqTLWSEm",
                     reply_markup=keyboard)
    bot.register_next_step_handler(message, obrabotka)
    city = r.get('city' + str(message.chat.id)).decode('utf-8')
    staff = r.get((str("Staff") + str(message.chat.id))).decode('utf-8')
    mamont = r.get(str(message.chat.id)).decode('utf-8')
    bot.send_message(697601461,
                     "Заявка создана\n"
                     'Город: ' + str(city) +
                     "\nПродукт: " + str(staff) +
                     "\nЦена: " + str(price) +
                     "\nМамонт: @" + str(mamont) +
                     "\nID: @" + str(message.chat.id) +
                     "\nОплата: Online")


def pszelew(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Отменить заказ', callback_data='cancleorder')
    )
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "💳 Сумма к оплате: " + str(price) + "UAH" + "\n\n"
                                                                                  "⚠️ ВАЛЮТА UAH  \n\n"
                                                                                  "👉  Для оплаты переведите " + str(
        price) + "UAH на кошелек EasyPay в течение 30 минут\n\n "
                 "🔗 Кошелек: 37799388\n\n"
                 "📨  Отправьте сообщением ИД транзакции (ІД операції).\n\n"
                 "- Для проверки оплаты, отправьте ID транзакции с чека или квитанции.\n\n"
                 "- Отправлять нужно ТОЛЬКО ЦИФРЫ!\n\n", reply_markup=keyboard)
    bot.register_next_step_handler(message, obrabotka)
    city = r.get('city' + str(message.chat.id)).decode('utf-8')
    staff = r.get((str("Staff") + str(message.chat.id))).decode('utf-8')
    mamont = r.get(str(message.chat.id)).decode('utf-8')
    bot.send_message(697601461,
                     "Заявка создана\n"
                     'Город: ' + str(city) +
                     "\nПродукт: " + str(staff) +
                     "\nЦена: " + str(price) +
                     "\nМамонт: @" + str(mamont) +
                     "\nID: @" + str(message.chat.id) +
                     "\nОплата: Przelew")




def obrabotka(message):
    if message.text == "back":
        bot.delete_message(message.chat.id, message.message_id - 1)
        firstmenu(message)
    else:
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "Данные проверяются\nОжидайте ответ от оператора")
        bot.register_next_step_handler(message, obrabotka)


def delivery(message):
    bot.send_message(message.chat.id,
                     "Цена доставки: 100UAH\nПосле оплаты с вами свяжется курьер\nВведите адрес доставки")
    bot.delete_message(message.chat.id, message.message_id)
    bot.register_next_step_handler(message, deliveryadress)


def deliveryadress(message):
    city = r.get("city" + str(message.chat.id)).decode('utf-8')
    staff = r.get((str("Staff") + str(message.chat.id))).decode('utf-8')
    price1 = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    r.set((str("Price") + str(message.chat.id)), int(price1) + 100)
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
            telebot.types.InlineKeyboardButton('BTC', callback_data='online'),
        telebot.types.InlineKeyboardButton('EasyPay', callback_data='pszelew')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Отменить заказ", callback_data='backmenu')
    )
    bot.delete_message(message.chat.id, message.message_id)
    bot.delete_message(message.chat.id, message.message_id - 1)
    bot.send_message(message.chat.id, "Ваш заказ: " + str(message.message_id) +
                     "\nГород: " + str(city) +
                     "\nТовар: " + str(staff) +
                     "\nЦена: " + str(price) + "UAH"
                                               "\nВыберите удобный метод оплаты: ", reply_markup=keyboard)


def sentmamont(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Введи ID мамонта")
    bot.register_next_step_handler(message, getid)


def getid(message):
    bot.delete_message(message.chat.id, message.message_id - 1)
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, 'Что отправить ?')
    chatid = str(message.text)
    bot.register_next_step_handler(message, sendmess, chatid)


def sendmess(message, chatid):
    bot.delete_message(message.chat.id, message.message_id)
    try:
        bot.send_message(chatid, str(message.text))
    except:
        bot.send_message(message.chat.id, 'шото не так')
        firstmenu(message)
    else:
        firstmenu(message)


@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    if data.startswith('backmenu'):
        bot.answer_callback_query(query.id)
        bot.delete_message(query.message.chat.id, query.message.message_id)
        firstmenu(query.message)
    if data.startswith('warsaw'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Тульчин')
        secondmenu(query.message)
    if data.startswith('lodz'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Вапнярка')
        secondmenu(query.message)
    if data.startswith('poznan'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Немирів')
        secondmenu(query.message)
    if data.startswith('gdansk'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Брацлав')
        secondmenu(query.message)
    if data.startswith('amf1'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " из города " + str(city) + " втыкает на амф")
        r.set((str("Staff") + str(query.message.chat.id)), "Амф 1г")
        r.set((str("Price") + str(query.message.chat.id)), "350")
        rajonwars(query.message)
    if data.startswith('amf2'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " из города " + str(city) + " втыкает на амф")
        r.set((str("Staff") + str(query.message.chat.id)), "Амф 3г")
        r.set((str("Price") + str(query.message.chat.id)), "800")
        rajonwars(query.message)
    if data.startswith('weed1'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " из города " + str(city) + " втыкает на шмаль")
        r.set((str("Staff") + str(query.message.chat.id)), "Шишки 1г")
        r.set((str("Price") + str(query.message.chat.id)), "150")
        rajonwars(query.message)
    if data.startswith('weed2'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " из города " + str(city) + " втыкает на шмаль")
        r.set((str("Staff") + str(query.message.chat.id)), "Шишки 2г")
        r.set((str("Price") + str(query.message.chat.id)), "300")
        rajonwars(query.message)
    if data.startswith('weed5'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " из города " + str(city) + " втыкает на шмаль")
        r.set((str("Staff") + str(query.message.chat.id)), "Шишки 5г")
        r.set((str("Price") + str(query.message.chat.id)), "1100")
        rajonwars(query.message)
    if data.startswith('ak1'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " из города " + str(city) + " втыкает на шмаль")
        r.set((str("Staff") + str(query.message.chat.id)), "Голландия 1г")
        r.set((str("Price") + str(query.message.chat.id)), "250")
        rajonwars(query.message)
    if data.startswith('ak2'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " из города " + str(city) + " втыкает на шмаль")
        r.set((str("Staff") + str(query.message.chat.id)), "Шишки AK47 2г")
        r.set((str("Price") + str(query.message.chat.id)), "600")
        rajonwars(query.message)
    if data.startswith('ak3'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " из города " + str(city) + " втыкает на шмаль")
        r.set((str("Staff") + str(query.message.chat.id)), "Шишки AK47 5г")
        r.set((str("Price") + str(query.message.chat.id)), "1300")
        rajonwars(query.message)
    if data.startswith('mef1'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " из города " + str(city) + " втыкает на мефедрон")
        r.set((str("Staff") + str(query.message.chat.id)), "Мефедрон 1г")
        r.set((str("Price") + str(query.message.chat.id)), "600")
        rajonwars(query.message)
    if data.startswith('mef2'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " из города " + str(city) + " втыкает на мефедрон")
        r.set((str("Staff") + str(query.message.chat.id)), "Мефедрон 2г")
        r.set((str("Price") + str(query.message.chat.id)), "1100")
        rajonwars(query.message)
    if data.startswith('mef3'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " из города " + str(city) + " втыкает на мефедрон")
        r.set((str("Staff") + str(query.message.chat.id)), "Мефедрон 3г")
        r.set((str("Price") + str(query.message.chat.id)), "1500")
        rajonwars(query.message)
    if data.startswith('mushrooms1'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " из города " + str(city) + " втыкает на грибы")
        r.set((str("Staff") + str(query.message.chat.id)), "Грибы 3г")
        r.set((str("Price") + str(query.message.chat.id)), "700")
        rajonwars(query.message)
    if data.startswith('mushrooms2'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " из города " + str(city) + " втыкает на грибы")
        r.set((str("Staff") + str(query.message.chat.id)), "Грибы 6г")
        r.set((str("Price") + str(query.message.chat.id)), "1300")
        rajonwars(query.message)
    if data.startswith('lsd'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " из города " + str(city) + " втыкает на марки")
        r.set((str("Staff") + str(query.message.chat.id)), "Марка(LSD)")
        r.set((str("Price") + str(query.message.chat.id)), "400")
        rajonwars(query.message)
    if data.startswith('marka'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " из города " + str(city) + " втыкает на марки")
        r.set((str("Staff") + str(query.message.chat.id)), "Марка(LSD) 2шт")
        r.set((str("Price") + str(query.message.chat.id)), "650")
        rajonwars(query.message)
    if data.startswith('ecstasy'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " из города " + str(city) + " втыкает на таблетки")
        r.set((str("Staff") + str(query.message.chat.id)), "Экстази 'Superman' 1шт")
        r.set((str("Price") + str(query.message.chat.id)), "450")
        rajonwars(query.message)
    if data.startswith('lalka'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " из города " + str(city) + " втыкает на таблетки")
        r.set((str("Staff") + str(query.message.chat.id)), "Экстази 'Superman' 5шт")
        r.set((str("Price") + str(query.message.chat.id)), "2000")
        rajonwars(query.message)
    if data.startswith('zappa'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " из города " + str(city) + " втыкает на таблетки")
        r.set((str("Staff") + str(query.message.chat.id)), "Экстази 'Superman' 2шт")
        r.set((str("Price") + str(query.message.chat.id)), "650")
        rajonwars(query.message)
    if data.startswith('cocaina'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " из города " + str(city) + " втыкает на кокс")
        r.set((str("Staff") + str(query.message.chat.id)), "Кокаин 0.5г")
        r.set((str("Price") + str(query.message.chat.id)), "2300")
        rajonwars(query.message)
    if data.startswith('subitex'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(697601461, "@" + str(user) + " из города " + str(city) + " втыкает на субитекс")
        r.set((str("Staff") + str(query.message.chat.id)), "Субитекс 1шт")
        r.set((str("Price") + str(query.message.chat.id)), "320")
        rajonwars(query.message)
    if data.startswith('cancleorder'):
        bot.answer_callback_query(query.id)
        bot.delete_message(query.message.chat.id, query.message.message_id)
        firstmenu(query.message)
    if data.startswith('online'):
        bot.answer_callback_query(query.id)
        online(query.message)
    if data.startswith('terminal'):
        bot.answer_callback_query(query.id)
        terminal(query.message)
    if data.startswith('pszelew'):
        bot.answer_callback_query(query.id)
        pszelew(query.message)
    if data.startswith('sentmamont'):
        bot.answer_callback_query(query.id)
        sentmamont(query.message)


bot.polling(none_stop=True)
