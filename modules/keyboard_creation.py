import telebot
import modules.bot_creation as bc
import modules.button_creation as btn
import modules.inline_buttons as inline_btn

reply_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True) 
inline_keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

for button in btn.button_list:
    reply_keyboard.add(button)
for inline_button in inline_btn.inline_list:
    inline_keyboard.add(inline_button)                                                                                                                                                                                                                                                              