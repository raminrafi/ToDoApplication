# ToDoApplication
To Do Application using Vue frontend, Django API Backend and SQLite Database 

//VIRTUAL ENVIRONMENT
Create virtual environment using the following commands
pip install virtualenvwrapper-win
Mkvirtualenv envv
workon envv // to activate the virtual environment

//VUE FRONTEND
The frontend has been created using vuejs and for vue to work we need to have nodejs installed
After nodejs installation, install vue in the virtual environment using command
npm install -g vue-cli
After that create project using the following commands 
vue init webpack frontend
code . //will open the project frontend in vscode
npm run dev //to run the application on http://localhost:8080/
//copy paste the files present in frontend-VueComponents in "src" file made when the project is created using the commands mentioned above^^

//BACKEND
For Django REST APIs installation use the following commands
pip install django
django-admin startproject backend
django-admin startapp "apiname"
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


