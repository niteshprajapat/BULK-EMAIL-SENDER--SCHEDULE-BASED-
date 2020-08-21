import schedule
import smtplib
import time
import pyautogui

sender_email=pyautogui.prompt("enter your email :: ")
sender_passwrd=pyautogui.prompt("enter your password :: ")
receiver_email=['niteshp282000@gmail.com','nitesh.19jdml019@jietjodhpur.ac.in','niteshprajapat7918@gmail.com']
msg=pyautogui.prompt("enter message :: ")
subject=pyautogui.prompt("enter subject :: ")
body="Subject : {}\n\n{}".format(subject,msg)


def sendemail():
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login(sender_email,sender_passwrd)
    server.sendmail(sender_email,receiver_email,body)
    print("\n Email Sent !!!")
    server.close()

schedule.every(5).seconds.do(sendemail)   # YOU CAN CHANGE ACCORDING TO YOUR NEED. SEND AT PARTICULAR TIME  
while True:
    schedule.run_pending()
    time.sleep(1)
