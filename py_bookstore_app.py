import tkinter as tk



main_window = tk.Tk()
main_window.title('Algebra - Book Store')
main_window.geometry('600x400')


lbl_publisher_name = tk.Label(main_window, text='Naziv izdavaca', font=('Segoe UI', 14))
lbl_publisher_name.grid(column=0, row=0, padx=20, pady=20)

ent_publisher_name_var = tk.StringVar()
ent_publisher_name = tk.Entry(main_window, textvariable=ent_publisher_name_var)
ent_publisher_name.grid(column=1, row=0, columnspan=2)




lbl_author_name = tk.Label(main_window, text='Ime autora', font=('Segoe UI', 14))
lbl_author_name.grid(column=0, row=1, padx=20, pady=20)

ent_author_name_var = tk.StringVar()
ent_author_name = tk.Entry(main_window, textvariable=ent_author_name_var)
ent_author_name.grid(column=1, row=1, columnspan=2)


lbl_author_last_name = tk.Label(main_window, text='Prezime autora', font=('Segoe UI', 14))
lbl_author_last_name.grid(column=0, row=2, padx=20, pady=20)

ent_author_last_name_var = tk.StringVar()
ent_author_last_name = tk.Entry(main_window, textvariable=ent_author_last_name_var)
ent_author_last_name.grid(column=1, row=2, columnspan=2)

lbl_book_title = tk.Label(main_window, text='Naziv knjige', font=('Segoe UI', 14))
lbl_book_title.grid(column=0, row=3, columnspan=2)




btn_save = tk.Button(main_window,
                     text='Snimi')
btn_save.grid(column=1, row=4, pady=20, sticky=tk.E)


main_window.mainloop()
