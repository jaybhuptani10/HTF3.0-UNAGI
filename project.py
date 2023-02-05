from googletrans import Translator
import datetime
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import webbrowser
import openai
import os
import csv
import random
from bs4 import BeautifulSoup
import pyautogui
import requests
import time
import wikipedia
import pyjokes
from translate import Translator
from email.message import EmailMessage
import ssl
import smtplib
from difflib import SequenceMatcher
import subprocess
import winshell
#htf044
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
chrome_options=Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless=True #we wont be able to see it
path="chromedriver.exe"
driver=webdriver.Chrome(path,options=chrome_options)
driver.maximize_window()#chrome maximized
website=r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
ButtonSelection=Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
ButtonSelection.select_by_visible_text('British English / Brian')
def speak(audio):
    lengh=len(str(audio))
    if lengh==0:
        pass
    else:
        print("")
        print(f"AI: {audio}")
        print("")
        Data=str(audio)
        xpathofsec='/html/body/div[4]/div[2]/form/textarea'
        driver.find_element(By.XPATH,value=xpathofsec).send_keys(Data)
        driver.find_element(By.XPATH,value='//*[@id="vorlesenbutton"]').click()
        driver.find_element(By.XPATH,value='/html/body/div[4]/div[2]/form/textarea').clear()
        if lengh>=30:
            sleep(3)
        elif lengh>=40:
            sleep(6)
        elif lengh>=55:
            sleep(10)
        elif lengh>=70:
            sleep(12)
        elif lengh>=100:
            sleep(14)
        elif lengh>=120:
            sleep(15)
        else:
            sleep(4)
def wishme(): 
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour <18:
        speak("good afternoon!")
    else:
        speak('good evening')
    speak("I am ROSS sir. how may i help you")
def  takecommand():
    #it takes microphone input from the user and returns output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 0.5
        r.energy_threshold = 1500
        audio=r.listen(source)
        try:
            print("recognising...")
            query = r.recognize_google(audio,language="en")
            print("user said:"+query)
        except Exception as  e:
            print("say that again please!")
            return "None"
        return query
if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()
         # logic for executing task based on query  
                    #opening queries 
        if 'youtube' in query:
            speak("opening youtube sir...")
            if query=='open youtube':
                webbrowser.open("youtube.com")
            else:
                query=query.replace('open ',"")
                query=query.replace(" in youtube","")
                webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
                speak(". opening youtube,sir")
                webbrowser.open("youtube.com")
        elif 'food' in query or 'zomato' in query or 'hungry' in query:
            webbrowser.open("https://www.zomato.com/")
        elif 'where' in query:
            query=query.replace("where is","")
            webbrowser.open("https://www.google.com/maps/place/"+query+"")
        elif 'google' in query:
            webbrowser.open("https://www.google.com/")
        elif 'camera' in query:
            speak("opening")
            os.system("start Microsoft.Windows.Camera:")
        elif 'write' in query:
            speak("what you want to enter")
            a=takecommand()
            file=open("Ross.txt",'w')
            file.write(a)
            file.close()
            speak("done file saved")
        elif 'show notes' in query:
            speak("Reading the files")
            file=open("Ross.txt",'r')
            l=file.read()
            speak(l)
            file.close()
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
        elif 'meaning of' in query:
            n=query.replace("what is the meaning of","")
            url=(f"https://www.dictionary.com/browse/{n}")
            r=requests.get(url)
            htmlcontent=r.content
            soup=BeautifulSoup(htmlcontent,'html.parser')
            try:
                a=soup.find(class_='one-click-content css-nnyc96 e1q3nk1v1')
                print(a.getText())
                speak(a.getText())
            except:
                print("Word not found")
                speak("word not found)")
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much seconds you want to stop jarvis from listening commands")
            a = int(takecommand())
            time.sleep(a)
            print(a)
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"sir,the time is{strTime} ")
        elif'opinion about women' in query:
            speak("women.")
            speak("hahahahaha")
        
        
        elif 'joke' in query:
            My_joke = pyjokes.get_joke(language="en", category="neutral")
            
            speak(My_joke)
        elif 'translate to spanish' in query:
        
            speak("what do u want to translate")
            n=takecommand()
            translator= Translator(from_lang="english",to_lang="spanish")
            translation = translator.translate(n)

            speak (translation)
        #translates to spanish
        elif 'translate to french' in query:
            
            speak("what do you want to translate")
            n=takecommand()
            translator= Translator(from_lang="english",to_lang="french")
            translation = translator.translate(n)
            speak (translation)
        #translates to french
        elif 'translate to hindi' in query:
            speak("what do you want to translate")
            n=takecommand()
            translator= Translator(from_lang="english",to_lang="hindi")
            translation = translator.translate(n)
            speak (translation)
        #translates to hindi
        elif 'translate to german' in query:

            speak("what do you want to translate")
            n=takecommand()
            translator= Translator(from_lang="english",to_lang="german")
            translation = translator.translate(n)
            speak (translation)
        #translates to german
        elif 'translate to latin' in query:
            speak("what do you want to translate")
            n=takecommand()
            translator= Translator(from_lang="english",to_lang="latin")
            translation = translator.translate(n)
            speak (translation)
        
        elif 'action movies' in query:
            m=[]
            j=0
            url=("https://www.imdb.com/search/title/?title_type=feature&genres=action&explore=genres")
            page=requests.get(url)
            soup=BeautifulSoup(page.content,'html.parser')
            movie=soup.find_all('h3',class_='lister-item-header')
            for i in movie:
                m.append(i.get_text().strip().replace('\n',"").replace('.',""))
                j+=1
                if(j==4):
                    break
            for i in m:
                speak(i[1:])
                sleep(1)
                
        elif 'comedy movies' in query:
            m=[]
            j=0
            url=("https://www.imdb.com/search/title/?title_type=feature&genres=comedy")
            page=requests.get(url)
            soup=BeautifulSoup(page.content,'html.parser')
            movie=soup.find_all('h3',class_='lister-item-header')
            for i in movie:
                m.append(i.get_text().strip().replace('\n',"").replace('.',""))
                j+=1
                if(j==4):
                    break
            for i in m:

                speak(i[1:])
                sleep(1)
        elif 'drama' in query:
            m=[]
            j=0
            url=("https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc")
            page=requests.get(url)
            soup=BeautifulSoup(page.content,'html.parser')
            movie=soup.find_all('h3',class_='lister-item-header')
            for i in movie:
                m.append(i.get_text().strip().replace('\n',"").replace('.',""))
                j+=1
                if(j==4):
                    break
            for i in m:

                speak(i[1:])
                sleep(1)
        elif 'fantasy' in query:
            m=[]
            j=0
            url=("https://www.imdb.com/search/title/?genres=fantasy&title_type=feature&explore=genres")
            page=requests.get(url)
            soup=BeautifulSoup(page.content,'html.parser')
            movie=soup.find_all('h3',class_='lister-item-header')
            for i in movie:
                m.append(i.get_text().strip().replace('\n',"").replace('.',""))
                j+=1
                if(j==4):
                    break
            for i in m:
    
                speak(i[1:])
                sleep(1)
        elif 'horror movies' in query:
            m=[]
            j=0
            url=("https://www.imdb.com/search/title/?title_type=feature&genres=horror")
            page=requests.get(url)
            soup=BeautifulSoup(page.content,'html.parser')
            movie=soup.find_all('h3',class_='lister-item-header')
            for i in movie:
                m.append(i.get_text().strip().replace('\n',"").replace('.',""))
                j+=1
                if(j==4):
                    break
            for i in m:
                
                speak(i[1:])  
                sleep(1) 
        elif 'romantic movies' in query or 'last option' in query:
            m=[]
            j=0
            url=("https://www.imdb.com/search/title/?title_type=feature&genres=romance")
            page=requests.get(url)
            soup=BeautifulSoup(page.content,'html.parser')
            movie=soup.find_all('h3',class_='lister-item-header')
            for i in movie:
                m.append(i.get_text().strip().replace('\n',"").replace('.',""))
                j+=1
                if(j==4):
                    break
            for i in m:
                speak(i[1:]) 
                sleep(1)    
        elif 'thriller movies' in query:
            m=[]
            j=0
            url=("https://www.imdb.com/search/title/?genres=thriller&groups=top_250&sort=user_rating,descc")
            page=requests.get(url)
            soup=BeautifulSoup(page.content,'html.parser')
            movie=soup.find_all('h3',class_='lister-item-header')
            for i in movie:
                m.append(i.get_text().strip().replace('\n',"").replace('.',""))
                j+=1
                if(j==4):
                    break
            for i in m:
                
                speak(i[1:])  
                sleep(1)
        elif 'romcom movies' in query:
            m=[]
            j=0
            url=("https://www.imdb.com/search/title/?genres=comedy,romance&explore=title_type,genres&title_type=movie")
            page=requests.get(url)
            soup=BeautifulSoup(page.content,'html.parser')
            movie=soup.find_all('h3',class_='lister-item-header')
            for i in movie:
                m.append(i.get_text().strip().replace('\n',"").replace('.',""))
                j+=1
                if(j==4):
                    break
            for i in m:
            
                speak(i[1:])    
                (1)
        elif 'scifi movies' in query:
            m=[]
            j=0
            url=("https://www.imdb.com/search/title/?genres=sci-fi&title_type=feature&explore=genres")
            page=requests.get(url)
            soup=BeautifulSoup(page.content,'html.parser')
            movie=soup.find_all('h3',class_='lister-item-header')
            for i in movie:
                m.append(i.get_text().strip().replace('\n',"").replace('.',""))
                j+=1
                if(j==4):
                    break
            for i in m:
        
                speak(i[1:])   
                sleep(1) 
        elif 'documentary' in query:
            m=[]
            j=0
            url=("https://www.imdb.com/search/title/?title_type=documentary&num_votes=10000,&languages=en&sort=user_rating,desc&explore=genres")
            page=requests.get(url)
            soup=BeautifulSoup(page.content,'html.parser')
            movie=soup.find_all('h3',class_='lister-item-header')
            for i in movie:
                m.append(i.get_text().strip().replace('\n',"").replace('.',""))
                j+=1
                if(j==4):
                    break
            for i in m:
                
                speak(i[1:])  
                sleep(1)    
             
        elif 'fiction movies' in query:
            m=[]
            j=0
            url=("https://www.imdb.com/search/title/?genres=sci-fi&languages=en&sort=user_rating,desc&title_type=feature&num_votes=10000,&explore=genres")
            page=requests.get(url)
            soup=BeautifulSoup(page.content,'html.parser')
            movie=soup.find_all('h3',class_='lister-item-header')
            for i in movie:
                m.append(i.get_text().strip().replace('\n',"").replace('.',""))
                j+=1
                if(j==4):
                    break
            for i in m:
                
                speak(i[1:])
                sleep(1)
        elif 'crime movies' in query:
            m=[]
            j=0
            url=("https://www.imdb.com/search/title/?genres=crime&title_type=feature&explore=genres")
            page=requests.get(url)
            soup=BeautifulSoup(page.content,'html.parser')
            movie=soup.find_all('h3',class_='lister-item-header')
            for i in movie:
                m.append(i.get_text().strip().replace('\n',"").replace('.',""))
                j+=1
                if(j==4):
                    break
            for i in m:
                
                speak(i[1:])
                sleep(1)
        elif 'survival movies' in query:
            m=[]
            j=0
            url=("https://www.imdb.com/list/ls033958690/")
            page=requests.get(url)
            soup=BeautifulSoup(page.content,'html.parser')
            movie=soup.find_all('h3',class_='lister-item-header')
            for i in movie:
                m.append(i.get_text().strip().replace('\n',"").replace('.',""))
                j+=1
                if(j==4):
                    break
            for i in m:
                
                speak(i[1:])
                sleep(1)
        elif 'zombie movies' in query:
            m=[]
            j=0
            url=("https://www.imdb.com/list/ls000058536/")
            page=requests.get(url)
            soup=BeautifulSoup(page.content,'html.parser')
            movie=soup.find_all('h3',class_='lister-item-header')
            for i in movie:
                m.append(i.get_text().strip().replace('\n',"").replace('.',""))
                j+=1
                if(j==4):
                    break
            for i in m:
                
                speak(i[1:])
                sleep(1)
                    
        elif 'superhero movies' in query:
            m=[]
            j=0
            url=("https://www.imdb.com/search/title/?at=0&count=100&keywords=superhero&num_votes=3000,&sort=user_rating&title_type=feature")
            page=requests.get(url)
            soup=BeautifulSoup(page.content,'html.parser')
            movie=soup.find_all('h3',class_='lister-item-header')
            for i in movie:
                m.append(i.get_text().strip().replace('\n',"").replace('.',""))
                j+=1
                if(j==4):
                    break
            for i in m:
                
                speak(i[1:])
                sleep(1)
        elif 'anime' in query:
            m=[]
            j=0
            url=("https://www.imdb.com/search/title/?at=0&genres=animation&keywords=anime&num_votes=1000,&sort=user_rating&title_type=tv_series")
            page=requests.get(url)
            soup=BeautifulSoup(page.content,'html.parser')
            movie=soup.find_all('h3',class_='lister-item-header')
            for i in movie:
                m.append(i.get_text().strip().replace('\n',"").replace('.',""))
                j+=1
                if(j==4):
                    break
            for i in m:
                print(i[1:])
                sleep(1)
        elif ' a movie' in query:
            speak("Jab we met")
        elif 'some movies' in query:
            speak("Jab we met, Iron man, Avengers, John wick, Tamasha")
        elif 'bollywood movie' in query:
            m=[]
            j=0
            url=("https://www.imdb.com/list/ls500849058/")
            page=requests.get(url)
            soup=BeautifulSoup(page.content,'html.parser')
            movie=soup.find_all('h3',class_='lister-item-header')
            for i in movie:
                m.append(i.get_text().replace('\n',"").replace('.',""))
                j+=1
                if(j==4):
                    break
            for i in m:
                speak(i[1:])
        
        elif 'hidden menu' in query:
            speak("opening")
            pyautogui.hotkey('winleft','x')
        elif 'task manager' in query:
            speak("opening")
            pyautogui.hotkey('ctrl','shift','esc')
        elif 'task view' in query:
            speak("opening")
            pyautogui.hotkey('winleft','tab')
        elif 'current window' in query:
            speak("closing")
            pyautogui.hotkey('alt','f4')
        elif 'last window' in query:
            pyautogui.hotkey('alt','tab')
        elif 'last tab' in query:
            pyautogui.hotkey('alt','tab')
        elif 'desktop' in query:
            pyautogui.hotkey('winleft','d')
        elif 'quick settings' in query:
            pyautogui.hotkey('winleft','a')
        elif 'file explorer' in query:
            pyautogui.hotkey('winleft','e')
        elif 'game bar' in query:
            pyautogui.hotkey('winleft','g')
        elif 'setting' in query:
            pyautogui.hotkey('winleft','i')
        elif 'calendar' in query:
            pyautogui.hotkey('winleft','n')
        elif 'send a mail' in query:
            email_sender="jaybhuptani10@gmail.com"
            email_password="woejzqgspqdcgfsg"
            email_rec="jaybhuptani1054@gmail.com"
            speak("What subject you want to give")
            subject=takecommand()
            speak("What body you would like to give")
            body=takecommand()
            em=EmailMessage()
            em['From']=email_sender
            em['To']=email_rec
            em['Subject']=subject
            em.set_content(body)
            ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                smtp.login(email_sender,email_password)
                smtp.sendmail(email_sender,email_rec,em.as_string())
            speak("done")

        elif 'open google maps' in query:
            speak(" opening google maps,sir")
            webbrowser.open("maps.google.com")
        elif 'open microsoft edge' in query:
            speak("opening microsoft edge application,sir")
            loc ='""C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe""'
            os.startfile(loc)
        elif 'open powerpoint' in query:
            speak("opening microsoft powerpoint,sir")
            loc = '"C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"'
            os.startfile(loc)
        elif 'open chrome' in query:
            speak("opeming google chrome,sir")
            loc='"C:\\Users\\jay bhuptani\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"'
            os.startfile(loc)
        elif 'open microsoft word' in query:
            speak("opening Microsoft word,sir")
            loc='"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"'
            os.startfile(loc)
        elif 'open excel' in query:
            speak("opening Microsoft excel,sir")
            loc='""C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE""'
            os.startfile(loc)
        elif 'close chrome' in query:
            speak("closing chrome,sir")
            os.system("taskkill /f /im chrome.exe")
        elif 'close microsoft edge' in query:
            speak("closing microsoft edge, sir")
            os.system("taskkill /f /im msedge.exe")
        elif 'close microsoft word' in query:
            speak("closing Microsoft word,sir")
            os.system("taskkill /f /im word.exe")
        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            os.system("shutdown /s /t 1")
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
        elif "restart" in query:
            speak("restarting")
            subprocess.call(["shutdown", "/r"])
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
        elif 'chat gpt' in query:
            query=query.replace("chat gpt","")
            openai.api_key = "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"#os.getenv("")
            response = openai.Completion.create(
            model="text-davinci-003",
            prompt=query,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
                        )
            content=response.choices[0].text.split('.')
            for i in content:
                speak(i)
                a=takecommand()
                if 'exit' in query:
                    exit()
                sleep(5)

        elif 'do you know' in query or 'who is' in query or 'what is' in query or 'how' in query :
            query=query.replace("do you know","")
            query=query.replace("who is","")
            try:
                results=wikipedia.summary(query,sentences=1)
                
                speak(results)
            except:
                print(f"I don't know {query}")
                speak(f"I don't know {query}")

        else:              
            def similar(a,b):
                return SequenceMatcher(None, a, b).ratio()
            maxs=0
            def chatbot(q):
                f=open('rossquestions.csv','r')
                maxs=0
                data=csv.reader(f)
                x=0
                d=[]
                for i in data:
                    d.append(i)
                    for j in range(0,len(i)):
                        qu=i[j]
                    
                        s=similar(qu,q)
                        if s>0.7:
                            if s>maxs:
                                maxs=s
                                x=j        
                d.pop(0)
                l=[]
                if x!=0:
                    for i in d:
                        #print(i[x])
                        l.append(i[x])    
                    r=random.randint(0,4)
                    speak(l[r])
            chatbot(query)

    '''else:
                openai.api_key = "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"#os.getenv("")
                response = openai.Completion.create(
                model="text-davinci-003",
                prompt=query,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
                        )
                content=response.choices[0].text.split('.')
                for i in content:
                    speak(i)
                    a=takecommand()
                    if 'exit' in query:
                        exit()
                    sleep(5)'''





        

