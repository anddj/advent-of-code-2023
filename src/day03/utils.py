from typing import Generator

def get_input_provider(file_path: str) -> Generator[str, None, None]:
    with open(file_path) as f:
        for line in f:
            yield line.rstrip()
