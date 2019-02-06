FROM python:3.7-alpine
RUN apk add --no-cache gcc libevent-dev linux-headers musl-dev libffi-dev openssl-dev pcre-dev
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt uwsgi certbot-dns-google certbot
COPY . /app
ENV DJANGO_DEBUG=FALSE DJANGO_SECRET_KEY=4yxCxk2fKHnZ6TTUaxX16KR1S+XlDFxIl60SvirizC9NaSt7Z5RXzPEB+P7O7jkpN2Vp5742so6H DJANGO_STATIC_ROOT=/srv/static DJANGO_DB_PATH=/srv/db/db.sqlite3
RUN mkdir -p /srv/static && \
    ./manage.py collectstatic --noinput
CMD ["./server.sh"]
VOLUME /etc/letsencrypt
VOLUME /srv/db
EXPOSE 80 443
