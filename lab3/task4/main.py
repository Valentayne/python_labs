
import os
import pandas as pd
import numpy as np

from lab3.task4.kmrwork import KmrWork

def generate_sample_csv(path, num_students=20, num_questions=5, seed=42):
    np.random.seed(seed)
    rows = []
    for i in range(1, num_students + 1):
        time_min = np.random.randint(20, 60)
        answers = np.random.randint(0, 2, num_questions).tolist()
        total = sum(answers) * 20  # max 100
        rows.append([f'S{i:03d}', time_min] + answers + [total])
    cols = ['id', 'time_minutes'] + [f'q{j+1}' for j in range(num_questions)] + ['total_score']
    df = pd.DataFrame(rows, columns=cols)
    df.to_csv(path, index=False)
    print(f"Згенеровано: {path}")


if __name__ == '__main__':
    os.makedirs('kmr_results', exist_ok=True)

    generate_sample_csv('kmr1.csv', seed=1)
    generate_sample_csv('kmr2.csv', seed=42)

    print("\n=== Створення об'єктів KmrWork ===")
    kmr1 = KmrWork('kmr1.csv', num=1)
    kmr2 = KmrWork('kmr2.csv', num=2)

    kmr1.file_info()
    kmr2.file_info()

    print("\n=== avg_plot() та marks_plot() для kmr2 ===")
    kmr2.avg_plot(kmr2.avg_stat())
    kmr2.marks_plot(kmr2.marks_stat())

    print("\n=== compare_csv() ===")
    KmrWork.compare_csv(kmr1, kmr2)

    print("\n=== compare_avg_plots() ===")
    KmrWork.compare_avg_plots(kmr1, kmr2)

    print("\n=== Топ-5 балів за хвилину (kmr1, оцінки 40-100) ===")
    best = kmr1.best_marks_per_time(40, 100)
    for item in best:
        print(f"  ID: {item[0]}, Оцінка: {item[1]}, Бал/хв: {item[2]}")