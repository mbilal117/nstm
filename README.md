# NesTech Marketing

[![Build Status](https://travis-ci.com/vitorfs/nstm.svg?branch=master)](https://travis-ci.com/vitorfs/nstm)
[![codecov](https://codecov.io/gh/vitorfs/nstm/branch/master/graph/badge.svg)](https://codecov.io/gh/vitorfs/nstm)
[![Documentation Status](https://readthedocs.org/projects/nstm/badge/?version=latest)](https://nstm.readthedocs.io/en/latest/?badge=latest)

Self-hosted email marketing solution. Compatible with any SMTP email service.

One-click deploy to Heroku:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Screenshots

![nstm new campaign](https://nstm.readthedocs.io/en/latest/_images/nstm-new-campaign.png)

![nstm campaigns](https://nstm.readthedocs.io/en/latest/_images/nstm-campaigns.png)

[More nstm screenshots.](https://nstm.readthedocs.io/en/latest/features.html#screenshots)

## Features

* Create and manage multiple mailing lists;
* Import lists from other providers (csv files or paste email addresses);
* Create reusable email templates;
* Customize sign up pages (subscribe, unsubscribe, thank you page, etc.);
* Default double opt-in for sign ups;
* Schedule email campaign to send on a specific date and time;
* Track email opens and clicks;
* Change link URL after email is sent;
* Reports with geolocation;
* Compatible with Mailgun, SendGrid, Mandrill, or any other SMTP email service.

## Quickstart

If you want to have a quick look or just run the project locally, you can get started by either forking this repository
or just cloning it directly:

```commandline
git clone git@github.com:mbilal117/nstm.git
```

Ideally, create a [virtualenv](https://docs.python-guide.org/dev/virtualenvs/) and install the projects dependencies:

```commandline
pip install -r requirements/development.txt
```

Create a local database:

```commandline
python manage.py migrate
```

Start development server:

```commandline
python manage.py runserver
```

Open your browser and access the setup page to create an admin account:

```commandline
http://127.0.0.1:8000/setup/
```

PS: Campaign scheduling will not work out-of-the-box. You need to install a message broker and [setup Celery](https://simpleisbetterthancomplex.com/tutorial/2017/08/20/how-to-use-celery-with-django.html) properly.

## Tech Specs

* Python 3.6
* Django 2.1
* PostgreSQL 10
* Celery 4.2
* RabbitMQ 3.7
* Bootstrap 4
* jQuery 3.3

PostgreSQL and RabbitMQ are soft dependencies. Other databases (supported by Django) can easily be used as well as other
message broker compatible with Celery.

The jQuery library is more of a Bootstrap dependency. There is very little JavaScript code in the project. For the most
part the code base is just plain Django and HTML templates.

Complete list of Python dependencies can be found in the requirements files.

## Documentation

This is just a pre-release of the project and I still have to work on a proper documentation and user guides.

For now you will only find documentation of the internal APIs in the source code.

[nstm.readthedocs.io](https://nstm.readthedocs.io)

## Who's using nstm?

Right now just myself. I'm currently using it for my blog newsletter at [nestechsystems.com](http://nestechsystems.com/).

Here is how my sign up page looks like: [sibt.co/newsletter](https://sibt.co/newsletter)

## License

The source code is released under the [MIT License](https://github.com/vitorfs/nstm/blob/master/LICENSE).
