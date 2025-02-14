@echo off
start /b python app.py
timeout /t 3
start /b python -m http.server 8000
timeout /t 3
start chrome "http://127.0.0.1:8000/index.html"
timeout /t 3
start /b python finder.py
exit
