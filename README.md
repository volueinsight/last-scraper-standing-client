# Wattsight's Last Scraper Standing - Client

This is the client code for our University Student Contest.

## What is this game?
This game is meant to (quite intensely) emulate the life as someone working with scrapers against a lot of sources.
Sources change unexpectedly and you must deal with these changes rapidly to ensure you don't lose data and keep your customers happy.

All teams start with 100 points. For every game tick (1 minute), 1 point is deducted from each scraper that does not deliver, or delivers the wrong data.
You can deliver as often as you want to. It does not deduct if you deliver the wrong data as long as you deliver the right data by the end of the current tick.
This means that you can debug and test without risking point deduction.

## How to install
Install Python 3.7 and pip.
We recommend using a virtual environment.
Suggested setup guide: https://docs.python-guide.org/starting/installation/

After python and pip is installed, run `pip install -r requirements.txt` in your shell.
This will install the required python packages to run the scripts.

Each scraper runs separately in its own shell and has its own script.

## How to sign up and run the game

Go to https://lss-game.wattsight.com and sign up if the registration is open.
Remember your access token and share it with anyone who will run the loaders on your team.
Change the value of the `TEAM_TOKEN` constant in `src/base_loader.py` to your access token.

To run a scraper run `python src/<scraper_name>.py`. For instance `python src/nordsnooker.py`.
`base_loader.py` is not a scraper but a common class for each of the standard scrapers. You do not need to run this.

It is recommended to run each scraper in a separate shell/process, as the probably will crash at some point.
This ensures that your working scrapers do not crash should one break.
You should also not detach from it as it may produce vital logs.

You are of course free to modify all parts of this code to optimise your loaders.

## General info
We do not admit outside pull-requests to this repo to improve the code. It is supposed to be in a fragile state.
Game registration is only open around the events and will only run during Wattsight events.
If you run the code outside of your event, you will likely get a 502 error as it will be taken down between events.
Registration and the game usually opens a couple of days before the event.
