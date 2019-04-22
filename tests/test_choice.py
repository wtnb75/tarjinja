import unittest
import tarjinja


class TJTest1(unittest.TestCase):
    def TestInput(self):
        self.assertTrue("Tar" in dict(tarjinja.input_items()))
        self.assertFalse("blabla" in dict(tarjinja.input_items()))

    def TestOutput(self):
        self.assertTrue("Tar" in dict(tarjinja.output_items()))
        self.assertFalse("blabla" in dict(tarjinja.output_items()))

    def TestFilter(self):
        self.assertTrue("Jinja" in dict(tarjinja.filter_items()))
        self.assertFalse("blabla" in dict(tarjinja.filter_items()))
