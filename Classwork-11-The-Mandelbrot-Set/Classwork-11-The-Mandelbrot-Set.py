configuracion = {}

archivo_config = open("config.txt", "r")
for linea in archivo_config:
    parametro, valor = linea.strip().split("=")
    configuracion[parametro] = float(valor) if "." in valor else int(valor)
archivo_config.close()

ancho = configuracion["ancho"]
alto = configuracion["alto"]
maximo_iteraciones = configuracion["maximo_iteraciones"]

archivo_salida = open("mandelbrot.csv", "w")
archivo_salida.write("fila,columna,iteraciones\n")

for fila in range(alto):
    for columna in range(ancho):
        parte_real = configuracion["real_minimo"] + (
            columna / ancho
        ) * (configuracion["real_maximo"] - configuracion["real_minimo"])

        parte_imaginaria = configuracion["imaginario_minimo"] + (
            fila / alto
        ) * (configuracion["imaginario_maximo"] - configuracion["imaginario_minimo"])

        numero_complejo = complex(parte_real, parte_imaginaria)

        z = 0 + 0j
        contador_iteraciones = 0

        while abs(z) <= 2 and contador_iteraciones < maximo_iteraciones:
            z = z * z + numero_complejo
            contador_iteraciones += 1

        archivo_salida.write(f"{fila},{columna},{contador_iteraciones}\n")

archivo_salida.close()