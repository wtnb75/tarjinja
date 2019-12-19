# copy directory
import os
import stat
import time
from typing import Generator, Tuple
from .iface import Input, Output
from logging import getLogger

log = getLogger(__name__)


class DirInput(Input):
    def walk(self) -> Generator[Tuple[str, int, float], None, None]:
        for root, dirs, files in os.walk(self.ifn):
            relpath = os.path.relpath(root, self.ifn)
            if relpath == ".":
                relpath = ""
            for fn in sorted(files):
                fromfn = os.path.join(root, fn)
                st = os.stat(fromfn)
                mode = st.st_mode
                yield os.path.join(relpath, fn), mode, st.st_mtime

    def readfile(self, fn: str) -> str:
        rfn = os.path.join(self.ifn, fn)
        if os.path.islink(rfn):
            return os.readlink(rfn)
        with open(rfn) as ifp:
            return ifp.read()


class SingleInput(Input):
    def walk(self) -> Generator[Tuple[str, int, float], None, None]:
        st = os.stat(self.ifn)
        yield os.path.basename(self.ifn), st.st_mode, st.st_mtime

    def readfile(self, fn: str) -> str:
        with open(self.ifn) as ifp:
            return ifp.read()


class DirOutput(Output):
    def writefile(self, fn: str, content: str, mode: int, ts: float = None):
        fname = os.path.join(self.ofn, fn)
        dirname = os.path.dirname(fname)
        os.makedirs(dirname, exist_ok=True)
        if (mode & stat.S_IFLNK) == stat.S_IFLNK:
            os.symlink(content, fname)
        else:
            with open(fname, "w") as ofp:
                ofp.write(content)
            os.chmod(fname, mode)
        if ts is not None:
            os.utime(fname, (ts, ts))


class ListOutput(Output):
    def writefile(self, fn: str, content: str, mode: int, ts: float = None):
        tsstr = "YYYY-mm-dd HH:MM"
        if ts is not None:
            tsstr = time.strftime("%Y-%m-%d %H:%M", time.localtime(ts))
        print("%o %d %s %s" % (mode, len(content), tsstr, fn))
