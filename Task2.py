from collections import deque  # Імпортуємо deque з модуля collections

def is_palindrome(text):
    # Приводимо текст до нижнього регістру і видаляємо пробіли
    normalized_text = ''.join(char.lower() for char in text if char.isalnum())  
    # Створюємо двосторонню чергу для зберігання символів
    two_sided_deque = deque()

    # Додаємо кожен символ нормалізованого тексту до двосторонньої черги
    for char in normalized_text:
        two_sided_deque.append(char)

    # Перевіряємо символи з обох кінців черги
    while len(two_sided_deque) > 1:
        if two_sided_deque.popleft() != two_sided_deque.pop():  # Порівнюємо символи з обох кінців
            return False  # Якщо символи не співпадають, це не паліндром
    
    return True  # Якщо всі символи співпадають, це паліндром

# Тестуємо функцію
text = "ABc C b A"
print(is_palindrome(text))  # Повинно вивести True, оскільки це паліндром
