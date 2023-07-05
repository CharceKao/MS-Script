import pyautogui
import pydirectinput
import time
import keyboard

import threading
import time
import os

def on_key_press(event):
    if event.name == 'f5':  # 检测按下的键是否为 F5 键
        print()
        keyboard.unhook_all()  # 解除键盘钩子，停止检测按键

def check_for_esc():
    while True:
        if keyboard.is_pressed('esc'):  # 检测按下的键是否为 Esc 键
            print("按下了 Esc 键，中止执行")
            os._exit(0)  # 退出程序
        time.sleep(0.05)  # 每隔 0.1 秒检测一次


def apple():
    y=0
    while y < 9999:
        pydirectinput.click(position.x, position.y)
        time.sleep(0.5)
        pydirectinput.press('enter') 
        y+=1
        print(y)
        if keyboard.is_pressed('esc'):
            print('esc')
            break

def p():
    y=0
    i=int(input('How many times?'))
    while y < i:
        pydirectinput.click(position.x, position.y)#方塊
        time.sleep(0.1)
        pydirectinput.press('enter')
        pydirectinput.press('enter')
        pydirectinput.press('enter')
        time.sleep(1.5)
        y+=1
        print(y)

# 创建一个线程来检测按下的键
esc_thread = threading.Thread(target=check_for_esc)
esc_thread.start()

print('按下F5，開始執行')
keyboard.on_press(on_key_press)  # 注册按键按下事件的回调函数
keyboard.wait('f5')  # 等待按下 F5 键

position = pyautogui.position()

position_tuple = (position.x, position.y)# 將位置數據轉換為元組

print(pyautogui.position())
pro=int(input('開哪個,輸入數字不用括號?(1)蘋果,艾比,畫框(2)方塊'))

if pro == 1:
    apple()
elif pro == 2:
    p()
else:
    print('請輸入 1 or 2')