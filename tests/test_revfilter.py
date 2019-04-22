import unittest
import tarjinja


class RevTest1(unittest.TestCase):
    s = "hello world"
    vals = {"name": "world", "dummy": [1, 2, 3]}

    def TestJinja(self):
        f = tarjinja.ReverseJinjaFilter()
        self.assertEquals("hello {{name}}", f.render(self.s, self.vals))

    def TestF(self):
        f = tarjinja.ReverseFstringFilter()
        self.assertEquals("hello {name}", f.render(self.s, self.vals))

    def TestTemplate(self):
        f = tarjinja.ReverseTemplateFilter()
        self.assertEquals("hello ${name}", f.render(self.s, self.vals))

    def TestPercent(self):
        f = tarjinja.ReversePercentFilter()
        self.assertEquals("hello %(name)s", f.render(self.s, self.vals))

    def TestFormat(self):
        f = tarjinja.ReverseFormatFilter()
        self.assertEquals("hello {name}", f.render(self.s, self.vals))

    def TestAbstract(self):
        f = tarjinja.AbstractReverseFilter()
        with self.assertRaises(NotImplementedError):
            f.render(self.s, self.vals)
