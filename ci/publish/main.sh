#!/usr/bin/env bash
set -e

echo "Upgrading pip and installing deps..."
python3 -m pip install --upgrade pip
pip install build requests tomli twine

echo "Checking version mismatch..."
PUBLISH=$(python3 << 'EOF'
import requests, tomli

with open("pyproject.toml", "rb") as f:
  data = tomli.load(f)

name = data["project"]["name"]
local_version = data["project"]["version"]

try:
  res = requests.get(f"https://pypi.org/pypi/{name}/json", timeout=5)
  res.raise_for_status()
  pypi_version = res.json()["info"]["version"]
except:
  pypi_version = None

print(str(local_version != pypi_version).lower())
EOF
)

echo "Should publish: $PUBLISH"

if [ "$PUBLISH" != "true" ]; then
  echo "Version already exists on PyPI, skipping."
  exit 0
fi

echo "Building package..."
python3 -m build

echo "Publishing to PyPI via OIDC..."
twine upload dist/*

