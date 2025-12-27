# primera version
source .venv/bin/activate
python mabel.py generate contracts/User.yaml

Tests snapshot
pytest /app > console.result 2>&1

pytest -q > console.result 2>&1