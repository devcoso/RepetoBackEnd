#¿Cómo ejecuto está aplicación?
1. Crea tu entorno virtual en la raíz del proyecto con 
```
python -m venv .venv
```
2. Activa el entorno virtual con
```
.\.venv\Scripts\activate
```
3. Después instala las dependencias con
```
pip install -r requirements.txt
```
4. Instala el dump de la db llamada repeto.dump
5. Crea tus archivos de environment  en un .env como el siguiente ejemplo
```
MYSQL_HOST = 'localhost'
MYSQL_DB = 'repeto'
MYSQL_USER = 'user'
MYSQL_PASSWORD = 'password'
```
6. Ejecuta el siguiente comando para correr el proyecto desde la raíz
```
python .\src\app.py
```

