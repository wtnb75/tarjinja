from typing import List
from logging import getLogger
import string
import re

from .iface import Filter


log = getLogger(__name__)


class TemplateFilter(Filter):
    pattern = string.Template.pattern

    def render(self, s: str, vals: dict) -> str:
        return string.Template(s).substitute(**vals)

    def var_names(self, s: str) -> List[str]:
        res = set()
        for i in self.pattern.finditer(s):
            v = i.group('braced')
            log.debug("found %s", v)
            if v is not None:
                res.add(v)
        log.debug("vars: %s", res)
        return res


class FormatFilter(TemplateFilter):
    pattern = re.compile(
        '(\{\{)*\{(?P<braced>(?a:[_a-z][_a-z0-9]*))\}(\}\})*', re.IGNORECASE | re.VERBOSE)

    def render(self, s: str, vals: dict) -> str:
        return s.format(**vals)


class PercentFilter(TemplateFilter):
    pattern = re.compile(
        '(\%\%)*\%\((?P<braced>(?a:[_a-z][_a-z0-9]*))\)', re.IGNORECASE | re.VERBOSE)

    def render(self, s: str, vals: dict) -> str:
        return s % vals


class FstringFilter(FormatFilter):
    def render(self, s: str, vals: dict) -> str:
        return eval("f" + repr(s), vals, {})
