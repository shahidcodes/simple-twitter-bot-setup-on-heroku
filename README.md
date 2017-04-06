# Simple Twitter Bot Setup On Heroku

# Pre-requisite
* Python Installed Obviously
* VirtualEnv Installed (pip install virtualenv)
* You must know how to deploy app on heroku [Read here](https://devcenter.heroku.com/articles/getting-started-with-python)

# Get Started
We're going to use heroku's worker dyno to acomplish this task. Although you can use job scheduling to run your bot at certain time than keep running it all time.

* **Clone this Repo**
* run `virtualenv twibot --no-site-packages` and activate it.
* Make changes to `main.py` because this is your Bot main entry file.
* see `main_example.py` for reference.
* When all done means when you've your working bot locally. Run `pip freeze requirements.txt` in the bot directory.
* And finally deploy and scale the worker dyno or run it.

For instance you can put your Twitter App credentials in `main_example.py` and run it.
# Quick Walkthrough

## Procfile
This is main file which tells Heroku, which dyno to use. We're using `worker` dyno. [Learn more about dyno](https://devcenter.heroku.com/articles/dynos).
So `worker: python main.py` tells heroku to run worker dyno and run `python main.py` command on that.
 
## Requirements (requirements.txt)
This is file created by pip when we run `pip freeze requirements.txt`. This is important because heroku will look for this file to install module dependency of your bot.

## Runtime (runtime.txt)
If you're using python 2.7 then change runtime in this file. Available runtimes are listed [here](https://devcenter.heroku.com/articles/python-runtimes)

## db.json
This file is part of `main_example.py` to keep track of retweets/day. 

# Further Ideas
* You're not limited to just retweet bot. Read Tweepy [Docs](tweepy.readthedocs.io). For example you can use filters to filter tweets by users or any other. 
* For Data Analysis people, you may want to use PGSQL provided by Heroku to store analysis data

# Me
### Twitter: [@sh4hidkh4n](https://twitter.com/sh4hidkh4n)
