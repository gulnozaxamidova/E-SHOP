#name: E-SHOP (online shop).

<p align='center'>
<img src="https://img.shields.io/badge/Django-239120?logo=django&logoColor=white" />
<img src="https://img.shields.io/badge/Python-239120?logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/SQL%20Server-CC2927?logo=microsoft-sql-server&logoColor=white" />
<img src="https://img.shields.io/badge/html5-E34F26?logo=html5&logoColor=white" />
<img src="https://img.shields.io/badge/css3-1572B6?logo=css3&logoColor=white" />
<img src="https://img.shields.io/badge/bootstrap-563D7C?logo=bootstrap&logoColor=white" />
<img src="https://img.shields.io/badge/Github-181717?logo=github&logoColor=white" />
<img src="https://img.shields.io/badge/PayPal-000144?logo=paypal&logoColor=white" />
</p>


<hr class="dotted">
It is an E-SHOP system built in Django. It contains all the essentials for adding products and use Razorpay and Stripe as payment systems.

## About this Project:

It is an E-commerce system built in Django. It contains all the essentials for adding products and use Razorpay and Stripe as payment systems.

The repository is a start point for most of my professional projects; for this, I'm using as a part of my portfolio, feel free to use wherever you want. I'll be happy if you provide any feedback or code improvements or suggestions.




## Some technical information:

- Django - 3.2.9
- Django Jazzmin - 2.4.9
- DRF - 3.13.1


## To Install:

Cloning the Repository:

```
$ git clone https://github.com/gulnozaxamidova/E-SHOP.git

$ cd E-SHOP 

```

Installing the environment control:

```
$ pip install virtualenv

$ virtualenv venv

```

Activating the environment:

on Windows:
```
venv\Scripts\activate

```
on Mac OS / Linux:
```
$ source venv/bin/activate

```

Installing dependencies:

```
$ pip install -r requirements.txt

```

Create a .venv file on ecommerce folder (/ecommerce/.venv) setting all requirements without using space after "=". 

Copy and paste on our .venv file:

```
DEBUG=
SECRET_KEY=
JAZZMIN_SETTINGS=

```

Last commands to start:

```
$ python manage.py makemigrations

$ python manage.py migrate

```
Create a super user:

```
$ python manage.py createsuperuser 

```

Finishing running server:

```
$ python manage.py runserver

```
## Deployment
```
https://e-onlineshop.herokuapp.com
login: e-shop
password: shop
```


## Contributing

You can send how many PR's do you want, I'll be glad to analyse and accept them! And if you have any question about the project...

📫Email-me: <a href='mailto:rosekhamidova@gmail.com'>rosekhamidova@gmail.com</a>



Thank you!




