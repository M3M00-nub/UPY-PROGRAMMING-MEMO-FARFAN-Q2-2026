from PIL import Image


config = {}

file = open("config.txt", "r")
lines = file.readlines()
for line in lines:
    parameter, value = line.strip().split("=")
    config[parameter] = float(value) if "." in value else int(value)
file.close()

print(config)

archivo = open("mandelbrot.csv", "r")
lineas = archivo.readlines()
archivo.close()

lineas.pop(0)

max_iter= config["max_iter"]
ancho, alto = config["ancho"], config["alto"]


img = Image.new("HSV", (ancho,alto))

for linea in lineas:
    row, column, iterations = linea.strip().split(",")
    iterations = int(iterations)
    row = int(row)
    column = int(column)
    
    if iterations == max_iter:
        brillo = 40
    else:
        brillo = int((iterations/ max_iter) * 255)
        
    img.putpixel((column,row), (brillo,255,255))
    
img_rgb = img.convert("RGB")
img_rgb.save("mandelbrot.png")
print("DONE")


try:
    file = open("config.txt", "r")
except FileNotFoundError:
    print("No se encontró el archivo config.txt")
    exit()

try:
    archivo = open("mandelbrot.csv", "r")
except FileNotFoundError:
    print("No se encontró el archivo mandelbrot.csv")
    exit()

for linea in lineas:
    try:
        row, column, iterations = linea.strip().split(",")
        row = int(row)
        column = int(column)
        iterations = int(iterations)
    except ValueError:
        print("El archivo mandelbrot.csv está mal formado")
        exit()

    try:
        img.putpixel((column, row), brillo)
    except IndexError:
        print("El csv no es consistente con el ancho/alto de config.txt")
        exit()