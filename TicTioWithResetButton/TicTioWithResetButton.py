from tkinter import messagebox, Label
from tkinter import *

turn = 1  # player1 or player 2

def win(player):
    messagebox.showinfo("Result", "Player " + player + " is winner")
    wind.destroy()



flag = 1  # to check if 9 position are filled


# check if there is a winner player


def reset():
    global turn, flag
    flag = 1
    turn = 1
    btn1["text"]=""
    btn2["text"]=""
    btn3["text"]=""
    btn4["text"]=""
    btn5["text"]=""
    btn6["text"]=""
    btn7["text"]=""
    btn8["text"]=""
    btn9["text"]=""


def check():
    global flag
    b1 = btn1["text"];  # get text in the button
    b2 = btn2["text"];
    b3 = btn3["text"];
    b4 = btn4["text"];
    b5 = btn5["text"];
    b6 = btn6["text"];
    b7 = btn7["text"];
    b8 = btn8["text"];
    b9 = btn9["text"];
    flag = flag + 1;
    if b1 == b2 and b1 == b3 and b1 == "O" or b1 == b2 and b1 == b3 and b1 == "X":
        win(btn1["text"])
    if b4 == b5 and b4 == b6 and b4 == "O" or b4 == b5 and b4 == b6 and b4 == "X":
        win(btn4["text"]);
    if b7 == b8 and b7 == b9 and b7 == "O" or b7 == b8 and b7 == b9 and b7 == "X":
        win(btn7["text"]);
    if b1 == b4 and b1 == b7 and b1 == "O" or b1 == b4 and b1 == b7 and b1 == "X":
        win(btn1["text"]);
    if b2 == b5 and b2 == b8 and b2 == "O" or b2 == b5 and b2 == b8 and b2 == "X":
        win(btn2["text"]);
    if b3 == b6 and b3 == b9 and b3 == "O" or b3 == b6 and b3 == b9 and b3 == "X":
        win(btn3["text"]);
    if b1 == b5 and b1 == b9 and b1 == "O" or b1 == b5 and b1 == b9 and b1 == "X":
        win(btn1["text"]);
    if b7 == b5 and b7 == b3 and b7 == "O" or b7 == b5 and b7 == b3 and b7 == "X":
        win(btn7["text"]);
    if flag == 10:
        messagebox.showinfo("Tie", "Match Tied!!!  Try again :)")
        wind.destroy()


def clicked1():
    global turn
    if btn1["text"] == "":
        if turn == 1:
            turn = 2  # next turn
            btn1["text"] = "X"
        elif turn == 2:
            turn = 1  # next turn
            btn1["text"] = "O"
        check()


def clicked2():
    global turn
    if btn2["text"] == "":
        if turn == 1:
            turn = 2  # next turn
            btn2["text"] = "X"
        elif turn == 2:
            turn = 1  # next turn
            btn2["text"] = "O"
        check()


def clicked3():
    global turn
    if btn3["text"] == "":
        if turn == 1:
            turn = 2  # next turn
            btn3["text"] = "X"
        elif turn == 2:
            turn = 1  # next turn
            btn3["text"] = "O"
        check()


def clicked4():
    global turn
    if btn4["text"] == "":
        if turn == 1:
            turn = 2  # next turn
            btn4["text"] = "X"
        elif turn == 2:
            turn = 1  # next turn
            btn4["text"] = "O"
        check()

def clicked5():
    global turn
    if btn5["text"] == "":
        if turn == 1:
            turn = 2  # next turn
            btn5["text"] = "X"
        elif turn == 2:
            turn = 1  # next turn
            btn5["text"] = "O"
        check()

def clicked6():
    global turn
    if btn6["text"] == "":
        if turn == 1:
            turn = 2  # next turn
            btn6["text"] = "X"
        elif turn == 2:
            turn = 1  # next turn
            btn6["text"] = "O"
        check()

def clicked7():
    global turn
    if btn7["text"] == "":
        if turn == 1:
            turn = 2  # next turn
            btn7["text"] = "X"
        elif turn == 2:
            turn = 1  # next turn
            btn7["text"] = "O"
        check()

def clicked8():
    global turn
    if btn8["text"] == "":
        if turn == 1:
            turn = 2  # next turn
            btn8["text"] = "X"
        elif turn == 2:
            turn = 1  # next turn
            btn8["text"] = "O"
        check()


def clicked9():
    global turn
    if btn9["text"] == "":
        if turn == 1:
            turn = 2  # next turn
            btn9["text"] = "X"
        elif turn == 2:
            turn = 1  # next turn
            btn9["text"] = "O"
        check()



wind = Tk()
wind.title("Tic Tac Toe")
wind.geometry("500x500")

l1 = Label(wind, text="Player 1", font=("Arial", 15))
l1.grid(row=0, column=0)

l2 = Label(wind, text="Player 2", font=("Arial", 15))
l2.grid(row=1, column=0)

btn1 = Button(wind, text="", bg="#E7E5E5", fg="black", width=3, height=1, font="Arial", command=clicked1)
btn1.grid(row=0, column=1)

btn2 = Button(wind, text="", bg="#E7E5E5", fg="black", width=3, height=1, font="Arial", command=clicked2)
btn2.grid(row=0, column=2)

btn3 = Button(wind, text="", bg="#E7E5E5", fg="black", width=3, height=1, font="Arial", command=clicked3)
btn3.grid(row=0, column=3)

btn4 = Button(wind, text="", bg="#E7E5E5", fg="black", width=3, height=1, font="Arial", command=clicked4)
btn4.grid(row=1, column=1)

btn5 = Button(wind, text="", bg="#E7E5E5", fg="black", width=3, height=1, font="Arial", command=clicked5)
btn5.grid(row=1, column=2)

btn6 = Button(wind, text="", bg="#E7E5E5", fg="black", width=3, height=1, font="Arial", command=clicked6)
btn6.grid(row=1, column=3)

btn7 = Button(wind, text="", bg="#E7E5E5", fg="black", width=3, height=1, font="Arial", command=clicked7)
btn7.grid(row=2, column=1)

btn8 = Button(wind, text="", bg="#E7E5E5", fg="black", width=3, height=1, font="Arial", command=clicked8)
btn8.grid(row=2, column=2)

btn9 = Button(wind, text="", bg="#E7E5E5", fg="black", width=3, height=1, font="Arial", command=clicked9)
btn9.grid(row=2, column=3)


reset = Button(wind, text="RESET",bg="white", fg="Black",width=9,height=1,font=('Helvetica','20'),command=reset)
reset.grid(column=1, row=5,columnspan=3,padx=10,pady=10)


wind.mainloop()
