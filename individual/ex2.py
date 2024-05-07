#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 10
# Один тестовый вопрос представляет собой словарь Task со следующими ключами: вопрос,
# пять вариантов ответа, номер правильного ответа, начисляемые баллы за правильный ответ.
# Для моделирования набора тестовых вопросов реализовать класс TestContent, содержащий
# список тестовых вопросов. Реализовать методы добавления и удаления тестовых вопросов,
# а также метод доступа к тестовому заданию по его порядковому номеру в списке. В списке не
# должно быть повторяющихся вопросов. Реализовать операцию слияния двух тестовых
# наборов, операцию пересечения и вычисления разности. Дополнительно реализовать
# операцию генерации конкретного объекта Test объемом не более вопросов из объекта
# типа TestContent.


class TestContent:
    MAX_SIZE = 100

    def __init__(self, size=MAX_SIZE):
        if size > TestContent.MAX_SIZE:
            raise ValueError(
                f"Размер не может превышать {TestContent.MAX_SIZE}"
            )
        self.__size = size
        self.__count = 0
        self.__tasks = []

    @property
    def size(self):
        return self.__size

    @property
    def count(self):
        return self.__count

    def add_task(self, task):
        if self.__count < self.__size:
            if task not in self.__tasks:
                self.__tasks.append(task)
                self.__count += 1
            else:
                print("Такой вопрос уже есть в тесте.")
        else:
            print("Достигнут лимит вопросов в тесте.")

    def remove_task(self, task):
        if task in self.__tasks:
            self.__tasks.remove(task)
            self.__count -= 1

    def __repr__(self):
        return f"{self.__tasks}"

    def __getitem__(self, key):
        if isinstance(key, int):
            if 0 <= key < self.__count:
                return self.__tasks[key]
            else:
                raise IndexError("Индекс вне диапазона")
        elif isinstance(key, slice):
            return self.__tasks[key]
        else:
            raise TypeError("Индекс должен быть целым числом или срезом")

    def __add__(self, other):
        if not isinstance(other, TestContent):
            raise ValueError("Объект должен быть экземпляром TestContent")
        result = TestContent(
            min(self.__size + other.size(), TestContent.MAX_SIZE)
        )
        for task in self.__tasks + other.__tasks:
            result.add_task(task)
        return result

    def __and__(self, other):
        if not isinstance(other, TestContent):
            raise ValueError("Объект должен быть экземпляром TestContent")

        result = TestContent(min(self.__size, other.size()))

        self_tasks_set = set(task["вопрос"] for task in self.__tasks)
        other_tasks_set = set(task["вопрос"] for task in other.__tasks)
        common_questions = self_tasks_set & other_tasks_set

        for task in self.__tasks:
            if task["вопрос"] in common_questions:
                result.add_task(task)
        return result

    def __sub__(self, other):
        if not isinstance(other, TestContent):
            raise ValueError("Объект должен быть экземпляром TestContent")

        result = TestContent(self.__size)

        self_tasks_set = set(task["вопрос"] for task in self.__tasks)
        other_tasks_set = set(task["вопрос"] for task in other.__tasks)
        unique_questions = self_tasks_set - other_tasks_set

        for task in self.__tasks:
            if task["вопрос"] in unique_questions:
                result.add_task(task)
        return result

    def generate_test(self, num_questions):
        if num_questions > self.__count:
            raise ValueError("Запрошено больше вопросов, чем доступно")
        import random

        selected_tasks = random.sample(self.__tasks, num_questions)
        new_test = TestContent(num_questions)
        for task in selected_tasks:
            new_test.add_task(task)
        return new_test


if __name__ == "__main__":
    test1 = TestContent(10)
    test2 = TestContent(10)

    test1.add_task(
        {
            "вопрос": "Вопрос 1",
            "ответы": ["a", "b", "c", "d", "e"],
            "правильный": 1,
            "баллы": 2,
        }
    )

    test1.add_task(
        {
            "вопрос": "Вопрос 2",
            "ответы": ["a", "b", "c", "d", "e"],
            "правильный": 2,
            "баллы": 2,
        }
    )

    test2.add_task(
        {
            "вопрос": "Вопрос 2",
            "ответы": ["a", "b", "c", "d", "e"],
            "правильный": 2,
            "баллы": 2,
        }
    )

    print(test1[:2])
    merged_test = test1 + test2
    print(merged_test.count)
    intersection_test = test1 & test2
    print(intersection_test.count)
    difference_test = test1 - test2
    print(difference_test.count)
    generated_test = test1.generate_test(1)
    print(generated_test.count)
