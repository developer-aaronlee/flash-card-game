from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    file = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_file = pandas.read_csv("data/french_words.csv")
    dict_file = original_file.to_dict("records")
else:
    dict_file = file.to_dict("records")


def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(dict_file)
    canvas.itemconfig(card_title, fill="black", text="French")
    canvas.itemconfig(card_word, fill="black", text=current_card["French"])
    canvas.itemconfig(canvas_img, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, fill="white", text="English")
    canvas.itemconfig(card_word, fill="white", text=current_card["English"])
    canvas.itemconfig(canvas_img, image=card_back)


def new_card():
    dict_file.remove(current_card)
    next_card()
    data = pandas.DataFrame(dict_file)
    data.to_csv("data/words_to_learn.csv", index=False)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526)
canvas_img = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", fill="black", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
check_button = Button(image=right_img, highlightthickness=0, command=new_card)
check_button.grid(column=0, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
cross_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
cross_button.grid(column=1, row=1)


flip_timer = window.after(3000, func=flip_card)
next_card()



window.mainloop()