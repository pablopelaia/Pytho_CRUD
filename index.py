from tkinter import *
from tkinter import messagebox
import sqlite3

raiz= Tk()

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

raiz.mainloop()
