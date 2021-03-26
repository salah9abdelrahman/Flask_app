flask_script: Flask-Script is a nice little extension which allows us to create command line interfaces, run server, start Python shell within the application context, make certain variables available inside the shell automatically and so on. 
    https://overiq.com/flask-101/extending-flask-with-flask-script/

Run application:
python manage.py run

Declare database url enviroment variable:
DATABASE_URL="postgresql:///username:password@localhost/database_name" 

Initiate a migration folder using init command for alembic to perform the migrations.
python manage.py db init

. Create a migration script from the detected changes in the model using the migrate command. 
This doesn’t affect the database yet.
python manage.py db migrate --message 'initial database migration'

Apply the migration script to the database by using the upgrade command
python manage.py db upgrade


to run tests
python manage.py test