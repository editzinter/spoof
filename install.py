#!/usr/bin/env python3
"""
Installation Script for Advanced OSS Spoofing Framework
Handles dependency installation and initial setup
"""

import os
import sys
import subprocess
import platform
import json
from pathlib import Path

class FrameworkInstaller:
    """Installer for the Advanced OSS Spoofing Framework"""
    
    def __init__(self):
        self.system = platform.system().lower()
        self.python_executable = sys.executable
        self.base_dir = Path(__file__).parent
        
    def check_python_version(self):
        """Check if Python version is compatible"""
        version = sys.version_info
        if version.major < 3 or (version.major == 3 and version.minor < 8):
            print("❌ Python 3.8 or higher is required")
            print(f"Current version: {version.major}.{version.minor}.{version.micro}")
            return False
        
        print(f"✅ Python version {version.major}.{version.minor}.{version.micro} is compatible")
        return True
    
    def check_privileges(self):
        """Check if running with appropriate privileges"""
        if self.system == "windows":
            try:
                import ctypes
                is_admin = ctypes.windll.shell32.IsUserAnAdmin()
                if not is_admin:
                    print("⚠️  Warning: Administrator privileges recommended for full functionality")
                    return False
                else:
                    print("✅ Running with Administrator privileges")
                    return True
            except:
                print("⚠️  Could not determine privilege level")
                return False
        else:
            if os.geteuid() != 0:
                print("⚠️  Warning: Root privileges recommended for full functionality")
                print("   Consider running with 'sudo' for complete access")
                return False
            else:
                print("✅ Running with root privileges")
                return True
    
    def install_dependencies(self):
        """Install required dependencies"""
        print("📦 Installing dependencies...")
        
        requirements_file = self.base_dir / "requirements.txt"
        if not requirements_file.exists():
            print("❌ requirements.txt not found")
            return False
        
        try:
            # Upgrade pip first
            subprocess.run([self.python_executable, "-m", "pip", "install", "--upgrade", "pip"], 
                         check=True, capture_output=True)
            
            # Install requirements
            subprocess.run([self.python_executable, "-m", "pip", "install", "-r", str(requirements_file)], 
                         check=True, capture_output=True)
            
            print("✅ Dependencies installed successfully")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install dependencies: {e}")
            return False
    
    def create_directories(self):
        """Create necessary directories"""
        print("📁 Creating directories...")
        
        directories = [
            "profiles",
            "logs",
            "backups",
            "temp"
        ]
        
        for directory in directories:
            dir_path = self.base_dir / directory
            dir_path.mkdir(exist_ok=True)
            print(f"   Created: {directory}/")
        
        print("✅ Directories created")
        return True
    
    def setup_configuration(self):
        """Setup initial configuration"""
        print("⚙️  Setting up configuration...")
        
        config_file = self.base_dir / "config.json"
        if config_file.exists():
            print("   Configuration file already exists")
            return True
        
        # Default configuration
        default_config = {
            "framework_settings": {
                "version": "1.0.0",
                "debug_mode": False,
                "enable_logging": True,
                "log_file": "logs/spoofing.log",
                "backup_original_values": True,
                "auto_restore_on_exit": True
            },
            "evasion_settings": {
                "enable_anti_vm": True,
                "enable_anti_debug": True,
                "enable_sandbox_evasion": True,
                "randomize_timing": True,
                "obfuscate_process": True
            }
        }
        
        try:
            with open(config_file, 'w') as f:
                json.dump(default_config, f, indent=2)
            print("✅ Configuration file created")
            return True
        except Exception as e:
            print(f"❌ Failed to create configuration: {e}")
            return False
    
    def generate_sample_profiles(self):
        """Generate sample profiles"""
        print("📋 Generating sample profiles...")
        
        try:
            # Import after dependencies are installed
            from advanced_oss_spoofer import ProfileGenerator
            
            generator = ProfileGenerator()
            profiles_dir = self.base_dir / "profiles"
            
            # Generate sample profiles
            sample_profiles = [
                ("windows", "sample_windows_gaming.json"),
                ("windows", "sample_windows_business.json"),
                ("macos", "sample_macos_developer.json"),
                ("linux", "sample_linux_server.json")
            ]
            
            for os_type, filename in sample_profiles:
                profile = generator.generate_random_profile(os_type)
                profile_path = profiles_dir / filename
                
                with open(profile_path, 'w') as f:
                    json.dump(profile.__dict__, f, indent=2)
                
                print(f"   Generated: {filename}")
            
            print("✅ Sample profiles generated")
            return True
            
        except Exception as e:
            print(f"❌ Failed to generate sample profiles: {e}")
            return False
    
    def test_installation(self):
        """Test the installation"""
        print("🧪 Testing installation...")
        
        try:
            # Test import
            from advanced_oss_spoofer import AdvancedOSSSpoofing
            
            # Test basic functionality
            spoofer = AdvancedOSSSpoofing()
            current_os = spoofer.detect_current_os()
            
            print(f"   Detected OS: {current_os}")
            print("✅ Installation test passed")
            return True
            
        except Exception as e:
            print(f"❌ Installation test failed: {e}")
            return False
    
    def display_usage_info(self):
        """Display usage information"""
        print("\n" + "="*60)
        print("🎉 Installation Complete!")
        print("="*60)
        print("\n📖 Quick Start:")
        print("   # View help")
        print("   python advanced_oss_spoofer.py --help")
        print("\n   # Generate a profile")
        print("   python advanced_oss_spoofer.py --generate --os windows --save my_profile.json")
        print("\n   # Start spoofing")
        print("   python advanced_oss_spoofer.py --start --random")
        print("\n   # Validate spoofing")
        print("   python advanced_oss_spoofer.py --validate")
        print("\n   # Stop spoofing")
        print("   python advanced_oss_spoofer.py --stop")
        
        print("\n🔧 Additional Tools:")
        print("   # Profile generator")
        print("   python profile_generator.py interactive")
        print("\n   # Testing suite")
        print("   python spoofing_tester.py --profile profiles/sample_windows_gaming.json")
        
        print("\n⚠️  Important Notes:")
        print("   - This tool is for educational purposes only")
        print("   - Use responsibly and in accordance with applicable laws")
        print("   - Some features require administrator/root privileges")
        print("   - Always backup important data before use")
        
        print("\n📚 Documentation:")
        print("   - README.md: Comprehensive documentation")
        print("   - config.json: Framework configuration")
        print("   - profiles/: Sample spoofing profiles")
        
    def run_installation(self):
        """Run the complete installation process"""
        print("🚀 Advanced OSS Spoofing Framework Installer")
        print("="*50)
        
        steps = [
            ("Checking Python version", self.check_python_version),
            ("Checking privileges", self.check_privileges),
            ("Installing dependencies", self.install_dependencies),
            ("Creating directories", self.create_directories),
            ("Setting up configuration", self.setup_configuration),
            ("Generating sample profiles", self.generate_sample_profiles),
            ("Testing installation", self.test_installation)
        ]
        
        failed_steps = []
        
        for step_name, step_function in steps:
            print(f"\n{step_name}...")
            try:
                if not step_function():
                    failed_steps.append(step_name)
            except Exception as e:
                print(f"❌ {step_name} failed: {e}")
                failed_steps.append(step_name)
        
        if failed_steps:
            print(f"\n⚠️  Installation completed with warnings:")
            for step in failed_steps:
                print(f"   - {step}")
            print("\nSome features may not work correctly.")
        else:
            print("\n✅ Installation completed successfully!")
        
        self.display_usage_info()

def main():
    """Main installation function"""
    installer = FrameworkInstaller()
    
    try:
        installer.run_installation()
    except KeyboardInterrupt:
        print("\n\nInstallation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\nInstallation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
