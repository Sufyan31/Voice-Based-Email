import speech_recognition as sr
import smtplib
# import pyaudio
# import platform
# import sys
from bs4 import BeautifulSoup
import email
import imaplib
from gtts import gTTS
import pyglet
import os, time
from tkinter import *


def get_email_info():
    tts = gTTS(text="Welcome to Email BOT", lang='en')
    ttsname = (
        "name.mp3")
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming=False)
    music.play()

    time.sleep(music.duration)
    os.remove(ttsname)

    # login from os
    login = os.getlogin
    print("You are logging from : " + login())

    # choices
    print("1. say compose to compose a mail.")
    tts = gTTS(text="option 1. compose a mail.", lang='en')
    ttsname = (
        "hello.mp3")
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming=False)
    music.play()

    time.sleep(music.duration)
    os.remove(ttsname)

    print("2. Check your inbox")
    tts = gTTS(text="option 2. say check to Check your inbox", lang='en')
    ttsname = ("second.mp3")
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming=False)
    music.play()

    time.sleep(music.duration)
    os.remove(ttsname)

    # this is for input choices
    tts = gTTS(text="Your choice ", lang='en')
    ttsname = ("hello.mp3")
    tts.save(ttsname)

    music = pyglet.media.load(ttsname, streaming=False)
    music.play()

    time.sleep(music.duration)
    os.remove(ttsname)

    # voice recognition part
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Your choice:")
        audio = r.listen(source)
        print("ok done!!")

    try:
        text = r.recognize_google(audio)
        print("You said : " + text)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    email_list = {
            'black': 'sufyanmohamed2002@gmail.com',
            'blue': 'dineshmn2003@gmail.com',
            'green': 'shrikaanth2002@gmail.com'
        }
    # choices details
    if text == 'Compose' or text == 'COMPOSE' or text == 'compose':
        r = sr.Recognizer()  # recognize
        with sr.Microphone() as source:

            tts = gTTS(text="To Whom you want to send email", lang='en')
            ttsname = ("who.mp3")
            tts.save(ttsname)
            music = pyglet.media.load(ttsname, streaming=False)
            music.play()
            time.sleep(music.duration)
            os.remove(ttsname)

            print("Send To :")
            audio = r.listen(source)
            print("ok done!!")
        try:
            send = r.recognize_google(audio)
            s = "You Said " + send
            tts = gTTS(text=s, lang='en')
            ttsname = ("txt1.mp3")
            tts.save(ttsname)
            music = pyglet.media.load(ttsname, streaming=False)
            music.play()
            time.sleep(music.duration)
            os.remove(ttsname)
            print("You said : " + send)
            sid = send
            if(sid == "blue" or sid == "Blue" or sid == "BLUE"):
                sendto = email_list["blue"]
            elif(sid == "black" or sid == "Black" or sid == "BLACK"):
                sendto = email_list["black"]
            elif (sid == "green" or sid == "Green" or sid == "GREEN"):
                sendto = email_list["green"]
            else:
                sendto = "dummetting00@gmail.com"
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        with sr.Microphone() as source:
            tts = gTTS(text="Your Message", lang='en')
            ttsname = ("msg.mp3")
            tts.save(ttsname)
            music = pyglet.media.load(ttsname, streaming=False)
            music.play()
            time.sleep(music.duration)
            os.remove(ttsname)

            print("Your message :")
            audio = r.listen(source)
            print("ok done!!")
        try:

            text1 = r.recognize_google(audio)
            s = "You Said "+text1
            tts = gTTS(text=s, lang='en')
            ttsname = ("txt.mp3")
            tts.save(ttsname)
            music = pyglet.media.load(ttsname, streaming=False)
            music.play()
            time.sleep(music.duration)
            os.remove(ttsname)
            print("You said : " + text1)
            msg = text1
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        mail = smtplib.SMTP('smtp.gmail.com', 587)  # host and port area
        mail.ehlo()  # Hostname to send for this command defaults to the FQDN of the local host.
        mail.starttls()  # security connection
        mail.login('sufyanmohamed2002@gmail.com', 'dmvrncqrbzsvmeoh')  # login part
        mail.sendmail('sufyanmohamed2002@gmail.com', sendto, msg)  # send part
        print("Congrats! Your mail has sent. ")
        tts = gTTS(text="Congrates! Your mail has send. ", lang='en')
        ttsname = ("send.mp3")
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming=False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
        mail.close()

    if text == 'Check' or text == 'check' or text == 'CHECK':
        mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)  # this is host and port area.... ssl security
        unm = ('sufyanmohamed2002@gmail.com')  # username
        psw = ('dmvrncqrbzsvmeoh')  # password
        mail.login(unm, psw)  # login
        stat, total = mail.select('Inbox')  # total number of mails in inbox
        print("Number of mails in your inbox :" + str(total))
        tts = gTTS(text="Total mails are :" + str(total), lang='en')  # voice out
        ttsname = ("total.mp3")
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming=False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)

        # unseen mails
        unseen = mail.search(None, 'UnSeen')  # unseen count
        print("Number of UnSeen mails :" + str(unseen))
        tts = gTTS(text="Your Unseen mail :" + str(unseen), lang='en')
        ttsname = (
            "unseen.mp3")  # Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming=False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)

        # search mails
        result, data = mail.uid('search', None, "ALL")
        inbox_item_list = data[0].split()
        new = inbox_item_list[-1]
        old = inbox_item_list[0]
        result2, email_data = mail.uid('fetch', new, '(RFC822)')  # fetch
        raw_email = email_data[0][1].decode("utf-8")  # decode
        email_message = email.message_from_string(raw_email)
        print("From: " + email_message['From'])
        print("Subject: " + str(email_message['Subject']))
        tts = gTTS(text="From: " + email_message['From'] + " And Your subject: " + str(email_message['Subject']), lang='en')
        ttsname = (
            "mail.mp3")  # Example: path -> C:\Users\sayak\Desktop> just change with your desktop directory. Don't use my directory.
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming=False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)

        # Body part of mails
        stat, total1 = mail.select('Inbox')
        stat, data1 = mail.fetch(total1[0], "(UID BODY[TEXT])")
        msg = data1[0][1]
        soup = BeautifulSoup(msg, "html.parser")
        txt = soup.get_text()
        print("Body :" + txt)
        mail.close()
        mail.logout()


win = Tk()
lbl1 = Label(win, text='Welcome to Email bot', fg='blue', font=('HP Simplified Hans', 20))
lbl2 = Label(win, text='INSTRUCTIONS', fg='darkviolet', font=('HP Simplified Hans', 16))
lbl3 = Label(win, text='1.Press the button in order to get started', font=('HP Simplified Hans', 12))
lbl4 = Label(win, text='2.Use microphones, as it is voice controlled', font=('HP Simplified Hans', 12))
lbl5 = Label(win, text='3.Say compose to send a mail', font=('HP Simplified Hans', 12))
lbl6 = Label(win, text='4.Say check to check for unread messages', font=('HP Simplified Hans', 12))
lbl7 = Label(win, text='Mail ID options', fg='darkviolet', font=('HP Simplified Hans', 16))
lbl8 = Label(win, text='black = sufyanmohamed2002@gmail.com', font=('HP Simplified Hans', 12))
lbl9 = Label(win, text='blue = dineshmn2003@gmail.com', fg='blue', font=('HP Simplified Hans', 12))
lbl10 = Label(win, text='green = shrikaanth2002@gmail.com', fg='green', font=('HP Simplified Hans', 12))
lbl1.place(x=150, y=0)
lbl2.place(x=179, y=50)
lbl3.place(x=109, y=90)
lbl4.place(x=109, y=110)
lbl5.place(x=109, y=130)
lbl6.place(x=109, y=150)
lbl7.place(x=179, y=180)
lbl8.place(x=109, y=220)
lbl9.place(x=109, y=240)
lbl10.place(x=109, y=260)
b1 = Button(win, text="GET STARTED", command=get_email_info)
b1.place(x=209, y=300)
win.title('MAIL BOT')
win.geometry("510x330")
win.mainloop()
