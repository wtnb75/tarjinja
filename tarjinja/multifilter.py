from .iface import Filter


class MultiFilter(Filter):
    def __init__(self, filters=None):
        self.filters = [] if filters is None else filters

    def add_filter(self, flt):
        self.filters.append(flt)

    def render(self, s: str, vals: dict) -> str:
        for filt in self.filters:
            s = filt.render(s, vals)
        return s
