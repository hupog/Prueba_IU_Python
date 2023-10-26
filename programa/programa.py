import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import os

# Nombre del archivo o carpeta que deseas agregar a la ruta
nombre_archivo = "calculadora.png"

# Obtener el directorio de inicio del usuario en Windows
directorio_inicio = os.path.expanduser("~")

# Construir la ruta completa y reemplazar las barras diagonales
ruta_completa = os.path.join(directorio_inicio, "Desktop/programa", nombre_archivo).replace("\\", "/")

# Nombre del archivo o carpeta que deseas agregar a la ruta
nombre_archivo2 = "caja_fuerte.png"

# Obtener el directorio de inicio del usuario en Windows
directorio_inicio2 = os.path.expanduser("~")

# Construir la ruta completa y reemplazar las barras diagonales
ruta_completa2 = os.path.join(directorio_inicio2, "Desktop/programa", nombre_archivo2).replace("\\", "/")

# Verificar la ruta completa
print(ruta_completa)

def verificar_codigo(event):
    texto = entry.get()
    if texto == "1234":
        abrir_nueva_pestana()
    else:
        label_resultado.config(text="Código incorrecto", bg="black", fg="white")

def abrir_nueva_pestana():
    nueva_pestana = ttk.Frame(tab_control)
    tab_control.add(nueva_pestana, text="Codigo correcto")
    tab_control.select(nueva_pestana)
    


    # Agregar una imagen a la segunda pestaña
    image_path2 = ruta_completa2  # Reemplaza con la ruta de tu segunda imagen
    image2 = PhotoImage(file=image_path2)
    image2 = image2.subsample(2)
    image_label2 = tk.Label(nueva_pestana, image=image2)
    image_label2.image = image2
    image_label2.pack()

# Crear la ventana principal
root = tk.Tk()
root.title("Caja fuerte")

# Crear el control de pestañas
tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Introducir contraseña")
tab_control.pack(expand=1, fill="both")

# Crear un marco para la imagen
frame = ttk.Frame(tab1)
frame.pack(padx=100, pady=10)


# Configurar la imagen (reemplaza con la ruta de tu imagen)
image_path = ruta_completa
image = PhotoImage(file=image_path)

# Reducir el tamaño de la imagen en 200 píxeles
image = image.subsample(2)  # 2 es el factor de escala

image_label = tk.Label(frame, image=image)
image_label.image = image
image_label.pack()

# Crear un marco para el formulario
form_frame = ttk.Frame(image_label)
form_frame.place(x=132, y=100)  # Ajusta la posición según tu preferencia

entry = tk.Entry(form_frame, font=("Arial", 16), justify="center", bg="black", fg="white")
entry.bind("<Return>", verificar_codigo)
entry.pack()

label_resultado = tk.Label(form_frame, text="")
label_resultado.pack()

root.mainloop()