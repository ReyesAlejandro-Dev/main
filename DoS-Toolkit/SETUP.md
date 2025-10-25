# Guía de Instalación - DoS-Toolkit

Instrucciones completas para instalar y configurar DoS-Toolkit en diferentes sistemas operativos.

## 📋 Requisitos Previos

### Windows
- Python 3.6+
- Git (opcional)
- Visual Studio Build Tools (para C/C++)

### Linux
- Python 3.6+
- GCC/Clang
- Make
- Git (opcional)

### macOS
- Python 3.6+
- Xcode Command Line Tools
- Homebrew (opcional)

---

## 🐍 Instalación de Python

### Windows

1. **Descargar Python**
   - Ir a https://www.python.org/downloads/
   - Descargar Python 3.9+ (recomendado)

2. **Instalar Python**
   - Ejecutar el instalador
   - ✅ Marcar "Add Python to PATH"
   - Completar instalación

3. **Verificar instalación**
   ```bash
   python --version
   pip --version
   ```

### Linux (Ubuntu/Debian)

```bash
# Actualizar paquetes
sudo apt update
sudo apt upgrade -y

# Instalar Python
sudo apt install python3 python3-pip python3-venv -y

# Verificar
python3 --version
pip3 --version
```

### Linux (Fedora/RHEL)

```bash
# Instalar Python
sudo dnf install python3 python3-pip -y

# Verificar
python3 --version
pip3 --version
```

### macOS

```bash
# Usando Homebrew
brew install python3

# O descargar desde https://www.python.org/downloads/

# Verificar
python3 --version
pip3 --version
```

---

## 📦 Instalación de Dependencias

### Python

```bash
# Navegar al directorio del proyecto
cd DoS-Toolkit

# Instalar dependencias
pip install -r python/requirements.txt

# O manualmente
pip install requests urllib3
```

### Go

#### Windows
1. Descargar desde https://golang.org/dl/
2. Ejecutar instalador
3. Verificar: `go version`

#### Linux
```bash
# Ubuntu/Debian
sudo apt install golang-go -y

# Fedora
sudo dnf install golang -y

# Verificar
go version
```

#### macOS
```bash
brew install go

# Verificar
go version
```

### Rust

#### Windows
1. Descargar desde https://rustup.rs/
2. Ejecutar instalador
3. Verificar: `rustc --version`

#### Linux/macOS
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Verificar
rustc --version
cargo --version
```

### C/C++

#### Windows
- Instalar Visual Studio Build Tools
- O MinGW-w64

#### Linux (Ubuntu/Debian)
```bash
sudo apt install build-essential gcc g++ make -y
```

#### Linux (Fedora)
```bash
sudo dnf install gcc gcc-c++ make -y
```

#### macOS
```bash
xcode-select --install
```

---

## 🚀 Instalación de DoS-Toolkit

### Opción 1: Descargar ZIP

1. Descargar el proyecto como ZIP
2. Extraer en la ubicación deseada
3. Abrir terminal en el directorio

### Opción 2: Clonar con Git

```bash
git clone https://github.com/usuario/DoS-Toolkit.git
cd DoS-Toolkit
```

### Opción 3: Descargar Manual

1. Crear carpeta: `DoS-Toolkit`
2. Copiar todos los archivos
3. Abrir terminal en el directorio

---

## ✅ Verificación de Instalación

### Verificar Python

```bash
# Verificar instalación
python --version

# Verificar módulos
python -c "import requests; print('requests OK')"
python -c "import urllib3; print('urllib3 OK')"
```

### Verificar Go

```bash
go version
go env
```

### Verificar Rust

```bash
rustc --version
cargo --version
```

### Verificar C/C++

```bash
# Windows
gcc --version

# Linux/macOS
gcc --version
make --version
```

---

## 🔧 Configuración Inicial

### 1. Permisos de Ejecución (Linux/macOS)

```bash
# Hacer ejecutable el CLI
chmod +x cli.py

# Hacer ejecutables los scripts
chmod +x python/attacks.py
chmod +x go/attacks.go
```

### 2. Variables de Entorno (Opcional)

#### Windows (PowerShell)
```powershell
$env:DOSTOOLKIT_HOME = "C:\ruta\a\DoS-Toolkit"
$env:PYTHONPATH = "$env:DOSTOOLKIT_HOME"
```

#### Linux/macOS (Bash)
```bash
export DOSTOOLKIT_HOME="/ruta/a/DoS-Toolkit"
export PYTHONPATH="$DOSTOOLKIT_HOME"
```

### 3. Alias (Opcional)

#### Linux/macOS
```bash
# Agregar al ~/.bashrc o ~/.zshrc
alias dostoolkit="python $DOSTOOLKIT_HOME/cli.py"

# Recargar
source ~/.bashrc
```

---

## 🧪 Prueba de Funcionamiento

### Prueba 1: CLI Principal

```bash
# Ejecutar CLI
python cli.py

# Debería mostrar el menú principal
```

### Prueba 2: Ataque HTTP-Flood (Prueba Local)

```bash
# Crear servidor de prueba (en otra terminal)
python -m http.server 8000

# Ejecutar ataque
python python/attacks.py --attack http_flood --target localhost --port 8000 --threads 5 --duration 10
```

### Prueba 3: Verificar Módulos

```bash
# Python
python -c "from python.core.http_flood import HTTPFlood; print('HTTPFlood OK')"
python -c "from python.core.syn_flood import SYNFlood; print('SYNFlood OK')"
python -c "from python.core.slowloris import Slowloris; print('Slowloris OK')"
python -c "from python.core.udp_amp import UDPAmplification; print('UDPAmplification OK')"
```

---

## 🐛 Solución de Problemas

### Error: "python: command not found"

**Solución:**
```bash
# Usar python3 en lugar de python
python3 cli.py

# O crear alias
alias python=python3
```

### Error: "ModuleNotFoundError: No module named 'requests'"

**Solución:**
```bash
# Instalar dependencias
pip install -r python/requirements.txt

# O instalar manualmente
pip install requests urllib3
```

### Error: "Permission denied" (Linux/macOS)

**Solución:**
```bash
# Dar permisos de ejecución
chmod +x cli.py
chmod +x python/attacks.py

# Ejecutar con python
python cli.py
```

### Error: "SYN-Flood requiere permisos de administrador"

**Solución:**
```bash
# Linux
sudo python attacks.py --attack syn_flood ...

# Windows (ejecutar como administrador)
# Abrir PowerShell como administrador y ejecutar
```

### Error: "go: command not found"

**Solución:**
```bash
# Verificar instalación
go version

# Si no está instalado, descargar desde https://golang.org/dl/
```

### Error: "cargo: command not found"

**Solución:**
```bash
# Instalar Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Recargar shell
source $HOME/.cargo/env
```

---

## 📝 Configuración Avanzada

### Configurar Proxies

Editar `config.py`:
```python
PROXY_CONFIG = {
    'timeout': 5,
    'test_url': 'http://httpbin.org/ip',
    'free_proxies': [
        'http://proxy1.com:8080',
        'http://proxy2.com:8080',
    ],
}
```

### Configurar Servidores DNS

Editar `config.py`:
```python
UDP_AMP_CONFIG = {
    'dns_servers': [
        '8.8.8.8',
        '1.1.1.1',
        'tu_servidor_dns',
    ],
}
```

### Configurar Logging

Editar `config.py`:
```python
LOGGING_CONFIG = {
    'level': 'DEBUG',  # Más detallado
    'file': 'dos_toolkit.log',
}
```

---

## 🔐 Configuración de Seguridad

### 1. Firewall

Asegúrate de que el firewall permita:
- Conexiones salientes (para ataques)
- Puerto 80, 443, 53, 123 (según sea necesario)

### 2. Antivirus

Algunos antivirus pueden bloquear el toolkit:
- Agregar a excepciones
- O deshabilitar temporalmente para pruebas

### 3. VPN (Recomendado)

Para mayor privacidad:
```bash
# Conectar a VPN antes de ejecutar
# Luego ejecutar el toolkit
python cli.py
```

---

## 📚 Próximos Pasos

1. **Leer documentación**: Ver [README.md](README.md)
2. **Ver ejemplos**: Ver [EJEMPLOS.md](EJEMPLOS.md)
3. **Configurar**: Editar [config.py](config.py)
4. **Ejecutar**: `python cli.py`

---

## 🆘 Soporte

Si encuentras problemas:

1. **Verificar requisitos**: Asegúrate de tener Python 3.6+
2. **Instalar dependencias**: `pip install -r python/requirements.txt`
3. **Revisar logs**: Ver `dos_toolkit.log`
4. **Consultar documentación**: Ver [README.md](README.md)

---

## ✨ ¡Listo!

Ahora puedes ejecutar:
```bash
python cli.py
```

¡Disfruta del DoS-Toolkit!
