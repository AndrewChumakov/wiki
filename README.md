<h1 align="center">Проект автоматизации тестирования сайта компании Wikipedia</h1>

# Описание

### Кейсы:

- Переход по страницам приветственного экрана
- Пропуск страницы приветственного экрана
- Поиск статьи

### Используемый стек технологий и инструментов:

| Python                                                | Pycharm                                                | Git                                                | Pytest                                                | Selene                                                | Appium                                                | Allure <br/> Report                                   | Jenkins                                                |                                                Telegram |
|:------------------------------------------------------|--------------------------------------------------------|----------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|--------------------------------------------------------|--------------------------------------------------------:|
| <img height="50" src="source/Python.png" width="50"/> | <img height="50" src="source/Pycharm.png" width="50"/> | <img height="50" src="source/git.svg" width="50"/> | <img height="50" src="source/Pytest.png" width="50"/> | <img height="50" src="source/Selene.png" width="50"/> | <img height="50" src="source/appium.png" width="50"/> | <img height="50" src="source/allure.svg" width="50"/> | <img height="50" src="source/Jenkins.svg" width="50"/> | <img height="50" src="source\Telegram.svg" width="50"/> |

# Запуск тестов с заданными параметрами

```   
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest --context=${CONTEXT}
```

# Сборка в Jenkins

Для запуска сборки необходимо перейти в раздел **"Build with Parameters"**, выбрать среду и нажать кнопку **"Build"**.

<p align="center">
<img title="Jenkins Build" src="source/build.png"> 
</p>

# Интеграция с Allure Report

<p align="center">   
<img title="Allure Report" src="source/allure_report.png">    
</p>

# Уведомление в Telegram

<p align="center">   
<img title="Telegram" src="source/telegram.png">    
</p>

