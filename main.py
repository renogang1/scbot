import telebot
import subprocess
bot = telebot.TeleBot('токен типа')
# start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'gavno')
# help
@bot.message_handler(commands=["help"])
def help(m, res=False):
    bot.send_message(m.chat.id,'/scexport - get exportnames of .sc')
# about
@bot.message_handler(commands=["tool_about"])
def about(m, res=False):
    bot.send_message(m.chat.id, 'amazing tool')

@bot.message_handler(commands=["scexport"])
def eft (m, res=False):
    bot.send_message(m.chat.id, 'Give me .sc file (not _tex.sc!)')
    @bot.message_handler(content_types=['document'])
    def handle_file(message):
        try:
            file_name = message.document.file_name
            savedir = 'files\\' + file_name
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            with open(savedir, 'wb') as new_file:
                new_file.write(downloaded_file)
            bot.reply_to(message, 'Thinking about it...')
            subprocess.call(['node', 'main.js', savedir, 'true', 'true'])
            bot.send_message(m.chat.id, 'Done! Sending...')
            f = open("export_names.txt","rb")
            bot.send_document(m.chat.id, f)
        except Exception as e:
            bot.reply_to(message, e)

# startbot
bot.polling(none_stop=True, interval=0)