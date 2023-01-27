import telebot
import modules.bot_creation as bc
import modules.keyboard_creation as kc
import modules.path as path


def press_new_sale_discounts(message):
    if message.text == "NEW" or message.text == "DISCOUNTS" or message.text == "SALE":
        photo_blue = path.find_path("images\\1.jpg")
        photo_green = path.find_path("images\\2.jpg")
        photo_pink = path.find_path("images\\3.jpg")
        photo_purple = path.find_path("images\\4.jpg")
        photo_transparent_clear= path.find_path("images\\5.jpg")
    
        bc.bot.send_photo(message.chat.id, open(photo_blue, "rb"), "Apple iPhone 14 Pro Max 128GB Deep Purple (MQ9T3)", reply_markup=kc.inline_keyboard)
        bc.bot.send_photo(message.chat.id, open(photo_green, "rb"), "Apple iPhone 14 Pro Max 256GB Gold (MQ9W3)", reply_markup=kc.inline_keyboard)
        bc.bot.send_photo(message.chat.id, open(photo_pink, "rb"), "Apple iPhone 14 Pro Max 128GB Space Black (MQ9P3)", reply_markup=kc.inline_keyboard)
        bc.bot.send_photo(message.chat.id, open(photo_purple, "rb"), "Apple iPhone 14 Pro Max 512GB Silver (MQAH3)", reply_markup=kc.inline_keyboard)
        bc.bot.send_photo(message.chat.id, open(photo_transparent_clear, "rb"), "Apple iPhone 14 Pro Max 128GB Gold (MQ9R3)", reply_markup=kc.inline_keyboard)
    