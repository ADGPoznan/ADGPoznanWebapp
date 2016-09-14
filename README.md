#AGD Poznań website

Website address:
* http://adg-poznan.appspot.com
* http://adg-poznan.pl

## Install requirements

```bash
cd webapp
pip install -r requirements.txt -t lib
```


## Test server

```bash
cd webapp
dev_appserver.py .
```

## Upload application

```bash
gcloud config set project adg-poznan
gcloud preview datastore create-indexes webapp/index.yaml
gcloud app deploy --no-promote webapp/app.yaml
```
