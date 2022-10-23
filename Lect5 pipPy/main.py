# from isOdd import isOdd
# # Библиотека проверки четности
# print(isOdd(1)) 
# print(isOdd(4)) 



# import time

# from progress.bar import Bar

# bar = Bar('Processing', max=20)
# for i in range(20):
#     # Do some work
#     time.sleep(1)
#     bar.next()
# bar.finish()

# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))

# print(emoji.emojize('Python is :thumbsup:', language='alias'))

# print(emoji.demojize('Python is 👍'))
# # Python is :thumbs_up:
# print(emoji.emojize("Python is fun :red_heart:"))

# print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
#  #red heart, not black heart
# print(emoji.is_emoji("👍"))


# import matplotlib.pyplot as plt
# import numpy as np

# list = [1,2,8,9,3,4,8,2,4,5,1,4]
# plt.plot(list)

# plt.show()



from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *



app = ApplicationBuilder().token("5327102789:AAE5r70rMCaJzeKJIlItf4FBKWOXXteY65M").build()

app.add_handler(CommandHandler("hi", hi_command))

app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

print('server start')

app.run_polling()
