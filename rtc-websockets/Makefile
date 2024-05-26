start:
	@echo Starting application...
	@cd src && python manage.py runserver

makemigrations:
	@echo Generating migrations...
	@cd src && python manage.py makemigrations database

migrate:
	@echo Applying migrations...
	@cd src && python manage.py migrate

createsuperuser:
	@echo Creating superuser...
	@cd src && python manage.py createsuperuser

run_redis:
	@echo Starting redis instance...
	@docker-compose up -d

stop_redis:
	@echo Shutting down redis...
	@docker-compose down