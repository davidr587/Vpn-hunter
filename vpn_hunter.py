import requests
import time
import csv
import os
from datetime import datetime  # 
from dotenv import load_dotenv
# David_Ramos

# 1. Configuración de credenciales de forma SEGURA
load_dotenv()  # Esto carga la bóveda secreta (.env)
API_KEY = os.getenv('ABUSEIPDB_API_KEY') 
URL = 'https://api.abuseipdb.com/api/v2/check'

cabeceras = {
    'Accept': 'application/json',
    'Key': API_KEY
}

try:
    with open('ips.txt', 'r') as archivo:
        lista_ips = archivo.readlines()
except FileNotFoundError:
    print("[!] Error: No se encontro el archivo 'ips.txt'.")
    exit()

print("\n[+] Iniciando analisis de IPs y generando reporte...\n")

fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
nombre_archivo = f"reporte_soc_{fecha_hora}.csv"

with open(nombre_archivo, 'w', newline='', encoding='utf-8-sig') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    
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
            respuesta = requests.get(URL, headers=cabeceras, params=parametros)
            datos = respuesta.json()
            info = datos['data']

            if "Data Center" in str(info['usageType']) or info['isTor']:
                estado = "ALERTA: Posible VPN/Proxy o Tor"
            else:
                estado = "OK: Residencial/Estandar"
            print(f"[*] Analizando: {info['ipAddress']} --> {estado}")
            
            # GUARDAMOS LOS DATOS EN EL CSV
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
print(f"[+] Se ha generado el archivo '{nombre_archivo}' en tu carpeta.\n")
input("\nPresiona Enter para cerrar la ventana...")
