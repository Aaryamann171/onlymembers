# onlymembers - A Containerized Web App
Assignment Submission for Capstone-II

### about
* __Premium Members__: Members who are also users. They get special perks. ;)
* __Members__: Regular Members with the basic perks.

### tech-stack

#### framework
django

#### database
sqlite3

### how to run
`docker-compose up`

### add members
* click on add members button to create a new member
<br> __OR__ <br>
* add members from the admin panel
you will then be redirected to the home page where you can see the updated list

### homepage url
http://127.0.0.1:8000/

### create regular members
http://127.0.0.1:8000/create/
<br> __OR__ <br>
click on the `add new member` button

### superuser credentials
username: oreo\
password: oreo171171

### add users to premium list
* `register` to be added to the list of premium member
<br> __OR__ <br>
Add users from the admin panel
* http://127.0.0.1:8000/admin/
* login using credentials
* add user

### dockerhub
https://hub.docker.com/r/aaryamann171/onlymembers \
`docker pull aaryamann171/onlymembers`
