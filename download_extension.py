"""
Download and extract GitHub Copilot extension metadata.
Extracts settings, commands, and other configuration from package.json.
"""

import json
import os
import zipfile
import requests
from pathlib import Path

# Extension details
EXTENSIONS = {
    "copilot": {
        "publisher": "GitHub",
        "name": "copilot",
        "display_name": "GitHub Copilot"
    },
    "copilot-chat": {
        "publisher": "GitHub",
        "name": "copilot-chat",
        "display_name": "GitHub Copilot Chat"
    }
}

EXTENSIONS_DIR = "extensions"
OUTPUT_DIR = "extension_metadata"

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (compatible; ExtensionDownloader/1.0)"
})


def download_extension(publisher, extension_name, display_name):
    """Download a VS Code extension .vsix file."""

    # VS Code Marketplace API endpoint
    url = f"https://{publisher}.gallery.vscodeassets.com/_apis/public/gallery/publisher/{publisher}/extension/{extension_name}/latest/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage"

    # Alternative URL format
    alt_url = f"https://marketplace.visualstudio.com/_apis/public/gallery/publishers/{publisher}/vsextensions/{extension_name}/latest/vspackage"

    output_file = os.path.join(EXTENSIONS_DIR, f"{extension_name}.vsix")

    print(f"\n{'='*60}")
    print(f"Downloading {display_name}...")
    print(f"{'='*60}")

    os.makedirs(EXTENSIONS_DIR, exist_ok=True)

    # Try primary URL first
    try:
        print(f"Trying: {alt_url}")
        resp = session.get(alt_url, timeout=60, stream=True)
        resp.raise_for_status()

        with open(output_file, 'wb') as f:
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)

        file_size = os.path.getsize(output_file)
        print(f"✓ Downloaded: {output_file} ({file_size / 1024 / 1024:.1f} MB)")
        return output_file

    except Exception as e:
        print(f"✗ Failed: {e}")
        return None


def extract_extension(vsix_file, extension_name):
    """Extract .vsix file (it's a zip archive)."""

    extract_dir = os.path.join(EXTENSIONS_DIR, extension_name)

    print(f"\nExtracting {vsix_file}...")

    try:
        with zipfile.ZipFile(vsix_file, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)

        print(f"✓ Extracted to: {extract_dir}")
        return extract_dir

    except Exception as e:
        print(f"✗ Extraction failed: {e}")
        return None


def parse_package_json(extension_dir, extension_name):
    """Parse package.json and extract metadata."""

    package_json_path = os.path.join(extension_dir, "extension", "package.json")

    if not os.path.exists(package_json_path):
        print(f"✗ package.json not found at {package_json_path}")
        return None

    print(f"\nParsing package.json...")

    with open(package_json_path, 'r', encoding='utf-8') as f:
        package_data = json.load(f)

    # Extract key information
    metadata = {
        "name": package_data.get("name"),
        "displayName": package_data.get("displayName"),
        "version": package_data.get("version"),
        "description": package_data.get("description"),
        "publisher": package_data.get("publisher"),
        "repository": package_data.get("repository"),
        "contributes": package_data.get("contributes", {}),
    }

    contributes = metadata["contributes"]

    # Count settings (handle both dict and list format)
    config = contributes.get('configuration', {})
    if isinstance(config, list):
        total_settings = sum(len(c.get('properties', {})) for c in config)
    else:
        total_settings = len(config.get('properties', {}))

    # Count what we found
    print(f"\n{'='*60}")
    print(f"Extension: {metadata['displayName']} v{metadata['version']}")
    print(f"{'='*60}")
    print(f"Settings:     {total_settings}")
    print(f"Commands:     {len(contributes.get('commands', []))}")
    print(f"Keybindings:  {len(contributes.get('keybindings', []))}")
    print(f"Views:        {len(contributes.get('views', {}))}")
    print(f"Menus:        {len(contributes.get('menus', {}))}")

    # Save full package.json
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_file = os.path.join(OUTPUT_DIR, f"{extension_name}_package.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(package_data, f, indent=2, ensure_ascii=False)
    print(f"\n✓ Saved full package.json: {output_file}")

    return metadata


def extract_settings(metadata, extension_name):
    """Extract and format all settings."""

    config = metadata["contributes"].get("configuration", {})

    # Handle both single config and array of configs
    if isinstance(config, dict):
        configs = [config]
    else:
        configs = config

    all_settings = {}

    for cfg in configs:
        properties = cfg.get("properties", {})
        all_settings.update(properties)

    if not all_settings:
        print(f"No settings found for {extension_name}")
        return

    # Save settings
    output_file = os.path.join(OUTPUT_DIR, f"{extension_name}_settings.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_settings, f, indent=2, ensure_ascii=False)
    print(f"✓ Saved settings: {output_file}")

    # Create markdown documentation
    md_file = os.path.join(OUTPUT_DIR, f"{extension_name}_settings.md")
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(f"# {metadata['displayName']} - Settings Reference\n\n")
        f.write(f"Version: {metadata['version']}\n\n")
        f.write(f"Total settings: {len(all_settings)}\n\n")
        f.write("---\n\n")

        for setting_key in sorted(all_settings.keys()):
            setting = all_settings[setting_key]

            f.write(f"## `{setting_key}`\n\n")

            desc = setting.get('description', setting.get('markdownDescription', 'No description'))
            f.write(f"{desc}\n\n")

            f.write(f"- **Type**: `{setting.get('type', 'unknown')}`\n")

            if 'default' in setting:
                default = json.dumps(setting['default'])
                f.write(f"- **Default**: `{default}`\n")

            if 'enum' in setting:
                f.write(f"- **Options**: {', '.join([f'`{v}`' for v in setting['enum']])}\n")

            if 'scope' in setting:
                f.write(f"- **Scope**: {setting['scope']}\n")

            f.write("\n")

    print(f"✓ Saved settings docs: {md_file}")


def extract_commands(metadata, extension_name):
    """Extract and format all commands."""

    commands = metadata["contributes"].get("commands", [])

    if not commands:
        print(f"No commands found for {extension_name}")
        return

    # Save commands
    output_file = os.path.join(OUTPUT_DIR, f"{extension_name}_commands.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(commands, f, indent=2, ensure_ascii=False)
    print(f"✓ Saved commands: {output_file}")

    # Create markdown documentation
    md_file = os.path.join(OUTPUT_DIR, f"{extension_name}_commands.md")
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(f"# {metadata['displayName']} - Commands Reference\n\n")
        f.write(f"Version: {metadata['version']}\n\n")
        f.write(f"Total commands: {len(commands)}\n\n")
        f.write("---\n\n")

        for cmd in commands:
            f.write(f"## `{cmd.get('command')}`\n\n")

            if 'title' in cmd:
                f.write(f"**{cmd['title']}**\n\n")

            if 'category' in cmd:
                f.write(f"Category: {cmd['category']}\n\n")

            if 'enablement' in cmd:
                f.write(f"Enablement: `{cmd['enablement']}`\n\n")

            f.write("\n")

    print(f"✓ Saved commands docs: {md_file}")


def extract_keybindings(metadata, extension_name):
    """Extract keybindings."""

    keybindings = metadata["contributes"].get("keybindings", [])

    if not keybindings:
        return

    output_file = os.path.join(OUTPUT_DIR, f"{extension_name}_keybindings.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(keybindings, f, indent=2, ensure_ascii=False)
    print(f"✓ Saved keybindings: {output_file}")


def main():
    print("GitHub Copilot Extension Metadata Extractor")
    print("=" * 60)

    for ext_key, ext_info in EXTENSIONS.items():
        # Download extension
        vsix_file = download_extension(
            ext_info["publisher"],
            ext_info["name"],
            ext_info["display_name"]
        )

        if not vsix_file:
            continue

        # Extract extension
        extract_dir = extract_extension(vsix_file, ext_info["name"])

        if not extract_dir:
            continue

        # Parse package.json
        metadata = parse_package_json(extract_dir, ext_info["name"])

        if not metadata:
            continue

        # Extract specific data
        extract_settings(metadata, ext_info["name"])
        extract_commands(metadata, ext_info["name"])
        extract_keybindings(metadata, ext_info["name"])

    print(f"\n{'='*60}")
    print("✓ Extraction complete!")
    print(f"{'='*60}")
    print(f"Output directory: {OUTPUT_DIR}/")
    print("\nGenerated files:")
    print("  - *_package.json     (Full package.json)")
    print("  - *_settings.json    (All settings)")
    print("  - *_settings.md      (Settings documentation)")
    print("  - *_commands.json    (All commands)")
    print("  - *_commands.md      (Commands documentation)")
    print("  - *_keybindings.json (Keybindings)")


if __name__ == "__main__":
    main()
