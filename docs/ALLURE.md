# Allure Reports

## Что настроено

| Компонент | Описание |
|-----------|----------|
| `allure-pytest` | Сбор результатов при запуске pytest |
| `tests/conftest.py` | Метки epic/feature/story, TMS id (TC-01, API-05), severity для smoke |
| `ApiClient` | Шаги Allure + request/response attachments |
| `UI failures` | Скриншот, URL, HTML страницы |
| `config/allure/` | categories.json, executor.json |
| `reports/` | allure-results (сырые данные) + allure-report (HTML) |

## 1. Установка Allure CLI (Windows)

Нужен для генерации HTML (pytest пишет только `allure-results`).

```powershell
npm install -g allure-commandline
```

Проверка: `allure --version`

## 2. Запуск тестов с Allure

```powershell
# Все тесты + очистка предыдущих результатов
.\scripts\run_tests_allure.ps1

# Только smoke
.\scripts\run_tests_allure.ps1 -Markers smoke

# Только API
.\scripts\run_tests_allure.ps1 -Markers api

# Вручную
pytest tests --alluredir=reports/allure-results --clean-alluredir --browser chromium
```

## 3. Генерация и просмотр отчёта

```powershell
# Собрать HTML и открыть в браузере
.\scripts\allure_report.ps1

# Временный сервер (удобно для CI-артефактов)
.\scripts\allure_report.ps1 -Serve

# Только открыть уже собранный отчёт
.\scripts\allure_report.ps1 -OpenOnly
```

Альтернатива без скрипта:

```powershell
allure generate reports/allure-results -o reports/allure-report --clean --config config/allure
allure open reports/allure-report
# или
allure serve reports/allure-results
```

## 4. Структура отчёта

- **Parent suite:** API / UI
- **Epic:** Automation Exercise API / UI
- **Suite:** имя test-класса (`TestAuth`, `TestProductsApi`, …)
- **Story:** имя теста
- **Labels:** `testCase` = TC-01, API-07; теги `smoke`, `api`, `ui`

## 5. Переменные окружения

```env
ALLURE_RESULTS_DIR=reports/allure-results
```

## 6. CI (GitHub Actions)

```yaml
- name: Run tests with Allure
  run: pytest tests --alluredir=reports/allure-results --browser chromium

- name: Publish Allure Report
  uses: simple-elf/allure-report-action@master
  if: always()
  with:
    allure_results: reports/allure-results
    allure_report: reports/allure-report
```

## 7. Аннотации в тестах (опционально)

```python
import allure

@allure.title("Регистрация нового пользователя")
@allure.description("Test Case 1 из automationexercise.com")
def test_case_01_register_user():
    with allure.step("Открыть главную страницу"):
        ...
```
