
class Statistic:
    def _get_data(self):
        if not hasattr(self, '_data') or self._data is None:
            self.read_csv()
        return self._data

    def _question_cols(self):
        df = self._get_data()
        return [c for c in df.columns if c.startswith('q')]

    def avg_stat(self):
        df = self._get_data()
        q_cols = self._question_cols()
        percentages = tuple(round(df[c].mean() * 100, 2) for c in q_cols)
        return percentages

    def marks_stat(self):
        df = self._get_data()
        counts = df['total_score'].value_counts().sort_index()
        return dict(counts)

    def marks_per_time(self):
        df = self._get_data()
        result = {}
        for _, row in df.iterrows():
            student_id = row.iloc[0]
            time = row['time_minutes']
            score = row['total_score']
            result[student_id] = round(score / time, 3) if time > 0 else 0
        return result

    def best_marks_per_time(self, bottom_margin, top_margin):
        df = self._get_data()
        filtered = df[(df['total_score'] >= bottom_margin) & (df['total_score'] <= top_margin)].copy()
        filtered['mpt'] = filtered.apply(
            lambda r: round(r['total_score'] / r['time_minutes'], 3) if r['time_minutes'] > 0 else 0, axis=1
        )
        top5 = filtered.nlargest(5, 'mpt')
        return tuple(
            (row.iloc[0], row['total_score'], row['mpt'])
            for _, row in top5.iterrows()
        )

