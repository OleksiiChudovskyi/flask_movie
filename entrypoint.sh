#!/bin/sh


# checking if the DB is launched
if [ "$POSTGRES_DB" = "fm" ]
then
    echo "*** Waite our postgres..."
    while ! nc -z "db" $POSTGRES_PORT; do
      sleep 0.5
    done
    echo "*** PostgreSQL have been launched..."
fi


# applying migration
echo "*** Running applying migrations..."
flask db migrate
flask db upgrade


# populating database
echo "*** Running populating database..."
python -c "from src.models._inserts import populate_films; populate_films()"


exec "$@"