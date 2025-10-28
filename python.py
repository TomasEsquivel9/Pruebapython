#  import random 
#  numero = random.randint (1,6) 
#  print (numero)
import subprocess
import platform
import time
archivo_salida = "resultado.txt"
#hosts = "host"
hosts = ["google.com","8.8.8.8","cloudflare.com","1.1.1.1"]
param = "-n" if platform.system().lower() == "windows" else "-c"
total_tiempo = 0 
cantidad = 0
Abrimos el archivo para escribir los resultados
with open(archivo_salida, "w") as file:
    file.write("Resultados del Ping:\n")
    file.write("====================\n\n")

    for host in hosts:
        print(f"Haciendo ping a {host}...")
        inicio = time.time()  tiempo de inicio

        Ejecutar comando ping
        comando = ["ping", param, "4", host]
        resultado = subprocess.run(comando, capture_output=True, text=True)

        fin = time.time()  tiempo de fin
        duracion = fin - inicio
        total_tiempo += duracion
        cantidad += 1

        Guardar resultado en archivo
        file.write(f"Host: {host}\n")
        file.write(resultado.stdout)
        file.write(f"Tiempo total del ping: {duracion:.2f} segundos\n")
        file.write("=" * 40 + "\n\n")

        print(f"Ping a {host} completado en {duracion:.2f} segundos\n")

Calcular promedio
promedio = total_tiempo / cantidad if cantidad > 0 else 0

print("===================================")
print(f"Tiempo promedio por host: {promedio:.2f} segundos")
print(f"Resultados guardados en: {archivo_salida}")
print("===================================") 
