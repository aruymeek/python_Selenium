class StockModel:

    def __init__(self, _nat, _idx, _now, _diff, _pct):
        self.nation = _nat
        self.index = _idx
        self.now = _now
        self.diff = _diff
        self.percent = _pct

    def SaveFormat(self):
        line = '{0};{1};{2};{3};{4}'.format(self.nation, self.index, self.now, self.diff, self.percent)

        return line

    def ReadFormat(self):
        if self.percent < 0:
            line = '[{0}] {1} | 현재가: {2} (전일대비 ▼{3}) | 등락률: {4}%'.format(self.nation, self.index, self.now, self.diff, self.percent)
        else:
            line = '[{0}] {1} | 현재가: {2} (전일대비 ▲{3}) | 등락률: {4}%'.format(self.nation, self.index, self.now, self.diff, self.percent)

        return line



