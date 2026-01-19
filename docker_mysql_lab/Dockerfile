FROM postgres:15

# Kopieer init script (fixing permission issues)
COPY init.sql /docker-entrypoint-initdb.d/

# Zet juiste permissies
RUN chmod 644 /docker-entrypoint-initdb.d/init.sql
