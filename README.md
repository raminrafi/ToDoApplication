# ToDoApplication
To Do Application using Vue frontend, Django API Backend and SQLite Database 

//VIRTUAL ENVIRONMENT
Create virtual environment using the following commands:
1. pip install virtualenvwrapper-win
2. mkvirtualenv envv
3. workon envv // to activate the virtual environment

//VUE FRONTEND
The frontend has been created using vuejs and for vue to work we need to have nodejs installed
After nodejs installation, install vue in the virtual environment using command: 
=> npm install -g vue-cli

//After that create project using the following commands 
1. vue init webpack frontend
2. code . //will open the project frontend in vscode
3. npm run dev //to run the application on http://localhost:8080/
//copy paste the files present in frontend-VueComponents in "src" file made when the project is created using the commands mentioned above^^

//BACKEND
For Django REST APIs installation use the following commands:
1. pip install django
2. django-admin startproject backend
3. django-admin startapp "apiname"
4. python manage.py makemigrations
5. python manage.py migrate
6. python manage.py runserver //this command will start development server at http://127.0.0.1:8000/

