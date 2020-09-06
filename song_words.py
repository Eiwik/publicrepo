# -- coding: utf-8 --
import xml.etree.ElementTree
from bs4 import BeautifulSoup
import urllib.request
from re import findall
from tkinter import *
from os import startfile
from tkinter import messagebox

def isLink(link):
    if findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', link):
        return True
    return False
def remove_tags(text):
    try:
        return ''.join(xml.etree.ElementTree.fromstring(text).itertext()).replace('*', '')
    except SyntaxError:
        messagebox.showerror("Error", "Not a valid link")

class Song:
    def __init__(self, link, lang):
        self.link = link
        self.lang = lang
        self.name = remove_tags(str(BeautifulSoup(urllib.request.urlopen(self.link), 'lxml').find('h2')))
    
    def downloadWords(self):
        words = BeautifulSoup(urllib.request.urlopen(self.link), 'lxml').findAll('div', class_=self.lang)
        for i in range(0, len(words)):
            words[i] = remove_tags((str(words[i])))
        f = open(f'{self.name + " " + self.lang + ".txt"}', 'w')
        f.write(f'{self.name}\n\n- - - - -\n')
        for line in words:
            f.write(f'{line}\n')
        f.close()

    def about(self):
        return f"Song name: {self.name}\nLanguage: {self.lang}\nLink: {self.link}"
#comments
class Block:
    def __init__(self, master):
        self.frame = LabelFrame()
        self.frame.pack(side=LEFT, padx=5, pady=5)
        self.b = Button(self.frame, text = 'Download')
        self.e = Entry(self.frame, width=40)
        self.l = Label(self.frame)
        self.lb = Listbox(master, selectmode = EXTENDED)
        self.e.pack()
        self.b.pack()
        self.l.pack()
        self.lb.pack()
        for elem in ['original', 'translate']:
            self.lb.insert(0, elem)

    def setFunc(self, func):
        self.b['command'] = eval(f'self.{func}')

    def downloadLyrics(self):
        link = self.e.get()
        lang = self.lb.get(ACTIVE)
        if not isLink(link):
            messagebox.showerror("Error", f"{link if isLink(link) else 'Value'} is not a link")
        else:
            Song(link, lang).downloadWords()
            self.frame['text'] = Song(link, lang).name
            self.l['text'] = Song(link, lang).about()

root = Tk()
root.resizable(False, False)
root.title("Song Parser")
main_window= Block(root)
main_window.setFunc('downloadLyrics')
startfile('https://www.amalgama-lab.com/')
root.mainloop()
    