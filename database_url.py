import os
from urllib.parse import urlparse
import json

if not 'DATABASE_URL' in os.environ:
    os.exit(0)

db_url = os.environ['DATABASE_URL']
result = urlparse(db_url)
db = result.path[1:]

# https://www.postgresql.org/docs/current/libpq-pgpass.html
with open('/pgadmin4/.pgpass', "w") as fp:
    fp.write("# hostname:port:database:username:password\n")
    fp.write(f"{result.hostname}:{result.port}:{db}:{result.username}:{result.password}")
os.chmod('/pgadmin4/.pgpass', 0o600)

# https://www.pgadmin.org/docs/pgadmin4/development/import_export_servers.html#json-format
with open('/pgadmin4/servers.json', 'w') as fp:
    json.dump({
        "Servers": {
            "1": {
                "Name": "Heroku",
                "Group": "Servers",
                "Port": result.port,
                "SSLMode": "prefer",
                "Host": result.hostname,
                "MaintenanceDB": db,
                "DBRestriction": db,
                "Username": result.username,
                "PassFile": "/home/pgadmin4/.pgpass"
            }
        }
    }, fp)
