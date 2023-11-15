# Файловый менеджер
### Функции
1. Открытие
2. Создание новых папок и файлов
3. Навигация по директориям
4. Вырезка
5. Копирование
6. Вставка
7. Переименовывание
8. Удаление
9. Поиск
10. Менеджмент аккаунтов

### Архитектура
* **classes (основные классы)**
  * AccountSettings.py (класс настроек аккаунта)
  * ChangeAccountSettings.py (класс изменения настроек аккаунта у администратора)
  * ChangeLogin.py (класс изменения логина от аккаунта)
  * ChangePassword.py (класс изменения пароля от аккаунта)
  * EditPermission.py (класс управления настройками пользователей)
  * Explorer.py (класс проводника)
  * Find.py (класс поиска)
  * Login.py (класс входа в систему аккаунтов)
  * PathEdit.py (класс ввода пути)
  * Registration.py (класс регистрации аккаунта)
  * Settings.py (класс настроек)
* **icons (иконки и работа с ними)**
  * иконки (в формате .png)
  * resources.qrc (файл для пользования иконками в qt desighnerе)
* **images (аватарки для обычного пользователя и администратора)**
  * admin.jpg (аватарка администратора)
  * user.jpg (аватарка пользователя)
* **ui (frontend)**
  * AccountSettingsUi.py (класс настроек аккаунта)
  * ChangeLoginUi.py (класс изменения логина от аккаунта)
  * ChangePasswordUi.py (класс изменения пароля от аккаунта)
  * EditPermissionUi.py (класс управления настройками пользователей)
  * ExplorerUi.py (класс проводника)
  * FindUi.py (класс поиска)
  * LoginUi.py (класс входа в систему аккаунтов)
  * PathEditUi.py (класс ввода пути)
  * RegistrationUi.py (класс регистрации аккаунта)
  * SettingsUi.py (класс настроек)
* **utils (полезные функции)**
  * checkName.py (проверяет название файла/папки на запрещенные символы и названия)
  * findNewName.py (ищет новое название для файла/папки, преобразует, если существует дубликат)
  * parsePath.py (парсит путь в общий вид)
  * parsePathToDir.py (парсит путь в виде, где только папки на пути)
  * parseToSend2Trash.py (парсит путь в вид для работы с send2trash)
  * randomQuestionLine.py (возвращает рандомную строку с подтверждением действия)
  * returnIndexAndPath.py (возвращает индекс и путь текущего View)
* main.py (основной файл запуска проекта)
* readme.md (файл с описанием проекта)
* requirements.txt (файл с необходимыми пакетами для работы проекта)

### Технологии
* requirements.txt
* Несколько форм
* Изученный виджеты
* Другие виджеты
* Стандартные диалоги
* Картинки
* Файл csv
* Несколько таблиц в БД
* Чтение из БД
* Запись в БД
* Изменение данных в БД
* exe