#pragma once
#include "bot/TelegramBot.h"

#include <string>
#include <map>
#include <set>

struct UserState {
    std::string token;
    std::set<std::string> exchanges;
};

class BotHandlers {
private:
    std::map<long long, UserState> states;

public:
    void handleUpdate(TelegramBot& bot, const nlohmann::json& update);

private:
    void handleMessage(TelegramBot& bot, const nlohmann::json& message);
    void handleCallback(TelegramBot& bot, const nlohmann::json& callback);
};