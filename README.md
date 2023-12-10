# LU-Dice-Bot
You can play dice in Telegram with this bot (Only Uzbek language available)

If you send dice object (they are cuurently 6) to this bot it will send back the same dice. Then bot will compare both dice outcomes and announce the winner (and looser)
This bot is created using Python 3 and aiogram 2

How to run the bot?
1. Download files from this repository
2. Install dependencies using pip (You need to install aiogram version 2)
3. Replace example bot token with real one (token of your own bot from BotFather) in config.py
4. Add admin ids, if you wish, in config.py
5. Run app.py


P.S. Procfile and runtime.txt files are for running bot on Heroku server properly and bot.conf file is for running bot on AWS using supervisorctl
