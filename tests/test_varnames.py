import unittest
import tarjinja


class VarNamasTest(unittest.TestCase):
    def test_jinja(self):
        f = tarjinja.JinjaFilter()
        r = f.var_names("hello {{name}}")
        self.assertIn("name", r)

    def test_template(self):
        f = tarjinja.TemplateFilter()
        r = f.var_names("hello ${name}")
        self.assertIn("name", r)
        r = f.var_names("hello $$${name}")
        self.assertIn("name", r)
        r = f.var_names("hello $${name}")
        self.assertNotIn("name", r)

    def test_format(self):
        f = tarjinja.FormatFilter()
        r = f.var_names("hello {name}")
        self.assertIn("name", r)

    def test_percent(self):
        f = tarjinja.PercentFilter()
        r = f.var_names("hello %(name)s")
        self.assertIn("name", r)

    def test_fstr(self):
        f = tarjinja.FstringFilter()
        r = f.var_names("hello {name}")
        self.assertIn("name", r)
