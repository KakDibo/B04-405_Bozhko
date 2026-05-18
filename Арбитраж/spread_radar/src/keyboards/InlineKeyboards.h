#pragma once
#include <string>
#include <set>
#include <nlohmann/json.hpp>

namespace InlineKeyboards {
    nlohmann::json mainMenu();
    nlohmann::json tokenMenu();
    nlohmann::json exchangeMenu(const std::set<std::string>& selected);
    nlohmann::json amountMenu();
    nlohmann::json restartMenu();
}