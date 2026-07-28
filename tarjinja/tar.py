import io
import os
import tarfile
import time
from collections.abc import Generator
from logging import getLogger

from .iface import Input, Output

log = getLogger(__name__)


class TarInput(Input):
    def __init__(self, ifn: str, **kwargs):
        super().__init__(ifn)
        self.tf = tarfile.open(ifn)
        self.encoding = "utf-8"

    def walknext(self) -> Generator[tuple[str, int, float], None, None]:
        # does not work?
        while True:
            n = self.tf.next()
            log.info("next %s", n)
            if n is None:
                break
            if not n.isfile():
                continue
            yield n.name, n.mode, n.mtime

    def walk(self) -> Generator[tuple[str, int, float], None, None]:
        for n in self.tf.getmembers():
            if not n.isfile():
                continue
            yield n.name, n.mode, n.mtime

    def readfile(self, fn: str) -> str:
        return self.tf.extractfile(fn).read().decode(self.encoding)


class TarOutput(Output):
    def __init__(self, ofn: str, **kwargs):
        super().__init__(ofn)
        _base, ext = os.path.splitext(ofn)
        ext = ext[1:]
        if ext == "tar":
            ext = ""
        self.tf = tarfile.open(ofn, f"w:{ext}")
        self.encoding = "utf-8"
        self.owner = "root"
        self.group = "root"

    def writefile(self, fn: str, content: str, mode: int, ts: float | None = None):
        bcont = content.encode(self.encoding)
        tinfo = tarfile.TarInfo(fn)
        tinfo.size = len(bcont)
        tinfo.mode = mode
        tinfo.type = tarfile.REGTYPE
        tinfo.uname = self.owner
        tinfo.gname = self.group
        if ts is None:
            tinfo.mtime = time.time()
        else:
            tinfo.mtime = ts
        self.tf.addfile(tinfo, io.BytesIO(bcont))

    def finish(self):
        self.tf.close()
