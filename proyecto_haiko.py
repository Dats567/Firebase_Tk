import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from time import sleep
from tkinter import *
datos =[]
regis =[]
contador = 0
# Fetch the service account key JSON file contents
cred = credentials.Certificate('C:/Users/Usuario\Documents/Alejandro/trabajos_programacion/git_consola/firebase_python/clave/clave.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://basedatoshaiko.firebaseio.com/'
})

ref = db.reference("Datos")
    
ventana = Tk()
ventana.geometry('850x850')
ventana.configure(bg = 'green')
ventana.title("Bienvenidos a el cajero")
texto = Label(ventana, text="Ingrese sus datos", bg='cadet blue1', font=("Arial Bold", 14), fg="red")
texto.place(x=20, y=20)

def entrada(input):
    global contador
    content = dato.get()
    dato.delete(0, END)#borro la información del entry
    regis.append(content)
    ref.update({
                    contador : content,
         }) 
    contador += 1
    print (content)
    print(regis)
    
Label(ventana, text="Input: ").place(x=20, y=60)
dato = Entry(ventana)
dato.bind('<Return>', entrada) 
dato.place(x=90, y=60)


ventana.mainloop() 