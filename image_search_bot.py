
BOT_HTTP_API_TOKEN = '1054046441:AAFnZ-OcC9B8VYkayo7x1ok1Z79wEOlWkUg'

if __name__== "__main__":
    
    from telegram.ext import Updater, CommandHandler, InlineQueryHandler
    import logging
    from telegram import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent

    updater = Updater(token=BOT_HTTP_API_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    def start(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    updater.start_polling()

    def chat_id(update, context):
        print(context)
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(update.effective_chat.id))

    chat_id_handler = CommandHandler('chat_id', chat_id)
    dispatcher.add_handler(chat_id_handler)

    def inline_photos(update, context):

        query = update.inline_query.query
        if not query:
            return
        results = list()

        from google_image_search import search_images_urls

        image_urls = search_images_urls(query, 30)

        cur_id = 1
        for image_url in image_urls:
            results.append(
                InlineQueryResultPhoto(
                    id="photo" + str(cur_id),
                    photo_url=image_url,
                    thumb_url=image_url,
                )
            )
            cur_id += 1
   
        context.bot.answer_inline_query(update.inline_query.id, results)

    inline_caps_handler = InlineQueryHandler(inline_photos)
    dispatcher.add_handler(inline_caps_handler)
