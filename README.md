# todo_app
A simple Django Todo App
## Installation

Create a project directory

```
mkdir todo
cd todo
```

Install Virtual enviornment

```
sudo apt-get install python-virtualenv
```
Clone the project

```
git clone https://github.com/shinasnp/todo_app.git

```
### Steps:
```
virtualenv -p python3 env
source env/bin/activate
cd todo_app
pip3 install -r requirement.txt
```
### run migrations
```
python manage.py makemigrations
python manage.py migrate
```

### Start server
```
python manage.py runserver
```
### For create Admin user
```
python manage.py createsuperuser
```

### Screen shots
![Screen Shot 2019-03-19 at 7 11 00 PM](https://user-images.githubusercontent.com/9362086/54610677-7ff97b00-4a7b-11e9-90fc-a6c6095e71b4.png)

![Screen Shot 2019-03-19 at 7 18 35 PM](https://user-images.githubusercontent.com/9362086/54610870-ea122000-4a7b-11e9-9718-0c716d62a673.png)
