"""Задача 4. Чат"""

from tkinter import Tk, Button, Text, END,  Entry


window = Tk()
window.title('Чат')
window.geometry('1024x768')

FLAG = 0
SAVE_NAME = ''


def chek_chat():
    """chek_chat
    """
    with open("Module23/04_chat/chat.txt",
              "r", encoding="utf8") as f:
        stuff = f.read()
        text_chat.delete("1.0", END)
        text_chat.insert("1.0", stuff)


def send_message():
    """send_message
    """
    text_help = Button(
        window,
        text='Введите имя и нажмите кнопку еще раз',
        width=45,
        height=20,
        state="disabled"
    )
    text_help.place(
        relx=0.5,
        rely=0.5,
        anchor="s",
        width=300,
        height=40
    )
    global FLAG, SAVE_NAME
    entry_message.config(state="normal")
    entry_message.insert("1", '')
    save_message = entry_message.get()
    entry_message.delete("0", END)
    if save_message and FLAG == 0:
        FLAG += 1
        entry_message.insert("1", '')
        SAVE_NAME = save_message + ': '
        save_message = ''
        text_help.config(text='Введите текст и нажмите кнопку еще раз ')
    if FLAG == 1 and save_message:
        save_name_message = SAVE_NAME + save_message
        with open("Module23/04_chat/chat.txt",
                  "a", encoding="utf8") as f:
            f.write(f'{save_name_message}\n')
            entry_message.config(state="disabled")
            FLAG = 0
            SAVE_NAME = ''
            save_name_message = ''


btn_view_the_chat = Button(
    window, text='1. Посмотреть текущий текст чата.',
    command=chek_chat
)
btn_view_the_chat.place(
    relx=0.5,
    rely=0.8,
    anchor="s",
    width=300,
    height=40
)
btn_send_message = Button(
    window,
    text='2. Ввести имя и отправить сообщение.',
    command=send_message
)
btn_send_message.place(
    relx=0.5,
    rely=0.9,
    anchor="s",
    width=300,
    height=40
)
text_chat = Text(
    window,
    width=45,
    height=20,
)

text_chat.pack(
    pady=20,
)
entry_message = Entry(
    width=50,
    state="disabled",
)
entry_message.place(
    relx=0.5,
    rely=0.6,
    anchor="s",
    width=300,
    height=30
)

window.mainloop()
