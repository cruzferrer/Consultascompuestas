import pandas as pd
from tkinter import *

class Inicio:
    def mostrarindex():
        root = Tk()
        root.title("Menú")
        root.geometry("200x320")
        root.resizable(False,False)
        root.config(background="red")

        def cosulta1ir():
            root.destroy()
            from union import union
            union.consulta1()
        
        def consulta2ir():
            root.destroy()
            from union import union
            union.consulta2()

        def consulta3ir():
            root.destroy()
            from union import union
            union.consulta3()
        def consulta4ir():
            root.destroy()
            from union import union
            union.consulta4()
        
        def consulta5ir():
            root.destroy()
            from union import union
            union.consulta5()
        
        def consulta6ir():
            root.destroy()
            from union import union
            union.consulta6()
        
        def consulta7ir():
            root.destroy()
            from union import union
            union.consulta7()

        consulta1=Button(root,text="Ir a la consulta 1", command=cosulta1ir)
        consulta1.pack()
        consulta1.place(relx=0.5,y=40,anchor="center")
        
        consulta2=Button(root,text="Ir a la consulta 2",command=consulta2ir)
        consulta2.pack()
        consulta2.place(relx=0.5,y=80,anchor="center")

        consulta3=Button(root,text="Ir a la consulta 3",command=consulta3ir)
        consulta3.pack()
        consulta3.place(relx=0.5,y=120,anchor="center")

        consulta4=Button(root,text="Ir a la consulta 4",command=consulta4ir)
        consulta4.pack()
        consulta4.place(relx=0.5,y=160,anchor="center")
        
        consulta5=Button(root,text="Ir a la consulta 5",command=consulta5ir)
        consulta5.pack()
        consulta5.place(relx=0.5,y=200,anchor="center")

        consulta6=Button(root,text="Ir a la consulta 6",command=consulta6ir)
        consulta6.pack()
        consulta6.place(relx=0.5,y=240,anchor="center")

        consulta7=Button(root,text="Ir a la consulta 7",command=consulta7ir)
        consulta7.pack()
        consulta7.place(relx=0.5,y=280,anchor="center")
        root.mainloop()

    mostrarindex()
