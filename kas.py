def reverse_words(text: str) -> str:
    """Переворачивает порядок слов в строке."""
    words = text.split()
    return " ".join(words[::-1])


if __name__ == "__main__":
    # Проверка на тестовых данных из условия
    assert reverse_words("я люблю python") == "python люблю я"
    assert reverse_words("hello    world  ") == "world hello"
    assert reverse_words("один") == "один"

    # Интерактивный ввод пользователя
    user_input = input("Введите строку: ")
    print(reverse_words(user_input))