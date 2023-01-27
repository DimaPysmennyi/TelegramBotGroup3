import telebot
import modules.bot_creation as bc
@bc.bot.callback_query_handler(func=lambda callback: callback.data)
def processing_request(callback):
    if callback.data == "замовити":
        bc.bot.send_message(callback.message.chat.id, "Замовлення оформлено!")
        bc.bot.send_message(-1001655053559, text="Оформлено товар")