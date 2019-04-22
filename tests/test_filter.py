import unittest
import tarjinja


class FilterTest(unittest.TestCase):
    def test_jinja(self):
        f = tarjinja.JinjaFilter()
        r = f.render("hello {{name}}", {"name": "world"})
        self.assertEqual(r, "hello world")

    def test_jinjabrace(self):
        f = tarjinja.JinjaFilter()
        r = f.render("hello {{names|brace}}", {"names": ["world", "order"]})
        self.assertEqual(r, "hello {world,order}")

    def test_template(self):
        f = tarjinja.TemplateFilter()
        r = f.render("hello ${name}", {"name": "world"})
        self.assertEqual(r, "hello world")
        r = f.render("hello $name", {"name": "world"})
        self.assertEqual(r, "hello world")

    def test_format(self):
        f = tarjinja.FormatFilter()
        r = f.render("hello {name}", {"name": "world"})
        self.assertEqual(r, "hello world")

    def test_percent(self):
        f = tarjinja.PercentFilter()
        r = f.render("hello %(name)s", {"name": "world"})
        self.assertEqual(r, "hello world")

    def test_fstr(self):
        f = tarjinja.FstringFilter()
        r = f.render("hello {name}", {"name": "world"})
        self.assertEqual(r, "hello world")
