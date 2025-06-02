# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import requests
import time

# إعدادات
URL_TO_CHECK = "https://progres.mesrs.dz/api/infos"  # ضع رابط سيرفرك
BOT_TOKEN = "7692895178:AAHszRdfhIhKtYO25YmLl2At2bv_0uldbX8"
CHAT_ID = "2083911159"  # احصل عليه من تيليغرام بإرسال رسالة للبوت واستخدام Bot API
CHECK_INTERVAL = 300  # كل 5 دقائق
last_status = None

def is_server_up(url):
    try:
        response = requests.get(url, timeout=10)
        return response.status_code == 200
    except requests.RequestException:
        return False

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload)

while True:
    status = is_server_up(URL_TO_CHECK)
    if last_status is None:
        last_status = status
    elif status != last_status:
        if status:
            send_telegram_message("✅ السيرفر عاد للعمل!")
        else:
            send_telegram_message("❌ السيرفر متوقف الآن!")
        last_status = status
    time.sleep(CHECK_INTERVAL)
