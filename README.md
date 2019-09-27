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

To run a scraper run `python src/<scraper_name>.py`. For instance `python src/nordsnooker.py`.
`base_loader.py` is not a scraper but a common class for each of the standard scrapers. You do not need to run this.

It is recommended to run each scraper in a separate shell/process, as the probably will crash at some point.
This ensures that your working scrapers do not crash should one break.
You should also not detach from it as it may produce vital logs.
