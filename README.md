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

## ⚙️ Uso
1. Colocar las IPs a investigar en el archivo `ips.txt` (una por línea).
2. Ejecutar el script: `python vpn_hunter.py`
3. El sistema evaluará el *Usage Type*, nodo Tor y *Confidence Score*, generando alertas en consola y exportando el análisis final al archivo `reporte_soc.csv`.

> *"La automatización es clave en la respuesta a incidentes. Esta herramienta reduce el tiempo de triaje inicial de minutos a segundos."*