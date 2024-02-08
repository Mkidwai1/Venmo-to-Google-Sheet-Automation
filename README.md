Venmo Transaction Tracker for Club
Hey everyone! 👋

So, I built this little project to help our club keep track of all our Venmo transactions. You know how we always get mixed up with who paid what and when? Well, this should make our lives a bit easier. 😄

What's This All About?
Basically, it's a script that takes our club's Venmo transactions and automatically puts them into a Google Sheet. No more manual entries, no more "Oops, I forgot to write that down" moments.

Why I Made This
We're all busy with classes, exams, and, you know, life. This script is here to take one less worry off our plates. We can now see all our transactions in one place, neatly organized. 📊

How It Works
The script does a few cool things:

Grabs the latest 50 transactions from our Venmo account (Venmo's API has a limit, learned that the hard way 😅).
Checks if each transaction is already in our Google Sheet to avoid duplicates.
Adds new transactions to the top of the sheet (right below the headers).
Changes the background color for easy reading: one color for incoming, another for outgoing money.
Getting Started
To get this up and running, you'll need a few things:

Venmo API access token (keep this secret! 🤫).
Google Sheets API setup (there are tons of tutorials out there).
A .env file to store your Venmo token (because security matters).
Python environment (cause that's what we're coding in).
Running the Script
Just fire up the script with Python. Make sure you've got all the dependencies installed (venmo_api, gspread, you know the drill).


```python3 the_script.py```

That's Pretty Much It!
Feel free to mess around with the code, tweak it, break it, fix it, and make it yours. If you come up with some cool improvements, definitely let the rest of us know!

Oh, and if you're not sure about something, just ask. We're all learning here. 🚀

Cheers,
Mahmood
