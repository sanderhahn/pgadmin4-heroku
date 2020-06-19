# Readme

Run pgadmin in a container on Heroku (parses the `DATABASE_URL` from the environment variables).

```bash
# get database url from an existing app
export DATABASE_URL=`heroku config:get DATABASE_URL -a example-hasura`
export PGADMIN_DEFAULT_EMAIL=admin
export PGADMIN_DEFAULT_PASSWORD=`python3 -c 'import secrets; print(secrets.token_urlsafe(16))'`

heroku create example-pgadmin --region eu
heroku stack:set container -a example-pgadmin

heroku config:set DATABASE_URL=$DATABASE_URL
heroku config:set PGADMIN_DEFAULT_EMAIL=$PGADMIN_DEFAULT_EMAIL
heroku config:set PGADMIN_DEFAULT_PASSWORD=$PGADMIN_DEFAULT_PASSWORD

git push heroku master

echo "Login: $PGADMIN_DEFAULT_EMAIL / $PGADMIN_DEFAULT_PASSWORD"
```

## Docker

```bash
docker build . -t pgadmin
docker run -e PORT=4444 -e DATABASE_URL=$DATABASE_URL -p 4444:4444 pgadmin
```
