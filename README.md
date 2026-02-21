
---

## 🧪 Тестування

Для тестування використовується:
- `pytest`
- `allure-pytest`

Тести автоматично запускаються через **GitHub Actions**  
та формують **Allure Report**, який публікується на GitHub Pages.

---

## 📊 Allure Report

👉 **Онлайн-звіт з тестування:**  
🔗 https://valentayne.github.io/python_labs/

У звіті доступні:
- Feature / Story структура
- Статус тестів (passed / failed)
- Детальна інформація про кожен тест

---

## ▶️ Локальний запуск тестів

```bash
pip install -r requirements.txt
pytest --alluredir=allure-results
allure serve allure-results