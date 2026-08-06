from pathlib import Path

root = Path(".")

# Count folders whose names start with 4 digits
count = sum(
    1
    for p in root.iterdir()
    if p.is_dir() and len(p.name) >= 4 and p.name[:4].isdigit()
)

template = Path(".github/README.template.md").read_text()

template = template.replace("{{SOLVED}}", str(count))

Path("README.md").write_text(template)

print(f"Updated README ({count} problems)")