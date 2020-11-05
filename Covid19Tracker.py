# Project to track Corona Virus updates for india

import requests
import bs4
import tkinter as tk
import plyer
import datetime
import time
import threading


def get_html_data(url):
    data = requests.get(url)
    return data


def get_corona_detail_of_india():
    url = "https://www.mygov.in/covid-19/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="information_row").find_all("div", class_="iblock_text")
    all_detail = ""
    for block in info_div:
        count = block.find("span", class_="icount").get_text().replace(" ", "")
        text = block.find("div", class_="info_label").get_text().replace("   ", "")
        all_detail = all_detail + text + " : " + count + "\n"
    return all_detail


# function used to reload the data from website
def refresh():
    newdata = get_corona_detail_of_india()
    mainLabel['text'] = newdata


# function for notification

def notify_me():
    while True:
        plyer.notification.notify(title='Covid19 cases of india', message=get_corona_detail_of_india(), timeout=10)
        time.sleep(30)


# creating GUI
root = tk.Tk()
root.geometry("900x800")
root.title("Corona Tracker for India")
f = ("poppins", 25, "bold")
mainLabel = tk.Label(root, text=get_corona_detail_of_india(), font=f)
mainLabel.pack()
reBtn = tk.Button(root, text="Refresh", font=f, relief="solid", command=refresh)
reBtn.pack()

# create a new thread
th1 = threading.Thread(target=notify_me())
th1.setDaemon(True)
th1.start()

root.mainloop()
