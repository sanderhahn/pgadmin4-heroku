FROM dpage/pgadmin4

ENV PGADMIN_DEFAULT_EMAIL=admin
ENV PGADMIN_DEFAULT_PASSWORD=password
ENV PGADMIN_LISTEN_ADDRESS=0.0.0.0
ENV MASTER_PASSWORD_REQUIRED=False
ENV PGPASSFILE=/pgadmin4/.pgpass

COPY ./database_url.py /pgadmin4/database_url.py
COPY ./entrypoint.sh /

USER root
RUN chown -R pgadmin:pgadmin /pgadmin4/

USER pgadmin
