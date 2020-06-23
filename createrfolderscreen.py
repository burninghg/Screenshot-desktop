import os
import datetime
import pyautogui as pa
import time
def get_file_path(dirs):
    time_format = "%y-%m-%d_%H-%M-%S"
    time_now=time.strftime(time_format,time.localtime())
    file_path=os.path.join(dirs,time_now)
    file_path=file_path+".png"
    return file_path
def screen_shot(file_path):
    im1 = pa.screenshot(file_path)
def sleeptime(hour,min,sec):
    return hour*3600+min*60+sec
second = sleeptime(0,5,0)
name = datetime.datetime.now().strftime('%y%m%d')
pwd = "D:\OneDrive - s.upc.edu.cn\YOGA\Pictures\monitor"+"\\"+name
def main():
    while True:
        word_name = os.path.exists(pwd)
        if not word_name:
            os.makedirs(pwd)
        time.sleep(second)
        screen_shot(get_file_path(pwd))

main()
