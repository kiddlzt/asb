from aiogram import Bot, F, Dispatcher
from aiogram.types import Message, FSInputFile, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command, CommandStart
import config
import asyncio
dp = Dispatcher()

bot = Bot(config.TOKEN)
welcomeImage = FSInputFile('welcome.png')

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer_photo(photo=welcomeImage, caption=f"👋{message.from_user.full_name} добро пожаловать! Я {config.USERNAME} если у тебя спамблок ты можешь оставить сообщение просто написав его и я напишу тебе сам!")

@dp.message()
async def message(message: Message, bot: Bot):
    if len(message.text) > 20:
        await bot.send_message(config.ID, f"📃Пользователь @{message.from_user.username} отправил новое сообщение:\n{message.text}", reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Ответить", url=f"https://t.me/{message.from_user.username}")]]))
        await message.reply("🤖 Я получил сообщение, ожидайте пока я напишу вам.")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())