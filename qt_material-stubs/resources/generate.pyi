import os
from pathlib import Path
from typing import Tuple

HOME: Path
RESOURCES_PATH: str

class ResourseGenerator:
    index: str
    contex: list[Tuple[str, str]]
    source: os.PathLike[str]
    secondary: str
    def __init__(
        self,
        primary: str,
        secondary: str,
        disabled: str,
        source: os.PathLike[str],
        parent: str = ...,
    ) -> None: ...
    def generate(self) -> None: ...
    def replace_color(self, content: str, replace: str, color: str = ...) -> str: ...
