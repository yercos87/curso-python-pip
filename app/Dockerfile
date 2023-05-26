
# Se indica la versión de python para ejecutar la aplicación
FROM python:3.10

# Con WORKDIR se crea la carpeta dentro del contenedor
WORKDIR /app
#
# Una buena práctica es copiar tus archivos, el archivo de las dependencias
# en este caso tus archivos .txt, el cual vamos a pasar del local al entorno en el que estamos trabajando,
# Para eso usamos COPY, seguidamente indicamos el archivo que queremos copiar y en donde lo queremos copiar (en el contenedor)
#
# En el campo del sottware una dependecia es una aplicación o una biblioteca requerida por otro programa
# para poder funcionar correctamente. Por ello se dice que dicho programa depende de tal aplicación o biblioteca
#
COPY requirements.txt /app/requirements.txt

# Con RUN se instala las dependencia que se enecunetran en el archivo requirements.txt
# --no-cache-dir No se agrega el cache
# --upgrade Actualiza las aplicaciones si encuentra alguna actualziación
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Se indica que copie todo lo que esta en la carpeta actuañ y lo mueva al entorno creado
COPY . app/

# Comando para que el contenedor se encuentre corriendo continuamente en un ciclo infinito "Es programación bash"
CMD bash -c "while true; do sleep 1; done"