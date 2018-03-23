<p align="center">
  <img src="https://eggplants.org/cuh8hg.svg" height="248">
  <h2 align="center">EmojiLang Bot</h2>
  <h3 align="center">A Discord bot for emoji-speaking people!</h2>
</p>

---

> _The :person_with_blond_hair:_kind has been :thinking:  a :question: for ages..._  
> **Is it possible to :person_with_blond_hair::speech_balloon::speech_balloon::person_with_blond_hair: only by using :joy::joy:?**  
> For the sake of :alembic:, I'm here to try to :bulb:!  

---

### What is this bot?
This Discord Bot deletes all messages that don't contain emojis. Only emojis, whitespaces and mentions are allowed.

### Okay... but why??
This was a joke made for [Ripple](https://ripple.moe)'s 2018 April's fool day.

---

### Setting up
- Install Python 3(.6) and pip  
- Create a Discord Bot and add it to your server  
- Create one or more channels in your Discord server for emoji-speaking people  
Then, set up the bot:
```bash
$ git clone ...
$ cd emojilang
$ cp config.sample.ini config.ini
$ nano config.ini
[put your token and channel_ids in config.ini]
[you can get the channel ID by right clicking the channel from the client and selecting 'Copy ID']
$ virtualenv -p $(which python3.6) .pyenv
$ source .pyenv/bin/activate
(.pyenv)$ pip install -r requirements.txt
(.pyenv)$ python emojilang.py
             ∩
　　　　　　　＼＼
　　　　　　　／　）
⊂＼＿／￣￣￣　 ／
　＼＿／ ° ͜ʖ °（
　　　）　　 　／⌒＼
　　／　 ＿＿＿／⌒＼⊃
　（　 ／
　　＼＼
     U
   E M O J I S ! ! !
     Made by Nyo

=> Starting Discord Bot
=> Logged in as Emoji Bot [xxxxxxxxxxxxxxx]. Ready!
```
The bot will start deleting non-emoji messages in the channels you've configured in the settings file.  
If you have the "Administrator" privilege on Discord, you can use the `;emoji` command to make the bot post an explaination message.

### License
This project is licensed under the GNU AGPL 3 License.  
See the “LICENSE” file for more information.
