import telebot 
import modules.bot_creation as bc
import modules.keyboard_creation as kc
import modules.button_creation
import modules.button_press as bp
import modules.request

@bc.bot.message_handler(commands=["start"])
def bot_start(message):
    bc.bot.send_message(message.chat.id, "Hello", reply_markup=kc.reply_keyboard)
    bc.bot.register_next_step_handler(message, bp.press_new_sale_discounts)

bc.bot.polling(none_stop=True)