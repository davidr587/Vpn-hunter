# 🛡️ SOC Threat Intelligence Automator (VPN/Proxy Hunter)

## 📌 Descripción del Proyecto
Herramienta de automatización desarrollada en Python para el triaje rápido de direcciones IP sospechosas. Diseñada para equipos de **Blue Team y Analistas SOC**, este script automatiza las consultas de inteligencia de amenazas (CTI) para identificar si el tráfico proviene de nodos Tor, VPNs comerciales o Centros de Datos utilizados con fines maliciosos.

## 🚀 Características Principales
* **Análisis por Lotes (Batch Processing):** Capacidad de procesar listas masivas de IPs extraídas de logs de firewalls o SIEMs.
* **Integración API:** Conexión directa con la API v2 de [AbuseIPDB](https://www.abuseipdb.com/).
* **Exportación de Evidencia:** Generación automática de reportes corporativos en formato `.csv` listos para ser ingeridos por otras herramientas o presentados a gerencia.
* **Seguridad (OPSEC):** Gestión segura de credenciales mediante variables de entorno (`.env`).

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.x
* **Librerías:** `requests`, `csv`, `python-dotenv`, `time`
* **Arquitectura:** Diseño modular y manejo de excepciones (Error Handling) para evitar interrupciones por límites de tasa (Rate Limiting).
* 
## 🔐 Configuración Previa
Para que la herramienta funcione en tu entorno local, necesitas tu propia clave de API gratuita:

1. Regístrate en [AbuseIPDB](https://www.abuseipdb.com/) y genera una API Key.
2. Crea un archivo llamado `.env` en la raíz de este proyecto.
3. Añade la siguiente línea reemplazando el valor con tu clave real:
   ```text
   ABUSEIPDB_API_KEY=tu_clave_api_aqui


## 🚀 Instalación y Uso

1. Descarga este repositorio y abre tu terminal en la carpeta del proyecto.
2. Crea un entorno virtual ejecutando el comando: `python -m venv venv`
3. Actívalo ejecutando venv\Scripts\activate (en Windows) o source venv/bin/activate (en Mac/Linux).
4. Instala las dependencias necesarias usando: `pip install requests python-dotenv`
5. Asegúrate de tener las IPs a analizar en el archivo `ips.txt` y tu credencial en el `.env`.
6. Inicia la herramienta ejecutando: `python vpn_hunter.py`

## Ejemplo de reporte generado
![Ejemplo de Reporte SOC Generado](ejemplo_reporte_soc.png)
