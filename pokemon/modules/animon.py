#Made By @Madepranav On Telegram & Github Id Superboyfan
import html
import random
import pokemon.modules.animonstring as animonstring
from pokemon import dispatcher
from telegram import ParseMode, Update, Bot
from pokemon.modules.disable import DisableAbleCommandHandler
from telegram.ext import run_async



@run_async
def animon(update: Update, context: CallbackContext):
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

    animon_type = random.choice(("Text", "Gif", "Sticker"))
    if animon_type == "Gif":
        try:
            temp = random.choice(animonstring.ANIMON_GIFS)
            reply_to.reply_animation(temp)
        except BadRequest:
            animon_type = "Text"

    if animon_type == "Sticker":
        try:
            temp = random.choice(animonstring.ANIMON_STICKERS)
            reply_to.reply_sticker(temp)
        except BadRequest:
            animon_type = "Text"

    if animon_type == "Text":
        temp = random.choice(animonstring.ANIMON_TEMPLATES)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)


__help__ = """
 • `/animon`*:* for random animon
"""

ANIMON_HANDLER = DisableAbleCommandHandler("animon", animon)


dispatcher.add_handler(ANIMON_HANDLER)

__mod_name__ = "ANIMON"
