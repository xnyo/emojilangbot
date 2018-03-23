import re

import discord
from discord import Member
from decouple import config, Csv
import emoji

CONFIG = {
    "BOT_TOKEN": config("BOT_TOKEN", default=""),
    "CHANNEL_ID": config("CHANNEL_ID", default="", cast=Csv(int))
}
client = discord.Client()
emoji_regex = re.compile(r"^[{}\s]+$".format(emoji.get_emoji_regexp().pattern), re.UNICODE)
mention_regex = re.compile(r"<@\d+>")


@client.event
async def on_ready():
    # Just for logging purposes
    print("=> Logged in as {} [{}]. Ready!".format(
        client.user.name, client.user.id
    ))


@client.event
async def on_message(message):
    # Ignore PMs, messages in different channels and our messages
    if message.server is None or int(message.channel.id) not in CONFIG["CHANNEL_ID"] or message.author == client.user:
        return

    # Post rules if needed
    if message.content.strip().lower() == ";emoji" \
            and type(message.author) is Member and message.author.server_permissions.administrator:
        await client.send_message(message.channel, "**:wave: Welcome to the :joy: :speaking_head: channel!**\n\n"
                                                   "_The_ :person_with_blond_hair:_kind  has been :thinking:_  "
                                                   "_a_ :question: _for ages..._\n"
                                                   "**Is it possible to :person_with_blond_hair::speech_balloon:"
                                                   ":speech_left::person_with_blond_hair: only by using :joy::joy:?**\n"
                                                   "For the sake of :alembic::nerd:, I'm here to try to :bulb:!\n"
                                                   "In this :hash:, you'll be able to :person_with_blond_hair:"
                                                   ":speech_balloon::speech_left::person_with_blond_hair: "
                                                   "only by :joy::joy:.\n\n"
                                                   "__**All :speech_balloon: containing :abcd:, :one: :two:, :symbols: "
                                                   "will get :put_litter_in_its_place:! :angry::anger:**__"
                                                   "\n**Have fun! :smile:**")

    # Strip mentions from the message
    clean_content = mention_regex.sub("", message.content).strip()

    # Delete the message if it contains numbers/letters/symbols
    if not clean_content or not emoji_regex.match(clean_content):
        await client.delete_message(message)
        print("=> Deleted message {}".format(message.content))


def main():
    print("""\033[92m            ∩
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
     Made by Nyo\033[0m\n""")
    print("=> Starting Discord Bot")
    client.run(CONFIG["BOT_TOKEN"])


if __name__ == "__main__":
    main()
