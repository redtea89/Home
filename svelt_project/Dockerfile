FROM node:18.2-bullseye-slim

WORKDIR /app/svelte

COPY package.json .
COPY package-lock.json .
RUN npm install
COPY . .
RUN npm run build
EXPOSE 8080

CMD ["npm", "start"]