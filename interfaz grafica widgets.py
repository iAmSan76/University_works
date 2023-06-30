from tkinter import * #importar la biblioteca tkinter
raiz=Tk()#objeto instansiado en una clase interna a realizar la raiz
raiz.title("Home home")
raiz.config(bg="cyan")

miFrame=Frame(raiz,width=500,height=400)
miFrame.pack()
miFrame.config(bg="pink")

miLabel=Label(miFrame,text="hola home")#instanciar mi label a partir de mi clase label
miLabel.pack()#2 empaqueta el label dentro del frame pero no es adecuado
miLabel.place(x=100,y=200)#3 posiciona el label respetando el frame
Label(miFrame, text="Hola sapos perros", fg="dark red").place(x=100,y=200)#cambia color de etra y abrevia pasos 2
Label(miFrame, text="Hola sapos perros", fg="dark blue",font=("Comic Sans MS",18)).place(x=100,y=200)#cambio de tipo de letra con font y color con fg

miImagen=photoImage(File="lol.jpg")
Label(miFrame,image=miImagen).place(x=300,y=50)

raiz.mainloop()
