from collections import deque

names = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}


def person_is_seller(name):
    """Функция проверяет, является ли человек продавцом"""
    return name[-1] == "m"

def search(name):
    """Поиск в ширину"""
    # Создание новой очереди
    search_queue = deque()
    # Все соседи добавляются в очередь поиска
    search_queue += names[name]
    # Этот массив исолььзуется для отслеживания уже проверенных людей
    searched = []
    
    # Пока очередь не пуста
    while search_queue:
        # Из очереди извлекается первый человек
        person = search_queue.popleft()
        # Человек проверяется в том случае, если он еще не был проверен
        if person not in searched:
            # Проверяем, является ли человек продавцом
            if person_is_seller(person):
                # Да, это продавец
                print(person + " is a mango seller!")
                return True
            else:
                # Нет, это не продавец. Все друзья этого человека добавляются в очередь
                search_queue += names[person]
                # Человек добавляется в список проверенных
                searched.append(person)
    # Если выполнение дошло до этой строки,
    # значит никто из друзей не является продавцом
    return False


search("you")