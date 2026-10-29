FROM nginx:alpine

# Копируем файл index.html
COPY index.html /usr/share/nginx/html/index.html

# Копируем нашу конфигурацию Nginx (заменяем стандартную)
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]