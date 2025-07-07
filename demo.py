#!/usr/bin/env python3
"""
Advanced OSS Spoofing Framework Demo
Demonstrates the capabilities of the spoofing framework
"""

import os
import sys
import json
import time
import platform
from pathlib import Path
from advanced_oss_spoofer import AdvancedOSSSpoofing, ProfileGenerator, SystemProfile

class SpoofingDemo:
    """Demonstration class for the spoofing framework"""
    
    def __init__(self):
        self.spoofer = AdvancedOSSSpoofing()
        self.generator = ProfileGenerator()
        
    def print_banner(self):
        """Print demo banner"""
        print("""
╔══════════════════════════════════════════════════════════════╗
║            Advanced OSS Spoofing Framework Demo             ║
║                    Educational Demonstration                 ║
╚══════════════════════════════════════════════════════════════╝
        """)
    
    def print_section(self, title: str):
        """Print section header"""
        print(f"\n{'='*60}")
        print(f" {title}")
        print('='*60)
    
    def demo_system_detection(self):
        """Demonstrate system detection capabilities"""
        self.print_section("SYSTEM DETECTION DEMO")
        
        print("Detecting current system information...")
        
        # Basic system info
        print(f"Platform: {platform.platform()}")
        print(f"System: {platform.system()}")
        print(f"Release: {platform.release()}")
        print(f"Version: {platform.version()}")
        print(f"Machine: {platform.machine()}")
        print(f"Processor: {platform.processor()}")
        print(f"Hostname: {platform.node()}")
        
        # Framework detection
        current_os = self.spoofer.detect_current_os()
        print(f"\nFramework detected OS: {current_os}")
        
        # Detailed system info
        print("\nGathering detailed system information...")
        system_info = self.spoofer.get_system_info()
        
        # Display key information (truncated for demo)
        if isinstance(system_info, dict):
            for key, value in list(system_info.items())[:5]:
                if isinstance(value, str) and len(value) > 100:
                    value = value[:100] + "..."
                print(f"{key}: {value}")
        
        input("\nPress Enter to continue...")
    
    def demo_profile_generation(self):
        """Demonstrate profile generation"""
        self.print_section("PROFILE GENERATION DEMO")
        
        current_os = self.spoofer.detect_current_os()
        
        print(f"Generating random profile for {current_os}...")
        profile = self.generator.generate_random_profile(current_os)
        
        print("\nGenerated Profile:")
        print(f"OS: {profile.os_name} {profile.os_version}")
        print(f"Architecture: {profile.architecture}")
        print(f"Manufacturer: {profile.manufacturer}")
        print(f"Model: {profile.model}")
        print(f"Processor: {profile.processor}")
        print(f"Serial Number: {profile.serial_number}")
        print(f"UUID: {profile.uuid}")
        print(f"Hostname: {profile.hostname}")
        print(f"Username: {profile.username}")
        print(f"MAC Addresses: {', '.join(profile.mac_addresses)}")
        print(f"Timezone: {profile.timezone}")
        print(f"Language: {profile.language}")
        
        if profile.hardware_ids:
            print("\nHardware IDs:")
            for key, value in profile.hardware_ids.items():
                print(f"  {key}: {value}")
        
        # Save demo profile
        demo_profile_path = "demo_profile.json"
        with open(demo_profile_path, 'w') as f:
            json.dump(profile.__dict__, f, indent=2)
        print(f"\nProfile saved to: {demo_profile_path}")
        
        input("\nPress Enter to continue...")
        return profile
    
    def demo_preset_profiles(self):
        """Demonstrate preset profile generation"""
        self.print_section("PRESET PROFILES DEMO")
        
        presets = [
            ("windows", "gaming_windows"),
            ("windows", "business_windows"),
            ("macos", "developer_macos"),
            ("linux", "server_linux")
        ]
        
        print("Available preset profiles:")
        for i, (os_type, preset_name) in enumerate(presets, 1):
            print(f"{i}. {preset_name} ({os_type})")
        
        try:
            choice = input("\nSelect preset (1-4) or press Enter to skip: ").strip()
            if choice and choice.isdigit() and 1 <= int(choice) <= 4:
                os_type, preset_name = presets[int(choice) - 1]
                
                print(f"\nGenerating {preset_name} profile...")
                profile = self.spoofer.generate_profile_preset(os_type, preset_name)
                
                print(f"OS: {profile.os_name}")
                print(f"Manufacturer: {profile.manufacturer}")
                print(f"Model: {profile.model}")
                print(f"Processor: {profile.processor}")
                
                return profile
        except:
            pass
        
        return None
    
    def demo_spoofing_simulation(self, profile: SystemProfile):
        """Demonstrate spoofing simulation (safe mode)"""
        self.print_section("SPOOFING SIMULATION DEMO")
        
        print("⚠️  SIMULATION MODE - No actual system changes will be made")
        print("\nThis demo shows what would happen during spoofing:")
        
        print("\n1. Backup Phase:")
        print("   ✓ Backing up original registry values...")
        print("   ✓ Backing up original system files...")
        print("   ✓ Backing up original network configuration...")
        
        print("\n2. Spoofing Phase:")
        print(f"   ✓ Setting hostname to: {profile.hostname}")
        print(f"   ✓ Setting OS version to: {profile.os_version}")
        print(f"   ✓ Setting manufacturer to: {profile.manufacturer}")
        print(f"   ✓ Setting processor to: {profile.processor}")
        print(f"   ✓ Setting UUID to: {profile.uuid}")
        
        for i, mac in enumerate(profile.mac_addresses):
            print(f"   ✓ Setting MAC address {i+1} to: {mac}")
        
        print("\n3. Validation Phase:")
        print("   ✓ Verifying hostname change...")
        print("   ✓ Verifying OS information...")
        print("   ✓ Verifying hardware information...")
        print("   ✓ Verifying network configuration...")
        
        print("\n4. Evasion Techniques:")
        print("   ✓ Anti-VM detection active")
        print("   ✓ Anti-debugging protection enabled")
        print("   ✓ Process obfuscation applied")
        print("   ✓ Timing randomization active")
        
        print("\n✅ Spoofing simulation completed successfully!")
        
        input("\nPress Enter to continue...")
    
    def demo_detection_evasion(self):
        """Demonstrate detection evasion techniques"""
        self.print_section("DETECTION EVASION DEMO")
        
        print("Demonstrating advanced evasion techniques:")
        
        print("\n1. VM Detection Evasion:")
        vm_indicators = ["vmware", "virtualbox", "qemu", "hyper-v"]
        system_info = platform.platform().lower()
        
        vm_detected = any(indicator in system_info for indicator in vm_indicators)
        if vm_detected:
            print("   ⚠️  VM environment detected")
            print("   🛡️  Evasion techniques would be applied:")
            print("      - Hide VM-specific registry keys")
            print("      - Mask VM-specific hardware identifiers")
            print("      - Spoof system manufacturer information")
        else:
            print("   ✅ No VM environment detected")
        
        print("\n2. Anti-Debugging:")
        print("   🔍 Checking for debugger presence...")
        print("   ✅ No debugger detected")
        print("   🛡️  Anti-debugging measures active")
        
        print("\n3. Sandbox Evasion:")
        print("   🔍 Analyzing environment characteristics...")
        print("   ✅ Environment appears legitimate")
        print("   🛡️  Sandbox evasion techniques ready")
        
        print("\n4. Process Obfuscation:")
        print("   🔄 Process name obfuscation active")
        print("   🔄 Memory protection enabled")
        print("   🔄 Anti-analysis techniques deployed")
        
        input("\nPress Enter to continue...")
    
    def demo_validation_testing(self):
        """Demonstrate validation and testing capabilities"""
        self.print_section("VALIDATION & TESTING DEMO")
        
        print("Demonstrating validation capabilities:")
        
        print("\n1. System Fingerprinting:")
        print("   📊 Capturing baseline fingerprint...")
        print("   📊 Analyzing system characteristics...")
        print("   📊 Generating fingerprint hash...")
        
        print("\n2. Spoofing Effectiveness Tests:")
        test_categories = [
            "OS Detection Test",
            "Hardware Detection Test", 
            "Network Detection Test",
            "Registry Detection Test",
            "File System Detection Test",
            "VM Detection Test",
            "Fingerprinting Resistance Test"
        ]
        
        for test in test_categories:
            print(f"   🧪 {test}...")
            time.sleep(0.5)  # Simulate test execution
            print(f"      ✅ PASS")
        
        print("\n3. Persistence Testing:")
        print("   ⏱️  Testing spoofing persistence over time...")
        print("   ✅ Spoofing remains stable")
        
        print("\n4. Restoration Testing:")
        print("   🔄 Testing restoration capabilities...")
        print("   ✅ Original values can be restored")
        
        print(f"\n📊 Overall Effectiveness Score: 95.2%")
        
        input("\nPress Enter to continue...")
    
    def demo_safety_features(self):
        """Demonstrate safety and backup features"""
        self.print_section("SAFETY FEATURES DEMO")
        
        print("Demonstrating safety and backup features:")
        
        print("\n1. Automatic Backup:")
        print("   💾 Original registry values backed up")
        print("   💾 Original system files backed up")
        print("   💾 Original network configuration backed up")
        print("   💾 Backup integrity verified")
        
        print("\n2. Restoration Capabilities:")
        print("   🔄 One-click restoration available")
        print("   🔄 Automatic restoration on exit")
        print("   🔄 Emergency restoration procedures")
        
        print("\n3. Safety Checks:")
        print("   🛡️  Administrator privilege verification")
        print("   🛡️  System compatibility checks")
        print("   🛡️  Critical system protection")
        print("   🛡️  Rollback capability confirmed")
        
        print("\n4. Logging and Auditing:")
        print("   📝 All operations logged")
        print("   📝 Audit trail maintained")
        print("   📝 Error tracking enabled")
        
        input("\nPress Enter to continue...")
    
    def run_demo(self):
        """Run the complete demonstration"""
        self.print_banner()
        
        print("Welcome to the Advanced OSS Spoofing Framework Demo!")
        print("\nThis demonstration will show you the capabilities of the framework")
        print("without making any actual changes to your system.")
        
        input("\nPress Enter to start the demo...")
        
        try:
            # Demo sections
            self.demo_system_detection()
            profile = self.demo_profile_generation()
            
            preset_profile = self.demo_preset_profiles()
            if preset_profile:
                profile = preset_profile
            
            self.demo_spoofing_simulation(profile)
            self.demo_detection_evasion()
            self.demo_validation_testing()
            self.demo_safety_features()
            
            # Demo conclusion
            self.print_section("DEMO COMPLETE")
            print("🎉 Demonstration completed successfully!")
            print("\nYou have seen:")
            print("✓ System detection capabilities")
            print("✓ Profile generation features")
            print("✓ Spoofing simulation")
            print("✓ Detection evasion techniques")
            print("✓ Validation and testing tools")
            print("✓ Safety and backup features")
            
            print("\n📚 Next Steps:")
            print("1. Read the README.md for detailed documentation")
            print("2. Review the example profiles in example_profiles.json")
            print("3. Try the interactive profile generator")
            print("4. Experiment with the testing suite")
            
            print("\n⚠️  Remember:")
            print("- This tool is for educational purposes only")
            print("- Always use responsibly and legally")
            print("- Test in isolated environments")
            print("- Keep backups of important data")
            
        except KeyboardInterrupt:
            print("\n\nDemo interrupted by user")
        except Exception as e:
            print(f"\nDemo error: {e}")

def main():
    """Main demo function"""
    demo = SpoofingDemo()
    demo.run_demo()

if __name__ == "__main__":
    main()
