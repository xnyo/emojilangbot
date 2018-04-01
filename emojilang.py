import asyncio
import regex

import discord
from discord import Member
from decouple import config, Csv
import emoji

CONFIG = {
    "BOT_TOKEN": config("BOT_TOKEN", default=""),
    "CHANNEL_IDS": config("CHANNEL_IDS", default="", cast=Csv(int))
}
client = discord.Client()

emoji_regex = regex.compile(r"^[{}\s]+$".format(emoji.get_emoji_regexp().pattern), regex.UNICODE)
other_forbidden_emojis = ["\U0001F170", "\U0001F171"]
forbidden_emojis_regex = regex.compile(
    u"([^\U0001F1E6-\U0001F1FF{r}]|^)[\U0001F1E6-\U0001F1FF{r}]([^\U0001F1E6-\U0001F1FF{r}]|$)".format(
        r="".join(other_forbidden_emojis)
    ),
    regex.UNICODE
)
flags_regex = regex.compile(u"([\U0001F1E6-\U0001F1FF][\U0001F1E6-\U0001F1FF])", regex.UNICODE)
mention_regex = regex.compile(r"<@\d+>")
FLAGS_EMOJIS = [
    v.replace(" ", "")
    for k, v in emoji.EMOJI_UNICODE.items()
    if all([0x1F1E6 <= ord(x) <= 0x1F1FF or x == " " for x in v])
]


def num_to_emoji(n):
    assert type(n) is int

    numbers = [":zero:", ":one:", ":two:", ":three:", ":four:", ":five:", ":six:", ":seven:", ":eight:", ":nine:"]
    n = str(n)
    s = ""

    for x in n:
        s += numbers[int(x)]
    return s


def is_emojilang(s):
    # Strip mentions from the message
    clean_content = mention_regex.sub("", s.content).strip()
    # print(clean_content)
    # print([(ord(x), hex(ord(x))) for x in clean_content])

    # Regexes check
    if not clean_content or not emoji_regex.match(clean_content) or forbidden_emojis_regex.match(clean_content):
        return False

    # Flags check
    for flag in flags_regex.findall(clean_content):
        if flag.strip() not in FLAGS_EMOJIS:
            return False

    # All fine
    return True


@client.event
async def on_ready():
    # Just for logging purposes
    print("=> Logged in as {} [{}]. Ready!".format(
        client.user.name, client.user.id
    ))


@client.event
async def on_message(message):
    # Ignore PMs, messages in different channels and our messages
    if message.server is None or int(message.channel.id) not in CONFIG["CHANNEL_IDS"] or message.author == client.user:
        return

    # Post rules if needed
    if type(message.author) is Member and message.author.server_permissions.administrator:
        if message.content.startswith(";emoji"):
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
        elif message.content.startswith(";clean"):
            # Delete trigger message immediately
            await client.delete_message(message)
            bot_response = await client.send_message(
                message.channel, ":robot: :timer: :envelope: :mag:    :five::zero::zero:"
            )
            try:
                counter = 0
                async for log in client.logs_from(message.channel, limit=500):
                    if log.author != client.user:
                        counter += 1
                        if not is_emojilang(log):
                            await client.delete_message(log)
            except:
                await client.edit_message(bot_response, ":warning: :frowning2: :envelope: :mag:")
                raise

            await client.edit_message(bot_response, ":grimacing: :ok_hand: :envelope: :mag: :point_right: {}".format(
                num_to_emoji(counter)
            ))
            await asyncio.sleep(5)
            await client.delete_message(bot_response)
            return

    # Strip mentions from the message
    if not is_emojilang(message):
        await client.delete_message(message)
        print("=> Deleted message {}".format(message.content))


@client.event
async def on_message_edit(before, after):
    # TODO: decorator
    # Ignore PMs, messages in different channels and our messages
    if before.server is None or int(before.channel.id) not in CONFIG["CHANNEL_IDS"] or before.author == client.user:
        return

    # Run emoji check again
    if not is_emojilang(after):
        await client.delete_message(after)
        print("=> Somebody tried to be akerino `{}` => `{}`".format(before.content, after.content))


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
