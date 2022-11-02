from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes



def bot_quantity():
    global candies
    if candies > 28:
        candy = candies % 29
    else:
        candy = candies
    # candy = random.randint(min, max)
    # print(f"{bot}, takes {candy} candies")
    return candy

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def new_game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global candies
    candies = 100
    await update.message.reply_text(f'Привет игрок {update.effective_user.first_name}, в корзине 101 конфета. Максимум можно брать 28 кофет. Цель - последним забрать остаток конфет. Делай свой ход: Напиши /game N. Где N - количество конфет, которое ты берешь')

async def game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global candies
    
    msg = update.message.text
    msg = msg.split()[1]    
    msg_number = int(msg)
    candies -= msg_number
    await update.message.reply_text(f'Осталось  {candies} конфет')
    bot_candy = bot_quantity()
    await update.message.reply_text(f'Бот берет {bot_candy} конфет')
    candies -= bot_candy
    await update.message.reply_text(f'Осталось {candies} конфет')

async def abc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    msg = filter(lambda x: 'ов' not in x, msg.split())
    my = " ".join(msg)
    await update.message.reply_text(my)
    
candies = 101

app = ApplicationBuilder().token('токен').build() 
#  тут ввести токен
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("abc", abc))
app.add_handler(CommandHandler("new_game", new_game))
app.add_handler(CommandHandler("game", game))
app.run_polling()