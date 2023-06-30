from tkinter import * #importar la biblioteca tkinter
raiz=Tk()#objeto instansiado en una clase interna a realizar la raiz
raiz.title("Ventana de pruebas")#2 aqui se coloca el titulo de la ventana
raiz.resizable(1,1)#3 metodo para setear y bloquear el redimensionamiento (x,y) son parametros boleanos y bloquea la ventana que se despliega (1,0) movera en una sola direecion el 0
raiz.geometry("600x400")#4 se usa para dimensinar la ventana
raiz.config(bg="light blue")#5 para cambiar el fondo de la pantalla)
miFrame=Frame()#6 creacion de un frame como otro objeto a apartir de la clase frame
miFrame.pack()#7 empaquetar el frmae dentro de la raiz.paramet side=rigt,left
miFrame.config(bg = "dark red")
miFrame.pack(fill = "y", expand=True)

miFrame.config(width="300",height="200")


raiz.mainloop()#metodo, es un bucle infinito, siempre debe ir al final
