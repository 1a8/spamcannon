# Spam Cannon

Some douche took over a PyPI package and tried to harvest environment variables with it. The compromised package has been taken down, but his Heroku server is still up. This package will send a bunch of fake data to his server to bloat his bandwidth (and bill) and spoil his data.

## Install

Clone from Github and install dependencies into a virtualenv.

```
git clone https://github.com/1a8/spamcannon.git
cd spamcannon
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
```

## Usage
Send volleys of 10 requests at a time
```
python -m spamcannon
```

Specify the volley size with `-v` or `--volley`
```
python -m spamcannon -v 100
```

Disable logging with `-s`
```
python -m spamcannon -v 100 -s
```
