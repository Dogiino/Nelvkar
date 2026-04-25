from tkinter import messagebox
import requests
import tkinter
import os

def GIT(Tipo,URL,NameArchivo=""):
    global Data
    Respuesta= requests.get(URL)
    if Tipo == 1:
        with open(os.path.join(os.path.join("Modulos_Data","ReproductorMp3"),NameArchivo),"wb") as Archivo:
            Archivo.write(Respuesta.content)
    elif Tipo == 2:
        Data = Respuesta.json()
        return Data
def filtrar(event=None):
    texto = Buscador.get().lower()
    Filtrados.delete(0, tkinter.END)

    for artista, canciones in Data.items():
        for titulo in canciones:
            if texto in titulo.lower() or texto in artista.lower():
                Filtrados.insert(tkinter.END,f"{artista} - {titulo}")
def descargar():
    seleccion = Filtrados.curselection()
    if not seleccion:return
    texto = Filtrados.get(seleccion)
    artista,titulo = texto.split(" - ")
    link = Data[artista][titulo]
    nombre = f"{artista} - {titulo}.mp3"
    messagebox.showinfo(f"{nombre}",f"Se esta descargando {nombre}")
    GIT(1,link,nombre)
    messagebox.showinfo(f"{nombre}",f"descargado: {nombre}")

Ventana = tkinter.Tk()

Ventana.title("Reproductor")
Ventana.geometry("650x500+100+100")
Ventana.resizable(False,False)
Ventana.configure(bg="#202020")

Buscador = tkinter.Entry(Ventana,
    width=78,
    font=("Arial",11),
    bg="#1B1B1B",
    fg="#BBBBBB",
    selectbackground="#444444",)
Filtrados= tkinter.Listbox(Ventana,
    font=("Arial",11),
    highlightbackground="#242424",
    highlightthickness=0,
    selectbackground="#3F3F3F",
    fg="#BBBBBB",
    bg="#242424",
    relief="flat",
    width=79,
    height=0,
    activestyle="none",
    cursor="hand2",)
Installer= tkinter.Button(Ventana,
    borderwidth=0,
    activebackground="#3F3F3F",
    activeforeground="#CACACA",
    text="Descargar",
    bg="#575757",
    fg="#FFFFFF",
    width=15,
    cursor="hand2",
    command=lambda:descargar())

Buscador.place(x=10,y=10)
Filtrados.place(x=8,y=40)
Installer.place(x=10,y=470)

Ruta = os.path.join("Modulos_Data","ReproductorMp3")
os.makedirs(Ruta,exist_ok=True)

GIT(2,"https://raw.githubusercontent.com/Dogiino/Nelvkar/refs/heads/ReproductorMp3/Data.json")

Buscador.bind("<KeyRelease>",filtrar)

Ventana.mainloop()