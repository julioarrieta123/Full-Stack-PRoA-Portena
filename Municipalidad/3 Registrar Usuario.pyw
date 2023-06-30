from tkinter import*
from tkinter import messagebox
from PIL import ImageTk, Image 


def ventana_principal():
	global ventana1
	ventana1=Tk()
	#---------esta porcion de codigo centrara mi ventana---------
	w = 500
	h = 380
	ws = ventana1.winfo_screenwidth()
	hs = ventana1.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	ventana1.geometry('%dx%d+%d+%d' % (w, h, x, y))
	
	#----------------------------------------------------------------------------------------------------
	ventana1.title("Bienvenidos")
	ventana1.iconbitmap("Imágenes/LogoProA.ico")
	
	#abrimos la imagen
	imagenA = Image.open("Imágenes/net.gif")
	#cambiamos el tamaño
	resized = imagenA.resize((450, 225), Image.ANTIALIAS)
	imagenA = ImageTk.PhotoImage(resized)
	label=Label(ventana1, image=imagenA).place(x=20, y=10)
	#------------------------------------------------------------------------------------------------------
	
	Button(ventana1,text="Iniciar Sesion", height="1" , width="30", bg="medium sea green", fg="black", font=("Calibri",15)). place(x=100, y=270)
	
	Button(ventana1,text="Registrarse", height="1" , width="30", bg="DeepPink2", fg="black", font=("Calibri",15), command=ventana_regitrar_usuario). place(x=100, y=320)
	
	ventana1.mainloop()
	
def insertar_datos():
	if (Usuario.get() == ""):
		messagebox.showinfo("Faltan Datos","Ingresar Usuario")
	elif (Mail.get() == ""):
		messagebox.showinfo("Faltan Datos","Ingresar Mail")
	elif (Contrasena.get() == ""):
		messagebox.showinfo("Faltan Datos","Ingresar Contraseña")
	elif (Contrasena2.get() == ""):
		messagebox.showinfo("Faltan Datos","Repetir Contraseña")
	elif (Contrasena.get() != Contrasena2.get()):
		messagebox.showinfo("Error","Las contraseñas no coinciden")
	
def limpiar_cajas():
	Usuario.set("")
	Mail.set("")
	Contrasena.set("")
	Contrasena2.set("")
def volver_inicio():
	ventana2.destroy()
	ventana_inicio()
def ventana_regitrar_usuario():
	ventana1.destroy()#indicamos que cierre la ventana principal
	global ventana2
	ventana2=Tk()
	#---------esta porcion de codigo centrara mi ventana---------
	w = 300
	h = 380
	ws = ventana2.winfo_screenwidth()
	hs = ventana2.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	ventana2.geometry('%dx%d+%d+%d' % (w, h, x, y))
	
	#----------------------------------------------------------------------------------------------------
	#abrimos la imagen
	imagenA = Image.open("Imágenes/NuevoUsuario.gif")
	#cambiamos el tamaño
	resized = imagenA.resize((105, 120), Image.ANTIALIAS)
	imagenA = ImageTk.PhotoImage(resized)
	label=Label(ventana2, image=imagenA).place(x=100, y=10)
		#------------------------------------------------------------------------------------------------------
	
	ventana2.title("Bienvenidos")
	ventana2.iconbitmap("Imágenes/LogoProA.ico")
	
	Label (ventana2, text="Usuario"). place(x=50, y=160)
	Label (ventana2, text="Mail"). place(x=50, y=200)
	Label (ventana2, text="Contraseña"). place(x=50, y=240)
	Label (ventana2, text="R.Contraseña"). place(x=50, y=280)
	
	global Usuario, Mail, Contrasena, Contrasena2
	Usuario = StringVar()
	Mail = StringVar()
	Contrasena = StringVar()
	Contrasena2 = StringVar()
	
	Entry(ventana2,textvariable= Usuario).place(x=140, y=160)
	Entry(ventana2,textvariable= Mail).place(x=140, y=200)
	Entry(ventana2,textvariable= Contrasena).place(x=140, y=240)
	Entry(ventana2,textvariable= Contrasena2).place(x=140, y=280)
	
	Button(ventana2,text="Guardar", width="10", command=insertar_datos, bg="green", fg="black"). place(x=18, y=320)
	Button(ventana2,text="Cancelar", width="10", command=limpiar_cajas, bg="Red", fg="black"). place(x=108, y=320)
	Button(ventana2,text="Salir", width="10", command= volver_inicio, bg="Navy", fg="black"). place(x=198, y=320)
	
	
	
	ventana2.mainloop()

ventana_principal()



