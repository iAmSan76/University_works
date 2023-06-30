from tkinter import * #importar la biblioteca tkinter

raiz=Tk()#objeto instansiado en una clase interna a realizar la raiz

raiz.title("Home home")
raiz.config(bg="cyan")

miFrame=Frame(raiz,width=1200,height=600)
miFrame.pack()

cuadroTexto=Entry(miFrame)
#cuadroTexto.pack()
#cuadroTexto.place(x=100,y=100)
cuadroTexto.grid(row=0,column=1)
miLabel=Label(miframe,text="nombre: ")
#miLabel.place(x=50,y=100)
#miLabel.grid(row=0,column=0)

#cuadroTexto=Entry(miFrame,text="nombre")
#miLabel.place(x=40,y=100)

raiz.mainloop()
