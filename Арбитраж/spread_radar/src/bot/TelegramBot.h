#pragma once
#include <string>
#include <nlohmann/json.hpp>

class TelegramBot {
private:
    std::string token;
    std::string apiUrl;

    std::string request(
        const std::string& method,
        const nlohmann::json& payload
    );

public:
    explicit TelegramBot(const std::string& token);

    nlohmann::json getUpdates(int offset);
    void sendMessage(
        long long chatId,
        const std::string& text,
        const nlohmann::json& replyMarkup = nullptr
    );

    void editMessage(
        long long chatId,
        int messageId,
        const std::string& text,
        const nlohmann::json& replyMarkup = nullptr
    );

    void answerCallbackQuery(const std::string& callbackQueryId);
};