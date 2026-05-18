#include "keyboards/InlineKeyboards.h"
#include "config/BotConfig.h"

using json = nlohmann::json;

namespace InlineKeyboards {

    json mainMenu() {
        return {
            {"inline_keyboard", {
                {
                    {{"text", "📡 Сканировать арбитраж"}, {"callback_data", "scan:start"}}
                },
                {
                    {{"text", "ℹ️ О проекте"}, {"callback_data", "info"}}
                }
            }}
        };
    }

    json tokenMenu() {
        json rows = json::array();

        for (const auto& token : BotConfig::tokens()) {
            rows.push_back(json::array({
                {{"text", token}, {"callback_data", "token:" + token}}
                }));
        }

        rows.push_back(json::array({
            {{"text", "⬅️ Назад"}, {"callback_data", "back:main"}}
            }));

        return { {"inline_keyboard", rows} };
    }

    json exchangeMenu(const std::set<std::string>& selected) {
        json rows = json::array();

        for (const auto& exchange : BotConfig::exchanges()) {
            std::string mark = selected.count(exchange) ? "✅ " : "☑️ ";

            rows.push_back(json::array({
                {{"text", mark + exchange}, {"callback_data", "exchange:" + exchange}}
                }));
        }

        rows.push_back(json::array({
            {{"text", "➡️ Далее"}, {"callback_data", "platforms:done"}}
            }));

        rows.push_back(json::array({
            {{"text", "⬅️ Назад"}, {"callback_data", "scan:start"}}
            }));

        return { {"inline_keyboard", rows} };
    }

    json amountMenu() {
        return {
            {"inline_keyboard", {
                {
                    {{"text", "100 USDT"}, {"callback_data", "amount:100"}},
                    {{"text", "500 USDT"}, {"callback_data", "amount:500"}}
                },
                {
                    {{"text", "1000 USDT"}, {"callback_data", "amount:1000"}},
                    {{"text", "5000 USDT"}, {"callback_data", "amount:5000"}}
                },
                {
                    {{"text", "⬅️ Назад"}, {"callback_data", "back:exchanges"}}
                }
            }}
        };
    }

    json restartMenu() {
        return {
            {"inline_keyboard", {
                {
                    {{"text", "🔁 Новый расчёт"}, {"callback_data", "scan:start"}}
                },
                {
                    {{"text", "🏠 Главное меню"}, {"callback_data", "back:main"}}
                }
            }}
        };
    }

}