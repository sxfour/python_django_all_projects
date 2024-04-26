#pragma once

#include <string>
#include <cpr/cpr.h>
#include <nlohmann/json.hpp>

namespace urls {
    constexpr std::string_view get_jwt_url{ "http://127.0.0.1:7631/teploset_api/token/" };
    constexpr std::string_view upload_arh_url{ "http://127.0.0.1:7631/teploset_docs/" };
    constexpr std::string_view test_conn{ "http://127.0.0.1:7631/" };
    constexpr std::string_view auth_jwt_body{ "{\"username\": \"root\", \"password\":\"toor\"}" };
}

// Получение нового токена
std::string get_jwt_refresh() {
    cpr::Response jwt_resp_r = cpr::Post(
        cpr::Url{ urls::get_jwt_url },
        cpr::Body{ urls::auth_jwt_body },
        cpr::Header{ {"Content-Type", "application/json"} },
        cpr::Timeout{ 1000 }
    );

    if (jwt_resp_r.status_code == 200) {
        const std::string jwt_resp_data = jwt_resp_r.text;

        return jwt_resp_data;
    }

    return jwt_resp_r.error.message;
}

// Проверка соединения до сервера
int test_conn() {
    cpr::Response test_conn_resp = cpr::Get(
        cpr::Url{ urls::test_conn },
        cpr::Timeout{ 1000 }
    );

    if (test_conn_resp.status_code == 404) {
        return 1;
    } 
    else {
        return 0;
    }
}

// Запись данных в json
int write_to_json(const std::string json_data, std::string file_name) {
    std::fstream file;
    file.open(file_name, std::ios_base::out);

    if (!file.is_open()) {
        return 0;
    }

    file.write(json_data.data(), json_data.size());
    file.close();

    return 1;
}

// Считывание с json
nlohmann::json read_data_json(std::string file_name) {
    std::ifstream f(file_name);
    nlohmann::json data = nlohmann::json::parse(f);

    return data;
}
