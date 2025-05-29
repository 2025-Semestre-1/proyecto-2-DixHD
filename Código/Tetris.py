from tkinter import Tk
from tkinter import *
import tkinter as tk
import pygame, random
from PIL import Image, ImageTk
import tkinter.font as tkFont

#===========Piezas=============#
O = [["o","o"], #Cuadrado
        ["o","o"]]#Pieza Amarilla

I = [["i"], #Palo
       ["i"],#Pieza Celeste
       ["i"],
       ["i"]]

L = [["L",    0],#L
       ["L",    0],#Pieza Naranja
       ["L","L"]]

J = [[0,    "j"],#L invertida
       [0,    "j"],#Pieza Rosa Palido
       ["j","j"]]

T = [["t","t","t"],# T
       [0,     "t",    0]]#Pieza Morada

Z = [["z","z", 0   ],#Z
       [0,    "z","z"]]#Pieza Verde

U = [["u",0,     "u"],# U 
        ["u","u","u"]]#Pieza Rosa

X = [[0,    "x", 0],#Equis
       ["x","x","x"],#Pieza Roja
       [0,     "x", 0]]

piezas = [O, I, L, J, T, Z, U, X]

#====================================
ventana = Tk()
ventana.resizable(False, False)
ventana.geometry("350x500")
ventana.configure(bg="#00002e")
ventana.title("Tetris")

fondo = Image.open("fondo.png").resize((20,20))
fondo = ImageTk.PhotoImage(fondo)

ladrillo = Image.open("ladrillo.png").resize((20,20))
ladrillo = ImageTk.PhotoImage(ladrillo)

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
def jugar():
    fondo_menu_1.destroy()
    musica()
    actualizar_interfaz()
    caida_bloque()
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


def sacar_figura(figura):
    largo_Y = lenL(figura)
    largo_X = lenL(figura[0])

def cargar_matriz():
    archivo = open("Matriz_Base.txt", "r")
    contenido = archivo.readlines()
    archivo.close()
    
    matriz = []
    for linea in contenido:
        matriz.append(list(linea.strip()))
    return matriz

def guardar_matriz(matriz):
    archivo = open("Matriz_Base.txt", "w")
    for fila in matriz:
        linea = "".join(fila)
        archivo.write(linea + "\n")
    archivo.close()
#-----------------------Movimientos-----------------------#
def mover_izquierda(event=None):
    matriz = cargar_matriz()
    for y in range(len(matriz[1:])):
        for x in range(len(matriz[y])):
            if matriz[y][x] in O:  # aquí usás la letra de tu pieza activa
                if matriz[y][x-1] == "0":  # verifica si la celda a la izquierda está vacía
                    matriz[y][x-1] = matriz[y][x]
                    matriz[y][x] = "0"
    guardar_matriz(matriz)
    actualizar_interfaz()

def mover_abajo():
    matriz = cargar_matriz()
    filas = len(matriz)
    columnas = len(matriz[0])
    for y in range(filas - 2, 0, -1):  
        for x in range(1, columnas - 1):  
            if matriz[y][x] == "o" and matriz[y + 1][x] == "0":
                matriz[y + 1][x] = "o"
                matriz[y][x] = "0"

    guardar_matriz(matriz)
    actualizar_interfaz()
    return True
    
def caida_bloque():
    if mover_abajo() == False:
        return
    mover_abajo() 
    ventana.after(500,caida_bloque)
    
def actualizar_interfaz():
    archivo = open("Matriz_Base.txt","r")
    contenido = archivo.readlines()
    archivo.close()
    for y in range(lenL(contenido)):
        fila = contenido[y].strip() 
        for x in range(lenL(fila)):
            if fila[x] == "+":
                celda = tk.Label(ventana, image=ladrillo, borderwidth=0)
            elif fila[x] == "0":
                celda = tk.Label(ventana, image=fondo, borderwidth=0)
            elif fila[x] == "o" or fila[x] == "o1":
                celda = tk.Label(ventana, image=pieza_amarilla, borderwidth=0)
            elif fila[x] == "i" or fila[x] == "i1":
                celda = tk.Label(ventana, image=pieza_celeste, borderwidth=0)
            elif fila[x] == "L" or fila[x] == "L1":
                celda = tk.Label(ventana, image=pieza_naranja, borderwidth=0)
            elif fila[x] == "j" or fila[x] == "j1":
                celda = tk.Label(ventana, image=pieza_rosa_claro, borderwidth=0)
            elif fila[x] == "t" or fila[x] == "t1":
                celda = tk.Label(ventana, image=pieza_morada, borderwidth=0)
            elif fila[x] == "z" or fila[x] == "z1":
                celda = tk.Label(ventana, image=pieza_verde, borderwidth=0)
            elif fila[x] == "u"or fila[x] == "u1":
                celda = tk.Label(ventana, image=pieza_rosa, borderwidth=0)
            elif fila[x] == "x" or fila[x] == "x1":
                celda = tk.Label(ventana, image=pieza_roja, borderwidth=0)
            else:
                continue
            celda.grid(row=y, column=x,padx=0, pady=0)
#iniciar_pieza(contenido,random.choice(piezas),1,6)



ventana.bind("<Left>",mover_izquierda)
ventana.bind("<Right>", lambda e: right)
ventana.bind("<Up>", lambda e: up)
ventana.bind("<Down>", mover_abajo)

fondo_menu = Image.open("fondo_menu.png").resize((350,300))
fondo_menu = ImageTk.PhotoImage(fondo_menu)
fondo_menu_1 = Label(ventana,image=fondo_menu,borderwidth=0)
fondo_menu_1.place(x=0, y=0)

boton_jugar = Button(ventana,text="Jugar",font="Minecraftia",command=jugar)
boton_jugar.place(x=130,y=300)


ventana.mainloop()
pygame.mixer.music.stop()






















