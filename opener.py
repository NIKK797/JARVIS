import os
import webbrowser


def open(command):



        if "youtube" in command:
            webbrowser.open("www.youtube.com")

        if "amazon" in command:
            webbrowser.open("www.amazon.in")

        if "google" in command:
            webbrowser.open("www.google.com")

        if "flipkart" in command:
            webbrowser.open("www.flipkart.in")


        if "map" in command:
            webbrowser.open("maps.google.com")

        if "taskmanager" in command or "task manager" in command:
               os.system("explorer C:\Windows\system32\Taskmgr.exe")

        if "android studio" in command or "androidstudio" in command:
            os.system("explorer C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Android Studio\Android Studio.lnk")

        if "etsy" in command:
            webbrowser.open("https://www.etsy.com/in-en/your/shops/me/dashboard?ref=hdr-mcpa")