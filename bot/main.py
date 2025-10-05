import logging
from telegram.ext import ApplicationBuilder
from config.settings import BOT_TOKEN, PROXY_URL

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

builder = ApplicationBuilder().token(BOT_TOKEN)

if PROXY_URL:
    builder = builder.proxy(PROXY_URL).get_updates_proxy(PROXY_URL)

app = builder.build()