from database import (
    init_db,
    add_entry,
    get_entries_count,
    search_entries,
    get_last_week_entries,
    delete_all_entries
)


def main():
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ДОПОЛНИТЕЛЬНЫХ ФУНКЦИЙ")
    print("=" * 60)
    
    # Инициализация БД
    init_db()
    
    # Очищаем базу перед тестом
    print("\n1. Очистка базы данных...")
    delete_all_entries()
    print("   ✓ База очищена")
    
    # Добавляем тестовые записи
    print("\n2. Добавление тестовых записей...")
    add_entry("Запись о работе", "Сегодня был продуктивный день на работе")
    add_entry("Запись о путешествии", "Планирую поездку в горы")
    add_entry("Рабочие заметки", "Важные рабочие моменты")
    add_entry("Личные мысли", "Размышления о жизни")
    print("   ✓ Добавлено 4 записи")
    
    # Тестируем get_entries_count
    print("\n3. Тестирование get_entries_count():")
    count = get_entries_count()
    print(f"   Количество записей: {count}")
    
    # Тестируем search_entries
    print("\n4. Тестирование search_entries('работа'):")
    results = search_entries('работа')
    print(f"   Найдено записей: {len(results)}")
    for entry in results:
        print(f"   - {entry['title']}")
    
    # Тестируем get_last_week_entries
    print("\n5. Тестирование get_last_week_entries():")
    results = get_last_week_entries()
    print(f"   Записей за последнюю неделю: {len(results)}")
    for entry in results:
        print(f"   - {entry['title']} ({entry['created_at']})")
    
    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ ДОПОЛНИТЕЛЬНЫХ ФУНКЦИЙ ЗАВЕРШЕНО!")
    print("=" * 60)


if __name__ == "__main__":
    main()