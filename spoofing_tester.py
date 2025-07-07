#!/usr/bin/env python3
"""
Advanced OSS Spoofing Tester
Comprehensive testing and validation tool for the spoofing framework
"""

import os
import sys
import json
import time
import platform
import subprocess
import hashlib
from typing import Dict, List, Any, Tuple
from advanced_oss_spoofer import AdvancedOSSSpoofing, SystemProfile

class SpoofingTester:
    """Comprehensive testing suite for spoofing effectiveness"""
    
    def __init__(self):
        self.spoofer = AdvancedOSSSpoofing()
        self.test_results = {}
        self.baseline_info = {}
        
    def run_comprehensive_test(self, profile: SystemProfile) -> Dict[str, Any]:
        """Run comprehensive spoofing test suite"""
        print("=== Starting Comprehensive Spoofing Test ===")
        
        # Capture baseline
        print("1. Capturing baseline system information...")
        self.baseline_info = self.capture_system_fingerprint()
        
        # Start spoofing
        print("2. Activating spoofing...")
        spoof_success = self.spoofer.start_spoofing(profile)
        
        if not spoof_success:
            return {"error": "Failed to start spoofing"}
        
        # Wait for spoofing to take effect
        time.sleep(2)
        
        # Run tests
        print("3. Running detection tests...")
        test_results = {
            "os_detection": self.test_os_detection(profile),
            "hardware_detection": self.test_hardware_detection(profile),
            "network_detection": self.test_network_detection(profile),
            "registry_detection": self.test_registry_detection(profile) if platform.system() == "Windows" else None,
            "file_system_detection": self.test_file_system_detection(profile),
            "vm_detection": self.test_vm_detection(),
            "fingerprinting_resistance": self.test_fingerprinting_resistance(profile),
            "persistence_test": self.test_spoofing_persistence(profile)
        }
        
        # Stop spoofing
        print("4. Stopping spoofing and restoring...")
        restore_success = self.spoofer.stop_spoofing()
        
        # Verify restoration
        print("5. Verifying restoration...")
        restoration_test = self.test_restoration()
        
        return {
            "spoof_activation": spoof_success,
            "test_results": test_results,
            "restoration": restore_success,
            "restoration_verification": restoration_test,
            "overall_score": self.calculate_overall_score(test_results)
        }
    
    def capture_system_fingerprint(self) -> Dict[str, Any]:
        """Capture comprehensive system fingerprint"""
        fingerprint = {}
        
        try:
            # Basic system info
            fingerprint["platform"] = platform.platform()
            fingerprint["system"] = platform.system()
            fingerprint["release"] = platform.release()
            fingerprint["version"] = platform.version()
            fingerprint["machine"] = platform.machine()
            fingerprint["processor"] = platform.processor()
            fingerprint["hostname"] = platform.node()
            
            # Network interfaces
            if platform.system() == "Windows":
                result = subprocess.run(["ipconfig", "/all"], capture_output=True, text=True)
                fingerprint["network"] = result.stdout
            else:
                result = subprocess.run(["ifconfig"], capture_output=True, text=True)
                fingerprint["network"] = result.stdout
            
            # System-specific information
            if platform.system() == "Windows":
                fingerprint.update(self._capture_windows_fingerprint())
            elif platform.system() == "Darwin":
                fingerprint.update(self._capture_macos_fingerprint())
            elif platform.system() == "Linux":
                fingerprint.update(self._capture_linux_fingerprint())
            
        except Exception as e:
            fingerprint["error"] = str(e)
        
        return fingerprint
    
    def _capture_windows_fingerprint(self) -> Dict[str, Any]:
        """Capture Windows-specific fingerprint"""
        fingerprint = {}
        
        try:
            # Registry information
            import winreg
            
            # Machine GUID
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 
                              r"SOFTWARE\Microsoft\Cryptography") as key:
                fingerprint["machine_guid"] = winreg.QueryValueEx(key, "MachineGuid")[0]
            
            # Computer name
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 
                              r"SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName") as key:
                fingerprint["computer_name"] = winreg.QueryValueEx(key, "ComputerName")[0]
            
            # WMI information
            import wmi
            c = wmi.WMI()
            
            for computer in c.Win32_ComputerSystem():
                fingerprint["wmi_computer"] = {
                    "Name": computer.Name,
                    "Manufacturer": computer.Manufacturer,
                    "Model": computer.Model
                }
                break
            
        except Exception as e:
            fingerprint["windows_error"] = str(e)
        
        return fingerprint
    
    def _capture_macos_fingerprint(self) -> Dict[str, Any]:
        """Capture macOS-specific fingerprint"""
        fingerprint = {}
        
        try:
            # System profiler
            result = subprocess.run(["system_profiler", "SPHardwareDataType", "-json"], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                fingerprint["system_profiler"] = json.loads(result.stdout)
            
            # Platform UUID
            result = subprocess.run(["ioreg", "-rd1", "-c", "IOPlatformExpertDevice"], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                fingerprint["platform_uuid"] = result.stdout
            
        except Exception as e:
            fingerprint["macos_error"] = str(e)
        
        return fingerprint
    
    def _capture_linux_fingerprint(self) -> Dict[str, Any]:
        """Capture Linux-specific fingerprint"""
        fingerprint = {}
        
        try:
            # DMI information
            dmi_files = [
                "/sys/class/dmi/id/product_name",
                "/sys/class/dmi/id/product_uuid",
                "/sys/class/dmi/id/board_vendor",
                "/sys/class/dmi/id/bios_version"
            ]
            
            fingerprint["dmi"] = {}
            for dmi_file in dmi_files:
                try:
                    with open(dmi_file, 'r') as f:
                        key = os.path.basename(dmi_file)
                        fingerprint["dmi"][key] = f.read().strip()
                except:
                    pass
            
            # Machine ID
            try:
                with open("/etc/machine-id", 'r') as f:
                    fingerprint["machine_id"] = f.read().strip()
            except:
                pass
            
        except Exception as e:
            fingerprint["linux_error"] = str(e)
        
        return fingerprint
    
    def test_os_detection(self, profile: SystemProfile) -> Dict[str, bool]:
        """Test OS detection spoofing"""
        results = {}
        
        # Test platform detection
        current_platform = platform.platform()
        results["platform_spoofed"] = profile.os_name.lower() in current_platform.lower()
        
        # Test system detection
        current_system = platform.system()
        expected_system = self._get_expected_system(profile.os_name)
        results["system_spoofed"] = current_system.lower() == expected_system.lower()
        
        # Test version detection
        current_version = platform.version()
        results["version_spoofed"] = profile.os_version in current_version
        
        return results
    
    def test_hardware_detection(self, profile: SystemProfile) -> Dict[str, bool]:
        """Test hardware detection spoofing"""
        results = {}
        
        # Test processor detection
        current_processor = platform.processor()
        results["processor_spoofed"] = profile.processor.lower() in current_processor.lower()
        
        # Test machine architecture
        current_machine = platform.machine()
        results["architecture_spoofed"] = profile.architecture in current_machine
        
        # Test hostname
        current_hostname = platform.node()
        results["hostname_spoofed"] = profile.hostname == current_hostname
        
        return results
    
    def test_network_detection(self, profile: SystemProfile) -> Dict[str, bool]:
        """Test network interface spoofing"""
        results = {}
        
        try:
            if platform.system() == "Windows":
                result = subprocess.run(["getmac"], capture_output=True, text=True)
                network_info = result.stdout
            else:
                result = subprocess.run(["ifconfig"], capture_output=True, text=True)
                network_info = result.stdout
            
            # Check if spoofed MAC addresses are present
            spoofed_macs_found = 0
            for mac in profile.mac_addresses:
                if mac.replace(":", "-").upper() in network_info.upper():
                    spoofed_macs_found += 1
            
            results["mac_addresses_spoofed"] = spoofed_macs_found > 0
            results["all_macs_spoofed"] = spoofed_macs_found == len(profile.mac_addresses)
            
        except Exception as e:
            results["network_test_error"] = str(e)
        
        return results
    
    def test_registry_detection(self, profile: SystemProfile) -> Dict[str, bool]:
        """Test Windows registry spoofing"""
        if platform.system() != "Windows":
            return {"not_applicable": True}
        
        results = {}
        
        try:
            import winreg
            
            # Test machine GUID
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 
                              r"SOFTWARE\Microsoft\Cryptography") as key:
                current_guid = winreg.QueryValueEx(key, "MachineGuid")[0]
                results["machine_guid_spoofed"] = current_guid == profile.uuid
            
            # Test computer name
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 
                              r"SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName") as key:
                current_name = winreg.QueryValueEx(key, "ComputerName")[0]
                results["computer_name_spoofed"] = current_name == profile.hostname
            
        except Exception as e:
            results["registry_test_error"] = str(e)
        
        return results
    
    def test_file_system_detection(self, profile: SystemProfile) -> Dict[str, bool]:
        """Test file system spoofing"""
        results = {}
        
        if platform.system() == "Linux":
            # Test /etc/hostname
            try:
                with open("/etc/hostname", 'r') as f:
                    current_hostname = f.read().strip()
                results["hostname_file_spoofed"] = current_hostname == profile.hostname
            except:
                results["hostname_file_error"] = True
            
            # Test machine-id
            try:
                with open("/etc/machine-id", 'r') as f:
                    current_machine_id = f.read().strip()
                expected_machine_id = profile.uuid.replace('-', '')
                results["machine_id_spoofed"] = current_machine_id == expected_machine_id
            except:
                results["machine_id_error"] = True
        
        return results
    
    def test_vm_detection(self) -> Dict[str, bool]:
        """Test VM detection evasion"""
        results = {}
        
        # Common VM detection methods
        vm_indicators = [
            "vmware", "virtualbox", "qemu", "xen", "hyper-v",
            "parallels", "bochs", "kvm"
        ]
        
        # Check system information for VM indicators
        system_info = platform.platform().lower()
        results["platform_vm_hidden"] = not any(indicator in system_info for indicator in vm_indicators)
        
        # Check processor information
        processor_info = platform.processor().lower()
        results["processor_vm_hidden"] = not any(indicator in processor_info for indicator in vm_indicators)
        
        return results
    
    def test_fingerprinting_resistance(self, profile: SystemProfile) -> Dict[str, bool]:
        """Test resistance to fingerprinting techniques"""
        results = {}
        
        # Create fingerprint hash before and after spoofing
        current_fingerprint = self.capture_system_fingerprint()
        
        # Compare with baseline
        baseline_hash = hashlib.md5(str(self.baseline_info).encode()).hexdigest()
        current_hash = hashlib.md5(str(current_fingerprint).encode()).hexdigest()
        
        results["fingerprint_changed"] = baseline_hash != current_hash
        
        # Test specific fingerprinting resistance
        results["hostname_changed"] = current_fingerprint.get("hostname") != self.baseline_info.get("hostname")
        results["platform_changed"] = current_fingerprint.get("platform") != self.baseline_info.get("platform")
        
        return results
    
    def test_spoofing_persistence(self, profile: SystemProfile) -> Dict[str, bool]:
        """Test spoofing persistence over time"""
        results = {}
        
        # Wait and test again
        time.sleep(5)
        
        # Re-run key tests
        os_test = self.test_os_detection(profile)
        hardware_test = self.test_hardware_detection(profile)
        
        results["os_persistence"] = any(os_test.values())
        results["hardware_persistence"] = any(hardware_test.values())
        
        return results
    
    def test_restoration(self) -> Dict[str, bool]:
        """Test that original values are properly restored"""
        results = {}
        
        # Capture current state
        current_fingerprint = self.capture_system_fingerprint()
        
        # Compare key values with baseline
        results["hostname_restored"] = current_fingerprint.get("hostname") == self.baseline_info.get("hostname")
        results["platform_restored"] = current_fingerprint.get("platform") == self.baseline_info.get("platform")
        
        return results
    
    def calculate_overall_score(self, test_results: Dict[str, Any]) -> float:
        """Calculate overall spoofing effectiveness score"""
        total_tests = 0
        passed_tests = 0
        
        for category, tests in test_results.items():
            if isinstance(tests, dict):
                for test_name, result in tests.items():
                    if isinstance(result, bool):
                        total_tests += 1
                        if result:
                            passed_tests += 1
        
        return (passed_tests / total_tests * 100) if total_tests > 0 else 0
    
    def _get_expected_system(self, os_name: str) -> str:
        """Get expected system name for OS"""
        if "windows" in os_name.lower():
            return "Windows"
        elif "macos" in os_name.lower():
            return "Darwin"
        elif any(distro in os_name.lower() for distro in ["ubuntu", "debian", "centos", "fedora", "arch"]):
            return "Linux"
        else:
            return "Unknown"

def main():
    """Main testing function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Advanced OSS Spoofing Tester")
    parser.add_argument('--profile', required=True, help='Profile file to test')
    parser.add_argument('--output', help='Output file for test results')
    parser.add_argument('--verbose', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    # Load profile
    try:
        with open(args.profile, 'r') as f:
            profile_data = json.load(f)
        profile = SystemProfile(**profile_data)
    except Exception as e:
        print(f"Failed to load profile: {e}")
        sys.exit(1)
    
    # Run tests
    tester = SpoofingTester()
    results = tester.run_comprehensive_test(profile)
    
    # Output results
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        print(f"Results saved to {args.output}")
    
    if args.verbose:
        print(json.dumps(results, indent=2, default=str))
    
    print(f"Overall Score: {results.get('overall_score', 0):.1f}%")

if __name__ == "__main__":
    main()
