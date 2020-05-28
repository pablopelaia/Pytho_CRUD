from tkinter import *
from tkinter import messagebox
from tkinter import ttk
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
    limpiar()


def limpiar():

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
    dibujaTabla(arbol)


def leeDatos():

    if miID.get()=="": 
        messagebox.showwarning("Dato requerido", "debe ingresar ID")
        return 0
    
    limpiar()

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
    
    cnx= sqlite3.connect("Usuario")    
    miCursor= cnx.cursor()

    datosFormulario= [miNombre.get(), miApellido.get(), miPass.get(), miDireccion.get(), comentarios.get('1.0', END)]
        
    for dato in datosFormulario:
        print(dato)

    miCursor.execute(
        "UPDATE DATO_USUARIOS SET NOMBRE_USUARIO=?, APELLIDO=?, CONTRASENA=?, DIRECCION=?, COMENTARIOS=?" + "WHERE ID=" + miID.get(), datosFormulario)
        
    cnx.commit()
    messagebox.showinfo("BBDD", "Registro actualizado con éxito")
    borraCampos()
    dibujaTabla(arbol)


def eliminaDatos():
    
    if miID.get()=="": 
        messagebox.showwarning("Dato requerido", "debe ingresar ID")
        return 0
    
    leeDatos()

    respuesta= messagebox.askokcancel("Borrar usuario", "¿Está seguro que quiere borrar el usuario")

    if respuesta==False: return 0
    
    cnx= sqlite3.connect("Usuario")    
    miCursor= cnx.cursor()

    miCursor.execute("DELETE FROM DATO_USUARIOS WHERE ID=" + miID.get())

    cnx.commit()
    borraCampos()
    dibujaTabla(arbol)
    messagebox.showinfo("Borrado", "Su usuario ha sido borrado")


def dibujaTabla(self):

    elementos= self.get_children()

    for elemento in elementos:

        self.delete(elemento)
    
    cnx= sqlite3.connect("Usuario")    
    miCursor= cnx.cursor()
    
    miCursor.execute("SELECT * FROM DATO_USUARIOS ORDER BY ID DESC")
    db= miCursor.fetchall()

    for fila in db:

        self.insert('', 0, text=fila[1], values= fila[2])



    cnx.commit()



raiz= Tk()

# Creo barra menu-----------------------------------------------------------------------

barraMenu= Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)
raiz.title("CRUD")

dbMenu=Menu(barraMenu, tearoff=0)
dbMenu.add_command(label="Conectar", command=conexionBBDD)
dbMenu.add_command(label="Borrar campos", command=borraCampos)
dbMenu.add_command(label="Salir", command=salirApp)

barraMenu.add_cascade(label="Opciones", menu=dbMenu)

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
cuadroNombre.focus()

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

# Tabla-----------------------------------------------------------------------------

contenedor= Frame(raiz)
contenedor.pack()
 
arbol= ttk.Treeview(contenedor, column=0, height=10, columns=1)
arbol.pack()
arbol.heading("#0", text='Nombre', anchor=CENTER)
arbol.heading("#1", text='Apellido', anchor=CENTER)
dibujaTabla(arbol)

raiz.mainloop()