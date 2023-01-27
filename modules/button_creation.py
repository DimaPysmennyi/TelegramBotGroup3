import telebot

button_list = []

button_new = telebot.types.KeyboardButton("NEW")
button_sale = telebot.types.KeyboardButton("SALE")
button_discounts = telebot.types.KeyboardButton("DISCOUNTS")

button_list.append(button_new)
button_list.append(button_sale)
button_list.append(button_discounts)