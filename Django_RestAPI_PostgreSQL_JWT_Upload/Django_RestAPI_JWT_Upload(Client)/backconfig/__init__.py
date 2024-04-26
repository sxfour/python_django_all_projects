# -*- coding: utf-8 -*-

from packages import main_imports


# Back основная форма.
class SendMessagePage(main_imports.QWidget, object):

    def __init__(self):
        super(SendMessagePage, self).__init__()
        self.ui = main_imports.UI_SendMessagePage()
        self.ui.setupUi(self)

        self.path_to_pdf = list()
        self.url_refresh = 'http:// set refresh url'
        self.url_send = 'http:// set url to download files'

        # Signals
        self.ui.pushButtonSend.clicked.connect(self.sendMessage)
        self.ui.toolButton.clicked.connect(self.setPathFile)
        self.ui.checkBox.clicked.connect(self.createRememberMe)

        # Проверка автозаполнения токена
        self.checkAutoLogin()

    def __del__(self):
        pass

    def sendMessage(self):
        name = self.checkCorrectLogin(self.ui.textEditName.toPlainText())
        jwt_token = self.ui.lineEditToken.text()

        if name[1]:
            date_now = main_imports.datetime.now().strftime("_%Y-%m-%d(%H_%M_%S)")
            try:
                pdf_to_send = {'upload_file': open(f'{self.path_to_pdf[0]}', 'rb')}
                refresh = main_imports.post(self.url_refresh, data={'refresh': '{0}'.format(jwt_token)})
                refresh_json = refresh.json()['access']
                data = {'name': '{0}_{1}'.format(name[0], date_now)}
                auth_headers = {'Authorization': 'Upload_MTS {0}'.format(refresh_json)}

                send_post_data = main_imports.post(self.url_send, data=data, files=pdf_to_send, headers=auth_headers)
                code_response = str(send_post_data.status_code)

                if code_response == '200':
                    main_imports.successWindow('Архив успешно отправлен\nStatus code: {0}'.format(code_response))
                else:
                    # Запись в лог
                    main_imports.error('[!] [EXCEPTION] Error '
                                       'sendMessage, more info : {0}'.format(send_post_data.json()), exc_info=True)

                    # Окно ошибки
                    main_imports.findErrorWindow(message='{0}'.format(code_response),
                                                 text='JSON: {0}'.format(send_post_data.json()))

            except (IndexError, main_imports.exceptions.JSONDecodeError) as ex:
                # Запись в лог
                main_imports.error('[!] [EXCEPTION] Error sendMessage, more info : {0}'.format(ex), exc_info=True)

                # Окно ошибки
                main_imports.findErrorWindow(message=ex, text='Error: {0} Сервер отверг запрос'
                                                              ' на добавление'.format(self.path_to_pdf))
            except Exception as ex:
                # Запись в лог
                main_imports.error('[!] [EXCEPTION] Error sendMessage, more info : {0}'.format(ex), exc_info=True)

                # Окно ошибки
                main_imports.findErrorWindow(message=ex, text='Сервер отверг запрос на добавление')

            self.path_to_pdf.clear()
            self.ui.toolButton.setChecked(False)
        else:
            # Окно ошибки
            main_imports.findErrorWindow(message=name[0], text='Ошибка фильтрации символов')

    # Выбор папки с документом
    def setPathFile(self):
        path_to_pdf = main_imports.pathDialogWindow('Выберите архив')[0]

        if path_to_pdf == '':
            self.ui.toolButton.setChecked(False)
            pass
        else:
            self.path_to_pdf.append(path_to_pdf)

            main_imports.successWindow('Путь: {0}...\nУспешно добавлен.'.format(path_to_pdf[:40]))

    # Проверка и автозаполнение поля при запуске
    def checkAutoLogin(self):
        try:
            with open('data_json/auto_login.json', 'r', encoding='utf8') as json_file:
                self.ui.lineEditToken.setText(str(main_imports.load(json_file)['data_jwt']))
                self.ui.checkBox.setChecked(True)
        except FileNotFoundError as ex:
            # Запись в лог
            main_imports.error('[!] [EXCEPTION] Error checkAutoLogin, more info : {0}'.format(ex), exc_info=True)
        except main_imports.decoder.JSONDecodeError as ex:
            main_imports.errorWindow(ex, 'Чтение с ошибками')

    # Сохранение токена в папку
    def createRememberMe(self):
        jwt_token_remember = self.ui.lineEditToken.text()

        # Получаем данные с запомнить и сохраняем в json
        if self.ui.checkBox.isChecked():
            dataToSaveJson = {'data_jwt': str(jwt_token_remember), }
            with open('data_json/auto_login.json', 'w') as file:
                main_imports.dump(dataToSaveJson, file)
        elif not self.ui.checkBox.isChecked():
            try:
                main_imports.remove('data_json/auto_login.json')
            except FileNotFoundError as ex:
                # Запись в лог
                main_imports.error('[!] [EXCEPTION] Error file path, more info : {0}'.format(ex), exc_info=True)

    def checkCorrectLogin(self, username):
        try:
            username_local = str(username)

            bad_request = list()
            good_string = ''
            check_phrase = username_local.strip()

            if len(check_phrase) < 10:
                for data in check_phrase:
                    code = ord(data)
                    if 1039 < code or (code == 1025 or code == 1105 or code == 32
                                       or code == 34 or code == 45 or code == 1103):
                        good_string += data
                    else:
                        bad_request.append(data)

                if good_string == '' or good_string == ' ' \
                        or good_string == '  ' or good_string == '   ':
                    main_imports.info('\n[!] [SEARCH] Request ignored : [{0}]'.format(bad_request))

                    bad_request.clear()
                    self.ui.textEditName.clear()

                    return [username, False]

                if len(bad_request) > 0:
                    main_imports.info('\n[!] [SEARCH] Filtered message : {0}'.format(bad_request))

                    self.ui.textEditName.clear()

                    return [username, False]

                # Фильтрация ошибочных запросов с содержанием пробелов или недопустимых символов
                elif len(good_string) != 0 and len(bad_request) == 0 and good_string != ' ' and good_string != '  ' \
                        and good_string != '   ' and good_string != '    ' and good_string != '     ' \
                        and good_string != '      ' and good_string != '      ' and good_string != '       ':

                    return [username, True]

            else:
                return [username, False]

        except Exception as ex:
            # Запись в лог
            main_imports.error('[!] [EXCEPTION] Error login page, more info : {0}'.format(ex), exc_info=True)
