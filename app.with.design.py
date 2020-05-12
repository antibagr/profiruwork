from tkinter import *
from tkinter import messagebox
import tkinter.font
import random

class App():

  a = random.randint(2,12)
  b = random.randint(2,12)
  root = Tk()
  root.title("Победи арифметика")
  root.geometry("400x300")
  

  good = ( "И как тебе это удается?","Ты же не подсмативаешь?","В яблочко!",
  " Мастерский ответ" , "Не останавливайся!", "Ладно, я задам что-нибудь посложнее!",
  "Очень неплохо", "Уау, превосходно!", "И э-э-это правильный ответ!", "Я недооценивал твою мощь!")

  bad = ("В следующий раз ты ответишь правильно" , " У всех бывают черные полосы",
  "Не переживай", "Ты был так близко!", "Упс, кажется, мимо", "Я знаю, ты хотел выбрать другой ответ",
  "Ошибки делают нас мудрее", "Капля концентрации и щепотка тишины", "Ай!", "Мы учимся на ошибках, ведь так?")

  phrase = "Поехали!"

  def __init__(self):
    self.counter = 1
    self.score = 0
    
    self.root.columnconfigure(0, weight=1)

    # c - counter
    self.c = Label(self.root, text="Бой {} из 5".format(self.counter))
    self.c.grid(column=0,row=0)
    self.c.config(font=("Calibri", 25))
    # t - task
    self.t = Label(self.root, text="{} * {}".format(self.a,self.b))
    self.t.grid(column=0,row=1)
    self.t.config(font=("Calibri", 35))
    
    # e - entry
    FontOfEntry = tkinter.font.Font(family="Calibri",size=35)
    self.e = Entry(self.root, font = FontOfEntry, width = 10)
    self.e.grid(column=0,row=2)
    self.e.focus()
    # bt - button
    self.bt = Button(self.root, text = "Ответить", command = self.clicked)
    self.bt.grid(column=0,row=3)
    self.bt.config(font=("Calibri", 25),bg="#ffd4e4",bd=3,highlightbackground="#ff0a65",fg="#060633")
    # p - phrase
    self.p = Label(self.root, text = self.phrase)
    self.p.grid(column=0,row=4)
    self.p.config(font=("Calibri", 12))
    self.root.mainloop()

  def clicked(self):
  
    a = self.e.get()
    if a.isdigit() and a != "":
      self.counter += 1
      if self.isRight(int(a)):
        self.Right()
      else :
       self.Wrong()

      if self.counter == 6:
       self.Ending()

      self.Refresh()


  def isRight(self,answer):
    return self.a*self.b == answer

  def Right(self):
    self.phrase = self.good[random.randint(0,9)]
    self.score += 1

  def Wrong(self):
    self.phrase = self.bad[random.randint(0,9)]

  def Refresh(self):
    self.p.configure(text = self.phrase)
    self.e.delete(0, 'end')
    self.a = random.randint(2,12)
    self.b = random.randint(2,12)
    self.c.configure(text="Бой {} из 5".format(self.counter))
    self.t.configure(text="{} * {}".format(self.a,self.b))
    self.e.focus()


  def Ending(self):
  
    endOfGame = "Правильных ответов : {},\nНеправильных ответов : {}".format(self.score,5-self.score)
    if self.score == 5:
        endOfGame = "Мастер!\n" + endOfGame
    
    messagebox.showwarning("Конец битвы!", endOfGame)
    self.score = 0
    self.counter = 1
    self.phrase = "Новый раунд!"

if __name__ == "__main__":
  App()
