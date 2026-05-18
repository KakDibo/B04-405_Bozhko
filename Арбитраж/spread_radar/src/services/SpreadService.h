#pragma once
#include <string>
#include <vector>
#include <optional>

struct BotSpreadResult {
    bool ok = false;
    std::string text;
};

class SpreadService {
public:
    BotSpreadResult calculate(
        const std::string& symbol,
        const std::vector<std::string>& exchanges,
        double amount
    );
};