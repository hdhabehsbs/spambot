 
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot("token", skip_pending=True)

@bot.message_handler(commands=["start"])
def menu(message):
    markup = InlineKeyboardMarkup(row_width=2)
    kanal = InlineKeyboardButton("📣 Kanalımız", url="https://t.me/WixstraGod")
    koruma = InlineKeyboardButton("Korumaya Al 🛡️", url="https://t.me/SpamProtectronOfficalBot?startgroup=a")
    markup.add(kanal,koruma)
    bot.send_message(message.chat.id, """
*Spam Protector*
_Gruplarınızı Korumak Amacı İle Yapılan Bir Bottur Botun Mantığı Spam Barındıran İçerikleri Gizlediği İçin Grubunuz Spama Düşmez Bölelikle Spam Tehlikesi Ortadan Kalkar_
*Yapmanız Gerekenler*

_•Grubunuza Eklemek. (Korumaya Al Butonuna Tıklayarak) 1.Adım_
_•Full Yetkiye Sahip Olması İle Grubunuz Güvende Olacaktır. (Yetki Veriniz) 2.Adım_
_•Grup İçerisinde /spam komutunu yazmak (Komutu Yazmak) 3. Adım_

_LÜTFEN GRUBUNUZA EKLEDİKTEN VE YETKİ VERDİKTEN SONRA GRUP
İÇERİSİNDE /spam YAZINIZ YOKSA KORUMA İŞLEMİ KAYIT ALITINA ALINMAZ_
""", reply_markup=markup, parse_mode="Markdown")
    
@bot.message_handler(commands=["spam"])
def menu(message):
    markup = InlineKeyboardMarkup(row_width=2)
    bilgi = InlineKeyboardButton("️Bilgilendirme 💬", url="https://t.me/Saygisizlar")
    markup.add(bilgi)
    
    bot.send_message(message.chat.id, """
*Yetki Kontrolü* ✅

_Bot Görevindedir Yetki Alınması Durumunda Etkisiz Kalır_




""", reply_markup=markup, parse_mode="Markdown")



    
print("Bot Aktif")

if __name__ =="__main__":
    bot.polling(none_stop=True)
