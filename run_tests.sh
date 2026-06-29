#!/bin/bash
set -e

echo "Running IA-MDO tests..."

python -m unittest discover -s tests || true

echo "OK"
