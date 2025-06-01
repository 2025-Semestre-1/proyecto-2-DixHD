from tkinter import Tk
from tkinter import *
import tkinter as tk
import pygame, random
from PIL import Image, ImageTk
import tkinter.font as tkFont
#===========Piezas=============#
O = [["o","o"], 
        ["o","o"]]#Pieza Amarilla
I = [["i"], 
       ["i"],#Pieza Celeste
       ["i"],
       ["i"]]
L = [["L",    0],
       ["L",    0],#Pieza Naranja
       ["L","L"]]
J = [[0,    "j"],
       [0,    "j"],#Pieza Rosa Palido
       ["j","j"]]
T = [["t","t","t"],
       [0,     "t",    0]]#Pieza Morada
Z = [["z","z", 0   ],
       [0,    "z","z"]]#Pieza Verde
U = [["u",0,     "u"],
        ["u","u","u"]]#Pieza Rosa
X = [[0,    "x", 0],
       ["x","x","x"],#Pieza Roja
       [0,     "x", 0]]
piezas = [O, I, L, J, T, Z, U, X]
letras = ["o","i","L","j","t","z","u","x"]
#=====================Ventana Principal(Base)=====================#
ventana = Tk()
ventana.resizable(False, False)
ventana.geometry("350x500")
ventana.configure(bg="#00002e")
ventana.title("Tetris")
#=====================Ventana de Juego=====================#
canvas = tk.Canvas(ventana, width=350, height=500, bg="#00002e", highlightthickness=0)
canvas.pack()

fondo_puntos = tk.Canvas(ventana, width=100, height=50, bg="black", highlightthickness=1)

#-----------------------Imagenes-----------------------#
fondo = Image.open("fondo.png").resize((20,20))
fondo = ImageTk.PhotoImage(fondo)
ladrillo = Image.open("ladrillo.png").resize((20,20))
ladrillo = ImageTk.PhotoImage(ladrillo)
fondo_menu = Image.open("fondo_menu.png").resize((350,300))
fondo_menu = ImageTk.PhotoImage(fondo_menu)
#------------Imagen para el menú------------#
fondo_menu_1 = Label(ventana,image=fondo_menu,borderwidth=0)
fondo_menu_1.place(x=0, y=0)
#------------Imagenes(Piezas)------------#
pieza_roja = Image.open("pieza_roja.png").resize((20,20))
pieza_roja = ImageTk.PhotoImage(pieza_roja)
pieza_rosa = Image.open("pieza_rosa.png").resize((20,20))
pieza_rosa = ImageTk.PhotoImage(pieza_rosa)
pieza_naranja = Image.open("pieza_naranja.png").resize((20,20))
pieza_naranja = ImageTk.PhotoImage(pieza_naranja)
pieza_amarilla = Image.open("pieza_amarilla.png").resize((20,20))
pieza_amarilla = ImageTk.PhotoImage(pieza_amarilla)
pieza_celeste = Image.open("pieza_celeste.png").resize((20,20))
pieza_celeste = ImageTk.PhotoImage(pieza_celeste)
pieza_naranja = Image.open("pieza_naranja.png").resize((20,20))
pieza_naranja = ImageTk.PhotoImage(pieza_naranja)
pieza_rosa_claro = Image.open("pieza_rosa_claro.png").resize((20,20))
pieza_rosa_claro = ImageTk.PhotoImage(pieza_rosa_claro)
pieza_morada = Image.open("pieza_morada.png").resize((20,20))
pieza_morada = ImageTk.PhotoImage(pieza_morada)
pieza_verde = Image.open("pieza_verde.png").resize((20,20))
pieza_verde = ImageTk.PhotoImage(pieza_verde)
#-----------------------Funciones Extras-----------------------#
def lenn(num):
    cont = 0
    while num != 0:
        num //= 10
        cont += 1
    return cont

def lenL(lista):
    cont = 0
    for elem in lista:
        cont += 1
    return cont

def musica():
    pygame.mixer.init()
    pygame.mixer.music.load("Tetris_Theme.mp3")
    pygame.mixer.music.play(-1)

def sonido_puntos():
    pygame.mixer.init()
    sonido = pygame.mixer.Sound("puntos.mp3")
    sonido.play()
#-----------------------Funciones Importantes-----------------------#
puntos = 0
texto_puntos = None
def jugar():
    global puntos, texto_puntos
    fondo_menu_1.destroy()
    boton_jugar.destroy()
    musica()
    actualizar_interfaz()
    crear_bloque()
    caida_bloque()
    fondo_puntos.place(x=245, y=80)
    texto_puntos = fondo_puntos.create_text(50, 25, text=str(puntos), fill="white", font=("Minecraftia", 15))

num_juego = 1
def crear_nuevo_juego():
    matriz_original = open("Matriz_Base.txt", "r")
    contenido = matriz_original.readlines()
    matriz_original.close()
    archivo_copia = open("Juego",num_juego,".txt", "w")
    num_juego += 1
    for linea in contenido:
        archivo_copia.write(linea)
    archivo_copia.close()

def crear_bloque():
    pieza = random.choice(piezas)
    matriz = cargar_matriz()
    filas_pieza = len(pieza)
    columnas_pieza = len(pieza[0])
    filas_matriz = len(matriz)
    columnas_matriz = len(matriz[0])
    pos_x = 5
    pos_y = 1
    for y in range(filas_pieza):  
        for x in range(columnas_pieza):
            letra = pieza[y][x]
            if letra != 0:
                if matriz[pos_y + y][pos_x + x] != "0":
                    game_over()
                    return
                matriz[pos_y + y][pos_x + x] = letra
    guardar_matriz(matriz)
    actualizar_interfaz()
def game_over():
    pygame.mixer.music.stop()
    canvas.create_text(175, 250, text= "GAME OVER", fill="red", font=("Minecraftia", 30))
def fijar_bloque():
    global puntos, texto_puntos
    matriz = cargar_matriz()
    for y in range(len(matriz)):
        for x in range(len(matriz[0])):
            if matriz[y][x] == "o":
                matriz[y][x] = "o1"
            elif matriz[y][x] == "i":
                matriz[y][x] = "i1"
            elif matriz[y][x] == "L":
                matriz[y][x] = "L1"
            elif matriz[y][x] == "j":
                matriz[y][x] = "j1"
            elif matriz[y][x] == "t":
                matriz[y][x] = "t1"
            elif matriz[y][x] == "z":
                matriz[y][x] = "z1"
            elif matriz[y][x] == "u":
                matriz[y][x] = "u1"
            elif matriz[y][x] == "x":
                matriz[y][x] = "x1"
    for y in range(1, len(matriz) - 1):
        if all(celda != "0" and celda != "+" for celda in matriz[y][1:-1]):
            # Línea completa: borrarla y desplazar las de arriba
            del matriz[y]
            matriz.insert(1, ["+"] + ["0"] * (len(matriz[0]) - 2) + ["+"])
            sonido_puntos()
            puntos += 100
            fondo_puntos.itemconfig(texto_puntos, text=str(puntos))
    guardar_matriz(matriz)
    crear_bloque()
#-----------------------Guardar y Cargar Matriz-----------------------#
def cargar_matriz():
    archivo = open("Matriz_Base.txt", "r")
    contenido = archivo.readlines()
    archivo.close()
    matriz = []
    for linea in contenido:
        fila = linea.strip().split(',') 
        matriz.append(fila)
    return matriz

def guardar_matriz(matriz):
    archivo = open("Matriz_Base.txt", "w")
    for fila in matriz:
        linea = ",".join(fila)
        archivo.write(linea + "\n")
    archivo.close()
#-----------------------Movimientos-----------------------#
def mover_izquierda(e):
    matriz = cargar_matriz()
    filas = len(matriz)
    columnas = len(matriz[0])
    for y in range(1, filas - 1):  
        for x in range(1, columnas - 1):  
            if matriz[y][x] in letras:
                if matriz[y][x - 1] != "0":
                    return False
                letra = matriz[y][x]
                matriz[y][x - 1] = letra
                matriz[y][x] = "0"
    guardar_matriz(matriz)
    actualizar_interfaz()
    return True

def mover_derecha(e): 
    matriz = cargar_matriz()
    filas = len(matriz)
    columnas = len(matriz[0])
    for y in range(1, filas - 1):  
        for x in range(columnas - 2, 0, -1):  
            if matriz[y][x] in letras:
                if matriz[y][x + 1] != "0":
                    return False
                letra = matriz[y][x]
                matriz[y][x + 1] = letra
                matriz[y][x] = "0"
    guardar_matriz(matriz)
    actualizar_interfaz()
    return True

def mover_abajo():
    matriz = cargar_matriz()
    filas = len(matriz)
    columnas = len(matriz[0])
    for y in range(filas - 1, 0, -1):  
        for x in range(1, columnas - 1):
            if matriz[y][x] in letras:
                if matriz[y + 1][x] != "0": # Revisa si abajo está vacio
                    return False
                letra = matriz[y][x]
                matriz[y + 1][x] = letra
                matriz[y][x] = "0"
    guardar_matriz(matriz)
    actualizar_interfaz()
    return True

def caida_bloque():
    if mover_abajo() == False:
        fijar_bloque()
    ventana.after(500,caida_bloque)
#-----------------------Actualizar GUI según Matriz-----------------------#
def actualizar_interfaz():
    canvas.delete("all")  # Borra todos los elementos dibujados
    matriz = cargar_matriz()
    for y in range(len(matriz)):
        for x in range(len(matriz[y])):
            if matriz[y][x] == "+":
                canvas.create_image(x*20, y*20, anchor="nw", image=ladrillo)
            elif matriz[y][x] == "0":
                canvas.create_image(x*20, y*20, anchor="nw", image=fondo)
            elif matriz[y][x] == "o" or matriz[y][x] == "o1":
                canvas.create_image(x*20, y*20, anchor="nw", image=pieza_amarilla)
            elif matriz[y][x] == "i" or matriz[y][x] == "i1":
                canvas.create_image(x*20, y*20, anchor="nw", image=pieza_celeste)
            elif matriz[y][x] == "L" or matriz[y][x] == "L1":
                canvas.create_image(x*20, y*20, anchor="nw", image=pieza_naranja)
            elif matriz[y][x] == "j" or matriz[y][x] == "j1":
                canvas.create_image(x*20, y*20, anchor="nw", image=pieza_rosa_claro)
            elif matriz[y][x] == "t" or matriz[y][x] == "t1":
                canvas.create_image(x*20, y*20, anchor="nw", image=pieza_morada)
            elif matriz[y][x] == "z" or matriz[y][x] == "z1":
                canvas.create_image(x*20, y*20, anchor="nw", image=pieza_verde)
            elif matriz[y][x] == "u" or matriz[y][x] == "u1":
                canvas.create_image(x*20, y*20, anchor="nw", image=pieza_rosa)
            elif matriz[y][x] == "x" or matriz[y][x] == "x1":
                canvas.create_image(x*20, y*20, anchor="nw", image=pieza_roja)
    guardar_matriz(matriz)
#-----------------------Botones-----------------------#
boton_jugar = Button(ventana,text="Jugar",font="Minecraftia",command=jugar)
boton_jugar.place(x=130,y=300)
#-----------------------Teclas-----------------------#
ventana.bind("<Left>",mover_izquierda)
ventana.bind("<Right>", mover_derecha)
ventana.bind("<Up>", lambda e: up)
#ventana.bind("<Down>", mover_abajo)
#-----------------------Bucles-----------------------#
ventana.mainloop()
pygame.mixer.music.stop()






















