# Advanced OSS Spoofing Framework - Usage Guide

## 🚀 Quick Start

### 1. Installation
```bash
# Run the installer
python install.py

# Or install manually
pip install -r requirements.txt
```

### 2. Basic Usage
```bash
# View system information
python advanced_oss_spoofer.py --info

# Generate a random profile
python advanced_oss_spoofer.py --generate --os windows --save my_profile.json

# Start spoofing with random profile
python advanced_oss_spoofer.py --start --random

# Validate spoofing effectiveness
python advanced_oss_spoofer.py --validate

# Stop spoofing and restore
python advanced_oss_spoofer.py --stop
```

## 📋 Command Reference

### Main Framework Commands

#### Information and Detection
```bash
# Display current system information
python advanced_oss_spoofer.py --info

# Display help
python advanced_oss_spoofer.py --help
```

#### Profile Management
```bash
# Generate random profile for current OS
python advanced_oss_spoofer.py --generate

# Generate profile for specific OS
python advanced_oss_spoofer.py --generate --os windows

# Generate and save profile
python advanced_oss_spoofer.py --generate --os linux --save server_profile.json

# Use preset profile
python advanced_oss_spoofer.py --generate --profile gaming_windows --save gaming.json
```

#### Spoofing Operations
```bash
# Start with random profile
python advanced_oss_spoofer.py --start --random

# Start with preset profile
python advanced_oss_spoofer.py --start --profile gaming_windows

# Start with custom profile file
python advanced_oss_spoofer.py --start --load my_profile.json

# Validate current spoofing
python advanced_oss_spoofer.py --validate

# Stop spoofing and restore
python advanced_oss_spoofer.py --stop
```

### Profile Generator Tool

#### Interactive Generation
```bash
# Interactive profile creation
python profile_generator.py interactive

# Interactive with auto-save
python profile_generator.py interactive --save my_profile.json
```

#### Bulk Generation
```bash
# Generate 10 random profiles
python profile_generator.py bulk --count 10

# Generate Windows profiles only
python profile_generator.py bulk --count 5 --os windows --output-dir windows_profiles

# Generate single profile
python profile_generator.py single --os macos --output mac_profile.json
```

#### Profile Management
```bash
# Validate profile
python profile_generator.py validate my_profile.json

# Analyze profile
python profile_generator.py analyze my_profile.json

# Merge multiple profiles
python profile_generator.py merge profile1.json profile2.json --output merged.json
```

### Testing and Validation

#### Comprehensive Testing
```bash
# Test with specific profile
python spoofing_tester.py --profile my_profile.json

# Test with verbose output
python spoofing_tester.py --profile my_profile.json --verbose

# Save test results
python spoofing_tester.py --profile my_profile.json --output test_results.json
```

#### Demo Mode
```bash
# Run interactive demo
python demo.py
```

## 🎯 Common Use Cases

### 1. Educational Learning
```bash
# Learn about system fingerprinting
python advanced_oss_spoofer.py --info

# Understand profile generation
python profile_generator.py interactive

# See spoofing simulation
python demo.py
```

### 2. Security Research
```bash
# Generate research profiles
python profile_generator.py bulk --count 50 --output-dir research_profiles

# Test detection evasion
python advanced_oss_spoofer.py --start --random --no-evasion
python advanced_oss_spoofer.py --validate

# Comprehensive analysis
python spoofing_tester.py --profile research_profile.json --output analysis.json
```

### 3. Penetration Testing
```bash
# Create stealth profile
python profile_generator.py single --os windows --output stealth_profile.json

# Apply spoofing
python advanced_oss_spoofer.py --start --load stealth_profile.json

# Validate effectiveness
python advanced_oss_spoofer.py --validate

# Test persistence
python spoofing_tester.py --profile stealth_profile.json
```

## ⚙️ Configuration

### Framework Configuration (config.json)
```json
{
  "framework_settings": {
    "debug_mode": false,
    "enable_logging": true,
    "auto_restore_on_exit": true
  },
  "evasion_settings": {
    "enable_anti_vm": true,
    "enable_anti_debug": true,
    "randomize_timing": true
  }
}
```

### Environment Variables
```bash
# Enable debug mode
export OSS_DEBUG=1

# Disable evasion techniques
export OSS_NO_EVASION=1

# Custom config file
export OSS_CONFIG=/path/to/config.json
```

## 🔧 Advanced Features

### Custom Profile Creation
```python
from advanced_oss_spoofer import SystemProfile

# Create custom profile
profile = SystemProfile(
    os_name="Windows 11 Pro",
    os_version="11.0.22621",
    architecture="x86_64",
    processor="Intel(R) Core(TM) i9-12900K",
    manufacturer="Custom Manufacturer",
    model="Custom Model",
    serial_number="CUSTOM123456",
    uuid="12345678-1234-5678-9012-123456789012",
    mac_addresses=["00:1B:44:11:3A:B7"],
    hostname="CUSTOM-PC",
    username="customuser",
    timezone="America/New_York",
    language="en-US",
    hardware_ids={},
    custom_attributes={}
)
```

### Programmatic Usage
```python
from advanced_oss_spoofer import AdvancedOSSSpoofing

# Initialize framework
spoofer = AdvancedOSSSpoofing()

# Generate profile
profile = spoofer.profile_generator.generate_random_profile("windows")

# Start spoofing
success = spoofer.start_spoofing(profile)

# Validate
results = spoofer.validate_spoofing()

# Stop
spoofer.stop_spoofing()
```

## 🛡️ Safety Guidelines

### Before Using
1. **Backup Important Data**: Always backup critical system data
2. **Test Environment**: Use in isolated/virtual environments first
3. **Administrator Rights**: Ensure proper privileges
4. **Antivirus**: Temporarily disable if necessary

### During Use
1. **Monitor System**: Watch for unexpected behavior
2. **Keep Backups**: Framework automatically creates backups
3. **Validate Changes**: Use validation tools regularly
4. **Emergency Stop**: Know how to quickly restore

### After Use
1. **Restore System**: Always restore original values
2. **Verify Restoration**: Check that system is back to normal
3. **Clean Temporary Files**: Remove temporary spoofing files
4. **Review Logs**: Check logs for any issues

## 🚨 Troubleshooting

### Common Issues

#### Permission Errors
```bash
# Windows: Run as Administrator
# Linux/macOS: Use sudo
sudo python3 advanced_oss_spoofer.py --start --random
```

#### Import Errors
```bash
# Install missing dependencies
pip install -r requirements.txt

# Platform-specific installation
pip install pywin32 wmi  # Windows
pip install python-dbus  # Linux
```

#### Spoofing Failures
```bash
# Check system compatibility
python advanced_oss_spoofer.py --info

# Validate profile
python profile_generator.py validate my_profile.json

# Test with verbose output
python advanced_oss_spoofer.py --start --load my_profile.json --verbose
```

#### Restoration Issues
```bash
# Force restoration
python advanced_oss_spoofer.py --stop

# Manual backup restoration
# Check backups/ directory for original values
```

### Getting Help
1. Check README.md for detailed documentation
2. Review configuration in config.json
3. Run demo.py for interactive learning
4. Check logs/ directory for error details
5. Use --verbose flag for detailed output

## 📚 Learning Resources

### Understanding System Spoofing
- System fingerprinting techniques
- Hardware identification methods
- Network interface spoofing
- Registry and file system modification

### Security Implications
- Detection evasion methods
- Anti-analysis techniques
- VM and sandbox detection
- Forensic considerations

### Best Practices
- Responsible disclosure
- Legal and ethical considerations
- Testing methodologies
- Documentation and reporting

---

**Remember**: This framework is for educational and research purposes only. Always use responsibly and in accordance with applicable laws and regulations.
