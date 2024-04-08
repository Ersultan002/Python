def count_letter_k(text):
    count = 0
    for char in text:
        if char.lower() == 'к':
            count += 1
    return count

# Пример текста для анализа
text = "Сегодня был прекрасный день. Солнце светило ярко, и птицы щебетали на ветках деревьев. Я прогулялся по парку и наслаждался природой. Вдруг я увидел старого друга, которого давно не видел. Мы поговорили о старых временах и посмеялись над нашими приключениями. Это было замечательно."

# Определение количества букв "к"
count_k = count_letter_k(text)
print("Количество букв 'к' в тексте:", count_k)