from tkinter import *
from tkinter import messagebox
import random

class App():

  a = random.randint(2,12)
  b = random.randint(2,12)
  root = Tk()
  root.title("Победи арифметика")
  root.geometry("800x500")

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

    # c - counter
    self.c = Label(self.root, text=r"Бой {self.counter} из 5")
    self.c.grid(column=0,row=0)
    # t - task
    self.t = Label(self.root, text=r"{self.a} * {self.b} = ")
    self.t.grid(column=1,row=1)
    # e - entry
    self.e = Entry(self.root, width = 10)
    self.e.grid(column=1,row=2)
    self.e.focus()
    # bt - button
    self.bt = Button(self.root, text = "Ответить", command = self.clicked)
    self.bt.grid(column=1,row=3)
    # p - phrase
    self.p = Label(self.root, text = self.phrase)
    self.p.grid(column=2,row=3)

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
    self.c.configure(text=r"Бой {self.counter} из 5")
    self.t.configure(text=r"{self.a} * {self.b} = ")
    self.e.focus()


  def Ending(self):
    messagebox.showwarning("Конец битвы!", "Правильных ответов : {},\n Неправильных ответов : {}".format(self.score,5-self.score))
    self.score = 0
    self.counter = 1
    self.phrase = "Новый раунд!"

if __name__ == "__main__":
  App()
