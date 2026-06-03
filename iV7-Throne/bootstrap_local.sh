#!/bin/bash
set -e

echo "Setting up iV7-Throne environment..."

python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

mkdir -p data/snapshots data/raw_archive_links reports
touch data/raw_archive_links/.gitkeep

echo "Setup complete. Activate with: source venv/bin/activate"
echo "Test with: python scripts/archive_api.py --url https://example.com"
