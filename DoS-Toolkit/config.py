#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuración Global del DoS-Toolkit
"""

# ============================================================================
# CONFIGURACIÓN DE ATAQUES
# ============================================================================

# Valores por defecto
DEFAULT_PORT = 80
DEFAULT_THREADS = 100
DEFAULT_DURATION = 60
DEFAULT_TIMEOUT = 5

# Límites de seguridad
MAX_THREADS = 10000
MAX_DURATION = 3600  # 1 hora
MIN_DURATION = 1
MIN_THREADS = 1

# ============================================================================
# CONFIGURACIÓN DE HTTP-FLOOD
# ============================================================================

HTTP_FLOOD_CONFIG = {
    'timeout': 5,
    'retries': 3,
    'user_agents': [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15',
        'Mozilla/5.0 (Android 11; Mobile; rv:89.0) Gecko/89.0 Firefox/89.0',
    ],
    'methods': ['GET', 'POST', 'HEAD'],
}

# ============================================================================
# CONFIGURACIÓN DE SYN-FLOOD
# ============================================================================

SYN_FLOOD_CONFIG = {
    'timeout': 2,
    'ttl': 255,
    'protocol': 6,  # TCP
    'flags': 0x02,  # SYN
}

# ============================================================================
# CONFIGURACIÓN DE SLOWLORIS
# ============================================================================

SLOWLORIS_CONFIG = {
    'timeout': 30,
    'min_delay': 5,
    'max_delay': 15,
    'header_delay': 10,
}

# ============================================================================
# CONFIGURACIÓN DE UDP-AMPLIFICATION
# ============================================================================

UDP_AMP_CONFIG = {
    'timeout': 2,
    'dns_servers': [
        '8.8.8.8',
        '8.8.4.4',
        '1.1.1.1',
        '1.0.0.1',
        '208.67.222.222',
        '208.67.220.220',
    ],
    'ntp_servers': [
        '0.pool.ntp.org',
        '1.pool.ntp.org',
        '2.pool.ntp.org',
        '3.pool.ntp.org',
    ],
}

# ============================================================================
# CONFIGURACIÓN DE PROXY
# ============================================================================

PROXY_CONFIG = {
    'timeout': 5,
    'test_url': 'http://httpbin.org/ip',
    'free_proxies': [
        'http://10.10.1.10:3128',
        'http://proxy.example.com:8080',
    ],
}

# ============================================================================
# CONFIGURACIÓN DE LOGGING
# ============================================================================

LOGGING_CONFIG = {
    'level': 'INFO',  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    'format': '[%(asctime)s] [%(levelname)s] %(message)s',
    'date_format': '%H:%M:%S',
    'file': 'dos_toolkit.log',
    'max_size': 10485760,  # 10MB
    'backup_count': 5,
}

# ============================================================================
# CONFIGURACIÓN DE COLORES (CLI)
# ============================================================================

COLORS = {
    'RESET': '\033[0m',
    'BOLD': '\033[1m',
    'RED': '\033[91m',
    'GREEN': '\033[92m',
    'YELLOW': '\033[93m',
    'BLUE': '\033[94m',
    'MAGENTA': '\033[95m',
    'CYAN': '\033[96m',
}

# ============================================================================
# MENSAJES
# ============================================================================

MESSAGES = {
    'welcome': '¡Bienvenido a DoS-Toolkit!',
    'select_language': 'Selecciona el lenguaje de ejecución:',
    'select_attack': 'Selecciona un tipo de ataque:',
    'enter_target': 'IP/Dominio objetivo:',
    'enter_port': 'Puerto (default 80):',
    'enter_threads': 'Número de threads (default 100):',
    'enter_duration': 'Duración en segundos (default 60):',
    'confirm_attack': '¿Continuar?',
    'attack_started': 'Ataque iniciado...',
    'attack_completed': 'Ataque completado',
    'error': 'Error',
    'warning': 'Advertencia',
    'info': 'Información',
}

# ============================================================================
# VALIDACIONES
# ============================================================================

def validate_port(port):
    """Valida que el puerto sea válido"""
    try:
        port = int(port)
        return 1 <= port <= 65535
    except:
        return False

def validate_threads(threads):
    """Valida que el número de threads sea válido"""
    try:
        threads = int(threads)
        return MIN_THREADS <= threads <= MAX_THREADS
    except:
        return False

def validate_duration(duration):
    """Valida que la duración sea válida"""
    try:
        duration = int(duration)
        return MIN_DURATION <= duration <= MAX_DURATION
    except:
        return False

def validate_target(target):
    """Valida que el objetivo sea válido"""
    if not target or len(target) < 3:
        return False
    return True

# ============================================================================
# FUNCIONES DE UTILIDAD
# ============================================================================

def get_default_config(attack_type):
    """Retorna configuración por defecto para un tipo de ataque"""
    configs = {
        'http_flood': HTTP_FLOOD_CONFIG,
        'syn_flood': SYN_FLOOD_CONFIG,
        'slowloris': SLOWLORIS_CONFIG,
        'udp_amplification': UDP_AMP_CONFIG,
    }
    return configs.get(attack_type, {})

def get_attack_info(attack_type):
    """Retorna información sobre un tipo de ataque"""
    info = {
        'http_flood': {
            'name': 'HTTP-Flood',
            'description': 'Envía múltiples solicitudes HTTP al objetivo',
            'speed': 'Muy rápido',
            'effectiveness': 'Alta',
            'requirements': 'Ninguno especial',
        },
        'syn_flood': {
            'name': 'SYN-Flood',
            'description': 'Inunda con paquetes SYN malformados',
            'speed': 'Muy rápido',
            'effectiveness': 'Alta',
            'requirements': 'Permisos de administrador',
        },
        'slowloris': {
            'name': 'Slowloris',
            'description': 'Mantiene conexiones HTTP abiertas indefinidamente',
            'speed': 'Lento (intencional)',
            'effectiveness': 'Alta',
            'requirements': 'Ninguno especial',
        },
        'udp_amplification': {
            'name': 'UDP-Amplification',
            'description': 'Explota servidores DNS/NTP para amplificar tráfico',
            'speed': 'Muy rápido',
            'effectiveness': 'Muy alta',
            'requirements': 'Acceso a servidores amplificadores',
        },
    }
    return info.get(attack_type, {})

# ============================================================================
# CONFIGURACIÓN DE SEGURIDAD
# ============================================================================

SECURITY_CONFIG = {
    'require_confirmation': True,
    'log_attacks': True,
    'rate_limit': True,
    'max_requests_per_second': 10000,
    'enable_warnings': True,
}

# ============================================================================
# CONFIGURACIÓN DE LENGUAJES
# ============================================================================

LANGUAGES_CONFIG = {
    'python': {
        'name': 'Python',
        'path': 'python',
        'cmd': 'python',
        'version': '3.6+',
        'available': True,
    },
    'go': {
        'name': 'Go',
        'path': 'go',
        'cmd': 'go',
        'version': '1.16+',
        'available': True,
    },
    'rust': {
        'name': 'Rust',
        'path': 'rust',
        'cmd': 'cargo',
        'version': '1.50+',
        'available': True,
    },
    'c_cpp': {
        'name': 'C/C++',
        'path': 'c_cpp',
        'cmd': 'gcc',
        'version': 'GCC 9+',
        'available': True,
    },
}
