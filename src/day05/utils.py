from typing import Generator
from io import TextIOWrapper

def get_input_provider(input_obj: str | TextIOWrapper) -> Generator[str, None, None]:
    if type(input_obj) == TextIOWrapper:
        with input_obj as f:
            for line in f:
                yield line.rstrip()
    elif type(input_obj) == str:
        for s in input_obj.split("\n"):
            yield s
    else:
        raise Exception("Invalid input type")
