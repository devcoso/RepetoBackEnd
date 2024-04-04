#¿Cómo ejecuto esta aplicación?
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
4. Instalar el dump de la db llamada repeto.dump
5. Crea tus archivos de environment  en un .env como el siguiente ejemplo
```
PGSQL_HOST = 'localhost'
PGSQL_USER = 'user'
PGSQL_PASSWORD = 'password'
PGSQL_DATABASE = 'repeto'

FRONTEND_URL = http://localhost:5173/
EMAIL_HOST = smtp.gmail.com
EMAIL_PORT = 'PORT'
EMAIL_USER = 'Correo'
EMAIL_PASS = 'Password'
```
6. Ejecuta el siguiente comando para correr el proyecto desde la raíz
```
python .\src\app.py
```

