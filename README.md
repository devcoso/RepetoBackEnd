Pasos para correr el proyecto
1.Crea tu entorno virtual en la raíz del proyecto con 
```
python -m venv venv
```
2.Después instala las dependencias con
```
pip install -r requirements.txt
```
3.Instala el dump de la db llamada repeto.dump
4.Crea tus archivos de envioroment en un .env como el siguiente ejemplo
```
MYSQL_HOST = 'localhost'
MYSQL_DB = 'repeto'
MYSQL_USER = 'user'
MYSQL_PASSWORD = 'password'
```

