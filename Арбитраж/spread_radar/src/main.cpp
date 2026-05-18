#include "bot/TelegramBot.h"
#include "handlers/BotHandlers.h"
#include "config/BotConfig.h"

#include <windows.h>
#include <iostream>
#include <thread>
#include <chrono>

int main() {
    SetConsoleOutputCP(CP_UTF8);
    SetConsoleCP(CP_UTF8);

    TelegramBot bot(BotConfig::token());
    BotHandlers handlers;

    int offset = 0;

    std::cout << "Spread Radar Telegram Bot started\n";

    while (true) {
        try {
            auto updates = bot.getUpdates(offset);

            if (!updates.value("ok", false)) {
                std::cerr << "Telegram API error\n";
                continue;
            }

            for (const auto& update : updates["result"]) {
                offset = update["update_id"].get<int>() + 1;
                handlers.handleUpdate(bot, update);
            }

        }
        catch (const std::exception& e) {
            std::cerr << "Error: " << e.what() << "\n";
            std::this_thread::sleep_for(std::chrono::seconds(3));
        }
    }

    return 0;
}