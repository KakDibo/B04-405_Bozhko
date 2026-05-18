#include "handlers/BotHandlers.h"
#include "keyboards/InlineKeyboards.h"
#include "services/SpreadService.h"

#include <vector>
#include <sstream>

using json = nlohmann::json;

void BotHandlers::handleUpdate(TelegramBot& bot, const json& update) {
    if (update.contains("message")) {
        handleMessage(bot, update["message"]);
    }

    if (update.contains("callback_query")) {
        handleCallback(bot, update["callback_query"]);
    }
}

void BotHandlers::handleMessage(TelegramBot& bot, const json& message) {
    long long chatId = message["chat"]["id"];

    std::string text = message.value("text", "");

    if (text == "/start") {
        states[chatId] = UserState{};

        bot.sendMessage(
            chatId,
            "Привет. Это Spread Radar Bot.\n\n"
            "Бот показывает возможный арбитраж между биржами: "
            "Binance, Coinbase и Kraken.\n\n"
            "Выбери действие:",
            InlineKeyboards::mainMenu()
        );

        return;
    }

    bot.sendMessage(
        chatId,
        "Используй /start, чтобы открыть меню.",
        InlineKeyboards::mainMenu()
    );
}

void BotHandlers::handleCallback(TelegramBot& bot, const json& callback) {
    std::string callbackId = callback["id"];
    std::string data = callback.value("data", "");

    long long chatId = callback["message"]["chat"]["id"];
    int messageId = callback["message"]["message_id"];

    bot.answerCallbackQuery(callbackId);

    if (data == "back:main") {
        states[chatId] = UserState{};

        bot.editMessage(
            chatId,
            messageId,
            "Главное меню:",
            InlineKeyboards::mainMenu()
        );

        return;
    }

    if (data == "info") {
        bot.editMessage(
            chatId,
            messageId,
            "Spread Radar — учебный проект для поиска разницы bid/ask "
            "между криптобиржами.\n\n "
            "Важно: это симуляция. Комиссии, задержки, ликвидность и перевод "
            "средств между биржами сейчас не учитываются.",
            InlineKeyboards::restartMenu()
        );

        return;
    }

    if (data == "scan:start") {
        states[chatId] = UserState{};

        bot.editMessage(
            chatId,
            messageId,
            "Выбери токен:",
            InlineKeyboards::tokenMenu()
        );

        return;
    }

    if (data.rfind("token:", 0) == 0) {
        std::string token = data.substr(6);

        states[chatId].token = token;
        states[chatId].exchanges.clear();

        bot.editMessage(
            chatId,
            messageId,
            "Токен: " + token + "\n\nТеперь выбери платформы:",
            InlineKeyboards::exchangeMenu(states[chatId].exchanges)
        );

        return;
    }

    if (data.rfind("exchange:", 0) == 0) {
        std::string exchange = data.substr(9);

        auto& selected = states[chatId].exchanges;

        if (selected.count(exchange)) {
            selected.erase(exchange);
        }
        else {
            selected.insert(exchange);
        }

        bot.editMessage(
            chatId,
            messageId,
            "Токен: " + states[chatId].token + "\n\nВыбери минимум две платформы:",
            InlineKeyboards::exchangeMenu(selected)
        );

        return;
    }

    if (data == "back:exchanges") {
        bot.editMessage(
            chatId,
            messageId,
            "Токен: " + states[chatId].token + "\n\nВыбери минимум две платформы:",
            InlineKeyboards::exchangeMenu(states[chatId].exchanges)
        );

        return;
    }

    if (data == "platforms:done") {
        if (states[chatId].exchanges.size() < 2) {
            bot.editMessage(
                chatId,
                messageId,
                "Нужно выбрать минимум две платформы.",
                InlineKeyboards::exchangeMenu(states[chatId].exchanges)
            );

            return;
        }

        bot.editMessage(
            chatId,
            messageId,
            "Выбери сумму симуляции:",
            InlineKeyboards::amountMenu()
        );
        return;
    }

    if (data.rfind("amount:", 0) == 0) {
        double amount = std::stod(data.substr(7));

        std::vector<std::string> exchanges(
            states[chatId].exchanges.begin(),
            states[chatId].exchanges.end()
        );

        bot.editMessage(
            chatId,
            messageId,
            "Считаю данные по биржам..."
        );

        SpreadService service;
        BotSpreadResult result = service.calculate(
            states[chatId].token,
            exchanges,
            amount
        );

        bot.sendMessage(
            chatId,
            result.text,
            InlineKeyboards::restartMenu()
        );

        return;
    }
}