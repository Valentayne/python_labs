import os
import matplotlib.pyplot as plt
import numpy as np
from lab3.task4.kmrcsv import KmrCsv
from lab3.task4.plots import Plots
from lab3.task4.statistics import Statistic


class KmrWork(KmrCsv, Statistic, Plots):
    kmrs = {}
    cat = 'kmr_results'

    def __init__(self, ref, num):
        super().__init__()
        self.set_ref(ref)
        self.set_num(num)
        self.set_cat(KmrWork.cat)
        self.read_csv()
        KmrWork.kmrs[num] = ref

    def compare_csv(self, other: 'KmrWork'):
        d1, d2 = self._data, other._data
        avg1 = d1['total_score'].mean()
        avg2 = d2['total_score'].mean()
        time1 = d1['time_minutes'].mean()
        time2 = d2['time_minutes'].mean()

        lines = [
            f"Порівняння КМР №{self._num} та КМР №{other._num}",
            f"Кількість виконаних КМР: {len(d1)} / {len(d2)}",
            f"Середній бал:            {avg1:.2f} / {avg2:.2f}",
            f"Середній час (хв):       {time1:.2f} / {time2:.2f}",
        ]
        report = '\n'.join(lines)
        print(report)
        path = os.path.join(KmrWork.cat, f'compare_{self._num}_vs_{other._num}.txt')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"Збережено: {path}")

    def compare_avg_plots(self, other: 'KmrWork'):
        avg1 = self.avg_stat()
        avg2 = other.avg_stat()
        n = max(len(avg1), len(avg2))
        x = np.arange(n)
        width = 0.35
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.bar(x - width/2, avg1[:n], width, label=f'КМР №{self._num}', color='steelblue')
        ax.bar(x + width/2, avg2[:n], width, label=f'КМР №{other._num}', color='coral')
        ax.set_title('Порівняння % правильних відповідей')
        ax.set_ylabel('% правильних відповідей')
        ax.set_xticks(x)
        ax.set_xticklabels([f'Q{i+1}' for i in range(n)])
        ax.legend()
        path = os.path.join(KmrWork.cat, f'compare_avg_{self._num}_vs_{other._num}.png')
        plt.savefig(path)
        plt.close()
        print(f"Збережено: {path}")