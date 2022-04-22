import telebot
import requests
import random

bot = telebot.TeleBot("bot id")

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


help="""Merhabalar, botun kullanımıyla ilgili bilgiler aşağıda örnekleriyle birlikte verilmiştir. Sorularınız ve önerileriniz için
twitter.com/smaugscoins adresinden iletişime geçebilirsiniz.

Genel Bilgiler:

💎 Bitcoin ve Ethereum dominans bilgisini öğrenmek için bota "genel" ya da "dominans" mesajını gönderebilirsiniz.

👀 Bitcoin için günlük korku & açgözlülük endeksini görmek için bota "fear" ya da "korku" mesajını gönderebilirsiniz


Kripto Para Bilgileri:

🧠İstediğiniz kripto paranın anlık fiyatını,kripto paranın sembolünü yazdıktan sonra "fiyat" ekleyip göndererek öğrenebilirsiniz(Örn: cspr fiyat)

🎃İstediğiniz kripto paranın sosyal medya hesaplarını ve whitepaperını,kripto paranın sembolünü yazdıktan sonra "sosyal" ekleyip göndererek öğrenebilirsiniz(Örn:doge sosyal)

🐞İstediğiniz kripto paranın genel bilgilerini, kripto paranın sembolünü yazdıktan sonra "bilgi" ekleyip göndererek öğrenebilirsiniz.(Örn: sxp bilgi)

🌟İstediğiniz kripto paranın yatırımcılarını, kripto paranın sembolünü yazdıktan sonra "founders" ekleyip göndererek öğrenebilirsiniz.(Örn: rsr founders)

🏆İstediğiniz kripto para için eklenmiş etiketleri, kripto paranın sembolünü yazdıktan sonra "tags" ekleyip göndererek öğrenebilirsiniz.(Örn: hopr tags)

🎗İstediğiniz kripto paranın logosunu, kripto paranın sembolünü yazdıktan sonra "logo" ekleyip göndererek öğrenebilirsiniz.(Örn: hopr logo)
"""



start= """Merhaba! Coin Analiz botuna Hoş geldiniz.
Bu bot sayesinde istediğiniz kripto para hakkında anlık olarak bilgi sahibi olabilirsiniz.
Botun kullanımı hakkında bilgi almak için /help yazısına tıklayabilirsiniz."""

    


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, start)

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, help) 
    
    
    
    
    
@bot.message_handler(content_types = ['text','photos'])
def get_text(message):
    if "fear" in message.text.lower() or "korku" in message.text.lower():
        try:
           randomsayi =  str(random.randint(6000,9600))
           bot.send_photo(message.chat.id,'https://alternative.me/crypto/fear-and-greed-index.png?'+randomsayi)
        except:  bot.send_message(message.chat.id,"Sunucu Bağlantıyı reddetti. Lütfen Tekrar deneyiniz. ")      
#---------------------------------------Fear İndex---------------------------------------------->>>     
    if "sosyal" in message.text.lower():
       coinadi =  message.text.upper().replace(" SOSYAL","");
       url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'
       parameters = {
           'symbol': coinadi}
       headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': 'coinmarketcap api key'}
       session = Session()
       session.headers.update(headers)
       try:
           response = session.get(url, params=parameters)
           dataiki = json.loads(response.text)
           website = "*🕸 Web Sitesi: *" + str(dataiki['data'][coinadi]['urls']['website']);
           twitter = "*🐦 Twitter Hesabı: *" + str(dataiki['data'][coinadi]['urls']['twitter']);
           whitepaper = "*📄 WhitePaper: *" + str(dataiki['data'][coinadi]['urls']['technical_doc']);
           bot.send_message(message.chat.id,website+"\n\n"+twitter+"\n\n"+whitepaper,parse_mode='Markdown')

       except (ConnectionError, Timeout, TooManyRedirects,KeyError) as e:
           print(e)
           bot.send_message(message.chat.id,"Verdiğiniz komut anlaşılmadı. Hata türü : "+str(e))

#---------------------------------------Sosyal Medya Hesapları--------------------------------->>>  
    if "genel" in message.text.lower() or "dominan" in message.text.lower() :
       url = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest'
       parameters = {
           'convert': 'USD'}
       headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': 'coinmarkeycapapikey'}
       session = Session()
       session.headers.update(headers)
       try:
           response = session.get(url, params=parameters)
           datagenel = json.loads(response.text)
           btcDominance = "*💰 BTC Dominance: *" + str(datagenel['data']['btc_dominance'])[0:4]+"%";
           ethDominance = "*💎 ETH Dominance: *" + str(datagenel['data']['eth_dominance'])[0:4]+"%";
           aktifKripto = "*✅ Aktif Kripto Para Sayısı: *" + str(datagenel['data']['active_cryptocurrencies']);
           toplamKripto = "*▶️ Toplam Kripto Para Sayısı: *" + str(datagenel['data']['total_cryptocurrencies']);
           bot.send_message(message.chat.id,btcDominance+"\n\n"+ethDominance+"\n\n"+aktifKripto+"\n\n"+toplamKripto,parse_mode='Markdown')

       except (ConnectionError, Timeout, TooManyRedirects,KeyError) as e:
           
           bot.send_message(message.chat.id,"Verdiğiniz komut anlaşılmadı. Hata türü : "+str(e))

#---------------------------------------Genel Bilgiler--------------------------------->>>  
    if "bilgi" in message.text.lower():
       coinadi =  message.text.upper().replace(" BILGI","");
       url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'
       parameters = {
           'symbol': coinadi}
       headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': 'coinmarkeycapapikey'}
       session = Session()
       session.headers.update(headers)
       try:
           response = session.get(url, params=parameters)
           databilgi = json.loads(response.text)   
           coininadi = "*💬 Adı : *" + str(databilgi['data'][coinadi]['name']);
           kategori = "*🧮 Kategori : *" + str(databilgi['data'][coinadi]['category']);
           aciklama = "*📖 Açıklama : *" + str(databilgi['data'][coinadi]['description']);
           #price = "*💸 Anlık Fiyatı : *" + str(databilgi['data'][coinadi]['quote']['USD']['price'])[0:6] + "$";
           eklenme ="*🕛 Eklenme Tarihi : *" + str(databilgi['data'][coinadi]['date_added'])[0:10];
           #totalSupply ="*▶️ Total Supply : *" + str(databilgi['data'][coinadi]['total_supply']);
           #circulatingSupply ="*🔄 Circulating Supply : *" + str(databilgi['data'][coinadi]['circulating_supply']);
           #try:
            #   oranimiz = str(databilgi['data']['circulating_supply']/databilgi['data'][coinadi]['total_supply']*100)[0:4];
           #except ZeroDivisionError:
           #     oranimiz = "Bilinmeyen"
           #piyasaOrani = "*👀 Piyasa Oranı : *"+ str(oranimiz) +"%";
           bot.send_message(message.chat.id,coininadi + "\n\n" +kategori+"\n\n" + eklenme+"\n\n"+aciklama,parse_mode='Markdown')
       except (ConnectionError, Timeout, TooManyRedirects,KeyError) as e:          
           bot.send_message(message.chat.id,"Verdiğiniz komut anlaşılmadı. Hata türü : "+str(e))
#----------------------------------Coin Bilgileri------------------------------------------------>>>           
                  
    if "founders" in message.text.lower():
       coinadiyatirim =  message.text.upper().replace(" FOUNDERS","");
       urlyatirim = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'
       parameters = {
           'symbol': coinadiyatirim}
       headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': 'coinmarkeycapapikey'}
       session = Session()
       session.headers.update(headers)
       try:
           response = session.get(urlyatirim, params=parameters)
           dataYatirim = json.loads(response.text)
           for b in dataYatirim['data'][coinadiyatirim]['tags']:
               if "portfolio" in b or "capital" in b:                   
                   bot.send_message(message.chat.id,"▶️ "+b)
       except (ConnectionError, Timeout, TooManyRedirects,KeyError) as e:       
           bot.send_message(message.chat.id,"Verdiğiniz komut anlaşılmadı. Hata türü : "+str(e))       
#---------------------------------Coin Yatırımcıları--------------------------------------------->>>         
                   
    if "tags" in message.text.lower():
       coinaditags =  message.text.upper().replace(" TAGS","");
       urlyatirim = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'
       parameters = {
           'symbol': coinaditags}
       headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': 'coinmarkeycapapikey'}
       session = Session()
       session.headers.update(headers)
       try:
           response = session.get(urlyatirim, params=parameters)
           datatags = json.loads(response.text)
           for b in datatags['data'][coinaditags]['tags']:
               if "portfolio" not in b and "capital" not in b:                   
                   bot.send_message(message.chat.id,"▶️ "+b)
       except (ConnectionError, Timeout, TooManyRedirects,KeyError) as e:
           
           bot.send_message(message.chat.id,"Verdiğiniz komut anlaşılmadı. Hata türü : "+str(e))
#---------------------------------Coin Tags--------------------------------------------->>>                     
    if "fiyat" in message.text.lower():
       coinadifiyat =  message.text.upper().replace(" FIYAT","");
       url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
       parameters = {
           'symbol': coinadifiyat}
       headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': 'coinmarkeycapapikey'}
       session = Session()
       session.headers.update(headers)
       try:
           response = session.get(url, params=parameters)
           datafiyat = json.loads(response.text)
           price = "*💸 Anlık Fiyatı : *" + str(datafiyat['data'][coinadifiyat]['quote']['USD']['price'])[0:6] + "$";
           totalSupply ="*▶️ Total Supply : *" + str(datafiyat['data'][coinadifiyat]['total_supply']);
           circulatingSupply ="*🔄 Circulating Supply : *" + str(datafiyat['data'][coinadifiyat]['circulating_supply']);
           changesaat ="*💎 Saatlik Değişim : *" + str(datafiyat['data'][coinadifiyat]['quote']['USD']['percent_change_1h'])[0:4]+"%";
           changegun ="*🔫 Günlük Değişim : *" + str(datafiyat['data'][coinadifiyat]['quote']['USD']['percent_change_24h'])[0:4]+"%";
           changehafta ="*⚔️ Haftalık Değişim : *" + str(datafiyat['data'][coinadifiyat]['quote']['USD']['percent_change_7d'])[0:4]+"%";
           
           try:
               oranimiz = str(datafiyat['data'][coinadifiyat]['circulating_supply']/datafiyat['data'][coinadifiyat]['total_supply']*100)[0:4];
           except ZeroDivisionError:
                oranimiz = "Bilinmeyen"
           piyasaOrani = "*👀 Piyasa Oranı : *"+ str(oranimiz) +"%";
           bot.send_message(message.chat.id,price+"\n\n"+totalSupply+"\n\n"+circulatingSupply+"\n\n"+piyasaOrani+"\n\n"+changesaat+"\n\n"+changegun+"\n\n"+changehafta,parse_mode='Markdown')
       except (ConnectionError, Timeout, TooManyRedirects) as e: 
           bot.send_message(message.chat.id,"Verdiğiniz komut anlaşılmadı. Hata türü : "+str(e))
#-------------------------------------------------Fiyat------------------------------------------------------------------>>>

    if "logo" in message.text.lower():
       coinadilogo =  message.text.upper().replace(" LOGO","");
       url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'
       parameters = {
           
           'symbol': coinadilogo}
       headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': 'coinmarkeycapapikey'}
       session = Session()
       session.headers.update(headers)
       try:
           response = session.get(url, params=parameters)
           databilgi = json.loads(response.text)
          
           coinlogo = str(databilgi['data'][coinadilogo]['logo']);
          
           bot.send_photo(message.chat.id,coinlogo)
       except (ConnectionError, Timeout, TooManyRedirects,KeyError) as e:
           bot.send_message(message.chat.id,"Verdiğiniz komut anlaşılmadı. Hata türü : "+str(e))
#---------------------------------------------Logo----------------------------------------------------------------------->>>
    if "puan" in message.text.lower():
       coinadipuan =  message.text.upper().replace(" PUAN","");
       url = 'https://pro-api.coinmarketcap.com/v1/partners/flipside-crypto/fcas/quotes/latest'
       parameters = {
           'symbol': coinadipuan}
       headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': 'coinmarkeycapapikey'}
       session = Session()
       session.headers.update(headers)
       try:
           response = session.get(url, params=parameters)
           datapuan = json.loads(response.text)
           coinname = "💎 İsim : "+str(datapuan['data'][coinadipuan]['name']);
           coinpuani = "🟩 Derece : "+str(datapuan['data'][coinadipuan]['grade']);
           coinskor = "🎯 Skor : "+str(datapuan['data'][coinadipuan]['score']);
           bot.send_message(message.chat.id,coinname+"\n\n"+coinpuani+"\n\n"+coinskor)
       except (ConnectionError, Timeout, TooManyRedirects,KeyError):
           bot.send_message(message.chat.id,"Bu kripto para puanlanmamış. ")
bot.polling()
























