# Chatbot using Tkinter for simple GUI
from tkinter import *

def send():
    user_input = e.get().lower()
    send_text = "\nYou: " + user_input
    txt.insert(END, send_text)
    e.delete(0, END)
    if user_input == "hello":
        txt.insert(END, "\nBot: Hi\n")
    elif user_input in ["hi", "hii", "hiiii"]:
        txt.insert(END, "\nBot: Hello\n")
    elif user_input == "how are you":
        txt.insert(END, "\nBot: I'm fine! How about you?\n")
    elif user_input in ["fine", "i am good", "i am doing good"]:
        txt.insert(END, "\nBot: Great! How can I help you?\n")
    else:
        txt.insert(END, "\nBot: Sorry, I didn't understand that.\n")

# Driver Code
root = Tk()
root.title("Chatbot")

txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100)
e.grid(row=1, column=0)

send_button = Button(root, text="Send", command=send)
send_button.grid(row=1, column=1)

root.mainloop()
