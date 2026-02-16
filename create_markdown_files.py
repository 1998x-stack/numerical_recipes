#!/usr/bin/env python3

import os
import glob

def create_markdown_file(python_file_path):
    """Create a markdown file alongside a Python file"""
    md_file_path = python_file_path.replace('.py', '.md')
    
    dir_path, file_name = os.path.split(python_file_path)
    section_name = file_name.replace('.py', '').replace('_', ' ').title()
    
    chapter_dir = os.path.basename(dir_path)
    chapter_number = chapter_dir.split('_')[0]
    
    markdown_content = f"""# {section_name}

## Description
This file contains the implementation of {section_name} from Chapter {chapter_number} of Numerical Recipes.

## Mathematical Background
<!-- Provide a brief overview of the mathematical concepts behind this algorithm -->

## Implementation Notes
<!-- Document any implementation details, considerations, or optimizations -->

## Usage Example
```python
# Example usage of the algorithm
```

## References
- Numerical Recipes, Chapter {chapter_number}: {section_name}
- Original page references: <!-- Add page numbers from the textbook -->
"""

    with open(md_file_path, 'w') as md_file:
        md_file.write(markdown_content)
    
    print(f"Created: {md_file_path}")

def find_python_files():
    """Find all Python files in the project directory"""
    base_path = "."
    py_files = []
    
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.py'):
                py_files.append(os.path.join(root, file))
    
    return py_files

def main():
    print("Creating markdown files for Python implementations...")
    
    python_files = find_python_files()
    
    for py_file in python_files:
        create_markdown_file(py_file)
    
    print(f"Created markdown files for {len(python_files)} Python files.")

if __name__ == "__main__":
    main()