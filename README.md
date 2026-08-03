# Audio Data Collection

Audio files in Opus 48k format with metadata index.

## Contents

- `index.json` — metadata index
- `*.opus` — audio files
- `validate.py` — validation script

## Usage

```python
import json

with open('index.json') as f:
    index = json.load(f)

print(f"Files: {index['fileCount']}")
```

## License

CC0-1.0 / Public Domain
