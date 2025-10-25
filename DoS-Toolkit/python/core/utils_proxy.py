#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Proxy Utilities Module
Herramientas para proxy, rotación de IPs y anonimización
"""

import socket
import random
import requests
from typing import List, Optional


class ProxyUtils:
    """Utilidades para manejo de proxies"""

    # Proxies públicos gratuitos (ejemplo)
    FREE_PROXIES = [
        'http://10.10.1.10:3128',
        'http://proxy.example.com:8080',
    ]

    def __init__(self):
        """Inicializa utilidades de proxy"""
        self.proxies = []
        self.current_proxy_index = 0

    def add_proxy(self, proxy_url: str):
        """
        Añade un proxy a la lista
        
        Args:
            proxy_url: URL del proxy (ej: http://ip:puerto)
        """
        self.proxies.append(proxy_url)

    def add_proxies(self, proxy_list: List[str]):
        """
        Añade múltiples proxies
        
        Args:
            proxy_list: Lista de URLs de proxies
        """
        self.proxies.extend(proxy_list)

    def get_random_proxy(self) -> Optional[str]:
        """Retorna un proxy aleatorio de la lista"""
        if not self.proxies:
            return None
        return random.choice(self.proxies)

    def get_next_proxy(self) -> Optional[str]:
        """Retorna el siguiente proxy en rotación"""
        if not self.proxies:
            return None
        proxy = self.proxies[self.current_proxy_index]
        self.current_proxy_index = (self.current_proxy_index + 1) % len(self.proxies)
        return proxy

    def test_proxy(self, proxy_url: str, timeout: int = 5) -> bool:
        """
        Prueba si un proxy funciona
        
        Args:
            proxy_url: URL del proxy
            timeout: Timeout en segundos
            
        Returns:
            True si el proxy funciona, False en caso contrario
        """
        try:
            proxies = {'http': proxy_url, 'https': proxy_url}
            response = requests.get('http://httpbin.org/ip', 
                                   proxies=proxies, 
                                   timeout=timeout)
            return response.status_code == 200
        except:
            return False

    def get_working_proxies(self, timeout: int = 5) -> List[str]:
        """
        Filtra solo los proxies que funcionan
        
        Args:
            timeout: Timeout para pruebas
            
        Returns:
            Lista de proxies funcionales
        """
        working = []
        for proxy in self.proxies:
            if self.test_proxy(proxy, timeout):
                working.append(proxy)
        return working

    def clear_proxies(self):
        """Limpia la lista de proxies"""
        self.proxies.clear()
        self.current_proxy_index = 0


class IPRotation:
    """Rotación de direcciones IP"""

    def __init__(self):
        """Inicializa rotación de IPs"""
        self.ips = []

    def add_ip(self, ip: str):
        """Añade una IP a la lista"""
        self.ips.append(ip)

    def add_ips(self, ip_list: List[str]):
        """Añade múltiples IPs"""
        self.ips.extend(ip_list)

    def get_random_ip(self) -> Optional[str]:
        """Retorna una IP aleatoria"""
        if not self.ips:
            return None
        return random.choice(self.ips)

    def generate_random_ip(self) -> str:
        """Genera una IP aleatoria válida"""
        return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"

    def generate_random_ips(self, count: int = 10) -> List[str]:
        """Genera múltiples IPs aleatorias"""
        return [self.generate_random_ip() for _ in range(count)]


class UserAgentRotation:
    """Rotación de User-Agents"""

    USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.59',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.59',
    ]

    def __init__(self):
        """Inicializa rotación de User-Agents"""
        self.custom_agents = []

    def add_user_agent(self, agent: str):
        """Añade un User-Agent personalizado"""
        self.custom_agents.append(agent)

    def get_random_user_agent(self) -> str:
        """Retorna un User-Agent aleatorio"""
        all_agents = self.USER_AGENTS + self.custom_agents
        return random.choice(all_agents)

    def get_browser_user_agent(self, browser: str = 'chrome') -> str:
        """
        Retorna un User-Agent de un navegador específico
        
        Args:
            browser: 'chrome', 'firefox', 'safari', 'edge'
        """
        browser_agents = {
            'chrome': [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            ],
            'firefox': [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
                'Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
            ],
            'safari': [
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
            ],
            'edge': [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.59',
            ]
        }
        
        agents = browser_agents.get(browser.lower(), self.USER_AGENTS)
        return random.choice(agents)


class HeaderRotation:
    """Rotación de headers HTTP"""

    COMMON_HEADERS = {
        'Accept': [
            'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        ],
        'Accept-Language': [
            'en-US,en;q=0.9',
            'es-ES,es;q=0.9',
            'fr-FR,fr;q=0.9',
            'de-DE,de;q=0.9',
        ],
        'Accept-Encoding': [
            'gzip, deflate',
            'gzip, deflate, br',
            'gzip, deflate, br, zstd',
        ],
    }

    def __init__(self):
        """Inicializa rotación de headers"""
        pass

    def get_random_headers(self) -> dict:
        """Retorna un conjunto aleatorio de headers"""
        headers = {}
        for header, values in self.COMMON_HEADERS.items():
            headers[header] = random.choice(values)
        return headers

    def get_custom_headers(self, **kwargs) -> dict:
        """Retorna headers personalizados"""
        headers = self.get_random_headers()
        headers.update(kwargs)
        return headers
