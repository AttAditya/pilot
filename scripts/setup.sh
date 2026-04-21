echo "Starting setup..."

if [ -z "$(which python3.14)" ]; then
  echo "Python3.14 is not installed."
  echo "Please install Python3.14 and try again."
  exit 1
fi

echo "Setting up virtual environment..."
python3.14 -m venv .venv
source .venv/bin/activate
echo "Installing dependencies..."
pip install -r requirements.txt

echo "Set up complete!"

