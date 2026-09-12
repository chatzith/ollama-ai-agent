# Ollama Agent

A small Python agent that classifies the contents of an input file as either
`Technical` or `General` using a local Ollama model.

## Requirements

- Python 3.13 or newer
- [Ollama](https://ollama.com/) installed and running
- The `mistral:latest` model available locally
- [`uv`](https://docs.astral.sh/uv/) for environment and dependency management

Pull the model before running the agent:

```powershell
ollama pull mistral:latest
```

## Usage

1. Place one input file in the `input/` directory next to `reader.py. The
	directory is created automatically if it does not exist.
2. Install the project dependencies:

	```powershell
	uv sync
	```

3. Run the agent:

	```powershell
	uv run .\main.py
	```

The agent asks Ollama for a JSON response with a `category` key and prints the
keys returned by the model. If the `input/` directory is empty, it prints
`No file found...` and does not call Ollama.

## Project Structure

```text
main.py       Run the classification request.
reader.py     Find and read the first file in input/.
input/        Place the file to classify here.
pyproject.toml Project metadata and dependencies.
```
