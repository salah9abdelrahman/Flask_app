



#### first create data base and add the url to app.main.config.py

#### Create tables and migration
Initiate a migration folder using init command for alembic to perform the migrations.
``` python manage.py db init ```

. Create a migration script from the detected changes in the model using the migrate command. 
This doesn’t affect the database yet.
``` python manage.py db migrate --message 'initial database migration' ```

Apply the migration script to the database by using the upgrade command
``` python manage.py db upgrade ```


### To Run application:
```python manage.py run```

#### see swagger
[http://127.0.0.1:5000/]


### To run tests
```python manage.py test```

### Database design

[er-digram.png](er-digram.png)
