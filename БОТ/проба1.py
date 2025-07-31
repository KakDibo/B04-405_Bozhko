import asyncio
import json
import random
import os
from datetime import datetime
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Game
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

# Конфигурация
BOT_TOKEN = "7596427516:AAGuvAu9W9iwsEuROSmQ65JUUf7mD0iM5Es"  # Замените на ваш токен
GAME_SHORT_NAME = "flappy_bird"  # Короткое имя игры в BotFather

# Инициализация бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()

# Структура для хранения данных пользователей
class UserData:
    def __init__(self):
        self.users = {}
        self.leaderboard = []
        self.load_data()
    
    def load_data(self):
        """Загрузка данных из файла"""
        try:
            if os.path.exists('user_data.json'):
                with open('user_data.json', 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.users = data.get('users', {})
                    self.leaderboard = data.get('leaderboard', [])
        except Exception as e:
            print(f"Ошибка загрузки данных: {e}")
    
    def save_data(self):
        """Сохранение данных в файл"""
        try:
            data = {
                'users': self.users,
                'leaderboard': self.leaderboard
            }
            with open('user_data.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Ошибка сохранения данных: {e}")
    
    def get_user_stats(self, user_id: int):
        """Получение статистики пользователя"""
        user_id_str = str(user_id)
        if user_id_str not in self.users:
            self.users[user_id_str] = {
                'games_played': 0,
                'best_score': 0,
                'total_score': 0,
                'last_played': None
            }
        return self.users[user_id_str]
    
    def update_score(self, user_id: int, score: int):
        """Обновление счета пользователя"""
        user_id_str = str(user_id)
        user_stats = self.get_user_stats(user_id)
        
        user_stats['games_played'] += 1
        user_stats['total_score'] += score
        user_stats['last_played'] = datetime.now().isoformat()
        
        if score > user_stats['best_score']:
            user_stats['best_score'] = score
        
        # Обновление таблицы лидеров
        self.update_leaderboard(user_id, score)
        self.save_data()
    
    def update_leaderboard(self, user_id: int, score: int):
        """Обновление таблицы лидеров"""
        # Удаляем старую запись пользователя
        self.leaderboard = [entry for entry in self.leaderboard if entry['user_id'] != user_id]
        
        # Добавляем новую запись
        self.leaderboard.append({
            'user_id': user_id,
            'score': score,
            'date': datetime.now().isoformat()
        })
        
        # Сортируем по убыванию счета
        self.leaderboard.sort(key=lambda x: x['score'], reverse=True)
        
        # Оставляем только топ-10
        self.leaderboard = self.leaderboard[:10]

# Глобальный объект для хранения данных
user_data = UserData()

# Создание клавиатур
def get_main_keyboard():
    """Главная клавиатура"""
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="🎮 Играть в Flappy Bird", callback_data="play_game"))
    builder.add(InlineKeyboardButton(text="📊 Моя статистика", callback_data="my_stats"))
    builder.add(InlineKeyboardButton(text="🏆 Таблица лидеров", callback_data="leaderboard"))
    builder.add(InlineKeyboardButton(text="ℹ️ Помощь", callback_data="help"))
    builder.adjust(2)
    return builder.as_markup()

def get_game_keyboard():
    """Клавиатура для запуска игры"""
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="🎮 Запустить игру", callback_data="launch_game"))
    builder.add(InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu"))
    builder.adjust(1)
    return builder.as_markup()

# Обработчики команд
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    """Обработчик команды /start"""
    welcome_text = """
🎮 Добро пожаловать в Flappy Bird Bot!

Этот бот позволяет играть в классическую игру Flappy Bird прямо в Telegram.

🎯 Цель игры: Управляйте птицей и пролетайте через трубы, не задевая их.

🎮 Нажмите "Играть в Flappy Bird" чтобы запустить полноценную игру в отдельном окне.

Выберите действие:
"""
    await message.answer(welcome_text, reply_markup=get_main_keyboard())

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    """Обработчик команды /help"""
    help_text = """
ℹ️ Справка по боту:

🎮 **Игра Flappy Bird:**
- Нажмите "Играть в Flappy Bird" для запуска игры
- Игра откроется в отдельном окне Telegram
- Управляйте птицей касанием экрана или нажатием клавиш
- Избегайте столкновений с трубами и границами экрана
- Каждая пройденная труба даёт 1 очко

📊 **Статистика:**
- Количество сыгранных игр
- Лучший результат
- Общий счёт

🏆 **Таблица лидеров:**
- Топ-10 игроков по лучшему результату
- Обновляется автоматически

🎯 **Управление:**
- Используйте кнопки для навигации
- В игре используйте касания или клавиши

Удачи в игре! 🐦
"""
    await message.answer(help_text, reply_markup=get_main_keyboard())

# Обработчики callback-запросов
@router.callback_query(lambda c: c.data == "main_menu")
async def main_menu(callback: CallbackQuery):
    """Возврат в главное меню"""
    await callback.message.edit_text(
        "🎮 Главное меню\nВыберите действие:",
        reply_markup=get_main_keyboard()
    )
    await callback.answer()

@router.callback_query(lambda c: c.data == "play_game")
async def show_game_info(callback: CallbackQuery):
    """Показать информацию об игре"""
    game_info_text = """
🎮 Flappy Bird - Классическая игра

🎯 **Цель:** Управляйте птицей и пролетайте через трубы

🎮 **Управление:**
- Касание экрана или нажатие клавиш для прыжка
- Избегайте столкновений с трубами
- Каждая труба = 1 очко

🚀 Нажмите "Запустить игру" чтобы начать!
"""
    await callback.message.edit_text(game_info_text, reply_markup=get_game_keyboard())
    await callback.answer()

@router.callback_query(lambda c: c.data == "launch_game")
async def launch_game(callback: CallbackQuery):
    """Запуск игры"""
    try:
        # Отправляем игру пользователю
        await bot.send_game(
            chat_id=callback.from_user.id,
            game_short_name=GAME_SHORT_NAME
        )
        await callback.answer("🎮 Игра запущена! Откройте её в Telegram.")
    except Exception as e:
        await callback.answer(f"❌ Ошибка запуска игры: {e}")
        print(f"Ошибка запуска игры: {e}")

@router.callback_query(lambda c: c.data == "my_stats")
async def show_stats(callback: CallbackQuery):
    """Показать статистику пользователя"""
    stats = user_data.get_user_stats(callback.from_user.id)
    
    stats_text = f"""
📊 Ваша статистика:

🎮 Игр сыграно: {stats['games_played']}
🏆 Лучший результат: {stats['best_score']}
📈 Общий счёт: {stats['total_score']}
"""
    
    if stats['last_played']:
        last_played = datetime.fromisoformat(stats['last_played'])
        stats_text += f"🕐 Последняя игра: {last_played.strftime('%d.%m.%Y %H:%M')}"
    
    await callback.message.edit_text(stats_text, reply_markup=get_main_keyboard())
    await callback.answer()

@router.callback_query(lambda c: c.data == "leaderboard")
async def show_leaderboard(callback: CallbackQuery):
    """Показать таблицу лидеров"""
    if not user_data.leaderboard:
        leaderboard_text = "🏆 Таблица лидеров пуста.\n\nСыграйте в игру, чтобы попасть в топ!"
    else:
        leaderboard_text = "🏆 Таблица лидеров:\n\n"
        for i, entry in enumerate(user_data.leaderboard, 1):
            try:
                user = await bot.get_chat(entry['user_id'])
                username = user.username or user.first_name
            except:
                username = f"Игрок {entry['user_id']}"
            
            date = datetime.fromisoformat(entry['date']).strftime('%d.%m')
            leaderboard_text += f"{i}. {username} - {entry['score']} очков ({date})\n"
    
    await callback.message.edit_text(leaderboard_text, reply_markup=get_main_keyboard())
    await callback.answer()

@router.callback_query(lambda c: c.data == "help")
async def show_help(callback: CallbackQuery):
    """Показать справку"""
    help_text = """
ℹ️ Справка по боту:

🎮 **Игра Flappy Bird:**
- Нажмите "Играть в Flappy Bird" для запуска игры
- Игра откроется в отдельном окне Telegram
- Управляйте птицей касанием экрана или нажатием клавиш
- Избегайте столкновений с трубами и границами экрана
- Каждая пройденная труба даёт 1 очко

📊 **Статистика:**
- Количество сыгранных игр
- Лучший результат
- Общий счёт

🏆 **Таблица лидеров:**
- Топ-10 игроков по лучшему результату
- Обновляется автоматически

🎯 **Управление:**
- Используйте кнопки для навигации
- В игре используйте касания или клавиши

Удачи в игре! 🐦
"""
    await callback.message.edit_text(help_text, reply_markup=get_main_keyboard())

# Обработчик результатов игры
@router.message(lambda message: message.game)
async def handle_game_result(message: types.Message):
    """Обработка результатов игры"""
    if message.game and message.game.short_name == GAME_SHORT_NAME:
        # Получаем результат игры из callback_data
        if hasattr(message, 'game_high_score'):
            score = message.game_high_score
        else:
            score = 0
        
        # Обновляем статистику пользователя
        user_data.update_score(message.from_user.id, score)
        
        # Отправляем сообщение с результатом
        result_text = f"""
🎮 Результат игры Flappy Bird!

🏆 Ваш счёт: {score}
📊 Игр сыграно: {user_data.get_user_stats(message.from_user.id)['games_played']}
🥇 Лучший результат: {user_data.get_user_stats(message.from_user.id)['best_score']}

Хотите сыграть ещё раз?
"""
        await message.answer(result_text, reply_markup=get_main_keyboard())

# Обработчик callback от игры
@router.callback_query(lambda c: c.data.startswith("game_"))
async def handle_game_callback(callback: CallbackQuery):
    """Обработка callback от игры"""
    if callback.data.startswith("game_"):
        # Извлекаем результат игры из callback_data
        try:
            score = int(callback.data.split("_")[1])
            user_data.update_score(callback.from_user.id, score)
            
            result_text = f"""
🎮 Результат игры Flappy Bird!

🏆 Ваш счёт: {score}
📊 Игр сыграно: {user_data.get_user_stats(callback.from_user.id)['games_played']}
🥇 Лучший результат: {user_data.get_user_stats(callback.from_user.id)['best_score']}

Хотите сыграть ещё раз?
"""
            await callback.message.edit_text(result_text, reply_markup=get_main_keyboard())
        except:
            await callback.answer("🎮 Игра завершена!")
    
    await callback.answer()

# Регистрация роутера
dp.include_router(router)

async def main():
    """Главная функция"""
    print("🤖 Бот запущен...")
    print("🎮 Flappy Bird Bot готов к работе!")
    print("📝 Убедитесь, что игра зарегистрирована в BotFather с именем: flappy_bird_game")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
