import os
from pyrogram import Client, filters
from os import system as cmd
import shutil
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , CallbackQuery

bot = Client(
    "voluemincreaser",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="5442625381:AAEsUxtm8tthl0yDtHuFlZmdAQnqeY0IM94"
)

CHOOSE_UR_LANG = "اختر نمط التضخيم "
CHOOSE_UR_LANG_BUTTONS = [
    [InlineKeyboardButton("5db",callback_data="mod1")],
     [InlineKeyboardButton("10db",callback_data="mod2")],
     [InlineKeyboardButton("15db",callback_data="mod3")],
     [InlineKeyboardButton("20db",callback_data="mod4")],
     [InlineKeyboardButton("25db",callback_data="mod5")]
]


@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم , أنا بوت تضخيم الصوتيات\n\n  لبقية البوتات هنا \n\n https://t.me/ibnAlQyyim/1120 ",disable_web_page_preview=True)

@bot.on_message(filters.private & filters.incoming &  filters.audio | filters.voice  )
def _telegram_file(client, message):
  
  global user_id
  user_id = message.from_user.id 
  file = message.audio
  global file_path
  file_path = message.download(file_name="./downloads/")
  global filename
  filename = os.path.basename(file_path)
  message.reply(
             text = CHOOSE_UR_LANG,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_LANG_BUTTONS)

        )
@bot.on_callback_query()
def callback_query(CLIENT,CallbackQuery):
  global langtoken
  if CallbackQuery.data == "mod1":
      langtoken = 5
  elif CallbackQuery.data == "mod2":
      langtoken = 10
  elif CallbackQuery.data == "mod3":
      langtoken = 15
  elif CallbackQuery.data == "mod4" :
      langtoken = 20
  elif CallbackQuery.data == "mod5":
      langtoken = 25
  
  CallbackQuery.edit_message_text(
      
      "جار التضخيم"
  )   
  cmd(f'''ffmpeg -i "{file_path}" -filter:a volume={langtoken}dB "{filename}"''')
  with open(filename, 'rb') as f:
        bot.send_audio(user_id, f)
  shutil.rmtree('./downloads/') 
  cmd(f'''unlink "{filename}"''')



bot.run()
