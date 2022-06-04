FROM node:18 AS build
# FROM node:18.2-bullseye-slim AS build

WORKDIR /app/svelte

COPY package.json .
COPY package-lock.json .
RUN npm install
COPY . .
RUN npm run build

FROM nginx
COPY --from=build /app/svelte/public /usr/share/nginx/html