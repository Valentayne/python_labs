
import os
import matplotlib.pyplot as plt

class Plots:
    def set_cat(self, cat):
        self._cat = cat
        os.makedirs(cat, exist_ok=True)

    def _cat_path(self, filename):
        cat = getattr(self, '_cat', '.')
        return os.path.join(cat, filename)

    def avg_plot(self, avg_tuple):
        questions = [f'Q{i+1}' for i in range(len(avg_tuple))]
        plt.figure(figsize=(10, 5))
        plt.bar(questions, avg_tuple, color='steelblue')
        plt.title(f'Відсоток правильних відповідей — КМР №{getattr(self, "_num", "")}')
        plt.ylabel('% правильних відповідей')
        plt.ylim(0, 100)
        path = self._cat_path(f'avg_plot_kmr{getattr(self, "_num", "")}.png')
        plt.savefig(path)
        plt.close()
        print(f"Збережено: {path}")

    def marks_plot(self, marks_dict):
        labels = list(map(str, marks_dict.keys()))
        values = list(marks_dict.values())
        plt.figure(figsize=(8, 5))
        plt.bar(labels, values, color='coral')
        plt.title(f'Розподіл оцінок — КМР №{getattr(self, "_num", "")}')
        plt.xlabel('Оцінка')
        plt.ylabel('Кількість студентів')
        path = self._cat_path(f'marks_plot_kmr{getattr(self, "_num", "")}.png')
        plt.savefig(path)
        plt.close()
        print(f"Збережено: {path}")

    def best_marks_plot(self, best_tuple):
        if not best_tuple:
            print("Немає даних для побудови графіка топ-5.")
            return
        ids = [str(t[0]) for t in best_tuple]
        mpts = [t[2] for t in best_tuple]
        plt.figure(figsize=(8, 5))
        plt.bar(ids, mpts, color='mediumseagreen')
        plt.title(f'Топ-5: середній бал за хвилину — КМР №{getattr(self, "_num", "")}')
        plt.xlabel('ID студента')
        plt.ylabel('Бал/хвилина')
        path = self._cat_path(f'best_marks_plot_kmr{getattr(self, "_num", "")}.png')
        plt.savefig(path)
        plt.close()
        print(f"Збережено: {path}")
