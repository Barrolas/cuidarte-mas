FROM node:18-alpine

WORKDIR /app

# Copiar archivos de dependencias
COPY package*.json ./

# Instalar dependencias
RUN npm ci --only=production

# Copiar código de la aplicación
COPY src/ ./src/
COPY sql/ ./sql/

# Crear directorio para uploads (persistido vía volumen en docker-compose)
RUN mkdir -p uploads/documentos

# Exponer puerto
EXPOSE 3000

# Comando para iniciar la aplicación
CMD ["node", "src/app.js"]

