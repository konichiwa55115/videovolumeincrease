from pyrogram import Client, filters
import subprocess
import os
from os import system as cmd
import shutil


bot = Client(
    "myfirs",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="6251349619:AAHWY6-_BIwHqTUzvH62ukVUThjohP13d5k"
)
@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, "  السلام عليكم أنا بوت منتجة الفيديوهات . فقط أرسل التصميم ( الغلاف) بدون ضغط للحفاظ على جودة الفيديو \n\n Send without compression \n\n لبقية البوتات هنا \n\n https://t.me/ibnAlQyyim/1120",disable_web_page_preview=True)
    
@bot.on_message(filters.private & filters.incoming & filters.document | filters.photo)
def _telegram_file(client, message):
  if os.path.isdir("./downloads/") :
        sent_message = message.reply_text('هناك عملية يتم الآن . أرسل الصوتية  بعد مدة من فضلك', quote=True)
        return
  else :
        pass
  user_id = message.from_user.id
  sent_message = message.reply_text('الآن أرسل الصوتية', quote=True)
  file = message.document
  file_path = message.download(file_name="pic")
  global picture
  pictrue=file_path


    

@bot.on_message(filters.private & filters.incoming & filters.audio | filters.voice )
def _telegram_file(client, message):
  if os.path.isdir("./downloads/") :
        sent_message = message.reply_text('هناك عملية يتم الآن . أرسل الصوتية  بعد مدة من فضلك', quote=True)
        return
  else :
        pass
  user_id = message.from_user.id
  sent_message = message.reply_text('[جار منتجة الفيديو', quote=True)
  file = message.audio
  global file_path
  file_path = message.download(file_name="aud")
  global mp3file
  mp3file = "mp3file.mp3"
  global mp4file
  mp4file="mp4file.mp4"
  global picture
  picture = "./downloads/pic"
  global res 
  cmd(f'ffmpeg -i {file_path} -af arnndn=m=./rnnoise-models/somnolent-hogwash-2018-09-01/sh.rnnn ./downloads/"mod"+{mp3file} -y')
  cmd(f'ffmpeg -i ./downloads/"mod"+{mp3file} -af volume=2 ./downloads/{mp3file} -y ')
  cmd(f'ffmpeg -r 1 -loop 1 -y -i {picture} -i ./downloads/{mp3file} -c:v libx264 -tune stillimage -c:a copy -shortest -vf scale=1920:1080 ./downloads/{mp4file}')

    # Upload transcription file to user
  with open(f'./downloads/{mp4file}', 'rb') as f:
        bot.send_video(message.chat.id, f)
  shutil.rmtree('./downloads/')

  

@bot.on_message(filters.private & filters.incoming & filters.video )
def _telegram_file(client, message):
  if os.path.isdir("./downloads/") :
        sent_message = message.reply_text('هناك عملية يتم الآن . أرسل التصميم  بعد مدة من فضلك', quote=True)
        return
  else :
        pass
  
  user_id = message.from_user.id
  sent_message = message.reply_text('[جار منتجة الفيديو', quote=True)
  file = message.audio
  global file_path
  file_path = message.download(file_name="aud")
  global mp3file
  mp3file = "mp3file.mp3"
  global mp4file
  mp4file="mp4file.mp4" 
  tempmp3 = "mod"+mp3file
  cmd(f'ffmpeg -i {file_path} -q:a 0 -map a ./downloads/{mp3file} -y')
  cmd(f'ffmpeg -i ./downloads/{mp3file} -af arnndn=m=./rnnoise-models/somnolent-hogwash-2018-09-01/sh.rnnn ./downloads/{tempmp3} -y ')
  cmd(f'ffmpeg -i ./downloads/{tempmp3} -af volume=2 ./downloads/{mp3file} -y ')
  cmd(f'ffmpeg -i {file_path} -i ./downloads{mp3file} -c:v copy -map 0:v:0 -map 1:a:0 ./downloads/{mp4file} -y')
  with open(f'./downloads/{mp4file}', 'rb') as f:
        bot.send_video(message.chat.id, f)
  shutil.rmtree('./downloads/')




bot.run()
