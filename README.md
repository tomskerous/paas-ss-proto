
### Requirements

Requires you to have Ruby 2.2.0 or higher

### Set up

Running in a virtualenv is advised. To create one, with Python 3, run

```
mkvirtualenv --python=`which python3` <name>
```

In future run `workon <name>` to activate the virtualenv you just created.

Install the dependencies

```
pip install -r requirements.txt
gem install bundle
```

We then need to fetch the latest GOVUK assets

```
python manage.py install_all_govuk_assets
```

Then you should be ready to run it

```
python manage.py runserver
```

Follow the instructions returned on the commandline to view it in your browser