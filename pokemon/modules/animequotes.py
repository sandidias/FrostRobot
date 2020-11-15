#Made By @Madepranav On Telegram & Github Id Superboyfan
import html
import random
import pokemon.modules.animequotesstring as animequotesstring
from pokemon import dispatcher
from telegram import ParseMode, Update, Bot
from pokemon.modules.disable import DisableAbleCommandHandler
from telegram.ext import run_async



@run_async
def animequotes(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message if message.reply_to_message else message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        patted_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(patted_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    animequotes_type = random.choice(("Text", "Gif", "Sticker"))
    if animequotes == "Gif":
        try:
            temp = random.choice(animequotesstring.ANIMEQUTOES_GIFS)
            reply_to.reply_animation(temp)
        except BadRequest:
            animequotes_type = "Text"

    if animequotes_type == "Sticker":
        try:
            temp = random.choice(animequotesstring.ANIMEQUTOES_STICKERS)
            reply_to.reply_sticker(temp)
        except BadRequest:
            animequotes_type = "Text"

    if animequotes_type == "Text":
        temp = random.choice(animequotesstring.ANIMEQUTOES_TEMPLATES)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)


__help__ = """
 • `/animequotes`*:* for random animequotes
"""

ANIMEQUTOES_HANDLER = DisableAbleCommandHandler("animequotes", animequotes)


dispatcher.add_handler(ANIMEQUTOES_HANDLER)

__mod_name__ = "ANIMEQUTOES"
