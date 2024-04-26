// WinAPI_Rest_Upload.cpp : Определяет точку входа для приложения.
//

#include "framework.h"
#include "WinAPI_Rest_Upload.h"
#include "rest_winapi.h"

#define MAX_LOADSTRING      100
#define BUTTON_SEND         5
#define LABEL_EDIT          7

#pragma comment(lib, "comctl32.lib")
#pragma comment(lib, "shlwapi.lib")

// Глобальные переменные:
HINSTANCE hInst;                                // текущий экземпляр
WCHAR szTitle[MAX_LOADSTRING];                  // Текст строки заголовка
WCHAR szWindowClass[MAX_LOADSTRING];            // имя класса главного окна

std::string token_jwt{};                        // Токен на сессию программы

// Отправить объявления функций, включенных в этот модуль кода:
ATOM                MyRegisterClass(HINSTANCE hInstance);
BOOL                InitInstance(HINSTANCE, int);
LRESULT CALLBACK    WndProc(HWND, UINT, WPARAM, LPARAM);
INT_PTR CALLBACK    About(HWND, UINT, WPARAM, LPARAM);
INT_PTR CALLBACK    InfoMessage(HWND, UINT, WPARAM, LPARAM);
INT_PTR CALLBACK    InfoMessageFile(HWND, UINT, WPARAM, LPARAM);

void                CreateDialogPathTo(HWND hWnd);
void                WindowAtCenter(HWND window);
void                setFont(HWND window, HFONT h);
void                get_data_window(HWND hWnd);

bool                convToString(std::string& s, const LPWSTR pw, UINT codepage = CP_ACP);

nlohmann::json      UpdateToken();

int APIENTRY wWinMain(_In_ HINSTANCE hInstance, _In_opt_ HINSTANCE hPrevInstance, _In_ LPWSTR lpCmdLine, _In_ int nCmdShow) {
    UNREFERENCED_PARAMETER(hPrevInstance);
    UNREFERENCED_PARAMETER(lpCmdLine);

    // TODO: Разместите код здесь.

    // Инициализация глобальных строк
    LoadStringW(hInstance, IDS_APP_TITLE, szTitle, MAX_LOADSTRING);
    LoadStringW(hInstance, IDC_WINAPIRESTUPLOAD, szWindowClass, MAX_LOADSTRING);
    MyRegisterClass(hInstance);

    // Выполнить инициализацию приложения:
    if (!InitInstance (hInstance, nCmdShow)) { return FALSE; }

    HACCEL hAccelTable = LoadAccelerators(hInstance, MAKEINTRESOURCE(IDC_WINAPIRESTUPLOAD));

    MSG msg;

    // Цикл основного сообщения:
    while (GetMessage(&msg, nullptr, 0, 0)) {
        if (!TranslateAccelerator(msg.hwnd, hAccelTable, &msg))
        {
            TranslateMessage(&msg);
            DispatchMessage(&msg);
        }
    }

    return (int) msg.wParam;
}

//
//  ФУНКЦИЯ: MyRegisterClass()
//
//  ЦЕЛЬ: Регистрирует класс окна.
//
ATOM MyRegisterClass(HINSTANCE hInstance) {
    WNDCLASSEXW wcex{};

    wcex.cbSize = sizeof(WNDCLASSEX);

    wcex.style          = CS_HREDRAW | CS_VREDRAW;
    wcex.lpfnWndProc    = WndProc;
    wcex.cbClsExtra     = 0;
    wcex.cbWndExtra     = 0;
    wcex.hInstance      = hInstance;
    wcex.hIcon          = LoadIcon(hInstance, MAKEINTRESOURCE(IDI_WINAPIRESTUPLOAD));
    wcex.hCursor        = LoadCursor(nullptr, IDC_ARROW);
    wcex.hbrBackground  = CreateSolidBrush(RGB(135, 206, 250));

    wcex.lpszMenuName   = MAKEINTRESOURCEW(IDC_WINAPIRESTUPLOAD);
    wcex.lpszClassName  = szWindowClass;
    wcex.hIconSm        = LoadIcon(wcex.hInstance, MAKEINTRESOURCE(IDI_SMALL));

    return RegisterClassExW(&wcex);
}

//
//   ФУНКЦИЯ: InitInstance(HINSTANCE, int)
//
//   ЦЕЛЬ: Сохраняет маркер экземпляра и создает главное окно
//
//   КОММЕНТАРИИ:
//
//        В этой функции маркер экземпляра сохраняется в глобальной переменной, а также
//        создается и выводится главное окно программы.
//
BOOL InitInstance(HINSTANCE hInstance, int nCmdShow) {
   hInst = hInstance; // Сохранить маркер экземпляра в глобальной переменной
   HFONT hFont;
   hFont = CreateFont(16, 0, 0, 600, FW_NORMAL, FALSE, FALSE, FALSE, 0, OUT_DEFAULT_PRECIS, CLIP_DEFAULT_PRECIS, NULL, NULL, L"Microsoft Sans Serif");

   HFONT hFont_title;
   hFont_title = CreateFont(20, 0, 0, 700, FW_NORMAL, FALSE, FALSE, FALSE, 0, OUT_DEFAULT_PRECIS, CLIP_DEFAULT_PRECIS, NULL, NULL, L"Microsoft Sans Serif");

   HWND hWnd;
   hWnd = CreateWindowW(szWindowClass, L"Отправка телефонограмм", WS_POPUPWINDOW | WS_VISIBLE | WS_CAPTION | BS_CENTER, 100, 100, 600, 272, 0, 0, hInstance, 0);

   HWND InfoLabel_1;
   InfoLabel_1 = CreateWindowW(L"static", L"- Обновите токен (Настройки -> Обновить токен)\n- Нажмите Прикрепить и отправить\n- Прикрепите архив\n- При успешном соединении получите успешный ответ", WS_CHILD | WS_VISIBLE, 110, 40, 400, 70, hWnd, NULL, NULL, NULL);
   setFont(InfoLabel_1, hFont);

   HWND InfoLabel;
   InfoLabel = CreateWindowW(L"static", L"Полная инструкция к отправке архивов (.pdf / .zip) телефонограмм:", WS_CHILD | WS_VISIBLE, 10, 10, 545, 100, hWnd, NULL, NULL, NULL);
   setFont(InfoLabel, hFont_title);

   HWND hButton;
   hButton = CreateWindow(TEXT("button"), TEXT("Прикрепить и отправить"), WS_VISIBLE | WS_CHILD, 375, 120, 180, 25, hWnd, (HMENU)5, NULL, NULL);
   setFont(hButton, hFont);

   if (!hWnd) { return FALSE; }

   ShowWindow(hWnd, nCmdShow);
   UpdateWindow(hWnd);

   return TRUE;
}

//
//  ФУНКЦИЯ: WndProc(HWND, UINT, WPARAM, LPARAM)
//
//  ЦЕЛЬ: Обрабатывает сообщения в главном окне.
//
//  WM_COMMAND  - обработать меню приложения
//  WM_PAINT    - Отрисовка главного окна
//  WM_DESTROY  - отправить сообщение о выходе и вернуться
//
//
LRESULT CALLBACK WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam) {
    switch (message) {
    case WM_CREATE: {
        // Центрирование окна
        WindowAtCenter(hWnd);
        break;
    }
    case WM_COMMAND: {
            int wmId = LOWORD(wParam);

            // Разобрать выбор в меню:
            switch (wmId) {
            case IDM_ABOUT: 
                DialogBox(hInst, MAKEINTRESOURCE(IDD_ABOUTBOX), hWnd, About);
                break;
            case IDM_EXIT:
                DestroyWindow(hWnd);
                break;
            case IDM_UPDATE_TOKEN:
                if (UpdateToken() == 0) { DialogBox(hInst, MAKEINTRESOURCE(IDD_SUCCESSBOX), hWnd, InfoMessage); }
                else { DialogBox(hInst, MAKEINTRESOURCE(IDD_ERRORBOX), hWnd, InfoMessage); }
                break;
            case IDM_VIEW_ALL:
                get_data_window(hWnd);
                break;
            case BUTTON_SEND:
                CreateDialogPathTo(hWnd);
                break;
            case ID_TEST_CONN:
                if (test_conn() == 1) { DialogBox(hInst, MAKEINTRESOURCE(IDD_SUCCESS_TEST), hWnd, InfoMessage); }
                else { DialogBox(hInst, MAKEINTRESOURCE(IDD_ERRORBOX), hWnd, InfoMessage); }
                break;
            default:
                return DefWindowProc(hWnd, message, wParam, lParam);
            }
        }
        break;
    case WM_PAINT: {
            PAINTSTRUCT ps;
            HDC hdc = BeginPaint(hWnd, &ps);
            // TODO: Добавьте сюда любой код прорисовки, использующий HDC...
            EndPaint(hWnd, &ps);
        }
        break;
    case WM_DESTROY:
        PostQuitMessage(0);
        break;
    default:
        return DefWindowProc(hWnd, message, wParam, lParam);
    }
    return 0;
}

// Обработчик сообщений для окна "О программе".
INT_PTR CALLBACK About(HWND hDlg, UINT message, WPARAM wParam, LPARAM lParam) {
    UNREFERENCED_PARAMETER(lParam);
    switch (message) {
    case WM_INITDIALOG:
        return (INT_PTR)TRUE;

    case WM_COMMAND:
        if (LOWORD(wParam) == IDOK || LOWORD(wParam) == IDCANCEL) {
            EndDialog(hDlg, LOWORD(wParam));
            return (INT_PTR)TRUE;
        }
        break;
    }
    return (INT_PTR)FALSE;
}

// Обработчик сообщений для окна "Информация".
INT_PTR CALLBACK InfoMessage(HWND hDlg, UINT message, WPARAM wParam, LPARAM lParam) {
    UNREFERENCED_PARAMETER(lParam);
    switch (message) {
    case WM_INITDIALOG:
        return (INT_PTR)TRUE;
    case WM_COMMAND:
        if (LOWORD(wParam) == IDOK || LOWORD(wParam) == IDCANCEL) {
            EndDialog(hDlg, LOWORD(wParam));
            return (INT_PTR)TRUE;
        }
        break;
    }
    return (INT_PTR)FALSE;
}

// Обработчик сообщений для окна "Ошибка указания архива".
INT_PTR CALLBACK InfoMessageFile(HWND hDlg, UINT message, WPARAM wParam, LPARAM lParam) {
    UNREFERENCED_PARAMETER(lParam);
    switch (message) {
    case WM_INITDIALOG:
        return (INT_PTR)TRUE;
    case WM_COMMAND:
        if (LOWORD(wParam) == IDOK || LOWORD(wParam) == IDCANCEL) {
            EndDialog(hDlg, LOWORD(wParam));
            return (INT_PTR)TRUE;
        }
        break;
    }
    return (INT_PTR)FALSE;
}

// Функция центрирования окна
void WindowAtCenter(HWND window) {
    int screenWidth = GetSystemMetrics(SM_CXSCREEN);
    int screenHeight = GetSystemMetrics(SM_CYSCREEN);

    RECT clientRect;

    GetClientRect(window, &clientRect);

    int clientWidth = clientRect.right - clientRect.left;
    int clientHeight = clientRect.bottom - clientRect.top;

    SetWindowPos(window, NULL, screenWidth / 2 - clientWidth / 2, screenHeight / 2 - clientHeight / 2, clientWidth, clientHeight, 0);
}

// Функция изменения шрифта в окне
void setFont(HWND window, HFONT h) { SendMessage(window, WM_SETFONT, (WPARAM)h, TRUE); }

// Функция обновления токена
nlohmann::json UpdateToken() {
    const std::string json_data = get_jwt_refresh();

    if (write_to_json(json_data, "rest_data.json") == 0) { exit(-1); }
    else { try { 
        token_jwt = read_data_json("rest_data.json")["access"];

        return 0;
    } 
    catch (nlohmann::json::parse_error& ex) { return 1; } }
}

// Создание диалогового окна с указанием пути до файла и отправка запроса на добавление архива на сервер
void CreateDialogPathTo(HWND hWnd) {
    OPENFILENAME ofn;

    wchar_t szFile[260]{};

    ZeroMemory(&ofn, sizeof(ofn));

    ofn.lStructSize = sizeof(ofn);
    ofn.hwndOwner = NULL;
    ofn.lpstrFile = szFile;
    ofn.lpstrFile[0] = '\0';
    ofn.nMaxFile = sizeof(szFile);
    ofn.lpstrFilter = L"Архив (*.zip)\0*.zip\0*.zip\0";
    ofn.nFilterIndex = 1;
    ofn.lpstrFileTitle = NULL;
    ofn.nMaxFileTitle = 0;
    ofn.lpstrInitialDir = NULL;
    ofn.Flags = OFN_PATHMUSTEXIST | OFN_FILEMUSTEXIST;

    if (GetOpenFileName(&ofn) == TRUE) {
        std::string convToStrPath("\?");

        PathStripPath(ofn.lpstrFile);

        convToString(convToStrPath, ofn.lpstrFile, CP_ACP);

        cpr::Response jwt_resp_r = cpr::Post(
            cpr::Url{ urls::upload_arh_url },
            cpr::Multipart{ {"name", "Krasnoarm_68"}, {"upload_file", cpr::File{convToStrPath}} },
            cpr::Header{ {"Authorization", "Upload_MTS " + token_jwt} },
            cpr::Timeout{ 1000 }
        );

        if (jwt_resp_r.status_code == 200) {
            const std::string jwt_resp_data = jwt_resp_r.text;

            DialogBox(hInst, MAKEINTRESOURCE(IDD_SUCCESSBOX_SEND), hWnd, InfoMessageFile);
        }
        else {
            DialogBox(hInst, MAKEINTRESOURCE(IDD_ERRORBOX), hWnd, InfoMessage);
        }
    }
}

// Получение всех записей с сервера в окно
void get_data_window(HWND hWnd) {
    cpr::Response get_data_r = cpr::Get(
        cpr::Url{ urls::upload_arh_url },
        cpr::Header{ {"Authorization", "Upload_MTS " + token_jwt} },
        cpr::Timeout{ 1000 }
    );

    if (get_data_r.status_code == 200) {
        const std::string get_data_resp = get_data_r.text;
    }
    else {
        DialogBox(hInst, MAKEINTRESOURCE(IDD_ERRORBOX), hWnd, InfoMessage);
    }
}

// Конфертация LPWSTR в string
bool convToString(std::string& s, const LPWSTR pw, UINT codepage) {
    bool res = false;
    char* p = 0;
    int bsz;

    bsz = WideCharToMultiByte(codepage, 0, pw, -1, 0, 0, 0, 0);
    if (bsz > 0) { 
        p = new char[bsz];
        int rc = WideCharToMultiByte(codepage, 0, pw, -1, p, bsz, 0, 0);
        if (rc != 0) {
            p[bsz - 1] = 0;
            s = p;
            res = true;
        }
    }
    delete[] p;

    return res;
}
