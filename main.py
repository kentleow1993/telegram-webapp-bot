import os

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo,
)
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                text="🎰 进入 4Win",
                web_app=WebAppInfo(
                    url="https://www.4win.vip/myr/home"
                ),
            )
        ]
    ]

    await update.message.reply_text(
        "欢迎来到 4Win！\n\n请点击下面按钮进入网站。",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
