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
4. Instalar el dump de la db llamada repeto.dump
5. Crea tus archivos de environment  en un .env como el siguiente ejemplo
```
SECRET_KEY=B!1w8*NAt1T^%kvhUI*S^_

PGSQL_HOST=localhost
PGSQL_DB=repeto
PGSQL_USER=root
PGSQL_PASSWORD=root

JWT_SECRET_KEY=daedb2dab55398b88cd3dca6a2bd167e77ba0a4900fef5f950581c9e264f5c27

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=user
EMAIL_PASS=password

FRONTEND_URL=http://localhost:5173/
```
6. Ejecuta el siguiente comando para correr el proyecto desde la raíz
```
python .src\app.py
```
