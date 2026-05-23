<div align="center">
  <h1>Тестирование приложения Automation Exercise</h1>
  <p>
    <strong>Python • Playwright</strong>
  </p>

[![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-9.0-orange?logo=pytest)](https://docs.pytest.org/)
[![Playwright](https://img.shields.io/badge/Playwright-1.59-blue?logo=playwright)](https://www.playwright.dev/)
[![Allure](https://img.shields.io/badge/Allure-2.15-purple?logo=allure)](https://allurereport.org/)
</div>

------------------------------------------------------------------------

## 📌 О проекте

Автоматизация тестирования веб-приложения [Automation Exercise](https://automationexercise.com).  

📋 Чек-листы тестирования:\
👉 UI - https://github.com/iivanitskiy/automation-exercise/blob/main/docs/UI_CHECKLIST.md\
👉 API - https://github.com/iivanitskiy/automation-exercise/blob/main/docs/API_CHECKLIST.md

------------------------------------------------------------------------

## 🛠️ Технологический стек

| Инструмент | Назначение |
|----------|------------|
| **Python** | Написание тестов |
| **Pytest** | Фреймворк для запуска тестов |
| **Playwright** | Управление браузером для UI-тестов |
| **Requests** | Выполнение HTTP-запросов для API-тестов |
| **Allure** | Генерация детальных отчетов |
| **Page Object Model** | Паттерн для структурирования UI-локаторов и логики |

------------------------------------------------------------------------

## Архитектура

```
automation-exercise-test/
├── config/                 # Настройки
├── docs/                   # Чек-листы
├── src/automation_exercise/
│   ├── api/                # API client, services, assertions
│   ├── data/               # Test data factory (Faker)
│   └── ui/                 # Page Object Model, components
├── tests/
│   ├── api/                # 14 API сценариев
│   └── ui/                 # 26 UI сценариев
└── testdata/               # Файлы для upload-тестов
```

### Best practices

- **Page Object Model** — страницы и компоненты (Header)
- **Service layer для API** — отдельные классы по доменам
- **Тестовые данные** — уникальные пользователи через Faker
- **Конфигурация через env** — `BASE_URL`, `HEADLESS`, таймауты
- **Маркеры pytest** — `smoke`, `ui`, `api`, `regression`
- **Фикстуры** — lifecycle пользователей (create → test → delete)
- **Playwright auto-waiting** — `expect()` вместо sleep
- **Параллельный запуск** — `pytest-xdist`

## Быстрый старт

```bash
# 1. Виртуальное окружение
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/macOS

# 2. Зависимости
pip install -r requirements.txt
playwright install chromium

# 3. Конфиг (опционально)
copy .env.example .env

# 4. Запуск
pytest                          # все тесты
pytest tests/api -m api         # только API
pytest tests/ui -m smoke        # smoke UI
pytest -n auto                  # параллельно
```

## Allure-отчёты

1. Установите [Allure CLI](https://allurereport.org/docs/install/) (`scoop install allure` на Windows).
2. Запустите тесты и сгенерируйте отчёт:

```powershell
.\scripts\run_tests_allure.ps1          # тесты → reports/allure-results
.\scripts\allure_report.ps1             # HTML → reports/allure-report + браузер
.\scripts\allure_report.ps1 -Serve      # allure open (live server)
```

## CI (пример)

```yaml
- run: pip install -r requirements.txt
- run: playwright install --with-deps chromium
- run: pytest -m "api or smoke" --browser chromium
```

## Ссылки

- [Test Cases](https://automationexercise.com/test_cases)
- [API List](https://automationexercise.com/api_list)
