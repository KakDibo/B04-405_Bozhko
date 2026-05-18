#pragma once
#include <string>
#include <vector>

struct BotConfig {
    static std::string token() {
        return "8878105953:AAGQqYX0m-QZT7i3T1YI3jvSXAV7_4t5c3A";
    }

    static std::vector<std::string> tokens() {
        return { "BTC-USDT", "ETH-USDT", "SOL-USDT" };
    }

    static std::vector<std::string> exchanges() {
        return { "Binance", "Coinbase", "Kraken" };
    }
};