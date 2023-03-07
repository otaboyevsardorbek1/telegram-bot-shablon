async def on_startup(dp):

    import middlewares
    middlewares.setup(dp)


    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)


    import filters
    filters.setup(dp)


    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)
    print('Bot ishladi')


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    import logging

    logging.basicConfig(level=logging.INFO)

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
