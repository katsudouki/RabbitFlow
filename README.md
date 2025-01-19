# RabbitFlow
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Babel](https://img.shields.io/badge/Babel-F9DC3e?style=for-the-badge&logo=babel&logoColor=black)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

small finance manager project that runs on localhost with multilanguage support


how run : 
```
git clone https://github.com/katsudouki/RabbitFlow.git
cd RabbitFlow
uv venv
#activate venv on linux
source .venv/bin/activate
#activacte venv on windows
.venv\Scripts\activate.bat
uv run app.py
```

#### 🛈 To test SSL correctly offline, import the certificates from the certs/mkcert/ folder into the browser.


how to translate : 

```
pybabel extract -F babel.cfg -o messages.pot .
pybabel update -i messages.pot -d translations
```
edit the messages.po file in the translations folder by changing msgstr "" of the variables to a translation
and finally run the command to compile the translations
```
pybabel compile -d translations
```
