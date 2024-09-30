from queue import Queue  # Імпортуємо чергу з модуля queue
import random  # Імпортуємо модуль генерації випадкових даних
import time  # Імпортуємо модуль для імітації затримки у часі

class Application:
    """Клас для моделювання заявки"""
    def __init__(self, number):
        self.number = number  # Унікальний номер заявки
        self.operations = random.randint(1, 5)  # Кількість операцій, які потрібно виконати для заявки

class ServiceCenter:
    """Клас для моделювання сервісного центру, що приймає та обробляє заявки"""
    def __init__(self):
        self.queue = Queue()  # Створюємо чергу для заявок

    def generate_request(self, application):
        """Додає нову заявку до черги"""
        self.queue.put(application)  # Додаємо заявку в чергу
        print(f"Заявку №{application.number} додано до черги з {application.operations} операціями")

    def process_request(self):
        """Обробляє заявки з черги"""
        if not self.queue.empty():  # Якщо черга не пуста
            current_application = self.queue.get()  # Отримуємо заявку з черги
            print(f"Обробляємо заявку №{current_application.number}")
            # Імітуємо виконання операцій для поточної заявки
            for operation in range(1, current_application.operations + 1):
                print(f"Виконано операцію {operation}/{current_application.operations} (ctr+C зупинити)")
                time.sleep(1)  # Імітуємо час, необхідний для виконання операції
        else:
            print("Черга порожня, немає заявок для обробки")

# Створюємо екземпляр сервісного центру
service_center = ServiceCenter()

# Основний цикл програми
application_number = 1  # Лічильник для унікальних номерів заявок
try:
    while True:  # Поки користувач не зупинить програму
        service_center.generate_request(Application(application_number))  # Генеруємо нову заявку
        service_center.process_request()  # Обробляємо заявку з черги
        application_number += 1  # Збільшуємо лічильник для наступної заявки
        time.sleep(2)  # Імітуємо затримку між заявками
except KeyboardInterrupt:
    print("Програму зупинено користувачем")
