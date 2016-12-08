import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import time
from threading import Thread
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import tweepy
import os
import coinmarketcap
import PIL
import urllib
from exchanges.coindesk import CoinDesk
from PIL import Image
ACCESS_KEY = '804765046786158593-G8KXOT3U1Wb5LVK3VQ1ImCgXdc0R2Kt'
ACCESS_SECRET = 'STsmZaLk0OR3EanLfW1CtvKdkrCCwcYudu8ogSEtn4Fwl'
CONSUMER_KEY = '7QaxRKX4wo2iqVjSdll8CPDiE'
CONSUMER_SECRET = '62zg79fj3fae2pcTnP7JL1Zh3jeIbJqRMxfHU9RVNuq14SJl6y'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.secure = True
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
done = 0
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
font = ImageFont.truetype("C:\Windows\Fonts\proximanova-regular-webfont.ttf",25)
bitcoinpricelist = []

def creategraph():
    global bitcoinpricelist
    print "Creating Graph"
    plt.figure 
    numbersin10s = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100, 1110, 1120, 1130, 1140, 1150, 1160, 1170, 1180, 1190, 1200, 1210, 1220, 1230, 1240, 1250, 1260, 1270, 1280, 1290, 1300, 1310, 1320, 1330, 1340, 1350, 1360, 1370, 1380, 1390, 1400, 1410, 1420, 1430, 1440, 1450, 1460, 1470, 1480, 1490, 1500, 1510, 1520, 1530, 1540, 1550, 1560, 1570, 1580, 1590, 1600, 1610, 1620, 1630, 1640, 1650, 1660, 1670, 1680, 1690, 1700, 1710, 1720, 1730, 1740, 1750, 1760, 1770, 1780, 1790, 1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870, 1880, 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100, 2110, 2120, 2130, 2140, 2150, 2160, 2170, 2180, 2190, 2200, 2210, 2220, 2230, 2240, 2250, 2260, 2270, 2280, 2290, 2300, 2310, 2320, 2330, 2340, 2350, 2360, 2370, 2380, 2390, 2400, 2410, 2420, 2430, 2440, 2450, 2460, 2470, 2480, 2490, 2500, 2510, 2520, 2530, 2540, 2550, 2560, 2570, 2580, 2590, 2600, 2610, 2620, 2630, 2640, 2650, 2660, 2670, 2680, 2690, 2700, 2710, 2720, 2730, 2740, 2750, 2760, 2770, 2780, 2790, 2800, 2810, 2820, 2830, 2840, 2850, 2860, 2870, 2880]
    x_series = np.array(numbersin10s)
    y_series_1 = np.array(bitcoinpricelist)
    f = plt.figure(facecolor=".6")
    f.add_subplot(111, axisbg=".6")
    plt.plot(x_series, y_series_1)
    plt.grid(b=True, which='both', color='0.13882323',linestyle='-')
    plt.grid(b=True, which='minor', color='r', linestyle='--')
    ax = plt.gca()
    ax.axes.get_xaxis().set_visible(False)
    ax.relim()
    ax.autoscale_view()
    plt.savefig("btcprice.png")
    global done
    if not done == 1:
        Thread(target = tweet).start()
        done = 1
    
def getbtcprice():
    while True:
        for i in range(0,288):
            global bitcoinpricelist
            bitcoinprice = CoinDesk().get_current_price()
            if not len(bitcoinpricelist) == 288:
                bitcoinpricelist.append(float(bitcoinprice))
            else:
                bitcoinpricelist[i] = float(bitcoinprice)
            time.sleep(300)
            if len(bitcoinpricelist) < 288:
                print len(bitcoinpricelist)
def onceready():
    run = 0
    while True:
        global bitcoinpricelist
        amount = len(bitcoinpricelist)
        if amount == 288:
            if run == 0:
                Thread(target = runit).start()
                run = 1

def runit():
    while True:
        creategraph()
        time.sleep(9000)

def tweet():
    while True:
        imagemod()
        btcprice = str(CoinDesk().get_current_price())
        status = ("The bitcoin price is $" + btcprice + ". #Bitcoin #Price")
        fn = os.path.abspath("finished.png")
        api.update_with_media(fn, status=status)
        time.sleep(7200)

def imagemod():
    bitcoinprice = CoinDesk().get_current_price()
    img = Image.open("btcprice.png")
    img2 = img.crop((63, 49, 735, 550))
    basewidth = 300
    wpercent = (basewidth/float(img2.size[0]))
    hsize = int((float(img2.size[1])*float(wpercent)))
    img2 = img2.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
    img3 = Image.open("template.png")
    img3.paste(img2, (0,90), img2)
    draw = ImageDraw.Draw(img3)
    draw.text((95, 20),str(bitcoinprice),(255,255,255),font=font)
    draw = ImageDraw.Draw(img3)
    draw = ImageDraw.Draw(img3)
    #if bitcoinpricelist[0] < bitcoinpricelist[143]:
        #img4 = Image.open("positive.png")
    #else:
    img4 = Image.open("negative.png")
    img3.paste(img4, (65,55), img4)
    draw = ImageDraw.Draw(img3)
    draw.text((105, 53),"1.9",(255,255,255),font=font)
    draw = ImageDraw.Draw(img3)
    draw = ImageDraw.Draw(img3)
    img3.save("finished.png")
  

Thread(target = getbtcprice).start()
Thread(target = onceready).start()
