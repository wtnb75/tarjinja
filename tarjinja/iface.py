import fnmatch
import copy
import braceexpand
from typing import Generator, Tuple
from logging import getLogger

log = getLogger(__name__)


class Input:
    def __init__(self, ifn: str, **kwargs):
        self.ifn = ifn

    def walk(self) -> Generator[Tuple[str, int, float], None, None]:
        raise NotImplementedError("walk")

    def readfile(self, fn: str) -> str:
        raise NotImplementedError("readfile")


class Filter:
    def __init__(self, **kwargs):
        pass

    def render(self, s: str, vals: dict) -> str:
        raise NotImplementedError("render")

    def renderfn(self, s: str, vals: dict) -> Generator[str, None, None]:
        return braceexpand.braceexpand(self.render(s, vals))

    def strtr(self, strng: str, replace: dict) -> str:
        # https://stackoverflow.com/questions/10931150/phps-strtr-for-python
        buffer = []
        i, n = 0, len(strng)
        while i < n:
            match = False
            for s, r in replace.items():
                if strng[i:len(s) + i] == s:
                    buffer.append(r)
                    i = i + len(s)
                    match = True
                    break
            if not match:
                buffer.append(strng[i])
                i = i + 1
        return ''.join(buffer)


class Output:
    def __init__(self, ofn: str, **kwargs):
        self.ofn = ofn

    def writefile(self, fn: str, content: str, mode: int, ts: float = None):
        raise NotImplementedError("writefile")

    def finish(self):
        log.debug("finished %s", self.ofn)


class Pipeline:
    def __init__(self, inp: Input, filt: Filter, outp: Output, passpat: str = None):
        self.inp = inp
        self.filt = filt
        self.outp = outp
        self.passpat = passpat

    def render(self, vals: dict):
        for fnpat, mode, ts in self.inp.walk():
            log.debug("walk %s (%o)", fnpat, mode)
            content = self.inp.readfile(fnpat)
            for fn in self.filt.renderfn(fnpat, vals):
                if self.passpat is not None and fnmatch.fnmatch(fn, self.passpat):
                    self.outp.writefile(fnpat, content, mode, ts)
                else:
                    v = copy.deepcopy(vals)
                    v["fname"] = fn
                    ocont = self.filt.render(content, v)
                    log.debug("write %s", fn)
                    self.outp.writefile(fn, ocont, mode, ts)
        self.outp.finish()
