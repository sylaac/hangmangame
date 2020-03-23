from tkinter import *

word = input("give a word ")
letters = []
try :
    for i in word:
        letters += [i]

except:
    print("give a proper word")
g = 0
e = 0
while g < len(word):
    at_least_one_good = 0
    position = 1
    the_try = input("choose a letter")
    for i in letters :
        if the_try == i :
            print("there is an ",the_try,"in position",position)
            g += 1
            at_least_one_good = 1
        position += 1
    if at_least_one_good == 0:
        e += 1
    window = Tk()

    canvas = Canvas(window, width=800, height = 600)
    file = "C://Users//titouan rit//Favorites//Links//pendu"+str(e)+".png"
    filename = PhotoImage(file = file)
    image = canvas.create_image(0,0 , anchor=NW, image=filename)
    canvas.pack()

window.mainloop()