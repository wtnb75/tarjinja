import unittest
import tempfile
import time
import tarjinja
from logging import getLogger

log = getLogger(__name__)


class InOutTest(unittest.TestCase):
    data = {
        "hello": "world",
        "abcde/efg": "xyzxyzxyz\n",
        "abcde/efg2": "xyzxyzxyz\n",
    }

    def output(self, output, data, tsnow):
        for k, v in data.items():
            output.writefile(k, v, 0o644, tsnow)
        output.finish()

    def check(self, input, data, tsnow):
        checked = set()
        for fn, mode, ts in input.walk():
            checked.add(fn)
            if tsnow is not None:
                self.assertTrue(abs(tsnow - ts) < 2)
            self.assertEqual(0o644, mode & 0o777)
            self.assertTrue(fn in data)
            self.assertEqual(data.get(fn), input.readfile(fn))
        self.assertEqual(set(data.keys()), checked)

    def TestTarXZ(self):
        tf = tempfile.NamedTemporaryFile(suffix=".tar.xz")
        now = time.time()
        taro = tarjinja.TarOutput(tf.name)
        self.output(taro, self.data, now)
        tari = tarjinja.TarInput(tf.name)
        self.check(tari, self.data, now)

    def TestTar(self):
        tf = tempfile.NamedTemporaryFile(suffix=".tar")
        now = time.time()
        taro = tarjinja.TarOutput(tf.name)
        self.output(taro, self.data, now)
        tari = tarjinja.TarInput(tf.name)
        self.check(tari, self.data, now)

    def TestZip(self):
        tf = tempfile.NamedTemporaryFile(suffix=".zip")
        now = time.time()
        taro = tarjinja.ZipOutput(tf.name)
        self.output(taro, self.data, now)
        tari = tarjinja.ZipInput(tf.name)
        self.check(tari, self.data, now)

    def TestDir(self):
        tf = tempfile.TemporaryDirectory()
        now = time.time()
        taro = tarjinja.DirOutput(tf.name)
        self.output(taro, self.data, now)
        tari = tarjinja.DirInput(tf.name)
        self.check(tari, self.data, now)

    def TestMem(self):
        taro = tarjinja.MemOutput("dummy")
        self.output(taro, self.data, None)
        tari = tarjinja.MemInput("dummy")
        for k, v in taro.items():
            tari[k] = v
        self.check(tari, self.data, None)
