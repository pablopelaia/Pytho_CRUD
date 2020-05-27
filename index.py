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
                APELLIDO VARCHAR(10),
                CONTRASENA VARCHAR(50),
                DIRECCION VARCHAR(50),
                COMENTARIOS VARCHAR(100) 
            )
            ''')
        
        messagebox.showinfo("BBDD", "Base de datos creada")
    
    except:
        
        messagebox.showwarning("¡Atención!", "La base de datos ya existe")
 
def salirApp():

    respuesta= messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")

    if respuesta=="yes":
        raiz.destroy()

def borraCampos():
    
    miID.set("")
    miNombre.set("")
    miApellido.set("")
    miPass.set("")
    miDireccion.set("")
    comentarios.delete(1.0,END)

def insertaDato():
    
    cnx= sqlite3.connect("Usuario")    
    miCursor= cnx.cursor()

    datosFormulario= [miNombre.get(), miApellido.get(), miPass.get(), miDireccion.get(), comentarios.get('1.0', END)]
        
    for dato in datosFormulario:
        print(dato)

    miCursor.execute("INSERT INTO DATO_USUARIOS VALUES (NULL, ?, ?, ?, ?, ?)", datosFormulario)        
        
    cnx.commit()
    messagebox.showinfo("BBDD", "Registro insertado con éxito")
    borraCampos()

def leeDatos():

    if miID.get()=="": 
        messagebox.showwarning("Dato requerido", "debe ingresar ID")
        return 0

    cnx= sqlite3.connect("Usuario")    
    miCursor= cnx.cursor()

    miCursor.execute("SELECT * FROM DATO_USUARIOS WHERE ID=" + miID.get())

    usuarioBuscado= miCursor.fetchall()
        
    for usuario in usuarioBuscado:

        print(usuario)
        
        miID.set(usuario[0])
        miNombre.set(usuario[1])
        miApellido.set(usuario[2])
        miPass.set(usuario[3])
        miDireccion.set(usuario[4])
        comentarios.insert(1.0, usuario[5])
        
    cnx.commit()

    







def refrescaDatos():
    pass

def eliminaDatos():
    pass

def ayuda():
    pass

raiz= Tk()

# Creo barra menu-----------------------------------------------------------------------

barraMenu= Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)

dbMenu=Menu(barraMenu, tearoff=0)
dbMenu.add_command(label="Conectar", command=conexionBBDD)
dbMenu.add_command(label="Salir", command=salirApp)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=borraCampos)

menuCRUD=Menu(barraMenu, tearoff=0)
menuCRUD.add_command(label="Crear", command=insertaDato)
menuCRUD.add_command(label="Leer", command=leeDatos)
menuCRUD.add_command(label="Actualizar", command=refrescaDatos)
menuCRUD.add_command(label="Borrar", command=eliminaDatos)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Acerca de...", command=ayuda)

barraMenu.add_cascade(label="BBDD", menu=dbMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", men=menuCRUD)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

# Comienzo de campos-----------------------------------------------------------------------

miFrame= Frame(raiz)
miFrame.pack()

miID= StringVar()
miNombre= StringVar()
miApellido= StringVar()
miPass= StringVar()
miDireccion= StringVar()

cuadroID= Entry(miFrame, textvariable= miID)
cuadroID.grid(row=0, column=1, padx=10, pady=10)
cuadroID.config(fg="green")

cuadroNombre= Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="blue", justify="center")

cuadroApellido= Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)
cuadroApellido.config(fg="blue", justify="center")

cuadroPass= Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=3, column=1, padx=10, pady=10)
cuadroPass.config(fg="red", justify="center", show="*")

cuadroAdress= Entry(miFrame, textvariable=miDireccion)
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

btnCrear= Button(botonera, text="Create", command=insertaDato)
btnCrear.grid(row=0, column=0, sticky="e", padx=10, pady=10)

btnLeer= Button(botonera, text="Read", command=leeDatos)
btnLeer.grid(row=0, column=1, sticky="e", padx=10, pady=10)

btnActualizar= Button(botonera, text="Up date", command=refrescaDatos)
btnActualizar.grid(row=0, column=2, sticky="e", padx=10, pady=10)

btnBorrar= Button(botonera, text="Delete", command=eliminaDatos)
btnBorrar.grid(row=0, column=3, sticky="e", padx=10, pady=10)


raiz.mainloop()
