FROM mysql:8.0

ENV MYSQL_DATABASE=pet \
    MYSQL_ROOT_PASSWORD=root \ 
    
COPY    ./init-db.d/scrip.sql/docker-entrypoint-initdb.d/

EXPOSE 3306
