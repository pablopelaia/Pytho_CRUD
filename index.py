from tkinter import *
from tkinter import messagebox
import sqlite3

# Funciones----------------------------------------------------------------------------

def conexionBBDD():

    cnx= sqlite3.connect("Usuario")

    miCursor= cnx.cursor()

    try:

        miCursor.execute('''CREATE TABLE DATO_USUARIOS (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_USUARIO VARCHAR(50),
                CONTRASENA VARCHAR(50),
                APELLIDO VARCHAR(10),
                DIRECCION VARCHAR(50),
                COMENTARIOS VARCHAR(100) 
            )
            ''')
        
        messagebox.showinfo("BBDD", "Base de datos creada")
    
    except:
        
        messagebox.showwarning("¡Atención!", "La base de datos ya existe")
 



raiz= Tk()

# Creo barra menu-----------------------------------------------------------------------

barraMenu= Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)

dbMenu=Menu(barraMenu, tearoff=0)
dbMenu.add_command(label="Conectar", command=conexionBBDD)
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

# Etiquetas-----------------------------------------------------------------------

idLabel= Label(miFrame, text="ID:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel= Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidoLabel= Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

passLabel= Label(miFrame, text="Contraseña:")
passLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

adressLabel= Label(miFrame, text="Dirección:")
adressLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentariosLabel= Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

# Botones-----------------------------------------------------------------------

botonera= Frame(raiz)
botonera.pack()

btnCrear= Button(botonera, text="Crear")
btnCrear.grid(row=0, column=0, sticky="e", padx=10, pady=10)

btnLeer= Button(botonera, text="Leer")
btnLeer.grid(row=0, column=1, sticky="e", padx=10, pady=10)

btnActualizar= Button(botonera, text="Actualizar")
btnActualizar.grid(row=0, column=2, sticky="e", padx=10, pady=10)

btnBorrar= Button(botonera, text="Borrar")
btnBorrar.grid(row=0, column=3, sticky="e", padx=10, pady=10)


raiz.mainloop()
