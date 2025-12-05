#!/usr/bin/env python3
"""
Advent of Code day setup script with automatic input download.
Usage: python new_day.py 5 [2025]
"""
import os
import sys
from pathlib import Path
from shutil import copy2

try:
    import requests
except ImportError:
    print("Warning: requests module not found. Input download will be skipped.")
    print("Install it with: pip install requests")
    requests = None

# ============================================================================
# CONFIGURATION - Edit these values
# ============================================================================
USER_SESSION_ID = "53616c7465645f5f24e29965346eca32e9bc9a840b706fa527a950332d9aa9b332b8d194de684519f8ffaf721e5133ee6b1bbbe6e318d4e81d36c4c09d89cd23"  # Replace with your session ID
DOWNLOAD_INPUT = True  # Set to False to skip downloading input
AUTHOR = "Rajesh M R"
# ============================================================================

USER_AGENT = "advent_of_code_setup_script"
AOC_URL = "https://adventofcode.com"
MAX_RETRY = 2


def download_input(year: int, day: int, save_path: Path) -> bool:
    """Download puzzle input from Advent of Code."""
    if not requests:
        print("    ⚠ Skipping input download (requests module not available)")
        return False
    
    if not USER_SESSION_ID or USER_SESSION_ID == "YOUR_SESSION_ID_HERE":
        print("    ⚠ Skipping input download (session ID not configured)")
        print("    → Get your session ID from browser cookies while logged into adventofcode.com")
        return False
    
    url = f"{AOC_URL}/{year}/day/{day}/input"
    
    for attempt in range(MAX_RETRY):
        try:
            response = requests.get(
                url,
                cookies={"session": USER_SESSION_ID},
                headers={"User-Agent": USER_AGENT},
                timeout=10
            )
            
            if response.ok:
                # Remove trailing newline that AoC adds
                save_path.write_text(response.text.rstrip("\n"))
                print(f"    ✓ Downloaded input from adventofcode.com")
                return True
            elif response.status_code == 404:
                print(f"    ⚠ Input not yet available (puzzle may not be released)")
                return False
            elif response.status_code == 400:
                print(f"    ⚠ Invalid session ID (check your configuration)")
                return False
            else:
                print(f"    ⚠ Server returned status code {response.status_code}")
                return False
                
        except requests.exceptions.Timeout:
            if attempt < MAX_RETRY - 1:
                print(f"    ⚠ Request timed out, retrying...")
            else:
                print(f"    ⚠ Request timed out after {MAX_RETRY} attempts")
        except requests.exceptions.RequestException as e:
            print(f"    ⚠ Network error: {e}")
            return False
        except Exception as e:
            print(f"    ⚠ Unexpected error: {e}")
            return False
    
    return False


def create_day(day: int, year: int = 2025, author: str = AUTHOR):
    """Create all files needed for a new Advent of Code day."""
    root = Path.cwd()
    template_path = root / "template"
    
    # Check if template folder exists
    if not template_path.exists():
        print(f"❌ Error: Template folder not found at {template_path}")
        print("   Please create a 'template' folder with puzzle.py and test_puzzle_day_.py")
        sys.exit(1)
    
    # Create day directory
    day_dir = root / str(year) / f"day_{day:02d}"
    day_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\n📅 Setting up Day {day}, {year}")
    print(f"📁 Directory: {day_dir}")
    
    # Create solution file (puzzle.py) from template
    solution_file = day_dir / "puzzle.py"
    template_puzzle = template_path / "puzzle.py"
    
    if not solution_file.exists():
        if template_puzzle.exists():
            # Read template and substitute placeholders
            template_content = template_puzzle.read_text()
            content = template_content.format(day=day, year=year, author=author)
            solution_file.write_text(content)
            print(f"✓ Created {solution_file.name}")
        else:
            print(f"  ⚠ Template file not found: {template_puzzle}")
    else:
        print(f"  → {solution_file.name} already exists, skipping")
    
    # Create test file from template
    test_file = day_dir / f"test_puzzle_day_{day}.py"
    template_test = template_path / "test_puzzle_day_.py"
    
    if not test_file.exists():
        if template_test.exists():
            # Read template and substitute placeholders
            template_content = template_test.read_text()
            content = template_content.format(day=day, year=year, author=author)
            test_file.write_text(content)
            print(f"✓ Created {test_file.name}")
        else:
            print(f"  ⚠ Template file not found: {template_test}")
    else:
        print(f"  → {test_file.name} already exists, skipping")
    
    # Create or download input file
    input_file = day_dir / "input.txt"
    if not input_file.exists():
        if DOWNLOAD_INPUT:
            if not download_input(year, day, input_file):
                # Create placeholder if download failed
                input_file.write_text("# Paste your input here\n")
                print(f"✓ Created placeholder {input_file.name}")
        else:
            input_file.write_text("# Paste your input here\n")
            print(f"✓ Created placeholder {input_file.name}")
    else:
        print(f"  → {input_file.name} already exists, skipping")
    
    # Create URL shortcut
    url_file = day_dir / "link.url"
    if not url_file.exists():
        url_content = f"[InternetShortcut]\nURL={AOC_URL}/{year}/day/{day}\n"
        url_file.write_text(url_content)
        print(f"✓ Created {url_file.name}")
    
    # Print next steps
    print(f"\n✨ Day {day} is ready!")
    print(f"\n📝 Next steps:")
    print(f"   1. Open: {solution_file}")
    if not DOWNLOAD_INPUT or not input_file.read_text().strip() or input_file.read_text().startswith("#"):
        print(f"   2. Add your input to: {input_file}")
        print(f"      (or download from: {AOC_URL}/{year}/day/{day}/input)")
    print(f"   3. Run tests:")
    print(f"      → All tests:    pytest {test_file} -v -s")
    print(f"      → Part 1 only:  pytest {test_file}::TestDay{day:02d}::test_part_one_solution -v -s")
    print(f"      → Or run:       python {solution_file}")
    print(f"   4. View problem:  {AOC_URL}/{year}/day/{day}")


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python new_day.py <day> [year]")
        print("\nExamples:")
        print("  python new_day.py 5        # Create day 5 for current year")
        print("  python new_day.py 10 2024  # Create day 10 for 2024")
        print("\nConfiguration:")
        print(f"  Author: {AUTHOR}")
        print(f"  Auto-download: {'Enabled' if DOWNLOAD_INPUT else 'Disabled'}")
        if DOWNLOAD_INPUT and (not USER_SESSION_ID or USER_SESSION_ID == "YOUR_SESSION_ID_HERE"):
            print("  ⚠ Session ID not configured - edit new_day.py to enable downloads")
        sys.exit(1)
    
    try:
        day = int(sys.argv[1])
        year = int(sys.argv[2]) if len(sys.argv) > 2 else 2025
        
        if not (1 <= day <= 25):
            print("Error: Day must be between 1 and 25")
            sys.exit(1)
        
        if year < 2015:
            print("Error: Advent of Code started in 2015")
            sys.exit(1)
        
        create_day(day, year)
        
    except ValueError:
        print("Error: Day and year must be integers")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nCancelled by user")
        sys.exit(1)


if __name__ == "__main__":
    main()