import customtkinter
from tkinter.messagebox import showinfo
import os
import tkinter as tk
from mtranslate import translate
import gtts
import pygame

language={
   "Arabic" :"ar",
    "bulgarian": "bg",
   "croatian":"hr",
   "czech":"cs",
    "danish":"da",
   "german":"de",
   "greek" :"el",
    "english":"en",
   " Estonian" :"et",
   "spanish":"es",
   "finnish": "fi",
    "french": "fr",
   "irish": "ga",
   "hindi":"hi",
   "bulgarian": "hu",
   "Hebrew" :"iw",
   "Italian": "it",
   "japanese": "ja",
   "korean": "ko",
   " latvian" :"lv",
    "Lithuanian" :"lt",
   "Dutch" :"nl",
    "norwegian": "no",
   "polish":"pl",
    "portuguese":"pt",
   "swedish": "sv",
    "roman" :"ro",
  "russian": "ru",
    "srt":"sr",
    "slovak": "sk",
    "slovenian": "sl",
  "taiwanese" :"th",
    "turkish":"tr",
   " Ukrainian" :"uk",
   " Chinese (simplified)": "zh-CN",
    "Chinese (traditional)": "zh-TW"
}
lan=list(language.keys())
root=customtkinter.CTk()
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")
root.title("Translator")
root.geometry("1000x700")

def paste():
    text=root.clipboard_get()
    fromlabel.delete("1.0","end")
    fromlabel.insert("1.0",text)

def copy():
    root.clipboard_clear()
    text = Tolabel.get("1.0", "end-1c")
    root.clipboard_append(text)

def translat():
    try:
        Tolabel.delete("1.0","end")
        translation = translate(fromlabel.get("1.0", "end-1c"),language[tselect.get()] )  
        Tolabel.insert("1.0",translation)
    except:
        showinfo("Erorr","Please Check Your Connection")
    
def fspek():
    try: 
        tts = gtts.gTTS(fromlabel.get("1.0", "end-1c"), lang=language[fselect.get()])
        tts.save("data.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("data.mp3")
        pygame.mixer.music.play()
    except PermissionError:
        pygame.mixer.music.unload()
        os.remove("data.mp3")
        fspek()
    
def tspek():
    try:
        tts = gtts.gTTS(Tolabel.get("1.0", "end-1c"), lang=language[tselect.get()])
        tts.save("data.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("data.mp3")
        pygame.mixer.music.play()
        
    except PermissionError:
        pygame.mixer.music.unload()
        os.remove("data.mp3")
        tspek()


def clear():
    Tolabel.delete("1.0","end")
    fromlabel.delete("1.0","end")

fselect=customtkinter.CTkOptionMenu(root,fg_color="#ffffff",text_color="black",values=lan,)
fselect.place(x=240,y=20)

f=customtkinter.CTkLabel(root,text="From:",font=("Roborto",20),text_color="#ffffff")
f.place(x=150,y=20)
fromlabel=customtkinter.CTkTextbox(root,width=400,height=250,font=("arial",14))
fromlabel.place(x=50,y=70)
pasteb=customtkinter.CTkButton(root,text="Paste",fg_color="#ffffff",text_color="black",command=paste)
pasteb.place(x=180,y=370)
fspeek=customtkinter.CTkButton(root,text="Speek",text_color="black",fg_color="#ffffff",width=40,height=20,command=fspek)
fspeek.place(y=320,x=50)

tselect=customtkinter.CTkOptionMenu(root,fg_color="#ffffff",text_color="black",values=lan)
tselect.place(x=760,y=20)
t=customtkinter.CTkLabel(root,text="To:",font=("Roborto",20),text_color="#ffffff")
t.place(x=670,y=20)
Tolabel=customtkinter.CTkTextbox(root,width=400,height=250,font=("arial",14))
Tolabel.place(x=550,y=70)
copyb=customtkinter.CTkButton(root,text="Copy",fg_color="#ffffff",text_color="black",command=copy)
copyb.place(x=680,y=370)
tspeek=customtkinter.CTkButton(root,text="Speek",text_color="black",fg_color="#ffffff",width=40,height=20,command=tspek)
tspeek.place(y=320,x=900)


clearb=customtkinter.CTkButton(root,text="Clear",text_color="black",fg_color="#ffffff",command=clear)
clearb.place(y=370,x=430)

trans=customtkinter.CTkButton(root,text="Translate",text_color="black",fg_color="#ffffff",command=translat)
trans.place(y=420,x=430)

root.mainloop()




