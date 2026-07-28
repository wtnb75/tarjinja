import time
from collections.abc import Generator
from logging import getLogger

from .iface import Input, Output

log = getLogger(__name__)


class MemInput(Input, dict):
    def __init__(self, fn: str):
        super().__init__(fn)
        self.mode = 0o644
        self.ts = time.time()

    def walk(self) -> Generator[tuple[str, int, float], None, None]:
        for k in self.keys():
            yield k, self.mode, self.ts

    def readfile(self, fn: str) -> str:
        return self.get(fn)


class MemOutput(Output, dict):
    def __init__(self, fn: str):
        super().__init__(fn)

    def writefile(self, fn: str, content: str, mode: int, ts: float | None = None):
        self[fn] = content
