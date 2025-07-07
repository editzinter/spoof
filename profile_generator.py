#!/usr/bin/env python3
"""
Profile Generator Utility
Standalone utility for generating spoofing profiles
"""

import json
import sys
import argparse
from pathlib import Path
from advanced_oss_spoofer import ProfileGenerator, SystemProfile

def generate_profile_interactive():
    """Interactive profile generation"""
    print("=== Interactive Profile Generator ===")
    
    # OS Selection
    print("\nSelect Operating System:")
    print("1. Windows")
    print("2. macOS")
    print("3. Linux")
    
    os_choice = input("Enter choice (1-3): ").strip()
    os_map = {"1": "windows", "2": "macos", "3": "linux"}
    os_type = os_map.get(os_choice, "windows")
    
    # Profile Type
    print(f"\nSelect {os_type.title()} Profile Type:")
    if os_type == "windows":
        print("1. Gaming System")
        print("2. Business Workstation")
        print("3. Home Computer")
        print("4. Server")
        print("5. Random")
    elif os_type == "macos":
        print("1. Developer MacBook")
        print("2. Creative Workstation")
        print("3. Business MacBook")
        print("4. Random")
    else:  # Linux
        print("1. Server")
        print("2. Desktop")
        print("3. Developer Workstation")
        print("4. Random")
    
    profile_choice = input("Enter choice: ").strip()
    
    # Generate profile
    generator = ProfileGenerator()
    
    if profile_choice == "5" or profile_choice == "4":  # Random
        profile = generator.generate_random_profile(os_type)
    else:
        # Generate based on type
        profile = generator.generate_random_profile(os_type)
        
        # Customize based on selection
        if os_type == "windows":
            if profile_choice == "1":  # Gaming
                profile.manufacturer = "MSI"
                profile.model = "Gaming Desktop"
                profile.processor = "Intel(R) Core(TM) i9-12900K CPU @ 3.20GHz"
            elif profile_choice == "2":  # Business
                profile.manufacturer = "Dell Inc."
                profile.model = "OptiPlex 7090"
                profile.processor = "Intel(R) Core(TM) i7-11700 CPU @ 2.50GHz"
            elif profile_choice == "3":  # Home
                profile.manufacturer = "HP"
                profile.model = "Pavilion Desktop"
                profile.processor = "AMD Ryzen 5 5600G 6-Core Processor"
        elif os_type == "macos":
            profile.manufacturer = "Apple Inc."
            if profile_choice == "1":  # Developer
                profile.model = "MacBook Pro"
                profile.processor = "Apple M2"
            elif profile_choice == "2":  # Creative
                profile.model = "iMac"
                profile.processor = "Apple M1"
    
    return profile

def generate_bulk_profiles(count: int, os_type: str = None) -> list:
    """Generate multiple profiles"""
    generator = ProfileGenerator()
    profiles = []
    
    for i in range(count):
        profile = generator.generate_random_profile(os_type)
        profiles.append(profile)
    
    return profiles

def save_profiles(profiles: list, output_dir: str):
    """Save profiles to files"""
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    for i, profile in enumerate(profiles):
        filename = f"profile_{i+1}_{profile.os_name.replace(' ', '_').lower()}.json"
        filepath = output_path / filename
        
        with open(filepath, 'w') as f:
            json.dump(profile.__dict__, f, indent=2)
        
        print(f"Saved: {filepath}")

def validate_profile(profile_path: str) -> bool:
    """Validate a profile file"""
    try:
        with open(profile_path, 'r') as f:
            profile_data = json.load(f)
        
        # Try to create SystemProfile object
        profile = SystemProfile(**profile_data)
        
        # Basic validation
        required_fields = [
            'os_name', 'os_version', 'architecture', 'processor',
            'manufacturer', 'model', 'serial_number', 'uuid',
            'mac_addresses', 'hostname', 'username'
        ]
        
        for field in required_fields:
            if not hasattr(profile, field) or not getattr(profile, field):
                print(f"Missing or empty field: {field}")
                return False
        
        print("Profile validation passed!")
        return True
        
    except Exception as e:
        print(f"Profile validation failed: {e}")
        return False

def merge_profiles(profile_paths: list, output_path: str):
    """Merge multiple profiles into one collection"""
    merged_profiles = {}
    
    for i, path in enumerate(profile_paths):
        try:
            with open(path, 'r') as f:
                profile_data = json.load(f)
            
            profile_name = f"profile_{i+1}"
            merged_profiles[profile_name] = profile_data
            
        except Exception as e:
            print(f"Failed to load {path}: {e}")
    
    with open(output_path, 'w') as f:
        json.dump(merged_profiles, f, indent=2)
    
    print(f"Merged {len(merged_profiles)} profiles into {output_path}")

def analyze_profile(profile_path: str):
    """Analyze and display profile information"""
    try:
        with open(profile_path, 'r') as f:
            profile_data = json.load(f)
        
        profile = SystemProfile(**profile_data)
        
        print("=== Profile Analysis ===")
        print(f"OS: {profile.os_name} {profile.os_version}")
        print(f"Architecture: {profile.architecture}")
        print(f"Hardware: {profile.manufacturer} {profile.model}")
        print(f"Processor: {profile.processor}")
        print(f"Serial: {profile.serial_number}")
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
        
        if profile.custom_attributes:
            print("\nCustom Attributes:")
            for key, value in profile.custom_attributes.items():
                print(f"  {key}: {value}")
                
    except Exception as e:
        print(f"Failed to analyze profile: {e}")

def main():
    parser = argparse.ArgumentParser(description="Profile Generator Utility")
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Interactive generation
    interactive_parser = subparsers.add_parser('interactive', help='Interactive profile generation')
    interactive_parser.add_argument('--save', help='Save generated profile to file')
    
    # Bulk generation
    bulk_parser = subparsers.add_parser('bulk', help='Generate multiple profiles')
    bulk_parser.add_argument('--count', type=int, required=True, help='Number of profiles to generate')
    bulk_parser.add_argument('--os', choices=['windows', 'macos', 'linux'], help='Target OS')
    bulk_parser.add_argument('--output-dir', default='profiles', help='Output directory')
    
    # Single profile generation
    single_parser = subparsers.add_parser('single', help='Generate single profile')
    single_parser.add_argument('--os', choices=['windows', 'macos', 'linux'], required=True, help='Target OS')
    single_parser.add_argument('--output', required=True, help='Output file')
    
    # Profile validation
    validate_parser = subparsers.add_parser('validate', help='Validate profile file')
    validate_parser.add_argument('profile', help='Profile file to validate')
    
    # Profile analysis
    analyze_parser = subparsers.add_parser('analyze', help='Analyze profile file')
    analyze_parser.add_argument('profile', help='Profile file to analyze')
    
    # Profile merging
    merge_parser = subparsers.add_parser('merge', help='Merge multiple profiles')
    merge_parser.add_argument('profiles', nargs='+', help='Profile files to merge')
    merge_parser.add_argument('--output', required=True, help='Output file')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    try:
        if args.command == 'interactive':
            profile = generate_profile_interactive()
            
            print("\n=== Generated Profile ===")
            print(json.dumps(profile.__dict__, indent=2))
            
            if args.save:
                with open(args.save, 'w') as f:
                    json.dump(profile.__dict__, f, indent=2)
                print(f"\nProfile saved to {args.save}")
        
        elif args.command == 'bulk':
            print(f"Generating {args.count} profiles...")
            profiles = generate_bulk_profiles(args.count, args.os)
            save_profiles(profiles, args.output_dir)
            print(f"Generated {len(profiles)} profiles in {args.output_dir}")
        
        elif args.command == 'single':
            generator = ProfileGenerator()
            profile = generator.generate_random_profile(args.os)
            
            with open(args.output, 'w') as f:
                json.dump(profile.__dict__, f, indent=2)
            print(f"Profile saved to {args.output}")
        
        elif args.command == 'validate':
            validate_profile(args.profile)
        
        elif args.command == 'analyze':
            analyze_profile(args.profile)
        
        elif args.command == 'merge':
            merge_profiles(args.profiles, args.output)
    
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
