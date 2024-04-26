# -*- coding: utf-8 -*-

from packages import main_imports

from backconfig import SendMessagePage

if __name__ == '__main__':
    # Логирование всех искл в файл Windows 10
    # main_imports.basicConfig(level=main_imports.INFO,cls
    #                          filename='logs/stack.log',
    #                          filemode='w',
    #                          format='%(asctime)s %(levelname)s %(message)s',
    #                          encoding="utf-8")

    # Логирование всех искл в файл Windows 7
    logger = main_imports.getLogger()
    logger.setLevel(main_imports.INFO)
    handler = main_imports.FileHandler('logs/stack.log', 'w', 'utf-8')
    logger.addHandler(handler)

    # Запуск UI.
    MainPage = main_imports.QApplication(main_imports.sys.argv)
    Window = SendMessagePage()

    Window.show()

    main_imports.sys.exit(MainPage.exec_())
