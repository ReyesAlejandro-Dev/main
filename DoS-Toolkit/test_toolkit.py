#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Pruebas - DoS-Toolkit
Verifica que todos los módulos estén correctamente instalados
"""

import sys
import os
from pathlib import Path

# Agregar ruta del proyecto
sys.path.insert(0, str(Path(__file__).parent))

class ToolkitTester:
    """Prueba la instalación del toolkit"""
    
    def __init__(self):
        self.tests_passed = 0
        self.tests_failed = 0
        self.base_path = Path(__file__).parent

    def print_header(self, text):
        """Imprime encabezado"""
        print(f"\n{'='*60}")
        print(f"  {text}")
        print(f"{'='*60}\n")

    def print_test(self, name, status, message=""):
        """Imprime resultado de prueba"""
        symbol = "✓" if status else "✗"
        color = "\033[92m" if status else "\033[91m"
        reset = "\033[0m"
        
        print(f"{color}[{symbol}]{reset} {name}")
        if message:
            print(f"    {message}")
        
        if status:
            self.tests_passed += 1
        else:
            self.tests_failed += 1

    def test_python_version(self):
        """Prueba versión de Python"""
        version = sys.version_info
        required = (3, 6)
        
        if version >= required:
            self.print_test(
                "Versión de Python",
                True,
                f"Python {version.major}.{version.minor}.{version.micro}"
            )
        else:
            self.print_test(
                "Versión de Python",
                False,
                f"Se requiere Python 3.6+, tienes {version.major}.{version.minor}"
            )

    def test_imports(self):
        """Prueba importaciones de módulos"""
        self.print_header("Pruebas de Importación")
        
        modules = [
            ('config', 'Configuración'),
            ('python.core.http_flood', 'HTTP-Flood'),
            ('python.core.syn_flood', 'SYN-Flood'),
            ('python.core.slowloris', 'Slowloris'),
            ('python.core.udp_amp', 'UDP-Amplification'),
            ('python.core.utils_proxy', 'Proxy Utils'),
        ]
        
        for module, name in modules:
            try:
                __import__(module)
                self.print_test(f"Módulo: {name}", True)
            except ImportError as e:
                self.print_test(f"Módulo: {name}", False, str(e))
            except Exception as e:
                self.print_test(f"Módulo: {name}", False, str(e))

    def test_dependencies(self):
        """Prueba dependencias externas"""
        self.print_header("Pruebas de Dependencias")
        
        dependencies = [
            ('requests', 'Requests'),
            ('urllib3', 'urllib3'),
        ]
        
        for module, name in dependencies:
            try:
                __import__(module)
                self.print_test(f"Dependencia: {name}", True)
            except ImportError:
                self.print_test(f"Dependencia: {name}", False, 
                              f"Instala con: pip install {module}")

    def test_file_structure(self):
        """Prueba estructura de archivos"""
        self.print_header("Pruebas de Estructura")
        
        files = [
            ('cli.py', 'CLI Principal'),
            ('config.py', 'Configuración'),
            ('python/attacks.py', 'Ataques Python'),
            ('python/core/http_flood.py', 'HTTP-Flood Core'),
            ('python/core/syn_flood.py', 'SYN-Flood Core'),
            ('python/core/slowloris.py', 'Slowloris Core'),
            ('python/core/udp_amp.py', 'UDP-Amplification Core'),
            ('python/core/utils_proxy.py', 'Proxy Utils Core'),
            ('python/requirements.txt', 'Requisitos Python'),
            ('README.md', 'README Principal'),
        ]
        
        for file_path, name in files:
            full_path = self.base_path / file_path
            exists = full_path.exists()
            self.print_test(f"Archivo: {name}", exists, str(file_path))

    def test_classes(self):
        """Prueba que las clases se puedan instanciar"""
        self.print_header("Pruebas de Clases")
        
        try:
            from python.core.http_flood import HTTPFlood
            flood = HTTPFlood('localhost', 80)
            self.print_test("Clase: HTTPFlood", True)
        except Exception as e:
            self.print_test("Clase: HTTPFlood", False, str(e))
        
        try:
            from python.core.syn_flood import SYNFlood
            syn = SYNFlood('localhost', 443)
            self.print_test("Clase: SYNFlood", True)
        except Exception as e:
            self.print_test("Clase: SYNFlood", False, str(e))
        
        try:
            from python.core.slowloris import Slowloris
            slow = Slowloris('localhost', 80)
            self.print_test("Clase: Slowloris", True)
        except Exception as e:
            self.print_test("Clase: Slowloris", False, str(e))
        
        try:
            from python.core.udp_amp import UDPAmplification
            udp = UDPAmplification('localhost', 53)
            self.print_test("Clase: UDPAmplification", True)
        except Exception as e:
            self.print_test("Clase: UDPAmplification", False, str(e))
        
        try:
            from python.core.utils_proxy import ProxyUtils, IPRotation, UserAgentRotation
            proxy = ProxyUtils()
            ip_rot = IPRotation()
            ua_rot = UserAgentRotation()
            self.print_test("Clase: Proxy Utils", True)
        except Exception as e:
            self.print_test("Clase: Proxy Utils", False, str(e))

    def test_config(self):
        """Prueba configuración"""
        self.print_header("Pruebas de Configuración")
        
        try:
            import config
            
            # Verificar constantes
            assert hasattr(config, 'DEFAULT_PORT')
            assert hasattr(config, 'DEFAULT_THREADS')
            assert hasattr(config, 'DEFAULT_DURATION')
            assert hasattr(config, 'HTTP_FLOOD_CONFIG')
            assert hasattr(config, 'SYN_FLOOD_CONFIG')
            assert hasattr(config, 'SLOWLORIS_CONFIG')
            assert hasattr(config, 'UDP_AMP_CONFIG')
            
            self.print_test("Configuración Global", True)
        except Exception as e:
            self.print_test("Configuración Global", False, str(e))

    def test_cli(self):
        """Prueba CLI"""
        self.print_header("Pruebas de CLI")
        
        try:
            from cli import DoSToolkitCLI
            cli = DoSToolkitCLI()
            
            assert hasattr(cli, 'languages')
            assert hasattr(cli, 'attacks')
            assert hasattr(cli, 'run')
            
            self.print_test("CLI Principal", True)
        except Exception as e:
            self.print_test("CLI Principal", False, str(e))

    def test_methods(self):
        """Prueba métodos de clases"""
        self.print_header("Pruebas de Métodos")
        
        try:
            from python.core.http_flood import HTTPFlood
            flood = HTTPFlood('localhost', 80)
            
            assert hasattr(flood, 'send_request')
            assert hasattr(flood, 'send_post_request')
            assert callable(flood.send_request)
            
            self.print_test("Métodos: HTTPFlood", True)
        except Exception as e:
            self.print_test("Métodos: HTTPFlood", False, str(e))
        
        try:
            from python.core.utils_proxy import ProxyUtils
            proxy = ProxyUtils()
            
            assert hasattr(proxy, 'add_proxy')
            assert hasattr(proxy, 'get_random_proxy')
            assert hasattr(proxy, 'test_proxy')
            
            self.print_test("Métodos: ProxyUtils", True)
        except Exception as e:
            self.print_test("Métodos: ProxyUtils", False, str(e))

    def print_summary(self):
        """Imprime resumen de pruebas"""
        self.print_header("Resumen de Pruebas")
        
        total = self.tests_passed + self.tests_failed
        percentage = (self.tests_passed / total * 100) if total > 0 else 0
        
        print(f"Total de pruebas: {total}")
        print(f"Pruebas exitosas: \033[92m{self.tests_passed}\033[0m")
        print(f"Pruebas fallidas: \033[91m{self.tests_failed}\033[0m")
        print(f"Porcentaje de éxito: {percentage:.1f}%\n")
        
        if self.tests_failed == 0:
            print("\033[92m✓ ¡Todas las pruebas pasaron!\033[0m")
            print("El toolkit está listo para usar.\n")
            return True
        else:
            print("\033[91m✗ Algunas pruebas fallaron.\033[0m")
            print("Por favor, revisa los errores anteriores.\n")
            return False

    def run_all_tests(self):
        """Ejecuta todas las pruebas"""
        print("\n" + "="*60)
        print("  DoS-Toolkit - Suite de Pruebas")
        print("="*60)
        
        self.test_python_version()
        self.test_file_structure()
        self.test_imports()
        self.test_dependencies()
        self.test_classes()
        self.test_config()
        self.test_cli()
        self.test_methods()
        
        success = self.print_summary()
        return success


def main():
    """Punto de entrada principal"""
    try:
        tester = ToolkitTester()
        success = tester.run_all_tests()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n[!] Pruebas interrumpidas por el usuario\n")
        sys.exit(1)
    except Exception as e:
        print(f"\n[!] Error durante las pruebas: {e}\n")
        sys.exit(1)


if __name__ == '__main__':
    main()
