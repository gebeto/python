# Хауди Хо Sublime Text

Плагин для Sublime Text для создания постов в vk.com/howdyho_net не выходя с редактора

## Установка

1. Откройте панель команд ctrl+shift+p
2. Введте **Howdy** и выберите **Создать пост**
3. В открывшемся списке выберите **Получить токен авторизации**, вас перенаправит на сайт авторизации ВК
4. Подтвердите доступ
5. С адресной строки скопируйте ваш **access_token** (Не обращайте внимание на предупреждение ***LOL***)
6. Откройте настройки плагина и добавте там текст ниже, вместо **YOUR_ACCESS_TOKEN** вставте ваш токен
7. Сохраните настройки и закройте


```json
{
    "access_token": "YOUR_ACCESS_TOKEN"
}
```