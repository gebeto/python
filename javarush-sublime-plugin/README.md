# JavaRush - SublimeText Plugin
 Плагин для решения задач на JavaRush! Аналог плгина для InteliJIDEA, только для Sublime Text:)
 
# Установка:
 1. Запускаем Sublime Text, переходим в Preferences-Package Control и выбираем **Add Repository**.
 2. Вводим **https://github.com/bboyheadman/JavaRush** и жмем ЕНТЕР.
 3. Опять заходим в Package Control и выбираем Install Package.
 4. Вводим в поиске **JavaRush**.
 5. Устанавливаем.

# Настройка:
**Можно зайти [СЮДА](http://javarush.ru/api/rest/user/server/statistics.json?v=2) и скопировать значение sessionID, дале все от шага №5, или все делать по инструкции**
 1. Переходим на [страничку с задачками](http://javarush.ru/levels/tasks.html) **(Вы должны войти в свой аккаунт)**
 2. Пишем в адресной строке **javascript:** и потом вставляем этот кусок кода **alert(window.controller.context.sessionId)**
 3. Должно получится так **javascript:alert(window.controller.context.sessionId)**
 4. Жмем ЕНТЕР, копируем всю строку с появившегося окна
 5. В SublimeText переходим в **/ Preferences / Package Settings / JavaRushPlugin / Settings-User**
 6. Там пишем {"sessionID":"**_СТРОКА С ШАГА №4_**"}
 7. Сохраните настройку.
 
 > **Не копируйте строку целиком(javascript:alert(window.controller.context.sessionId))
 > При вставке в адресную строку, браузер сотрет префикс "javascript:" и ничего не сработает**

## Что надо сделать:
 - [x] Получение задачи
 - [x] Отправка задачи на проверку

## Скриншоты:
 ![скриншот1](https://raw.githubusercontent.com/bboyheadman/images/master/javarush/JavaRushGet.jpg)
 ![скриншот2](https://raw.githubusercontent.com/bboyheadman/images/master/javarush/JavaRushGetTask.jpg)
 ![скриншот3](https://raw.githubusercontent.com/bboyheadman/images/master/javarush/JavaRushFai.jpg)
 ![скриншот4](https://raw.githubusercontent.com/bboyheadman/images/master/javarush/JavaRushSuc.jpg)

## Я в соц сетях: 
 - [ВКонтакте](http://vk.com/gebeto)
 - [Facebook](https://facebook.com/bboyheadman)
 - [Instagram](https://www.instagram.com/slavik.nychkalo)
 - [YouTube](https://www.youtube.com/channel/UCF9KTUwwy1n193oFyQylBiQ)
