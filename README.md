# auto-mate

auto-mate is a discord-self-bot that messages your significant other as you, so that you can do other stuff without worrying too much about forgetting to message them.

<div align="center">
  <div style="float:left;margin-right:10px;">
  <img height=auto width=300 src="https://media.tenor.com/4Lp8MIVn9DEAAAAC/cute.gif"><br>
    <p style="font-size:1.5vw;">It sends GIFS like this!</p>
  </div>
</div>

## Contents
```
auto-mate
├── keep_alive.py
├── main.py
├── messages.py
├── requirements.txt
└── 
```
The bot sends a message once in the morning, once in the day and once at night. A new message is chosen randomly from ```messages.py```. These messages can be easily changed to be more personal. ```main.py``` has the bot code that handles the scheduling and message sending.

To make the bot work, an authorisation token needs to be set up along with the user ID of the receiver. More details about this is under [Setting up the bot](https://github.com/sttaseen/discord-bot/new/main?readme=1#setting-up-the-bot).

A webserver can be created with repl.it so that the code can be run on the cloud instead of having a computer running it 24/7. More details about this is under [Setting up repl.it](https://github.com/sttaseen/discord-bot/new/main?readme=1#setting-up-replit).

## Requirements

```Python >= 3.10``` must be [installed](https://www.python.org/downloads/) with pip. 

Clone the repo, if not done already and go inside the repo:
```
git clone https://github.com/sttaseen/discord-bot.git
cd discord-bot
````

### Installing Dependencies
Install dependencies by running the following from the root of the repo:
```
pip install -r requirements.txt
```

## Setting up the bot

### Authorisation Token
The authorisation token is needed to send the message as you. This token is very sensitive so don't share it with anyone. The easiest way to get this is through discord on browser.
After logging in on the browser, go to a server or a dm and press ```CTRL+SHIFT+I``` to go to ```Inspect Mode```. Then, click on the ```Network``` tab as shown below:

<div align="center">
  <div style="float:left;margin-right:10px;">
  <img height=auto width=400 src="https://user-images.githubusercontent.com/67076071/210667834-0f68b704-d91e-49b1-8c38-ba5cc77d8ef3.png"><br>
    <p style="font-size:1.5vw;">Network Tab under Inspect</p>
  </div>
</div>

After that, send a message through discord. A new entry called ```messages``` will pop up. Click on it, scroll down to ```Request Headers``` and look for ```authorization```. The value for it is the token that we need.

<div align="center">
  <div style="float:left;margin-right:10px;">
  <img height=auto width=400 src="https://user-images.githubusercontent.com/67076071/210668243-62bcb752-2ddf-4208-9c4d-30a497db100e.png"><br>
    <p style="font-size:1.5vw;">Authorization Token</p>
  </div>
</div>

Copy its value and set it as ```TOKEN``` inside ```main.py```

### Setting the user ID
Now, we need to set up the receiver for our messages. Turn on developer mode for discord by going to Settings > Advanced and then Developer Mode = On. Then, right-click on the user that you want to send the messages to, and a new menu-button, ```Copy ID``` will show up. After clicking it, paste it under ```USER_ID``` inside ```main.py```.

### Changing time zone
This is optional, but make sure to change the ```UTC``` value accordingly to the timezone you are in. Default is ```UTC+13```.

## Setting up repl.it

Uncomment the ```# keep_alive()``` in ```main.py``` and copy every ```.py``` files into a repl.it project. Then, use this [video](https://youtu.be/SPTfmiYiuok?t=3522) to set up the bot on a web server so that it runs 24/7 on the cloud.

<div align="center">
  <div style="float:left;margin-right:10px;">
  <img src="https://user-images.githubusercontent.com/67076071/210669737-c9c70bf5-1566-4584-85b5-871b3093c2b9.png"><br>
    <p style="font-size:1.5vw;">Bot running on repl.it 24/7</p>
  </div>
</div>

## Disclaimers

Self-bots are against Discord's Terms of Service. So use this code responsibly. Do not spam users or it might get you banned.

This code only sends three messages per day and is originally made to message someone I know. I am not liable for any harm or bans caused due to the misuse of this bot.
