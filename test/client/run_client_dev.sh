#!/usr/bin/env sh
if [ -n "$(ls -A /app/node_modules)" ]; then
  echo "запускаем клиент"
else
  echo "проинсталируем библиотеки"
  npm install
fi

npm run lint -- --fix ;
HOST=0 PORT=3000 npm run dev ;
rm -rf /app/node_modules/*
chmod -R 777 /app/node_modules
mkdir /app/node_modules

