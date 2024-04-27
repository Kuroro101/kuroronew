import requests , re
import telebot 

url = "https://m.photofunia.com/categories/halloween/blood_writing"

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryohlfuyMygb1aEMcp',
    'Referer': 'https://m.photofunia.com/categories/halloween/blood_writing',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
}
token = "Token"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=["start"])
def welcome(message):
	bot.reply_to(message,'مـرحـبـاً انـا بـوت كـتـابـة الاسـم عـلى حائط بــدم ')
	
@bot.message_handler(content_types=['text'])
def dm(message):
    text = message.text
    data = f'------WebKitFormBoundaryohlfuyMygb1aEMcp\r\nContent-Disposition: form-data; name="text"\r\n\r\n{text}\r\n------WebKitFormBoundaryohlfuyMygb1aEMcp--\r\n'
    
    try:
    	response = requests.post(url,headers=headers,data=data).text
    	
    	img = re.findall('''<ul class="images">
                     <li>
               <a href="(.*?)?download">
                  Large</a>
            </li>''', response)[0]
    	im = img.split('?')[:1][0]
    	bot.send_photo(message.chat.id,im,reply_to_message_id=message.message_id)
    except:
        bot.reply_to(message, "حـاول بـوقت اخـر")

bot.infinity_polling()