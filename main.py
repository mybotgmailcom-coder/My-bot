import os
import re
import time
import telebot
import yt_dlp
import requests
from flask import Flask
from threading import Thread

# --- [ 1. إعدادات السيرفر والإنعاش ] ---
app = Flask('')
@app.route('/')
def home(): return "🛡️ نظام الإنعاش والشريط يعملان!"

def run_flask(): app.run(host='0.0.0.0', port=8080)

def self_ping(my_url):
    time.sleep(20)
    while True:
        try:
            requests.get(my_url)
            print("🔄 [الإنعاش الذاتي]: نبضة نشاط...")
        except: pass
        time.sleep(120)

# --- [ 2. إعدادات البوت - ضع بياناتك هنا ] ---
TOKEN = '8435550693:AAHukv4wnBdXyT2CSHE29mAlEwjkqOSicUI'
MY_ID = 8750837960 
MY_REPLIT_URL = "https://your-project-name.replit.dev" 

bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")

# --- [ 3. نظام شريط التحميل الذكي ] ---
def progress_hook(d):
    if d['status'] == 'downloading':
        # حساب النسبة المئوية
        p = d.get('_percent_str', '0%')
        p = p.replace('%','')
        try:
            percent = float(p)
        except:
            percent = 0
            
        # صنع شكل الشريط [████░░░░]
        bar_length = 10
        filled_length = int(bar_length * percent / 100)
          
