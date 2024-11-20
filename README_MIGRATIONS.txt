
# Instrucciones para manejar migraciones con Flask-Migrate

1. Abre una terminal en la raíz del proyecto y activa tu entorno virtual.
2. Ejecuta el comando para inicializar las migraciones:
   flask db init

3. Genera un archivo de migración para crear las tablas en la base de datos:
   flask db migrate -m "Initial migration for gestion system"

4. Aplica las migraciones a la base de datos MySQL:
   flask db upgrade

# Asegúrate de que tu servidor MySQL esté corriendo y que el usuario/contraseña coincidan con la configuración en config.py.
