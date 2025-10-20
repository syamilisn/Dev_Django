%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
RUN PROJECT COMMANDS
---------------------------------------
bubble\Scripts\activate
python manage.py runserver
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
ADMIN ACCOUNT ACCESS
---------------------------------------
Username: admin
Password: 1234
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
GIT COMMANDS
---------------------------------------
git status
git add .
git commit -m "updated files"
git push
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
DJANGO COMMANDS
---------------------------------------
mkdir CKD_PROJECT
cd hello
echo "#CKD project" >> README.md
---------------------------------------
python -m venv bubble
bubble\Scripts\activate
pip install django
django-admin startproject hello .
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser
python manage.py startapp app1
python manage.py makemigrations app1
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%