from database import (
    init_db,
    add_entry,
    get_all_entries,
    get_entry,
    update_entry,
    delete_entry
)


def main():
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ БАЗЫ ДАННЫХ 'ЛИЧНЫЙ ДНЕВНИК'")
    print("=" * 60)
    
    # 1. Инициализируем базу данных
    print("\n1. Инициализация базы данных...")
    init_db()
    print("   ✓ База данных инициализирована")
    
    # 2. Добавляем 3 записи с разными заголовками и текстом
    print("\n2. Добавление 3 записей...")
    add_entry("Первая запись", "Это содержание первой записи в дневнике")
    add_entry("Вторая запись", "Содержание второй записи, которое мы будем обновлять")
    add_entry("Третья запись", "Текст третьей записи, которую мы удалим")
    print("   ✓ Добавлено 3 записи")
    
    # 3. Выводим все записи в формате: id. Заголовок (дата)
    print("\n3. Все записи в базе данных:")
    print("-" * 60)
    entries = get_all_entries()
    for entry in entries:
        print(f"{entry['id']}. {entry['title']} ({entry['created_at']})")
    print("-" * 60)
    
    # 4. Выводим одну запись с id = 2
    print("\n4. Запись с id = 2:")
    print("-" * 60)
    entry = get_entry(2)
    if entry:
        print(f"Заголовок: {entry['title']}")
        print(f"Содержание: {entry['content']}")
        print(f"Дата: {entry['created_at']}")
    print("-" * 60)
    
    # 5. Обновляем запись с id = 2
    print("\n5. Обновление записи с id = 2...")
    update_entry(2, "Обновлённая вторая запись", "Это новое содержание второй записи после обновления")
    print("   ✓ Запись обновлена")
    
    # 6. Выводим обновлённую запись для проверки
    print("\n6. Обновлённая запись с id = 2:")
    print("-" * 60)
    entry = get_entry(2)
    if entry:
        print(f"Заголовок: {entry['title']}")
        print(f"Содержание: {entry['content']}")
        print(f"Дата: {entry['created_at']}")
    print("-" * 60)
    
    # 7. Удаляем запись с id = 3
    print("\n7. Удаление записи с id = 3...")
    delete_entry(3)
    print("   ✓ Запись удалена")
    
    # 8. Выводим оставшиеся записи
    print("\n8. Оставшиеся записи:")
    print("-" * 60)
    entries = get_all_entries()
    for entry in entries:
        print(f"{entry['id']}. {entry['title']} ({entry['created_at']})")
    print("-" * 60)
    
    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ ЗАВЕРШЕНО УСПЕШНО!")
    print("=" * 60)


if __name__ == "__main__":
    main()