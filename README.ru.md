# SmartProxyRules

Генератор AutoProxy/GFWList для расширения [SmartProxy](https://github.com/salarcode/SmartProxy).

## Описание

Этот репозиторий содержит скрипт для автоматической генерации списка прокси-правил в формате AutoProxy/GFWList из настроек SmartProxy и дополнительных доменов.

## Файлы

- **SmartProxyRules.json** - Экспортированные настройки из SmartProxy
- **domains.txt** - Дополнительные домены (один домен на строку)
- **generate_gfwlist.py** - Скрипт генерации GFWList
- **gfwlist.txt** - Сгенерированный список правил (AutoProxy формат)
- **gfwlist.base64.txt** - Base64-кодированная версия списка

## Использование

### 1. Генерация списка правил

```bash
python generate_gfwlist.py
```

Скрипт:
- Извлекает домены из SmartProxyRules.json (только активные правила с прокси)
- Добавляет домены из domains.txt
- Генерирует gfwlist.txt и gfwlist.base64.txt

### 2. Использование в SmartProxy

1. Загрузите `gfwlist.txt` на веб-сервер или GitHub Pages
2. В SmartProxy перейдите в настройки профиля "Умный прокси"
3. Добавьте подписку на правила (Rules Subscription)
4. Укажите URL вашего gfwlist.txt

## Формат AutoProxy/GFWList

```
[AutoProxy 0.2.9]
! Title: SmartProxy Rules
! Last Modified: 2025-10-06
||domain1.com
||domain2.com
```

Где `||domain.com` означает проксирование домена и всех его поддоменов.

## Лицензия

Apache License 2.0
