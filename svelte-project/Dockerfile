FROM node:18.2-bullseye-slim AS build

WORKDIR /app/svelte

COPY package.json .
COPY package-lock.json .
RUN npm install
COPY . .
RUN npm run build

FROM nginx:1.22-alpine
COPY --from=build /app/svelte/public /usr/share/nginx/html