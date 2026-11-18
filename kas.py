def reverse_words(text: str) -> str:
    words = text.split()
    return " ".join(words[::-1])


if __name__ == "__main__":
    assert reverse_words("я люблю python") == "python люблю я"
    assert reverse_words("hello    world  ") == "world hello"
    assert reverse_words("один") == "один"

    user_input = input("Введите строку: ")
    print(reverse_words(user_input))
