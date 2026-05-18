#include "services/SpreadService.h"

#include "exchange/BinanceClient.h"
#include "exchange/CoinbaseClient.h"
#include "exchange/KrakenClient.h"
#include "core/SpreadCalculator.h"
#include "core/Fee.h"

#include <sstream>
#include <iomanip>
#include <map>

BotSpreadResult SpreadService::calculate(
    const std::string& symbol,
    const std::vector<std::string>& exchanges,
    double amount
) {
    std::vector<TokenPrice> prices;

    BinanceClient binance;
    CoinbaseClient coinbase;
    KrakenClient kraken;

    for (const auto& exchange : exchanges) {
        if (exchange == "Binance") {
            prices.push_back(binance.getTokenPrice(symbol));
        }
        else if (exchange == "Coinbase") {
            prices.push_back(coinbase.getTokenPrice(symbol));
        }
        else if (exchange == "Kraken") {
            prices.push_back(kraken.getTokenPrice(symbol));
        }
    }

    std::map<std::string, Fee> fees;

    Fee zeroFee;
    zeroFee.FeePct = 0.0;

    fees["Binance"] = zeroFee;
    fees["Coinbase"] = zeroFee;
    fees["Kraken"] = zeroFee;

    SpreadCalculator calculator;
    auto result = calculator.simulate(prices, amount, fees);

    std::ostringstream out;
    out << std::fixed << std::setprecision(2);

    out << "📡 Spread Radar\n\n";
    out << "Актив: " << symbol << "\n";
    out << "Сумма: " << amount << " USDT\n\n";

    out << "Котировки:\n";

    for (const auto& price : prices) {
        if (!price.ok) {
            out << "❌ " << price.site << ": " << price.error << "\n";
            continue;
        }

        out << "✅ " << price.site
            << "\nBid: " << price.bid
            << "\nAsk: " << price.ask
            << "\n\n";
    }

    if (!result.has_value()) {
        return {
            false,
            out.str() + "\nНедостаточно данных для расчёта спреда."
        };
    }

    const auto& sim = result.value();

    out << "Лучший маршрут:\n";
    out << "Купить на: " << sim.buySite << "\n";
    out << "Цена покупки ask: " << sim.bestAsk << "\n\n";

    out << "Продать на: " << sim.sellSite << "\n";
    out << "Цена продажи bid: " << sim.bestBid << "\n\n";

    out << "Спред: " << sim.spreadAbs << " USDT\n";
    out << "Спред: " << sim.spreadPct << "%\n\n";

    out << "Комиссии: не учитываются\n";
    out << "Расчётная прибыль: " << sim.profit << " USDT ";
    out << "(" << sim.profitPct << "%)\n";

    return { true, out.str() };
}