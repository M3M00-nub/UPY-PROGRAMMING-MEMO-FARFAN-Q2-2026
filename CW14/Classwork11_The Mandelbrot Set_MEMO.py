config = {}

file = open("config.txt", "r")

for line in file:
    parameter, value = line.strip().split("=")
    config[parameter] = float(value) if "." in value else int(value)
file.close()

width, height, max_iter = config["ancho"], config["alto"], config["max_iter"]

output = open("mandelbrot.csv", "w")
output.write("row,column,iterations\n")

for row in range(height):
    for column in range(width):
        real = config["real_min"] + (column / width) * (config["real_max"] - config["real_min"])
        imag = config["imag_min"] + (row / height) * (config["imag_max"] - config["imag_min"])
        c = complex(real, imag)
        
        z = 0 + 0j
        iterations = 0
        
        while (abs(z) <=2) and (iterations < max_iter):
            z = z * z + c
            iterations += 1
        
        output.write(f"{row},{column},{iterations}\n")
        

try:
    file = open("config.txt", "r")
except FileNotFoundError:
    print("No se encontró el archivo config.txt")
    exit()

for line in file:
    line = line.strip()
    if line == "":
        continue
    try:
        parameter, value = line.split("=")
    except ValueError:
        print("El archivo config.txt está mal formado")
        file.close()
        exit()
    config[parameter] = float(value) if "." in value else int(value)

try:
    width = config["ancho"]
    height = config["alto"]
    max_iter = config["max_iter"]
    real_min = config["real_min"]
    real_max = config["real_max"]
    imag_min = config["imag_min"]
    imag_max = config["imag_max"]
except KeyError as falta:
    print(f"Falta el parámetro {falta} en config.txt")
    exit()

# Decimal error
if not isinstance(width, int) or not isinstance(height, int):
    print("Los parámetros 'ancho' y 'alto' deben ser números enteros")
    exit()