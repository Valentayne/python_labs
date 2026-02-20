import pandas as pd

class KmrCsv:
    ref = 'kmr_default.csv'
    num = 0

    def __init__(self):
        self._ref = KmrCsv.ref
        self._num = KmrCsv.num
        self._data = None

    def set_ref(self, ref):
        self._ref = ref

    def get_ref(self):
        return self._ref

    def set_num(self, num):
        self._num = num

    def read_csv(self):
        self._data = pd.read_csv(self._ref)
        return self._data

    def file_info(self):
        if self._data is None:
            self.read_csv()
        print(f"КМР №{self._num}: виконали {len(self._data)} студентів, файл: {self._ref}")
        return len(self._data)
