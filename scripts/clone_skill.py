import os
import shutil
import sys
import re
import json

def clone_skill(source_name, target_name, changes):
    """
    Clones a skill and applies changes.
    changes: dict containing 'replacements' (dict)
    """
    source_dir = os.path.expanduser(f"~/.hermes/skills/{source_name}")
    target_dir = os.path.expanduser(f"~/.hermes/skills/{target_name}")
    
    if not os.path.exists(source_dir):
        print(f"ERROR: Source skill {source_name} not found.")
        return False

    if os.path.exists(target_dir):
        print(f"WARNING: Target skill {target_name} already exists. Overwriting.")
        shutil.rmtree(target_dir)

    # 1. Copy Directory
    print(f"Copying {source_name} to {target_name}...")
    shutil.copytree(source_dir, target_dir)
    
    # 2. Modify Files
    replacements = changes.get("replacements", {})
    
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            filepath = os.path.join(root, file)
            
            # Skip binary files
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                continue

            original_content = content
            
            # Apply Replacements
            for old, new in replacements.items():
                content = content.replace(old, new)
            
            # Write back if changed
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Patched: {file}")

    print(f"SUCCESS: Skill {target_name} created at {target_dir}")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python clone_skill.py <source_name> <target_name> '<json_changes>'")
        sys.exit(1)
    
    source = sys.argv[1]
    target = sys.argv[2]
    
    changes = {}
    if len(sys.argv) > 3:
        try:
            changes = json.loads(sys.argv[3])
        except json.JSONDecodeError:
            changes = {"replacements": {}}
    
    clone_skill(source, target, changes)
