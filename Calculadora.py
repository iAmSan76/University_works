"""Integrantes:
Werney Barajas
Santiago Palacios
Sebastián Merchán
Actividad:
Realizar una calculadora sencilla con las operaciones básicas"""

# Lo primero es invocar a la clase tkinter para poder trabajar con sus métodos, luego se importan las librerias sys la cual sirve para
# un cierre repentino del programa, esto se da cuando se divide entre 0, y la libreria time es para generar un delay en el programa en caso de
# un error.
from tkinter import*
import sys
import time

#Creación de la ventana
ven=Tk()
ven.title=("Calculadora")
ven.config(bg='gray')

#Creación del frame
frame=Frame(ven,width="600",height='1200')
frame.pack()
frame.config(bg='gray')

#Variables de control
op=StringVar()
ope=''
result=0.0
aux=''
cont=0.0

# Este metodo se invoca cada vez que oprimo un número, más no una operación o el igual
def clik(comm):
        #Defino las variables globales con las cuales voy a trabajar
        global  ope,cont

        #Verifico si ya escribí una operación
        if(ope!=''):
                cont+=1
                #Escribo mis números en pantalla
                op.set(comm)
                ope = ''

                #obtengo el número de mi pantalla
                err = float(op.get())

                if(aux=='div'):

                        if(err==0):
                                #Si quiero hacer una división entre cero envío un mensaje y cierro el programa
                                print('MATH ERROR')
                                (time.sleep(3))
                                sys.exit(1)
        else:
                #Si todavía no estoy haciendo una operación concateno mis números en pantalla
                op.set(op.get()+comm)

#Esta función se invoca cuando se quiere hacer una suma
def opera(num,veri):
        global ope,result,aux

        #Verífico si mi operacíon anterior es diferente a una suma, si es así envío mi
        # número a mi operación a realizar, pero con una verificación distinta, para saber que
        # mi siguente operación es una suma.
        if((aux!='suma')and(aux!='')):
                if(aux=='resta'):
                        menos(op.get(),4)
                elif(aux=='mult'):
                        por(op.get(),5)
                elif(aux=='div'):
                        div(op.get(),6)
        elif((aux=='')or(aux=='suma')):
                #Realizo las verificaciónes para envíar mi siguiente operción,
                # y realizo una suma la cual se muestra en mi calculadora
                result+=float(num)
                if(veri==1):
                        ope='suma'
                elif(veri==0):
                        ope='resta'
                elif(veri==7):
                        ope='mult'
                elif(veri==10):
                        ope='div'
                aux=ope
                op.set(result)





#Esta función se invoca cuando se oprime la resta
def menos(num,veri):
        global ope, result,aux

        if((aux!='resta')and(aux!='')):
                if(aux=='suma'):
                        opera(op.get(),0)
                elif(aux=='mult'):
                        por(op.get(),2)
                elif(aux=='div'):
                        div(op.get(),3)
        elif((aux=='')or(aux=='resta')):
                #para evitar problemas con los números que se
                # imprimen se mira una condición y se hace la operación
                if(result!=0.0):
                        result =result-float(num)
                        if(veri==1):
                                ope='resta'
                        if(veri==4):
                                ope='suma'
                        if(veri==8):
                                ope='mult'
                        if(veri==11):
                                ope='div'
                        aux=ope
                        op.set(result)
                elif(result==0.0):
                        result =float(num)-result
                        if(veri==1):
                                ope='resta'
                        if(veri==4):
                                ope='suma'
                        if(veri==8):
                                ope='mult'
                        if(veri==11):
                                ope='div'

                        aux=ope
                        op.set(result)

#Esta función se invoca cuando se desea multiplicar
def por(num,veri):
        global ope,result,aux

        if((aux!='mult')and(aux!='')):
                if(aux=='suma'):
                        opera(op.get(),7)
                elif(aux=='resta'):
                        menos(op.get(),8)
                elif(aux=='div'):
                        div(op.get(),9)
        else:
                # Se miran un condición para cuando el programa
                # multiplica por 0
                if (result != 0.0):
                        result = result * float(num)
                        if(veri==1):
                                ope = 'mult'
                        if(veri==2):
                                ope='resta'
                        if(veri==5):
                                ope='suma'
                        if(veri==12):
                                ope='div'
                        aux = ope
                        op.set(result)
                elif (result == 0.0):
                        result = float(num)
                        if(veri==1):
                                ope = 'mult'
                        if(veri==2):
                                ope='resta'
                        if(veri==5):
                                ope='suma'
                        if(veri==12):
                                ope='div'
                        aux = ope
                        op.set(result)

#Esta función se invoca cuando se oprime la división
def div(num,veri):
        global  ope,aux,result,cont


        if((aux!='div')and(aux!='')):
                if(aux=='suma'):
                        opera(op.get(),10)
                elif(aux=='resta'):
                        menos(op.get(),11)
                elif(aux=='mult'):
                        por(op.get(),12)
        else:
                # Se mira una condición para el programa no
                # confunta una división estilo 0/a con una
                # tipo a/0.
                if((result==0.0)and(cont!=0.0)):
                        result=0.0

                if(result==0.0)and(cont==0.0):
                        result=float(num)

                        if (veri == 6):
                                ope = 'suma'
                        elif (veri == 3):
                                ope = 'resta'
                        elif (veri == 9):
                                ope = 'mult'
                        elif (veri == 1):
                                ope = 'div'
                        aux = ope
                        op.set(result)
                else:

                        result=result/float(num)

                        if(veri==6):
                                ope='suma'
                        elif(veri==3):
                                ope='resta'
                        elif(veri==9):
                                ope='mult'
                        elif(veri==1):
                                ope='div'
                        aux=ope
                        op.set(result)




#Esta se invoca cuando se oprime el boton igual.
def final():
        global result,aux

        #El programa realiza la operación requerida y borra el resultado para
        #siguentes operaciones.
        if(aux=='suma'):
                 op.set(result+float(op.get()))
                 result = 0.0

        if(aux=='resta'):
                op.set(float(result) - float(op.get()))
                result=0.0
        if(aux=='mult'):
                op.set(float(result) * float(op.get()))
                result=0.0
        if(aux=='div'):
                op.set(float(result)/float(op.get()))
                result=0.0



#Creación de la pantalla
pant=Entry(frame,textvariable=op)
pant.grid(row=0,column=0,padx=10,pady=25, columnspan=5)
pant.config(bg='gray')

""" Se crean lo botones, los cules se mostraran en el frame, y tendran un comando
 dicho comando es el número a escribir, por otro lado los botones los cuales poseen una operación 
 enviarán el número que obtienen en pantalla y una verificación a un método de cada operación, ya que si 
 se oprimen botones de diferentes operaciónes, puede que el programa se equivoque"""

#Se crea la primera fila de botones

bt7=Button(frame,text="7",width="5",height='5',command=lambda:clik("7"))
bt7.grid(row=3,column=0)

bt8=Button(frame,text="8",width="5",height='5',command=lambda:clik("8"))
bt8.grid(row=3,column=1)

bt9=Button(frame,text="9",width="5",height='5',command=lambda:clik("9"))
bt9.grid(row=3,column=2)

btme=Button(frame,text="-",width="5",height='5',command=lambda:menos(op.get(),1))
btme.grid(row=3,column=3)

btd=Button(frame,text="/",width="5",height='5',command=lambda:div(op.get(),1))
btd.grid(row=3,column=4)

#Se crea la segunda fila de botones
bt4=Button(frame,text="4",width="5",height='5',command=lambda:clik("4"))
bt4.grid(row=4,column=0)


bt5=Button(frame,text="5",width="5",height='5',command=lambda:clik("5"))
bt5.grid(row=4,column=1)


bt6=Button(frame,text="6",width="5",height='5',command=lambda:clik("6"))
bt6.grid(row=4,column=2)


btma=Button(frame,text="+",width="5",height='5',command=lambda:opera(op.get(),1))
btma.grid(row=4,column=3)

bt0=Button(frame,text="0",width="5",height='5',command=lambda:clik("0"))
bt0.grid(row=4,column=4)

#Se crea la tercera fila

bt1=Button(frame,text="1",width="5",height='5',command=lambda:clik("1"))
bt1.grid(row=5,column=0)

bt2=Button(frame,text="2",width="5",height='5',command=lambda:clik("2"))
bt2.grid(row=5,column=1)

bt3=Button(frame,text="3",width="5",height='5',command=lambda:clik("3"))
bt3.grid(row=5,column=2)

btp=Button(frame,text="x",width="5",height='5',command=lambda:por(op.get(),1))
btp.grid(row=5,column=3)

bti=Button(frame,text="=",width="5",height='5',command=lambda:final())
bti.grid(row=5,column=4)

#Por ultimo se coloca la instrucción para que mi calculadora esté siempre activa.
ven.mainloop()
