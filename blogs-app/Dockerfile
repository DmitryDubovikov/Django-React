FROM node:18-alpine as build

# Задаем рабочий каталог
WORKDIR /usr/src/app
# Копируем туда наши json файлы
ADD *.json ./
# Устанавливаем все пакеты и зависимости указанные в json
RUN npm install

ADD ./public ./public
ADD ./src ./src