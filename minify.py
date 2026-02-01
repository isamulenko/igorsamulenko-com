#!/usr/bin/env python3
"""
Minify HTML/CSS/JS while preserving text content whitespace.
Usage: python3 minify.py [input_file] [output_file]
Default: minify.py index.html s3/index.html
"""

import re
import sys
import os

def minify_css(match):
    """Minify CSS within style tags."""
    css = match.group(1)
    css = re.sub(r'/\*[\s\S]*?\*/', '', css)  # Remove comments
    css = re.sub(r'^\s+', '', css, flags=re.MULTILINE)  # Remove leading whitespace
    css = re.sub(r'\s+', ' ', css)  # Collapse whitespace
    css = re.sub(r'\s*{\s*', '{', css)
    css = re.sub(r'\s*}\s*', '}', css)
    css = re.sub(r'\s*;\s*', ';', css)
    css = re.sub(r':\s+', ':', css)
    css = re.sub(r',\s+', ',', css)
    return '<style>' + css.strip() + '</style>'

def minify_js(match):
    """Minify JS within script tags."""
    js = match.group(1)
    js = re.sub(r'//[^\n]*\n', '\n', js)  # Remove single-line comments
    js = re.sub(r'/\*[\s\S]*?\*/', '', js)  # Remove multi-line comments
    js = re.sub(r'^\s+', '', js, flags=re.MULTILINE)  # Remove leading whitespace
    js = re.sub(r'\n+', '\n', js)  # Collapse newlines
    js = '\n'.join(line for line in js.split('\n') if line.strip())
    return '<script>' + js.strip() + '</script>'

def minify_html(content):
    """Minify HTML while preserving text content."""
    # Remove HTML comments
    content = re.sub(r'<!--[\s\S]*?-->', '', content)

    # Minify CSS
    content = re.sub(r'<style>([\s\S]*?)</style>', minify_css, content)

    # Minify JS
    content = re.sub(r'<script>([\s\S]*?)</script>', minify_js, content)

    # Clean up HTML lines
    lines = content.split('\n')
    lines = [line.strip() for line in lines]
    lines = [line for line in lines if line]
    content = '\n'.join(lines)

    # Remove whitespace between tags (preserves text content)
    content = re.sub(r'>\s+<', '><', content)

    return content

def main():
    # Default paths
    input_file = 'index.html'
    output_file = 's3/index.html'

    # Parse arguments
    if len(sys.argv) >= 2:
        input_file = sys.argv[1]
    if len(sys.argv) >= 3:
        output_file = sys.argv[2]

    # Check input exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)

    # Create output directory if needed
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read input
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_size = len(content)

    # Minify
    content = minify_html(content)

    minified_size = len(content)

    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    # Report
    reduction = (1 - minified_size / original_size) * 100
    print(f"Minified: {input_file} -> {output_file}")
    print(f"Original: {original_size:,} bytes")
    print(f"Minified: {minified_size:,} bytes ({reduction:.1f}% smaller)")

if __name__ == '__main__':
    main()
