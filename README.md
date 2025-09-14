# Python UV Starter

This is a simple Python [uv](https://docs.astral.uv) starter in Firebase Studio.

## Running

```
uv run main.py
```

## Add dependencies

```
uv add ruff
```

## Virtual Environment

To create a virtual environment:
```
uv venv
```

To activate the virtual environment:

**Linux/macOS (bash/zsh):**
```
source .venv/bin/activate
```

**Fish:**
```
source .venv/bin/activate.fish
```

**Windows (PowerShell):**
```
.venv\Scripts\Activate.ps1
```

To deactivate the virtual environment:
```
deactivate
```

## Catatan Penting

Setiap membuka/membuat terminal baru, wajib mengaktifkan *virtual environment* dengan cara:
```bash
source .venv/bin/activate
```

## Running FastAPI in Development

To run a FastAPI project in development mode:
```
uv run fastapi dev
```

## Troubleshooting

### PylintE0401:import-error for FastAPI

If you encounter an `Unable to import 'fastapi' (PylintE0401:import-error)` message in your IDE, it's likely that the linter is not using the correct Python environment.

To fix this, you need to configure your IDE to use the Python interpreter from the `uv` virtual environment.

**For VS Code:**

1.  Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on macOS).
2.  Type `Python: Select Interpreter` and select it.
3.  Choose the interpreter that points to your virtual environment's Python executable (e.g., `./.venv/bin/python`).

For other IDEs, look for similar settings to change the Python interpreter or Python path. The path to the interpreter will be `<your_project_folder>/.venv/bin/python`.
