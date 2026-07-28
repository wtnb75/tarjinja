import unittest

import tarjinja


class RevTest1(unittest.TestCase):
    s = "hello world"
    vals = {"name": "world", "dummy": [1, 2, 3]}

    def test_jinja(self):
        f = tarjinja.ReverseJinjaFilter()
        self.assertEqual("hello {{name}}", f.render(self.s, self.vals))

    def test_f(self):
        f = tarjinja.ReverseFstringFilter()
        self.assertEqual("hello {name}", f.render(self.s, self.vals))

    def test_template(self):
        f = tarjinja.ReverseTemplateFilter()
        self.assertEqual("hello ${name}", f.render(self.s, self.vals))

    def test_percent(self):
        f = tarjinja.ReversePercentFilter()
        self.assertEqual("hello %(name)s", f.render(self.s, self.vals))

    def test_format(self):
        f = tarjinja.ReverseFormatFilter()
        self.assertEqual("hello {name}", f.render(self.s, self.vals))

    def test_abstract(self):
        f = tarjinja.AbstractReverseFilter()
        with self.assertRaises(NotImplementedError):
            f.render(self.s, self.vals)
