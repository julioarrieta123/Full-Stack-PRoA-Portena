from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image #pip install pillow
import pymysql


def ventana_inicio(): #creamos la ventana inicio
	global ventana1
	ventana1=Tk()
	#-------está porción de código va a centrar mi ventana---------
	w = 500
	h = 380
	ws = ventana1.winfo_screenwidth()
	hs = ventana1.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	ventana1.geometry('%dx%d+%d+%d' % (w, h, x, y))
	#----------------------------------------------------------
	ventana1.title("Bienvenidos")
	ventana1.iconbitmap("Imágenes/LogoProA.ico")#https://www.online-convert.com/es
	#------------------------------------------------------
	#abrimos la imagen
	imagenA = Image.open("Imágenes/net.gif")
	#cambiamos el tamaño
	resized = imagenA.resize((450, 225), Image.ANTIALIAS)
	imagenA = ImageTk.PhotoImage(resized)
	label=Label(ventana1,image=imagenA).place(x=20,y=10)
	#-----------------------------------------------------
	
	#https://wiki.tcl-lang.org/page/Colors+with+Names fuentes de colores                
	Button(ventana1,text="Iniciar Sesión", height="1", width="30",bg="navy", fg="white", font=("Calibri", 15),command = login).place(x=100,y=270)
	Button(ventana1,text="Registrar Usuario", height="1", width="30",bg="navy", fg="white", font=("Calibri", 15), command=ventana_registrar_usuario).place(x=100,y=320)

	ventana1.mainloop()

def insertar_datos():
	if (usuario.get()== ""):
		messagebox.showinfo("Faltan datos","ingrese Usuario")
	elif (mail.get()== ""):
		messagebox.showinfo("Faltan datos","ingrese Mail")
	elif (contrasena1.get()== ""):
		messagebox.showinfo("Faltan datos","ingrese Contraseña")
	elif (contrasena2.get()== ""):
		messagebox.showinfo("Faltan datos","Repita Contraseña")
	elif (contrasena1.get()!= contrasena2.get()):
		messagebox.showinfo("Error","Las Contraseñas no Coinciden")
		
	basedatos = pymysql.connect(host="localhost", user="root", passwd="",db="sistemaproa") #+Creamos la base de datos indicandole la ruta (ubicación)
	fcursor=basedatos.cursor()
	
	fcursor.execute("SELECT Contrasena FROM usuarios WHERE Usuario='"+ usuario.get()+"'")
	
	if fcursor.fetchall():
		messagebox.showinfo("Aviso","Usuario ya registrado")
	else:
		
		sql= "INSERT INTO Usuarios (Usuario, Mail, Contrasena) VALUES ('{0}','{1}', '{2}')".format(usuario.get(), mail.get(), contrasena1.get())
		try: 
			fcursor.execute(sql)
			basedatos.commit()
			messagebox.showinfo("Registro","Se registro el Usuario con exito")
			limpiar_cajas()
			return 
		except:
			messagebox.showinfo("Registro","No se registro el Usuario")
			limpiar_cajas()
	basedatos.close()

def limpiar_cajas():
	usuario.set("")
	mail.set("")
	contrasena1.set("")
	contrasena2.set("")

def volver_inicio():
	ventana2.destroy() #destruimos ventana 2
	ventana_inicio() # volvemos a crear ventana 1 llamando a la función

def ventana_registrar_usuario():
	ventana1.destroy()#indicamos que cierre la ventana principal
	global ventana2
	ventana2=Tk()
	#-------está porción de código centrara mi ventana---------
	w = 300
	h = 360
	ws = ventana2.winfo_screenwidth()
	hs = ventana2.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	ventana2.geometry('%dx%d+%d+%d' % (w, h, x, y))
	#----------------------------------------------------------
	ventana2.title("Registar Usuario")
	ventana2.iconbitmap("Imágenes/LogoProA.ico")#https://www.online-convert.com/es
	
	#------------------------------------------------------
	#abrimos la imagen
	imagenB = Image.open("Imágenes/NuevoUsuario.gif")
	#cambiamos el tamaño
	resized = imagenB.resize((105, 120), Image.ANTIALIAS)
	imagenB = ImageTk.PhotoImage(resized)
	label=Label(ventana2,image=imagenB).place(x=100,y=10)
	#-----------------------------------------------------
		
	Label(ventana2, text="Usuario").place(x=50,y=160)
	Label(ventana2, text="Mail").place(x=50,y=200)
	Label(ventana2, text="Contraseña").place(x=50,y=240)
	Label(ventana2, text="R. Contraseña").place(x=50,y=280)
	
	global usuario, mail, contrasena1, contrasena2
	usuario = StringVar()
	mail = StringVar()
	contrasena1 = StringVar()
	contrasena2 = StringVar()

	Entry(ventana2,textvariable= usuario).place(x=140,y=160)
	Entry(ventana2,textvariable= mail).place(x=140,y=200)
	Entry(ventana2,textvariable=contrasena1, show="*").place(x=140,y=240)
	Entry(ventana2,textvariable=contrasena2, show="*").place(x=140,y=280)
	
	Button(ventana2,text="Guardar", width="10", command=insertar_datos,bg="green", fg="white").place(x=18,y=320)
	Button(ventana2,text="Cancelar",width="10", command=limpiar_cajas,bg="red", fg="white").place(x=108,y=320)
	Button(ventana2,text="Salir", width="10", command=volver_inicio,bg="navy", fg="white").place(x=198,y=320)
	
	ventana2.mainloop()

def login():
	ventana1.destroy()#indicamos que cierre la ventana principal
	global ventana3
	ventana3=Tk()
	#-------está porción de código centrara mi ventana---------
	w = 300
	h = 300
	ws = ventana3.winfo_screenwidth()
	hs = ventana3.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	ventana3.geometry('%dx%d+%d+%d' % (w, h, x, y))
	#----------------------------------------------------------
	ventana3.title("Iniciar Sesion")
	ventana3.iconbitmap("Imágenes/LogoProA.ico")#https://www.online-convert.com/es
	
	#------------------------------------------------------
	#abrimos la imagen
	imagen = Image.open("Imágenes/login.png")
	#cambiamos el tamaño
	resized = imagen.resize((105, 120), Image.ANTIALIAS)
	imagen = ImageTk.PhotoImage(resized)
	label=Label(ventana3,image=imagen).place(x=100,y=10)
	#-----------------------------------------------------
	
	global usuarioL, contrasenaL
	usuarioL = StringVar()
	contrasenaL = StringVar()
	
	Label (ventana3, text="Usuario").place(x=50, y=160)
	Label (ventana3, text="Contraseña").place(x=50, y=200)
	
	Entry(ventana3, textvariable= usuarioL). place (x=140, y=160)
	Entry(ventana3, textvariable= contrasenaL, show="*"). place (x=140, y=200)
	
	
insertar_datos()
