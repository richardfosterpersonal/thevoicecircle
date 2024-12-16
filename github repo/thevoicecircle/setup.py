#!/usr/bin/env python3
import json
import os
from pathlib import Path

# Create directories
directories = [
    'frontend/src/components',
    'frontend/src/pages',
    'frontend/src/utils',
    'backend/apis',
    'backend/models',
    'docs'
]

print("Creating directories...")
for dir_path in directories:
    Path(dir_path).mkdir(parents=True, exist_ok=True)
    print(f"Created: {dir_path}")

print("Setup complete!")
