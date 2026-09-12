"""Read the source content used by the Ollama agent."""

import os
from pathlib import Path


def prepare() -> bytes:
    """Return the contents of a file as raw bytes."""

    app_path = Path(__file__).parent.resolve()
    input_path = Path.joinpath(app_path, "input")

    if not os.path.exists(input_path):
        os.makedirs(input_path)

    files = [f for f in os.listdir(input_path)]

    if len(files) > 0:
        with open(Path.joinpath(input_path, files[0]).resolve(), "rb") as f:
            content = f.read()
        return content

    return False
