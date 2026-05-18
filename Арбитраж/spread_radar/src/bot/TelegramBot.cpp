#include "bot/TelegramBot.h"

#include <windows.h>
#include <winhttp.h>
#include <stdexcept>
#include <sstream>

#pragma comment(lib, "winhttp.lib")

using json = nlohmann::json;

static std::wstring toWide(const std::string& str) {
    if (str.empty()) return L"";

    int size = MultiByteToWideChar(CP_UTF8, 0, str.c_str(), -1, nullptr, 0);
    std::wstring result(size - 1, 0);

    MultiByteToWideChar(CP_UTF8, 0, str.c_str(), -1, result.data(), size);

    return result;
}

TelegramBot::TelegramBot(const std::string& token)
    : token(token), apiUrl("api.telegram.org") {
}

std::string TelegramBot::request(
    const std::string& method,
    const json& payload
) {
    std::wstring host = toWide(apiUrl);
    std::wstring path = toWide("/bot" + token + "/" + method);
    std::string body = payload.dump();

    HINTERNET session = WinHttpOpen(
        L"SpreadRadarBot/1.0",
        WINHTTP_ACCESS_TYPE_DEFAULT_PROXY,
        WINHTTP_NO_PROXY_NAME,
        WINHTTP_NO_PROXY_BYPASS,
        0
    );

    if (!session) {
        throw std::runtime_error("WinHttpOpen failed");
    }

    HINTERNET connect = WinHttpConnect(
        session,
        host.c_str(),
        INTERNET_DEFAULT_HTTPS_PORT,
        0
    );

    if (!connect) {
        WinHttpCloseHandle(session);
        throw std::runtime_error("WinHttpConnect failed");
    }

    HINTERNET request = WinHttpOpenRequest(
        connect,
        L"POST",
        path.c_str(),
        nullptr,
        WINHTTP_NO_REFERER,
        WINHTTP_DEFAULT_ACCEPT_TYPES,
        WINHTTP_FLAG_SECURE
    );

    if (!request) {
        WinHttpCloseHandle(connect);
        WinHttpCloseHandle(session);
        throw std::runtime_error("WinHttpOpenRequest failed");
    }

    std::wstring headers = L"Content-Type: application/json\r\n";

    BOOL sent = WinHttpSendRequest(
        request,
        headers.c_str(),
        static_cast<DWORD>(headers.size()),
        reinterpret_cast<LPVOID>(body.data()),
        static_cast<DWORD>(body.size()),
        static_cast<DWORD>(body.size()),
        0
    );

    if (!sent) {
        WinHttpCloseHandle(request);
        WinHttpCloseHandle(connect);
        WinHttpCloseHandle(session);
        throw std::runtime_error("WinHttpSendRequest failed");
    }

    if (!WinHttpReceiveResponse(request, nullptr)) {
        WinHttpCloseHandle(request);
        WinHttpCloseHandle(connect);
        WinHttpCloseHandle(session);
        throw std::runtime_error("WinHttpReceiveResponse failed");
    }

    std::string response;
    DWORD size = 0;

    do {
        DWORD downloaded = 0;

        if (!WinHttpQueryDataAvailable(request, &size)) {
            break;
        }

        if (size == 0) {
            break;
        }

        std::string buffer(size, '\0');

        if (!WinHttpReadData(
            request,
            buffer.data(),
            size,
            &downloaded
        )) {
            break;
        }

        buffer.resize(downloaded);
        response += buffer;

    } while (size > 0);

    WinHttpCloseHandle(request);
    WinHttpCloseHandle(connect);
    WinHttpCloseHandle(session);

    return response;
}

json TelegramBot::getUpdates(int offset) {
    json payload = {
        {"timeout", 25},
        {"offset", offset}
    };

    return json::parse(request("getUpdates", payload));
}

void TelegramBot::sendMessage(
    long long chatId,
    const std::string& text,
    const json& replyMarkup
) {
    json payload = {
        {"chat_id", chatId},
        {"text", text}
    };

    if (!replyMarkup.is_null()) {
        payload["reply_markup"] = replyMarkup;
    }

    request("sendMessage", payload);
}

void TelegramBot::editMessage(
    long long chatId,
    int messageId,
    const std::string& text,
    const json& replyMarkup
) {
    json payload = {
        {"chat_id", chatId},
        {"message_id", messageId},
        {"text", text}
    };

    if (!replyMarkup.is_null()) {
        payload["reply_markup"] = replyMarkup;
    }

    request("editMessageText", payload);
}
void TelegramBot::answerCallbackQuery(const std::string& callbackQueryId) {
    json payload = {
        {"callback_query_id", callbackQueryId}
    };

    request("answerCallbackQuery", payload);
}