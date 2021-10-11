from telebot import TeleBot
import config

bot = TeleBot(config.API)

@bot.message_handler(commands=['start'])
def welcome(message):

    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    message_text = message.text

    print(f"{str(user_id) + ' ' + user_first_name} написал {message_text}")
    bot.reply_to(message, 'Приветствую, хозяин!')

if __name__=="__main__":
    bot.polling(none_stop=True, timeout=60)
