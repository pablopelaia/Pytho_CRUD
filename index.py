from tkinter import *
from tkinter import messagebox
import sqlite3

raiz= Tk()

# Creo barra menu-----------------------------------------------------------------------
barraMenu= Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)

dbMenu=Menu(barraMenu, tearoff=0)
dbMenu.add_command(label="Conectar")
dbMenu.add_command(label="Salir")

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos")

menuCRUD=Menu(barraMenu, tearoff=0)
menuCRUD.add_command(label="Crear")
menuCRUD.add_command(label="Leer")
menuCRUD.add_command(label="Actualizar")
menuCRUD.add_command(label="Borrar")

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=dbMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", men=menuCRUD)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

# Comienzo de campos-----------------------------------------------------------------------

miFrame= Frame(raiz)
miFrame.pack()

cuadroID= Entry(miFrame)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre= Entry(miFrame)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadroPass= Entry(miFrame)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(fg="red", justify="right", show="?")

cuadroApellido= Entry(miFrame)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroAdress= Entry(miFrame)
cuadroAdress.grid(row=4, column=1, padx=10, pady=10)

comentarios= Text(miFrame, width=16, height=5)
comentarios.grid(row=5, column=1, padx=10, pady=10)

scrVertical=Scrollbar(miFrame, command=comentarios.yview)
scrVertical.grid(row=5, column=2, sticky="nsew")

comentarios.config(yscrollcommand=scrVertical.set)

raiz.mainloop()
