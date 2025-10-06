# SmartProxyRules

[![Generate GFWList](https://github.com/YOUR_USERNAME/SmartProxyRules/actions/workflows/generate-gfwlist.yml/badge.svg)](https://github.com/YOUR_USERNAME/SmartProxyRules/actions/workflows/generate-gfwlist.yml)

Генератор AutoProxy/GFWList для расширения [SmartProxy](https://github.com/salarcode/SmartProxy).

## Описание

Этот репозиторий содержит скрипт для автоматической генерации списка прокси-правил в формате AutoProxy/GFWList из настроек SmartProxy и дополнительных доменов. GitHub Actions автоматически обновляет список при изменении правил.

## Файлы

- **SmartProxyRules.json** - Экспортированные настройки из расширения SmartProxy
- **domains.txt** - Дополнительные домены (один домен на строку)
- **generate_gfwlist.py** - Python скрипт для генерации GFWList
- **gfwlist.txt** - Сгенерированный список правил (AutoProxy формат) ⭐
- **gfwlist.base64.txt** - Base64-кодированная версия списка
- **.github/workflows/generate-gfwlist.yml** - GitHub Actions workflow для автоматической генерации

## Использование

### 1. Генерация списка правил

#### Автоматическая генерация (GitHub Actions)

При каждом изменении `SmartProxyRules.json` или `domains.txt` GitHub Actions автоматически генерирует новые файлы `gfwlist.txt` и `gfwlist.base64.txt`.

Также можно запустить вручную:
1. Перейдите во вкладку Actions в репозитории
2. Выберите "Generate GFWList"
3. Нажмите "Run workflow"

#### Локальная генерация

```bash
python generate_gfwlist.py
```

Скрипт:
- Извлекает домены из SmartProxyRules.json (только активные правила с прокси)
- Добавляет домены из domains.txt
- Генерирует gfwlist.txt и gfwlist.base64.txt

### 2. Использование в SmartProxy

Используйте прямую ссылку на gfwlist.txt из GitHub:

```
https://raw.githubusercontent.com/ВАШ_ЮЗЕРНЕЙМ/SmartProxyRules/main/gfwlist.txt
```

Или для base64 версии:

```
https://raw.githubusercontent.com/ВАШ_ЮЗЕРНЕЙМ/SmartProxyRules/main/gfwlist.base64.txt
```

В SmartProxy:
1. Перейдите в настройки профиля "Умный прокси"
2. Добавьте подписку на правила (Rules Subscription)
3. Укажите URL вашего файла

## Формат AutoProxy/GFWList

```
[AutoProxy 0.2.9]
! Title: SmartProxy Rules
! Last Modified: 2025-10-06
||domain1.com
||domain2.com
```

Где `||domain.com` означает проксирование домена и всех его поддоменов.

## Как это работает

1. **Экспортируйте настройки SmartProxy** → Сохраните как `SmartProxyRules.json`
2. **Добавьте свои домены** → Отредактируйте `domains.txt` (опционально)
3. **Отправьте в GitHub** → GitHub Actions автоматически сгенерирует `gfwlist.txt`
4. **Подпишитесь в SmartProxy** → Используйте raw URL из GitHub

## Лицензия

Apache License 2.0
