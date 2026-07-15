#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ====================================================================
# بوت اختراق X7x - النسخة النهائية مع تلوين الأزرار (Bot API 9.4)
# المطور: X7x
# قناة التحديثات: @VIP_x77x
# يوزر المطور: @VlP_X7x
# توكن البوت: 8940915673:AAF8j8ljTa2ABjonVhJVKTJz0iaMrg1H-iQ
# ====================================================================

import json
import re
import os
import tempfile
import random
import string
import time
import requests
from datetime import datetime
from flask import Flask, request, jsonify

# ==================== الإعدادات الأساسية ====================
TOKEN = "8940915673:AAFS7f2Zy-Fx7i6evUaJEUid4yCPecAcjcM"
OWNER_ID = 7292128411
OWNER_USERNAME = "@VlP_X7x"
CHANNEL_USERNAME = "@Grizi_32"
FORCE_CHANNELS = ["@Grizi_32", "@x7x_mane", "@x7x_H", "@x7xhaker"]
WELCOME_IMAGE_URL = "https://i.ibb.co/zKgxjKz/IMG-20260706-223613-015.jpg"

API_URL = f"https://api.telegram.org/bot{TOKEN}/"
app = Flask(__name__)

# ==================== روابط الخدمات (30 صفحة مزورة) ====================
SERVICE_LINKS = [
    "https://example1.com", "https://example2.com", "https://example3.com",
    "https://example4.com", "https://example5.com", "https://example6.com",
    "https://example7.com", "https://example8.com", "https://example9.com",
    "https://example10.com", "https://example11.com", "https://example12.com",
    "https://example13.com", "https://example14.com", "https://example15.com",
    "https://example16.com", "https://example17.com", "https://example18.com",
    "https://example19.com", "https://example20.com", "https://example21.com",
    "https://example22.com", "https://example23.com", "https://example24.com",
    "https://example25.com", "https://example26.com", "https://example27.com",
    "https://example28.com", "https://example29.com", "https://example30.com"
]

# ==================== قنوات تلفزيون (90 قناة) ====================
TV_CHANNELS = [
    "https://www.masrplay.xyz/", "https://www.nilesat.com.eg/", "https://www.cbc-eg.com/",
    "https://www.alarabiya.net/", "https://www.aljazeera.net/", "https://www.mbc.net/",
    "https://www.rotana.net/", "https://www.bbc.com/arabic", "https://www.euronews.com/arabic",
    "https://www.cnnarabic.com/", "https://www.skynewsarabia.com/", "https://www.dmi.ae/",
    "https://www.dubaitv.ae/", "https://www.adtv.ae/", "https://www.kuna.net.kw/",
    "https://www.kuwaittv.net/", "https://www.alwatanvoice.com/", "https://www.qatartv.qa/",
    "https://www.beinsports.com/ar/", "https://www.bna.bh/", "https://www.bahraintv.com/",
    "https://www.oman-tv.gov.om/", "https://www.omannews.gov.om/", "https://www.jrtv.jo/",
    "https://www.ammannet.net/", "https://www.teleliban.com/", "https://www.lbcgroup.tv/",
    "https://www.mtv.com.lb/", "https://www.pbc.ps/", "https://www.alquds.com/",
    "https://www.imn.iq/", "https://www.aliraqiya.tv/", "https://www.ortas.online/",
    "https://www.syria.tv/", "https://www.yementv.net/", "https://www.almotamar.net/",
    "https://www.ljtv.ly/", "https://www.libyaalahrartv.com/", "https://www.tunisiatv.tn/",
    "https://www.nessma.tv/", "https://www.entv.dz/", "https://www.ennaharonline.com/",
    "https://www.snrt.ma/", "https://www.2m.ma/", "https://www.sudantv.net/",
    "https://www.sudan24.net/", "https://www.sntv.so/", "https://www.hiiraan.com/",
    "https://www.rmi.mr/", "https://www.alakhbar.info/", "https://www.bbc.com/",
    "https://www.cnn.com/", "https://www.foxnews.com/", "https://www.msnbc.com/",
    "https://www.nbcnews.com/", "https://www.abcnews.go.com/", "https://www.cbsnews.com/",
    "https://www.pbs.org/", "https://www.npr.org/", "https://www.aljazeera.com/",
    "https://www.france24.com/", "https://www.dw.com/", "https://www.euronews.com/",
    "https://www.rt.com/", "https://www.sky.com/", "https://www.channel4.com/",
    "https://www.itv.com/", "https://www.bbc.co.uk/", "https://www.cbc.ca/",
    "https://www.ctvnews.ca/", "https://www.globalnews.ca/", "https://www.theguardian.com/",
    "https://www.telegraph.co.uk/", "https://www.independent.co.uk/", "https://www.thetimes.co.uk/",
    "https://www.wsj.com/", "https://www.nytimes.com/", "https://www.washingtonpost.com/",
    "https://www.latimes.com/", "https://www.chicagotribune.com/", "https://www.houstonchronicle.com/",
    "https://www.sfgate.com/", "https://www.boston.com/", "https://www.philly.com/",
    "https://www.dallasnews.com/", "https://www.azcentral.com/", "https://www.denverpost.com/",
    "https://www.seattletimes.com/", "https://www.startribune.com/", "https://www.bostonglobe.com/"
]

# ==================== قنوات راديو (30 قناة) ====================
RADIO_CHANNELS = [
    "https://www.bbc.co.uk/sounds/play/live:bbc_world_service",
    "https://www.npr.org/streams/", "https://www.rt.com/on-air/",
    "https://www.france24.com/en/live", "https://www.dw.com/en/live-tv/",
    "https://www.aljazeera.com/live/", "https://www.euronews.com/live",
    "https://www.skynews.com.au/live", "https://www.cbc.ca/listen/live",
    "https://www.abc.net.au/radio/", "https://www.radiofrance.fr/",
    "https://www.rai.it/", "https://www.rtve.es/", "https://www.zdf.de/",
    "https://www.ard.de/", "https://www.srf.ch/", "https://www.orf.at/",
    "https://www.svt.se/", "https://www.nrk.no/", "https://www.dr.dk/",
    "https://www.yle.fi/", "https://www.ruv.is/", "https://www.lrt.lt/",
    "https://www.lsm.lv/", "https://www.err.ee/", "https://www.trt.net.tr/",
    "https://www.kan.org.il/", "https://www.iba.org.il/", "https://www.mbc.net/radio/",
    "https://www.rotana.net/radio/"
]

# ==================== كاميرات مراقبة (20 كاميرا) ====================
CCTV_CAMERAS = [
    "https://www.earthcam.com/", "https://www.skylinewebcams.com/",
    "https://www.livecam.com/", "https://www.webcamtaxi.com/",
    "https://www.camvista.com/", "https://www.livefromiceland.is/",
    "https://www.niagarafallslive.com/", "https://www.timesquare.com/",
    "https://www.empirestatebuilding.com/", "https://www.eiffeltower.com/",
    "https://www.bigben.com/", "https://www.colosseum.com/",
    "https://www.sydneyharbour.com/", "https://www.tokyo-tower.com/",
    "https://www.venicecanals.com/", "https://www.parisstreets.com/",
    "https://www.londonbridge.com/", "https://www.berlinwall.com/",
    "https://www.moscowkremlin.com/", "https://www.dubaifountain.com/"
]

# ==================== رموز نادرة ومزخرفة للاستخدام ====================
RARE_EMOJIS = [
    "☠️", "💀", "🩸", "🗡️", "⚔️", "🖤", "💣", "🔮", "👁️", "🗿",
    "꧁", "꧂", "༺", "༻", "☬", "✯", "★", "☆", "❂", "『', '」", "「", "】",
    "᪥", "᪦", "ᪧ", "᪨", "᪩", "᪪", "᪫", "᪬", "᪭", "ⵔ", "ⵕ", "ⵖ",
    "𒀭", "𒀮", "𒀯", "𒀰", "𒀱", "𒀲", "𒀳", "𒀴", "𒀵", "𓀀", "𓀁", "𓀂"
]

def random_rare_emoji():
    return random.choice(RARE_EMOJIS)

def fancy_text(text):
    """إضافة رموز نادرة حول النص"""
    emoji = random_rare_emoji()
    return f"{emoji} {text} {emoji}"

# ==================== دوال مساعدة ====================
def send_message(chat_id, text, reply_markup=None, parse_mode="HTML"):
    data = {"chat_id": chat_id, "text": text, "parse_mode": parse_mode}
    if reply_markup:
        data["reply_markup"] = reply_markup
    try:
        requests.post(API_URL + "sendMessage", json=data, timeout=30)
    except:
        pass

def send_photo(chat_id, photo, caption=None, reply_markup=None):
    data = {"chat_id": chat_id, "photo": photo}
    if caption:
        data["caption"] = caption
    if reply_markup:
        data["reply_markup"] = reply_markup
    try:
        requests.post(API_URL + "sendPhoto", json=data, timeout=30)
    except:
        pass

def edit_message(chat_id, message_id, text, reply_markup=None):
    data = {"chat_id": chat_id, "message_id": message_id, "text": text}
    if reply_markup:
        data["reply_markup"] = reply_markup
    try:
        requests.post(API_URL + "editMessageText", json=data, timeout=30)
    except:
        pass

def answer_callback(callback_id, text=None, show_alert=False):
    data = {"callback_query_id": callback_id}
    if text:
        data["text"] = text
    if show_alert:
        data["show_alert"] = True
    try:
        requests.post(API_URL + "answerCallbackQuery", json=data, timeout=30)
    except:
        pass

def create_button(text, callback_data=None, url=None, style=None):
    """إنشاء زر مع دعم التلوين style: 'danger', 'success', 'primary'"""
    btn = {"text": text}
    if callback_data:
        btn["callback_data"] = callback_data
    if url:
        btn["url"] = url
    if style:
        btn["style"] = style  # إضافة خاصية التلوين (Bot API 9.4)
    return btn

def generate_random_visa():
    first_names = ["Ahmed","Mohamed","Hassan","Omar","Ali","Mahmoud","Khaled","Youssef","Ibrahim","Tariq"]
    last_names = ["Hassan","Ali","Mohamed","Ahmed","Khaled","Mahmoud","Youssef","Ibrahim","Tariq","Saeed"]
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    visa_number = "4" + ''.join(random.choices(string.digits, k=15))
    exp_month = random.randint(1, 12)
    exp_year = random.randint(24, 28)
    cvv = random.randint(100, 999)
    pin = ''.join(random.choices(string.ascii_uppercase, k=4))
    balance = round(random.uniform(100, 5000), 2)
    return f"""
{random_rare_emoji()} ========== فيزا مكسورة ========== {random_rare_emoji()}
👤 الاسم: {name}
💳 الرقم: {visa_number}
📅 تاريخ الانتهاء: {exp_month}/{exp_year}
🔒 رمز (CVV): {cvv}
🔑 الرقم السري (PIN): {pin}
💵 الرصيد المتاح: ${balance}
⚡ استخدمها بحذر، العيون تراقبك.
{random_rare_emoji()} ================================== {random_rare_emoji()}
"""

def generate_random_usernames(count=8):
    return ['@' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(5, 10))) for _ in range(count)]

def generate_random_passwords(count=5):
    chars = string.ascii_letters + string.digits + '!@#$%^&*'
    return [''.join(random.choices(chars, k=random.randint(12, 16))) for _ in range(count)]

def generate_fancy_text(name):
    chars_map = {
        'a': ['𝒶','𝓪','𝔞','𝕒','𝖆','𝖺','𝗮','𝘢','𝙖','𝚊','ᗩ','卂','ⓐ','🅐','🄰','Ꭿ','Ꮧ','α','ά','ą'],
        'b': ['𝒷','𝓫','𝔟','𝕓','𝖇','𝖻','𝗯','𝘣','𝙗','𝚋','ᗷ','乃','ⓑ','🅑','🄱','Ᏸ','Ᏼ','β','в','ь'],
        'c': ['𝒸','𝓬','𝔠','𝕔','𝖈','𝖼','𝗰','𝘤','𝙘','𝚌','ᑕ','匚','ⓒ','🅒','🄲','ፈ','Ꮯ','¢','ς','с'],
        'd': ['𝒹','𝓭','𝔡','𝕕','𝖉','𝖽','𝗱','𝘥','𝙙','𝚍','ᗪ','ᗪ','ⓓ','🅓','🄳','Ꮄ','Ꭰ','∂','δ','ď'],
        'e': ['ℯ','𝓮','𝔢','𝕖','𝖊','𝖾','𝗲','𝘦','𝙚','𝚎','ᗴ','乇','ⓔ','🅔','🄴','Ꮛ','Ꮧ','є','έ','ε'],
        'f': ['𝒻','𝓯','𝔣','𝕗','𝖋','𝖿','𝗳','𝘧','𝙛','𝚏','ᖴ','千','ⓕ','🅕','🄵','Ꭶ','Ꭰ','ƒ','ϝ','ғ'],
        'g': ['ℊ','𝓰','𝔤','𝕘','𝖌','𝗀','𝗴','𝘨','𝙜','𝚐','ᘜ','ᘜ','ⓖ','🅖','🄶','Ꮆ','Ꮐ','g','ģ','ğ'],
        'h': ['𝒽','𝓱','𝔥','𝕙','𝖍','𝗁','𝗵','𝘩','𝙝','𝚑','ᕼ','卄','ⓗ','🅗','🄷','Ꮒ','Ꮋ','ħ','ђ','н'],
        'i': ['𝒾','𝓲','𝔦','𝕚','𝖎','𝗂','𝗶','𝘪','𝙞','𝚒','I','丨','ⓘ','🅘','🄸','Ꭵ','Ꮖ','ι','ί','і'],
        'j': ['𝒿','𝓳','𝔧','𝕛','𝖏','𝗃','𝗷','𝘫','𝙟','𝚓','ᒍ','ᒍ','ⓙ','🅙','🄹','Ꮰ','Ꭻ','נ','ϳ','ј'],
        'k': ['𝓀','𝓴','𝔨','𝕜','𝖐','𝗄','𝗸','𝘬','𝙠','𝚔','ᛕ','Ҡ','ⓚ','🅚','🄺','Ꮶ','Ꮶ','к','κ','ķ'],
        'l': ['𝓁','𝓵','𝔩','𝕝','𝖑','𝗅','𝗹','𝘭','𝙡','𝚕','ㄥ','ㄥ','ⓛ','🅛','🄻','Ꮭ','Ꮮ','ℓ','ł','ļ'],
        'm': ['𝓂','𝓶','𝔪','𝕞','𝖒','𝗆','𝗺','𝘮','𝙢','𝚖','ᗰ','爪','ⓜ','🅜','🄼','Ꮇ','Ꮇ','м','ϻ','ṃ'],
        'n': ['𝓃','𝓷','𝔫','𝕟','𝖓','𝗇','𝗻','𝘯','𝙣','𝚗','ᑎ','几','ⓝ','🅝','🄽','Ꮑ','Ꮑ','и','ή','ń'],
        'o': ['ℴ','𝓸','𝔬','𝕠','𝖔','𝗈','𝗼','𝘰','𝙤','𝚘','ᗝ','ㄖ','ⓞ','🅞','🄾','Ꭷ','Ꮻ','σ','ό','ο'],
        'p': ['𝓅','𝓹','𝔭','𝕡','𝖕','𝗉','𝗽','𝘱','𝙥','𝚙','ᑭ','卩','ⓟ','🅟','🄿','Ꮲ','Ꮲ','ρ','ϸ','р'],
        'q': ['𝓆','𝓺','𝔮','𝕢','𝖖','𝗊','𝗾','𝘲','𝙦','𝚚','ᑫ','ᑫ','ⓠ','🅠','🅀','Ꭴ','Ꮔ','q','ϥ','q'],
        'r': ['𝓇','𝓻','𝔯','𝕣','𝖗','𝗋','𝗿','𝘳','𝙧','𝚛','ᖇ','尺','ⓡ','🅡','🅁','Ꮢ','Ꮢ','я','г','ŗ'],
        's': ['𝓈','𝓼','𝔰','𝕤','𝖘','𝗌','𝘀','𝘴','𝙨','𝚜','ᔕ','丂','ⓢ','🅢','🅂','Ꮥ','Ꮪ','ѕ','ş','ś'],
        't': ['𝓉','𝓽','𝔱','𝕥','𝖙','𝗍','𝘁','𝘵','𝙩','𝚝','丅','ㄒ','ⓣ','🅣','🅃','Ꮦ','Ꭲ','т','ţ','t'],
        'u': ['𝓊','𝓾','𝔲','𝕦','𝖚','𝗎','𝘂','𝘶','𝙪','𝚞','ᑌ','ㄩ','ⓤ','🅤','🅄','Ꮼ','Ꮜ','υ','ύ','u'],
        'v': ['𝓋','𝓿','𝔳','𝕧','𝖛','𝗏','𝘃','𝘷','𝙫','𝚟','ᐯ','ᐯ','ⓥ','🅥','🅅','Ꮙ','Ꮩ','ν','ϑ','v'],
        'w': ['𝓌','𝔀','𝔴','𝕨','𝖜','𝗐','𝘄','𝘸','𝙬','𝚠','ᗯ','山','ⓦ','🅦','🅆','Ꮗ','Ꮤ','ω','ώ','w'],
        'x': ['𝓍','𝔁','𝔵','𝕩','𝖝','𝗑','𝘅','𝘹','𝙭','𝚡','᙭','乂','ⓧ','🅧','🅇','ጀ','᙭','χ','ϰ','x'],
        'y': ['𝓎','𝔂','𝔶','𝕪','𝖞','𝗒','𝘆','𝘺','𝙮','𝚢','ᖻ','ㄚ','ⓨ','🅨','🅈','Ꭹ','Ꮍ','у','ý','ÿ'],
        'z': ['𝓏','𝔃','𝔷','𝕫','𝖟','𝗓','𝘇','𝘻','𝙯','𝚣','乙','乙','ⓩ','🅩','🅉','ፚ','Ꮓ','z','ž','ż']
    }
    name = name.lower()
    results = []
    for _ in range(30):
        fancy = ''
        for char in name:
            if char in chars_map:
                fancy += random.choice(chars_map[char])
            else:
                fancy += char
        prefixes = ['✦','✧','★','☆','❂','『','「','【','꧁','༺','☬','✯']
        suffixes = ['✦','✧','★','☆','❂','』','」','】','꧂','༻','☬','✯']
        if random.choice([True, False]):
            fancy = random.choice(prefixes) + ' ' + fancy + ' ' + random.choice(suffixes)
        results.append(fancy)
    return list(set(results))

def shorten_url(long_url):
    try:
        response = requests.get(f"https://tinyurl.com/api-create.php?url={long_url}", timeout=10)
        if response.status_code == 200 and response.text:
            return response.text
    except:
        pass
    return None

def get_ip_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query", timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'success':
                return data
    except:
        pass
    return None

def get_phone_info(phone):
    try:
        response = requests.get(f"https://api.agatz.xyz/api/phone?number={phone}", timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get('status'):
                return data.get('data')
    except:
        pass
    try:
        response = requests.get(f"http://apilayer.net/api/validate?access_key=test&number={phone}&country_code=", timeout=10)
        if response.status_code == 200:
            return response.json()
    except:
        pass
    return None

def detect_country_code(phone):
    phone = re.sub(r'[^0-9]', '', phone)
    country_codes = {
        '20': 'مصر', '966': 'السعودية', '971': 'الإمارات', '965': 'الكويت', '974': 'قطر',
        '973': 'البحرين', '968': 'عمان', '962': 'الأردن', '961': 'لبنان', '970': 'فلسطين',
        '964': 'العراق', '963': 'سوريا', '967': 'اليمن', '218': 'ليبيا', '216': 'تونس',
        '213': 'الجزائر', '212': 'المغرب', '249': 'السودان', '252': 'الصومال', '222': 'موريتانيا'
    }
    for code, country in country_codes.items():
        if phone.startswith(code):
            return country
    return 'غير معروف'

def check_force_subscription(user_id):
    for channel in FORCE_CHANNELS:
        try:
            response = requests.get(f"https://api.telegram.org/bot{TOKEN}/getChatMember?chat_id={channel}&user_id={user_id}", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('ok'):
                    status = data.get('result', {}).get('status', '')
                    if status not in ['member', 'administrator', 'creator']:
                        return False, channel
                else:
                    return False, channel
            else:
                return False, channel
        except:
            return False, channel
    return True, None

# ==================== دوال البحث عن حسابات Gmail ====================
def get_accounts_by_email(email):
    try:
        import holehe
        data = holehe.check_email(email)
        accounts = []
        for service, info in data.items():
            if info.get("rateLimit") == False and info.get("exists") == True:
                accounts.append({
                    "service": service,
                    "url": info.get("url", ""),
                    "exists": True
                })
        return accounts
    except:
        return None

def get_user_info_by_id(user_id):
    try:
        response = requests.get(f"https://api.telegram.org/bot{TOKEN}/getChat?chat_id={user_id}", timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get('ok'):
                return data.get('result')
    except:
        pass
    return None

def create_temp_email():
    try:
        response = requests.get("https://api.temp-mail.org/request/domains/format/json", timeout=10)
        if response.status_code == 200:
            domains = response.json()
            if domains:
                domain = random.choice(domains)
                username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(8, 12)))
                email = f"{username}@{domain}"
                return email
    except:
        pass
    return None

def check_temp_email_inbox(email):
    try:
        response = requests.get(f"https://api.temp-mail.org/request/mail/id/{email}/format/json", timeout=10)
        if response.status_code == 200:
            messages = response.json()
            if messages:
                return messages
    except:
        pass
    return None

# ==================== دوال إرسال القنوات بالتتابع ====================
def send_tv_channels(chat_id):
    send_message(chat_id, f"{random_rare_emoji()} **جاري تحميل القنوات التلفزيونية المخترقة...** {random_rare_emoji()}")
    time.sleep(2)
    send_message(chat_id, f"{random_rare_emoji()} **تم العثور على 90 قناة مخترقة!** {random_rare_emoji()}")
    time.sleep(1)
    for i, channel in enumerate(TV_CHANNELS[:90]):
        send_message(chat_id, f"{i+1}. {channel}")
        time.sleep(0.3)
    send_message(chat_id, f"{random_rare_emoji()} **تم الانتهاء من عرض جميع القنوات.** {random_rare_emoji()}")

def send_radio_channels(chat_id):
    send_message(chat_id, f"{random_rare_emoji()} **جاري تحميل القنوات الإذاعية المخترقة...** {random_rare_emoji()}")
    time.sleep(2)
    send_message(chat_id, f"{random_rare_emoji()} **تم العثور على 30 قناة إذاعية مخترقة!** {random_rare_emoji()}")
    time.sleep(1)
    for i, channel in enumerate(RADIO_CHANNELS[:30]):
        send_message(chat_id, f"{i+1}. {channel}")
        time.sleep(0.3)
    send_message(chat_id, f"{random_rare_emoji()} **تم الانتهاء من عرض جميع القنوات.** {random_rare_emoji()}")

def send_cctv_cameras(chat_id):
    send_message(chat_id, f"{random_rare_emoji()} **جاري تحميل كاميرات المراقبة المخترقة...** {random_rare_emoji()}")
    time.sleep(2)
    send_message(chat_id, f"{random_rare_emoji()} **تم العثور على 20 كاميرا مراقبة مخترقة!** {random_rare_emoji()}")
    time.sleep(1)
    for i, cam in enumerate(CCTV_CAMERAS[:20]):
        send_message(chat_id, f"{i+1}. {cam}")
        time.sleep(0.3)
    send_message(chat_id, f"{random_rare_emoji()} **تم الانتهاء من عرض جميع الكاميرات.** {random_rare_emoji()}")

# ==================== القوائم ====================
def get_main_menu():
    return {
        "inline_keyboard": [
            [create_button(f"{random_rare_emoji()} اختراق صفحات التواصل", "hack_pages", style="danger")],
            [create_button(f"{random_rare_emoji()} اختراق الهاتف", "hack_phone", style="danger")],
            [create_button(f"{random_rare_emoji()} أشياء أخرى", "other_tools", style="primary")],
            [create_button(f"{random_rare_emoji()} خدمات مدفوعة", "paid_services", style="success")],
            [create_button(f"{random_rare_emoji()} معلومات عن المطور", "about_me", style="primary")],
            [create_button(f"{random_rare_emoji()} تقييم البوت", "rate_bot", style="success")],
            [create_button(f"{random_rare_emoji()} رسالة للمطور", "message_owner", style="primary")],
            [create_button(f"{random_rare_emoji()} قناة المطور", "channel_link", style="primary"), create_button(f"{random_rare_emoji()} حساب المطور", "owner_link", style="primary")],
            [create_button(f"{random_rare_emoji()} التحقق من الاشتراك", "check_subscription", style="primary")],
            [create_button(f"{random_rare_emoji()} زخرفة أسماء", "fancy_name", style="success")],
            [create_button(f"{random_rare_emoji()} معرفة مستخدم من ID", "get_user_id_info", style="primary")],
            [create_button(f"{random_rare_emoji()} البحث عن حسابات Gmail", "search_gmail", style="danger")],
            [create_button(f"{random_rare_emoji()} إنشاء بريد مؤقت", "create_temp_email", style="success")],
            [create_button(f"{random_rare_emoji()} فحص بريد مؤقت", "check_temp_email_inbox", style="primary")]
        ]
    }

# ==================== معالجة Webhook ====================
@app.route("/", methods=["POST"])
def webhook():
    try:
        update = request.get_json()
        if not update:
            return jsonify({"status": "error", "message": "No update"}), 400
        
        if "message" in update:
            handle_message(update)
        elif "callback_query" in update:
            handle_callback(update)
        
        return jsonify({"status": "ok"})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/", methods=["GET"])
def index():
    return f"{random_rare_emoji()} بوت الاختراق X7x يعمل عبر Webhook! {random_rare_emoji()}"

# ==================== معالجة الرسائل ====================
def handle_message(update):
    msg = update.get("message", {})
    chat_id = msg.get("chat", {}).get("id")
    text = msg.get("text", "")
    first_name = msg.get("from", {}).get("first_name", "مستخدم")
    message_id = msg.get("message_id")
    user_id = msg.get("from", {}).get("id")
    
    if not chat_id:
        return
    
    # التحقق من الاشتراك
    subscribed, missing_channel = check_force_subscription(user_id)
    if not subscribed:
        text2 = f"{random_rare_emoji()} **للوصول إلى عالم الظل، يجب عليك الانضمام إلى قنواتنا السرية أولاً:**\n\n"
        for channel in FORCE_CHANNELS:
            if channel == missing_channel:
                text2 += f"• ❌ {channel} (أنت غير مشترك هنا!)\n"
            else:
                text2 += f"• ✅ {channel}\n"
        text2 += f"\n🔗 اشترك في القناة المفقودة ثم اضغط /start مرة أخرى.\n\n{OWNER_USERNAME}"
        keyboard = {"inline_keyboard": [[create_button(f"🔗 اشترك في {missing_channel}", url=f"https://t.me/{missing_channel.replace('@', '')}", style="danger")]]}
        send_message(chat_id, text2, keyboard)
        return
    
    # حالة المستخدم
    user_state = app.config.get("user_states", {}).get(str(chat_id), {})
    state = user_state.get("state")
    
    # معالجة الحالات
    if state == "awaiting_phone":
        phone = re.sub(r'[^0-9+]', '', text)
        if len(phone) < 8:
            send_message(chat_id, "❌ رقم غير صالح. أرسل رقم صحيح.")
            return
        country = detect_country_code(phone)
        info = get_phone_info(phone)
        if info:
            result = f"""
{random_rare_emoji()} **معلومات الرقم:** {random_rare_emoji()}

📱 الرقم: {phone}
🌍 الدولة: {country}
📡 المشغل: {info.get('carrier', 'غير معروف')}
📍 المنطقة: {info.get('location', 'غير معروف')}
🕒 الوقت: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        else:
            result = f"""
{random_rare_emoji()} **معلومات الرقم:** {random_rare_emoji()}

📱 الرقم: {phone}
🌍 الدولة: {country}
⚠️ لم نتمكن من جلب معلومات إضافية.
"""
        send_message(chat_id, result)
        app.config["user_states"][str(chat_id)] = {}
        show_main_menu(chat_id)
        return
    
    if state == "awaiting_target_phone":
        phone = re.sub(r'[^0-9+]', '', text)
        if len(phone) < 8:
            send_message(chat_id, "❌ رقم غير صالح. أرسل رقم صحيح.")
            return
        country = detect_country_code(phone)
        send_message(chat_id, f"""
{random_rare_emoji()} **استهداف الرقم:** {phone} {random_rare_emoji()}

🌍 الدولة: {country}
🩸 جاري اختراق الرقم...
💀 تم تدمير الرقم بنجاح!
⚠️ (X7x يحبك)
""")
        app.config["user_states"][str(chat_id)] = {}
        show_main_menu(chat_id)
        return
    
    if state == "awaiting_ip":
        ip = text.strip()
        if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip):
            send_message(chat_id, "❌ IP غير صالح. أرسل عنوان IP صحيح.")
            return
        info = get_ip_info(ip)
        if info:
            result = f"""
{random_rare_emoji()} **معلومات الـ IP:** {random_rare_emoji()}

🌍 IP: {ip}
📍 الدولة: {info.get('country', 'غير معروف')} ({info.get('countryCode', '')})
🏙️ المنطقة: {info.get('regionName', 'غير معروف')}
🏢 المدينة: {info.get('city', 'غير معروف')}
📡 مزود الخدمة: {info.get('isp', 'غير معروف')}
🖥️ المنظمة: {info.get('org', 'غير معروف')}
🗺️ خط العرض: {info.get('lat', 'غير معروف')}
🗺️ خط الطول: {info.get('lon', 'غير معروف')}
⏳ المنطقة الزمنية: {info.get('timezone', 'غير معروف')}
"""
        else:
            result = f"""
{random_rare_emoji()} **معلومات الـ IP:** {random_rare_emoji()}

🌍 IP: {ip}
⚠️ لم نتمكن من جلب معلومات إضافية.
"""
        send_message(chat_id, result)
        app.config["user_states"][str(chat_id)] = {}
        show_main_menu(chat_id)
        return
    
    if state == "awaiting_phone_lookup":
        phone = re.sub(r'[^0-9+]', '', text)
        if len(phone) < 8:
            send_message(chat_id, "❌ رقم غير صالح. أرسل رقم صحيح.")
            return
        info = get_phone_info(phone)
        country = detect_country_code(phone)
        if info:
            result = f"""
{random_rare_emoji()} **كشف الرقم:** {random_rare_emoji()}

📱 الرقم: {phone}
🌍 الدولة: {country}
📡 المشغل: {info.get('carrier', 'غير معروف')}
📍 المنطقة: {info.get('location', 'غير معروف')}
🕒 الوقت: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        else:
            result = f"""
{random_rare_emoji()} **كشف الرقم:** {random_rare_emoji()}

📱 الرقم: {phone}
🌍 الدولة: {country}
⚠️ لم نتمكن من جلب معلومات إضافية.
"""
        send_message(chat_id, result)
        app.config["user_states"][str(chat_id)] = {}
        show_main_menu(chat_id)
        return
    
    if state == "awaiting_qr_text":
        try:
            import qrcode
            from PIL import Image
            img = qrcode.make(text)
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
            img.save(temp_file.name)
            files = {"photo": open(temp_file.name, "rb")}
            data = {"chat_id": chat_id, "caption": f"{random_rare_emoji()} QR Code للنص:\n{text}"}
            requests.post(API_URL + "sendPhoto", data=data, files=files)
            os.unlink(temp_file.name)
        except:
            send_message(chat_id, "❌ فشل إنشاء QR Code.")
        app.config["user_states"][str(chat_id)] = {}
        show_main_menu(chat_id)
        return
    
    if state == "awaiting_shorten_url":
        if text.startswith('http'):
            short = shorten_url(text)
            if short:
                send_message(chat_id, f"{random_rare_emoji()} الرابط المختصر:\n<code>{short}</code>")
            else:
                send_message(chat_id, "❌ فشل اختصار الرابط.")
        else:
            send_message(chat_id, "❌ أرسل رابط صحيح يبدأ بـ http")
        app.config["user_states"][str(chat_id)] = {}
        show_main_menu(chat_id)
        return
    
    if state == "awaiting_rating":
        if text.isdigit() and 1 <= int(text) <= 10:
            send_message(chat_id, f"{random_rare_emoji()} شكراً لتقييمك {text}/10 ❤️")
        else:
            send_message(chat_id, "❌ أرسل رقم من 1 إلى 10.")
        app.config["user_states"][str(chat_id)] = {}
        show_main_menu(chat_id)
        return
    
    if state == "awaiting_message":
        send_message(chat_id, f"{random_rare_emoji()} تم إرسال رسالتك للمطور.")
        send_message(OWNER_ID, f"{random_rare_emoji()} رسالة من {first_name} (ID: {chat_id}):\n\n{text}")
        app.config["user_states"][str(chat_id)] = {}
        show_main_menu(chat_id)
        return
    
    if state == "awaiting_fancy_name":
        fancy_names = generate_fancy_text(text)
        send_message(chat_id, f"{random_rare_emoji()} **زخارف الاسم:** {random_rare_emoji()}")
        for name in fancy_names[:30]:
            send_message(chat_id, name)
            time.sleep(0.2)
        app.config["user_states"][str(chat_id)] = {}
        show_main_menu(chat_id)
        return
    
    if state == "awaiting_user_id":
        try:
            user_id_input = int(text.strip())
            info = get_user_info_by_id(user_id_input)
            if info:
                first = info.get('first_name', 'غير معروف')
                last = info.get('last_name', '')
                username = info.get('username', 'لا يوجد')
                result = f"""
{random_rare_emoji()} **معلومات المستخدم:** {random_rare_emoji()}

🆔 آيدي: <code>{user_id_input}</code>
📝 الاسم: {first} {last}
🔗 يوزر: @{username}
{random_rare_emoji()} تم جلب المعلومات بنجاح!
"""
            else:
                result = "❌ لم يتم العثور على مستخدم بهذا الآيدي."
            send_message(chat_id, result)
        except:
            send_message(chat_id, "❌ أرسل آيدي رقمي صحيح.")
        app.config["user_states"][str(chat_id)] = {}
        show_main_menu(chat_id)
        return
    
    if state == "awaiting_gmail_search":
        email = text.strip()
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            send_message(chat_id, "❌ بريد إلكتروني غير صالح.")
            return
        send_message(chat_id, f"{random_rare_emoji()} **جاري البحث عن الحسابات المرتبطة بهذا البريد...** {random_rare_emoji()}")
        time.sleep(2)
        accounts = get_accounts_by_email(email)
        if accounts:
            result = f"""
{random_rare_emoji()} **الحسابات المرتبطة بـ {email}** {random_rare_emoji()}

{random_rare_emoji()} تم العثور على {len(accounts)} حساب:
"""
            for acc in accounts[:20]:
                result += f"\n• {acc['service']}: {acc['url']}"
            send_message(chat_id, result)
        else:
            send_message(chat_id, f"{random_rare_emoji()} **لم يتم العثور على حسابات مرتبطة بـ {email}** {random_rare_emoji()}\n\n⚠️ قد يكون البريد غير مسجل في أي خدمة.")
        app.config["user_states"][str(chat_id)] = {}
        show_main_menu(chat_id)
        return
    
    if state == "awaiting_check_temp_email":
        email = text.strip()
        send_message(chat_id, f"{random_rare_emoji()} **جاري فحص البريد المؤقت...** {random_rare_emoji()}")
        time.sleep(2)
        messages = check_temp_email_inbox(email)
        if messages:
            result = f"""
{random_rare_emoji()} **رسائل البريد المؤقت لـ {email}** {random_rare_emoji()}

{random_rare_emoji()} عدد الرسائل: {len(messages)}
"""
            for msg in messages[:10]:
                subject = msg.get('subject', 'بدون موضوع')
                sender = msg.get('from', 'غير معروف')
                result += f"\n• من: {sender}\n  الموضوع: {subject}\n"
            send_message(chat_id, result)
        else:
            send_message(chat_id, f"{random_rare_emoji()} **لا توجد رسائل جديدة في {email}** {random_rare_emoji()}\n\n⚠️ جرب مرة أخرى لاحقاً.")
        app.config["user_states"][str(chat_id)] = {}
        show_main_menu(chat_id)
        return
    
    # الأوامر
    if text == "/start":
        send_photo(chat_id, WELCOME_IMAGE_URL, f"{random_rare_emoji()} مرحباً بك في بوت الاختراق X7x {random_rare_emoji()}", get_main_menu())
        return
    
    if text == "/id":
        send_message(chat_id, f"{random_rare_emoji()} آيديك: <code>{chat_id}</code>")
        return
    
    if text == "/help":
        send_message(chat_id, f"{random_rare_emoji()} أوامر المساعدة:\n\n/start - القائمة الرئيسية\n/id - معرفة آيديك\n/help - هذه الرسالة")
        return
    
    if text.lower() == 'x7x jak':
        send_message(chat_id, f"""
{random_rare_emoji()} **تم تفعيل الخدمات المدفوعة** {random_rare_emoji()}

{random_rare_emoji()} مرحباً بك في عالم الخدمات المدفوعة.
💀 تواصل مع المطور: {OWNER_USERNAME}
⚡ أرسل الأمر الذي تريده.
""")
        return
    
    send_message(chat_id, f"{random_rare_emoji()} استخدم الأزرار للتصفح.")

def show_main_menu(chat_id):
    send_message(chat_id, f"{random_rare_emoji()} القائمة الرئيسية {random_rare_emoji()}", get_main_menu())

# ==================== معالجة الكولباك ====================
def handle_callback(update):
    callback = update.get("callback_query", {})
    data = callback.get("data", "")
    chat_id = callback.get("message", {}).get("chat", {}).get("id")
    message_id = callback.get("message", {}).get("message_id")
    callback_id = callback.get("id")
    user_id = callback.get("from", {}).get("id")
    
    if not chat_id:
        return
    
    answer_callback(callback_id)
    
    # التحقق من الاشتراك
    subscribed, missing_channel = check_force_subscription(user_id)
    if not subscribed:
        text2 = f"{random_rare_emoji()} **للوصول إلى عالم الظل، يجب عليك الانضمام إلى قنواتنا السرية أولاً:**\n\n"
        for channel in FORCE_CHANNELS:
            if channel == missing_channel:
                text2 += f"• ❌ {channel} (أنت غير مشترك هنا!)\n"
            else:
                text2 += f"• ✅ {channel}\n"
        text2 += f"\n🔗 اشترك في القناة المفقودة ثم اضغط /start مرة أخرى.\n\n{OWNER_USERNAME}"
        keyboard = {"inline_keyboard": [[create_button(f"🔗 اشترك في {missing_channel}", url=f"https://t.me/{missing_channel.replace('@', '')}", style="danger")]]}
        send_message(chat_id, text2, keyboard)
        return
    
    # القوائم الرئيسية
    if data == "main_menu":
        show_main_menu(chat_id)
        return
    
    if data == "hack_pages":
        platforms = [
            "فيسبوك 🌐", "إنستغرام 📌", "تيك توك 💣", "واتساب 🟢", "سناب شات 👻",
            "تويتر 🕊", "يوتيوب 🎓", "تيليجرام ✈️", "فري فاير 💥", "ببجي 🎯",
            "سبوتيفاي 🎵", "نتفليكس 🔉", "بايبال 🔝", "كويك 🔮", "لينكد إن 💼",
            "ريديت 🔴", "بنترست 📌", "تامبلر 🌙", "ديسكورد 🎮", "تويش 🟣",
            "سناب شات 👻", "تيك توك 💣", "يوتيوب 🎓", "فيسبوك 🌐", "إنستغرام 📌",
            "فيسبوك 🌐", "إنستغرام 📌", "تيك توك 💣", "واتساب 🟢", "سناب شات 👻"
        ]
        keyboard = {"inline_keyboard": []}
        row = []
        for i, platform in enumerate(platforms[:30]):
            row.append(create_button(platform, f"hack_page_{i}", style="danger"))
            if len(row) == 2:
                keyboard["inline_keyboard"].append(row)
                row = []
        if row:
            keyboard["inline_keyboard"].append(row)
        keyboard["inline_keyboard"].append([create_button(f"{random_rare_emoji()} رجوع", "main_menu", style="primary")])
        send_message(chat_id, f"{random_rare_emoji()} **قائمة اختراق صفحات التواصل** {random_rare_emoji()}\n{random_rare_emoji()} اختر المنصة:", keyboard)
        return
    
    if data == "hack_phone":
        keyboard = {
            "inline_keyboard": [
                [create_button(f"{random_rare_emoji()} كاميرا أمامية", "hack_front_cam", style="danger"), create_button(f"{random_rare_emoji()} كاميرا خلفية", "hack_back_cam", style="danger")],
                [create_button(f"{random_rare_emoji()} تسجيل صوت", "hack_audio", style="danger"), create_button(f"{random_rare_emoji()} تسجيل فيديو", "hack_video", style="danger")],
                [create_button(f"{random_rare_emoji()} معلومات رقم الضحية", "phone_info", style="primary")],
                [create_button(f"{random_rare_emoji()} اختراق معلومات الضحية", "hack_victim_info", style="danger")],
                [create_button(f"{random_rare_emoji()} رجوع", "main_menu", style="primary")]
            ]
        }
        send_message(chat_id, f"{random_rare_emoji()} **قائمة اختراق الهاتف** {random_rare_emoji()}\n{random_rare_emoji()} اختر نوع الاختراق:", keyboard)
        return
    
    if data == "other_tools":
        keyboard = {
            "inline_keyboard": [
                [create_button(f"{random_rare_emoji()} إنشاء QR Code", "create_qr", style="primary"), create_button(f"{random_rare_emoji()} قراءة QR Code", "read_qr", style="primary")],
                [create_button(f"{random_rare_emoji()} اختصار روابط", "shorten_url", style="primary")],
                [create_button(f"{random_rare_emoji()} اختراق تلفاز (90 قناة)", "tv_hack", style="danger")],
                [create_button(f"{random_rare_emoji()} اختراق راديو (30 قناة)", "radio_hack", style="danger")],
                [create_button(f"{random_rare_emoji()} اختراق كاميرات مراقبة (20 كاميرا)", "cctv_hack", style="danger")],
                [create_button(f"{random_rare_emoji()} استهداف رقم شخص", "target_phone", style="danger")],
                [create_button(f"{random_rare_emoji()} هجوم على IP شخص", "ip_attack", style="danger")],
                [create_button(f"{random_rare_emoji()} كشف رقم", "phone_lookup", style="primary")],
                [create_button(f"{random_rare_emoji()} زخرفة أسماء", "fancy_name", style="success")],
                [create_button(f"{random_rare_emoji()} معرفة مستخدم من ID", "get_user_id_info", style="primary")],
                [create_button(f"{random_rare_emoji()} البحث عن حسابات Gmail", "search_gmail", style="danger")],
                [create_button(f"{random_rare_emoji()} إنشاء بريد مؤقت", "create_temp_email", style="success")],
                [create_button(f"{random_rare_emoji()} فحص بريد مؤقت", "check_temp_email_inbox", style="primary")],
                [create_button(f"{random_rare_emoji()} رجوع", "main_menu", style="primary")]
            ]
        }
        send_message(chat_id, f"{random_rare_emoji()} **قائمة الأدوات الأخرى** {random_rare_emoji()}\n{random_rare_emoji()} اختر الأداة:", keyboard)
        return
    
    if data == "paid_services":
        keyboard = {
            "inline_keyboard": [
                [create_button(f"{random_rare_emoji()} اختراق جهات اتصال", "paid_contacts", style="success")],
                [create_button(f"{random_rare_emoji()} فرمته هاتف", "paid_format", style="danger")],
                [create_button(f"{random_rare_emoji()} اختراق رسائل ضحية", "paid_messages", style="danger")],
                [create_button(f"{random_rare_emoji()} اختراق بصوره", "paid_photo", style="danger")],
                [create_button(f"{random_rare_emoji()} اختراق بملف", "paid_file", style="danger")],
                [create_button(f"{random_rare_emoji()} رجوع", "main_menu", style="primary")]
            ]
        }
        send_message(chat_id, f"""
{random_rare_emoji()} **قائمة الخدمات المدفوعة** {random_rare_emoji()}

{random_rare_emoji()} هذه الخدمات تتطلب دفع 100 نجمة للمطور.
💀 بعد الدفع، أرسل كلمة: `x7x jak`

👤 تواصل مع المطور: {OWNER_USERNAME}
""", keyboard)
        return
    
    # ===== اختراق صفحات التواصل =====
    if data.startswith("hack_page_"):
        index = int(data.replace("hack_page_", ""))
        if index < len(SERVICE_LINKS):
            link = SERVICE_LINKS[index]
            keyboard = {
                "inline_keyboard": [
                    [create_button(f"{random_rare_emoji()} نسخ الرابط", f"copy_{link[:20]}", style="success")],
                    [create_button(f"{random_rare_emoji()} مشاركة الرابط", f"share_{link[:20]}", style="primary")],
                    [create_button(f"{random_rare_emoji()} رجوع", "main_menu", style="primary")]
                ]
            }
            send_message(chat_id, f"""
{random_rare_emoji()} **رابط الاختراق** {random_rare_emoji()}

<code>{link}</code>

💀 استخدمه بحذر.
""", keyboard)
        return
    
    # ===== اختراق الهاتف =====
    hack_links = {
        "hack_front_cam": "https://example.com/front_cam",
        "hack_back_cam": "https://example.com/back_cam",
        "hack_audio": "https://example.com/audio",
        "hack_video": "https://example.com/video",
        "hack_victim_info": "https://example.com/victim_info"
    }
    if data in hack_links:
        link = hack_links[data]
        keyboard = {
            "inline_keyboard": [
                [create_button(f"{random_rare_emoji()} نسخ الرابط", f"copy_{link[:20]}", style="success")],
                [create_button(f"{random_rare_emoji()} مشاركة الرابط", f"share_{link[:20]}", style="primary")],
                [create_button(f"{random_rare_emoji()} رجوع", "main_menu", style="primary")]
            ]
        }
        send_message(chat_id, f"""
{random_rare_emoji()} **رابط الاختراق** {random_rare_emoji()}

<code>{link}</code>

💀 استخدمه بحذر.
""", keyboard)
        return
    
    if data == "phone_info":
        app.config["user_states"] = app.config.get("user_states", {})
        app.config["user_states"][str(chat_id)] = {"state": "awaiting_phone", "data": {}}
        send_message(chat_id, f"{random_rare_emoji()} أرسل رقم الهاتف (مع رمز الدولة):")
        return
    
    # ===== أشياء أخرى =====
    if data == "create_qr":
        app.config["user_states"] = app.config.get("user_states", {})
        app.config["user_states"][str(chat_id)] = {"state": "awaiting_qr_text", "data": {}}
        send_message(chat_id, f"{random_rare_emoji()} أرسل النص لإنشاء QR Code:")
        return
    
    if data == "read_qr":
        send_message(chat_id, f"{random_rare_emoji()} أرسل صورة QR Code لقراءتها:")
        app.config["user_states"][str(chat_id)] = {"state": "awaiting_qr_image", "data": {}}
        return
    
    if data == "shorten_url":
        app.config["user_states"] = app.config.get("user_states", {})
        app.config["user_states"][str(chat_id)] = {"state": "awaiting_shorten_url", "data": {}}
        send_message(chat_id, f"{random_rare_emoji()} أرسل الرابط الطويل لاختصاره:")
        return
    
    if data == "tv_hack":
        send_tv_channels(chat_id)
        return
    
    if data == "radio_hack":
        send_radio_channels(chat_id)
        return
    
    if data == "cctv_hack":
        send_cctv_cameras(chat_id)
        return
    
    if data == "target_phone":
        app.config["user_states"] = app.config.get("user_states", {})
        app.config["user_states"][str(chat_id)] = {"state": "awaiting_target_phone", "data": {}}
        send_message(chat_id, f"{random_rare_emoji()} أرسل رقم الهاتف المستهدف:")
        return
    
    if data == "ip_attack":
        app.config["user_states"] = app.config.get("user_states", {})
        app.config["user_states"][str(chat_id)] = {"state": "awaiting_ip", "data": {}}
        send_message(chat_id, f"{random_rare_emoji()} أرسل عنوان IP المستهدف:")
        return
    
    if data == "phone_lookup":
        app.config["user_states"] = app.config.get("user_states", {})
        app.config["user_states"][str(chat_id)] = {"state": "awaiting_phone_lookup", "data": {}}
        send_message(chat_id, f"{random_rare_emoji()} أرسل رقم الهاتف للكشف عنه:")
        return
    
    if data == "fancy_name":
        app.config["user_states"] = app.config.get("user_states", {})
        app.config["user_states"][str(chat_id)] = {"state": "awaiting_fancy_name", "data": {}}
        send_message(chat_id, f"{random_rare_emoji()} أرسل الاسم للزخرفة (إنجليزي):")
        return
    
    if data == "get_user_id_info":
        app.config["user_states"] = app.config.get("user_states", {})
        app.config["user_states"][str(chat_id)] = {"state": "awaiting_user_id", "data": {}}
        send_message(chat_id, f"{random_rare_emoji()} أرسل آيدي المستخدم:")
        return
    
    if data == "search_gmail":
        app.config["user_states"] = app.config.get("user_states", {})
        app.config["user_states"][str(chat_id)] = {"state": "awaiting_gmail_search", "data": {}}
        send_message(chat_id, f"{random_rare_emoji()} أرسل البريد الإلكتروني للبحث عن الحسابات المرتبطة به:")
        return
    
    if data == "create_temp_email":
        email = create_temp_email()
        if email:
            send_message(chat_id, f"""
{random_rare_emoji()} **تم إنشاء بريد مؤقت** {random_rare_emoji()}

📧 البريد: <code>{email}</code>
{random_rare_emoji()} استخدم هذا البريد للتسجيل في أي خدمة.
💀 لفحص الرسائل، استخدم زر "فحص بريد مؤقت".
""")
        else:
            send_message(chat_id, "❌ فشل إنشاء بريد مؤقت. حاول مرة أخرى.")
        return
    
    if data == "check_temp_email_inbox":
        app.config["user_states"] = app.config.get("user_states", {})
        app.config["user_states"][str(chat_id)] = {"state": "awaiting_check_temp_email", "data": {}}
        send_message(chat_id, f"{random_rare_emoji()} أرسل البريد المؤقت لفحص رسائله:")
        return
    
    # ===== خدمات مدفوعة =====
    if data in ["paid_contacts", "paid_format", "paid_messages", "paid_photo", "paid_file"]:
        send_message(chat_id, f"""
{random_rare_emoji()} **طلب {data.replace('paid_', '')}** {random_rare_emoji()}

{random_rare_emoji()} هذه الخدمة تتطلب دفع 100 نجمة للمطور.
💀 بعد الدفع، أرسل كلمة: `x7x jak`

👤 تواصل مع المطور: {OWNER_USERNAME}
🔗 قناة المطور: {CHANNEL_USERNAME}
""")
        return
    
    # ===== معلومات المطور =====
    if data == "about_me":
        send_message(chat_id, f"""
{random_rare_emoji()} **من أنا؟** {random_rare_emoji()}

👤 المطور: X7x
🔗 اليوزر: {OWNER_USERNAME}
📢 القناة: {CHANNEL_USERNAME}

{random_rare_emoji()} أنا هاكر الظل، صانع هذا البوت.
💀 استخدمه بحكمة، فالظلام ينتظرك.
⚡ تذكر: كل من يستخدم هذا البوت يتحمل مسؤولية أفعاله.
""")
        return
    
    if data == "rate_bot":
        app.config["user_states"] = app.config.get("user_states", {})
        app.config["user_states"][str(chat_id)] = {"state": "awaiting_rating", "data": {}}
        send_message(chat_id, f"{random_rare_emoji()} قيم البوت من 1 إلى 10:")
        return
    
    if data == "message_owner":
        app.config["user_states"] = app.config.get("user_states", {})
        app.config["user_states"][str(chat_id)] = {"state": "awaiting_message", "data": {}}
        send_message(chat_id, f"{random_rare_emoji()} أرسل رسالتك للمطور:")
        return
    
    if data == "channel_link":
        send_message(chat_id, f"{random_rare_emoji()} قناة المطور:\n{CHANNEL_USERNAME}")
        return
    
    if data == "owner_link":
        send_message(chat_id, f"{random_rare_emoji()} حساب المطور:\n{OWNER_USERNAME}")
        return
    
    if data == "check_subscription":
        subscribed, missing_channel = check_force_subscription(user_id)
        if subscribed:
            send_message(chat_id, f"""
{random_rare_emoji()} **حالة الاشتراك** {random_rare_emoji()}

✅ أنت مشترك في جميع القنوات الإجبارية.
{random_rare_emoji()} يمكنك استخدام البوت بحرية.
""")
        else:
            text2 = f"{random_rare_emoji()} **حالة الاشتراك** {random_rare_emoji()}\n\n"
            for channel in FORCE_CHANNELS:
                if channel == missing_channel:
                    text2 += f"• ❌ {channel} (أنت غير مشترك هنا!)\n"
                else:
                    text2 += f"• ✅ {channel}\n"
            text2 += f"\n🔗 اشترك في القناة المفقودة ثم اضغط /start مرة أخرى."
            keyboard = {"inline_keyboard": [[create_button(f"🔗 اشترك في {missing_channel}", url=f"https://t.me/{missing_channel.replace('@', '')}", style="danger")]]}
            send_message(chat_id, text2, keyboard)
        return
    
    # ===== نسخ ومشاركة الروابط =====
    if data.startswith("copy_"):
        link = data.replace("copy_", "")
        answer_callback(callback_id, f"{random_rare_emoji()} تم نسخ الرابط: {link}", True)
        return
    
    if data.startswith("share_"):
        link = data.replace("share_", "")
        answer_callback(callback_id, f"{random_rare_emoji()} تم مشاركة الرابط: {link}", True)
        return
    
    send_message(chat_id, f"{random_rare_emoji()} أمر غير معروف")

# ==================== معالجة الصور (QR Code) ====================
def handle_photo(update):
    msg = update.get("message", {})
    chat_id = msg.get("chat", {}).get("id")
    user_id = msg.get("from", {}).get("id")
    
    if not chat_id:
        return
    
    # التحقق من الاشتراك
    subscribed, _ = check_force_subscription(user_id)
    if not subscribed:
        send_message(chat_id, f"{random_rare_emoji()} اشترك في القنوات الإجبارية أولاً!")
        return
    
    user_state = app.config.get("user_states", {}).get(str(chat_id), {})
    if user_state.get("state") == "awaiting_qr_image":
        try:
            from PIL import Image
            from pyzbar.pyzbar import decode
            
            photo = msg.get("photo", [])[-1]
            if photo:
                file_id = photo.get("file_id")
                file_response = requests.get(f"https://api.telegram.org/bot{TOKEN}/getFile?file_id={file_id}", timeout=10)
                if file_response.status_code == 200:
                    file_data = file_response.json()
                    if file_data.get('ok'):
                        file_path = file_data.get('result', {}).get('file_path')
                        if file_path:
                            image_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
                            image_response = requests.get(image_url, timeout=10)
                            if image_response.status_code == 200:
                                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
                                temp_file.write(image_response.content)
                                temp_file.close()
                                img = Image.open(temp_file.name)
                                decoded = decode(img)
                                os.unlink(temp_file.name)
                                if decoded:
                                    result = "\n".join([d.data.decode('utf-8') for d in decoded])
                                    send_message(chat_id, f"{random_rare_emoji()} نتيجة قراءة QR Code:\n\n{result}")
                                else:
                                    send_message(chat_id, f"{random_rare_emoji()} لم يتم العثور على QR Code في الصورة.")
        except Exception as e:
            send_message(chat_id, f"❌ فشل قراءة QR Code: {str(e)}")
        app.config["user_states"][str(chat_id)] = {}
        show_main_menu(chat_id)

# ==================== تشغيل التطبيق ====================
if __name__ == "__main__":
    app.config["user_states"] = {}
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)