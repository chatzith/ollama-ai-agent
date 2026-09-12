"""Categorize file content with an Ollama language model."""

import json

from ollama import generate

from reader import prepare


def main() -> None:
    """Classify the first file in the input directory with Ollama."""

    content = prepare()
    if not isinstance(content, bytes):
        print("No file found...")
        return

    prompt = f"""
You are an experienced IT Office Engineer.
Read the content {content} and categorize it Technical or General.
The response must be in JSON format with the key 'category'. Don't include any other information.
"""

    response = generate(
        model="mistral:latest",
        prompt=prompt,
        format="json",
        stream=False,
    )
    result = json.loads(response.response)
    print(result["category"])


if __name__ == "__main__":
    main()
