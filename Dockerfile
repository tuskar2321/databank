FROM centos:7.2.1511

ENV DEBIAN_FRONTEND=noninteractive

RUN yum install -y epel-release \
    yum updateinfo

# Для корректной работы yum в оверлейной файловой системе
RUN yum install -y yum-plugin-ovl

RUN yum install -y \
    httpd \
    httpd-tools \
    libcurl \
    libqt4-qt3support \
    php-gd \
    php-mbstring \
    php-pgsql \
    php-xml \
    php-xmlrpc \
    postgis \
    postgresql-server \
    postgresql \
    postgresql-contrib \
    pwgen \
    sudo \
    supervisor

# setup postgres
RUN sed -i 's/.*requiretty$/#Defaults requiretty/' /etc/sudoers

RUN mkdir /db && chmod 777 /db && chown postgres /db
RUN sudo -u postgres initdb -E utf8 -D /db

ADD ./postgresql.conf /var/lib/pgsql/data/postgresql.conf
RUN chown -v postgres.postgres /var/lib/pgsql/data/postgresql.conf
RUN echo "host all  all    0.0.0.0/0  trust" > /db/pg_hba.conf
RUN echo 'local all   all   trust' >> /db/pg_hba.conf

EXPOSE 5432

# setup httpd
ENV SERVICE_RUN_USER  www-data
ENV SERVICE_RUN_GROUP www-data

ENV SERVICE_LOCK_DIR=/var/lock/httpd
ENV SERVICE_LOG_DIR=/var/log/httpd
ENV SERVICE_PID_FILE=/var/run/httpd.pid
ENV SERVICE_RUN_DIR=/var/run/httpd

RUN mkdir /var/lock/httpd || true

EXPOSE 80

RUN echo 'ServerName localhost' >> /etc/httpd/conf/httpd.conf

ADD ./gisserver.noarch.rpm /usr
ADD ./giswebservicese.noarch.rpm /usr
ADD ./geodbse.noarch.rpm /usr

RUN yum localinstall -y /usr/gisserver.noarch.rpm || true
RUN yum localinstall -y /usr/giswebservicese.noarch.rpm || true
RUN yum localinstall -y /usr/geodbse.noarch.rpm

CMD \
    bash -c "sudo -u postgres /usr/bin/postgres -D /db -c config_file=/var/lib/pgsql/data/postgresql.conf &" && \
    /bin/bash /usr/appservice/startgis.bat && \
    /bin/bash /usr/gisserver/gsservice.bat && \
    sleep 2 && \
    /bin/bash /var/Panorama/GeoDBSE/base/createdb/creategeodb.bat || true && \
    echo "geodb backup restored" && \
    /usr/sbin/httpd -D FOREGROUND
