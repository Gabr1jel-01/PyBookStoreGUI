import tkinter as tk


counter = 1
def count_handler():
    global counter
    message = lbl_header_welcome_var.get()
    lbl_display_message_var.set(f'Gumb kliknut {counter} puta.')
    counter += 1


def reset_counter_handler():
    global counter
    counter = 1
    lbl_display_message_var.set(f'Brojac resetiran')


def copy_to_clipboard():
    main_window.clipboard_append(lbl_display_message_var.get())





main_window = tk.Tk()
main_window.title('Algebra - Book Store')
main_window.geometry('600x400')


lbl_header_welcome_var = tk.StringVar()
lbl_header_welcome_var.set('Dobro dosli u nasu prvu Tkinter aplikaciju')
lbl_header_welcome = tk.Label(main_window,
                              font=('Segoe UI', 20),
                              textvariable=lbl_header_welcome_var)
lbl_header_welcome.pack()

lbl_display_message_var = tk.StringVar()
lbl_display_message = tk.Label(main_window,
                              font=('Segoe UI', 16),
                              textvariable=lbl_display_message_var)
lbl_display_message.pack()

btn_count = tk.Button(main_window,
                     text='Pokreni brojac',
                     command=count_handler)
btn_count.pack(padx=30, pady=30)

btn_reset = tk.Button(main_window,
                      text='Resetiraj brojac',
                      command=reset_counter_handler)
btn_reset.pack(padx=10, pady=10)

btn_copy = tk.Button(main_window,
                      text='Kopiraj brojac',
                      command=copy_to_clipboard)
btn_copy.pack(padx=10, pady=10)


main_window.mainloop()