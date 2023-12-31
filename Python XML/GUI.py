#pip install bs4
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()

marco1 = tk.Frame(raiz,padx=50,pady=50)

archivo = open("interfaz.xml","r")

contenido = archivo.read()

xml = BeautifulSoup(contenido,"xml")

for campo in xml.find_all("campo"):
    tipo = campo.get("tipo")
    texto = campo.get("texto")
    if tipo == "entrada":
        ttk.Entry(marco1).pack(padx=10,pady=10)
    elif tipo == "etiqueta":
        ttk.Label(marco1,text=texto).pack(padx=10,pady=10)
    elif tipo == "desplegable":
        for opciones in xml.find_all("opciones"):
            valor1 = opciones.get("valor1")
            valor2 = opciones.get("valor2")
            valor3 = opciones.get("valor3")
            desplegable = ttk.Combobox(marco1,values=[valor1,valor2,valor3])
            desplegable.current(1)
            desplegable.pack(padx=10,pady=10)
    elif tipo == "spinbox":
        ttk.Spinbox(marco1,from_=1,to=99).pack(padx=10,pady=10)
    elif tipo == "boton":
        ttk.Button(marco1,text=texto).pack(padx=10,pady=10)

archivo.close()
marco1.pack()

marco2 = tk.Frame(raiz,padx=50,pady=50,background="light blue")

archivo = open("interfaz.xml","r")

contenido = archivo.read()

xml = BeautifulSoup(contenido,"xml")

for campo in xml.find_all("campo"):
    tipo = campo.get("tipo")
    texto = campo.get("texto")
    if tipo == "tabla":
        for columnas in xml.find_all("columnas"):
            columna1 = columnas.get("columna1")
            columna2 = columnas.get("columna2")
            columna3 = columnas.get("columna3")
            tabla = ttk.Treeview(marco2,columns=(columna1,columna2,columna3))
            tabla.heading("#0",text="Identificador")
            tabla.heading("#1",text=columna1)
            tabla.heading("#2",text=columna2)
            tabla.heading("#3",text=columna3)
            for fila in xml.find_all("fila1"):
                dato1 = fila.get("dato1")
                dato2 = fila.get("dato2")
                dato3 = fila.get("dato3")
                
                tabla.insert('','0',text="Jugador 1",values=(dato1,dato2,dato3))
            for fila in xml.find_all("fila2"):

                dato1 = fila.get("dato1")
                dato2 = fila.get("dato2")
                dato3 = fila.get("dato3")

                tabla.insert('','1',text="Jugador 2",values=(dato1,dato2,dato3))

            tabla.pack(padx=10,pady=10)    

archivo.close()

marco2.pack()        

tk.mainloop()
