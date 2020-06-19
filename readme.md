# Readme

Run pgAdmin 4 in a container on Heroku by using the `DATABASE_URL` from the config:

```bash
# get database url from an existing app
export DATABASE_URL=`heroku config:get DATABASE_URL -a hasura-heroku`

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
