power = False
from tkinter import *
import random
q1 = random.randint(1,10)
q2 = random.randint(1,10)
q3 = random.randint(1,5)
real_answer = q1*q2-q3 

root = Tk()
root.minsize(600,300)
Enter = Entry()
root.title("The Math Game")
title = Label(root, text = "The Math Game")
question = Label(root,text = "do you want to play( yes or  No)")

def Change():
    if Enter.get() == "yes":
        real_question = Label(root,text = f"what is {q1}*{q2}-{q3}")
        real_question.place(x=50,y=80)
        Enter2 = Entry()
        Enter2.place(x=250,y=80)
        def Change2():
            if int(Enter2.get()) == real_answer:
                real_question.config(text="Correct")
            else:
                real_question.config(text= f"The Real answer is {real_answer}")
        Button2 = Button(root,text= "Enter",command=Change2)
        Button2.place(x=400,y=80)

Enter_button = Button(root,text="Enter",command=Change)
title.place(x=50,y=20)
question.place(x=50,y=50)
Enter.place(x=250,y=50)
Enter_button.place(x=400,y=50)
    

root.mainloop()
