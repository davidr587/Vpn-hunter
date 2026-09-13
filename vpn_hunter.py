import requests
import time
import csv
import os
from dotenv import load_dotenv

# 1. Configuración de credenciales de forma SEGURA
load_dotenv()  # Esto carga la bóveda secreta (.env)
API_KEY = os.getenv('ABUSEIPDB_API_KEY') # Extraemos la llave sin mostrarla en el código
URL = 'https://api.abuseipdb.com/api/v2/check'

cabeceras = {
    'Accept': 'application/json',
    'Key': API_KEY
}


# 2. Intentamos abrir el archivo de IPs sospechosas
try:
    with open('ips.txt', 'r') as archivo:
        lista_ips = archivo.readlines()
except FileNotFoundError:
    print("[!] Error: No se encontro el archivo 'ips.txt'.")
    exit()

print("\n[+] Iniciando caceria de IPs y generando reporte corporativo...\n")

# 3. ¡NUEVO! ABRIMOS EL ARCHIVO CSV PARA ESCRIBIR
# Usamos 'w' de write (escribir) y codificación utf-8 para no tener problemas con acentos
with open('reporte_soc.csv', 'w', newline='', encoding='utf-8') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    
    # Escribimos la fila de encabezados (Títulos de las columnas)
    escritor_csv.writerow(['IP Analizada', 'País', 'ISP', 'Tipo de Red', '¿Es Tor?', 'Prob. Abuso (%)', 'Estado/Alerta'])

    # 4. Bucle por cada IP
    for ip_cruda in lista_ips:
        ip = ip_cruda.strip()
        
        if not ip:
            continue

        parametros = {
            'ipAddress': ip,
            'maxAgeInDays': '90'
        }

        try:
            # Hacemos la consulta
            respuesta = requests.get(URL, headers=cabeceras, params=parametros)
            datos = respuesta.json()
            info = datos['data']

            # Lógica SOC (Decidimos la alerta)
            if "Data Center" in str(info['usageType']) or info['isTor']:
                estado = "ALERTA: Posible VPN/Proxy o Tor"
            else:
                estado = "OK: Residencial/Estandar"

            # Imprimimos en pantalla para que el analista vea el progreso
            print(f"[*] Analizando: {info['ipAddress']} --> {estado}")
            
            # ¡NUEVO! GUARDAMOS LOS DATOS EN EL CSV
            es_tor = 'Sí' if info['isTor'] else 'No'
            escritor_csv.writerow([
                info['ipAddress'], 
                info['countryCode'], 
                info['isp'], 
                info['usageType'], 
                es_tor, 
                info['abuseConfidenceScore'], 
                estado
            ])
            
            # Pausa obligatoria
            time.sleep(1)
            
        except Exception as e:
            print(f"[!] Error consultando la IP {ip}: {e}")

print("\n[+] Analisis completado con exito.")
print("[+] Se ha generado el archivo 'reporte_soc.csv' en tu carpeta.\n")