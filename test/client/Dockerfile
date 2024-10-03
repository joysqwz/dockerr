FROM node:16
RUN npm install -g http-server 
RUN npm install -g @vue/cli-service
RUN npm install -g @vue/cli
RUN npm install -g vue
# делаем каталог 'app' текущим рабочим каталогом
WORKDIR /app

# копируем 'package.json' 
COPY package*.json ./

# устанавливаем зависимости проекта
RUN npm install
RUN npm install --save
RUN npm install -g serve
# копируем файлы и каталоги проекта в текущий рабочий каталог (т.е. в каталог 'app')
COPY . .

# собираем приложение для production с минификацией
#RUN npm run build

ENV VUE_APP_URL startUrl + ''
EXPOSE 8080
CMD [ "http-server", "dist" ]
