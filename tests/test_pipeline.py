import os
import unittest
import time
import tempfile
import test.support
import tarjinja


class PipeTest(unittest.TestCase):
    def test_pipe(self):
        tf = tempfile.NamedTemporaryFile()
        s = "hello ${name}"
        expstr = "hello world"
        with open(tf.name, "w") as ofp:
            ofp.write(s)
        input = tarjinja.SingleInput(tf.name)
        output = tarjinja.ListOutput("dummy")
        f = tarjinja.MultiFilter([])
        f.add_filter(tarjinja.TemplateFilter())
        pl = tarjinja.Pipeline(input, f, output)
        with test.support.captured_stdout() as outs:
            pl.render({"name": "world"})
        mode = os.stat(tf.name).st_mode
        ts = time.strftime(
            "%Y-%m-%d %H:%M", time.localtime(os.stat(tf.name).st_mtime))
        expected = "%o %d %s %s\n" % (
            mode, len(expstr), ts, os.path.basename(tf.name))
        self.assertEquals(expected, outs.getvalue())
