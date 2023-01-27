import telebot

order_bt = telebot.types.InlineKeyboardButton("Замовити", callback_data="замовити")
site_bt = telebot.types.InlineKeyboardButton("Перейти до сайту", url="https://allo.ua/")

inline_list = []
inline_list.append(order_bt)
inline_list.append(site_bt)