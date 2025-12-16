FROM node:20-alpine

# ------------------------------------------------------------------
# Application
# ------------------------------------------------------------------
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy frontend source
COPY . .

# Vite dev server
EXPOSE 8000

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "8000"]
