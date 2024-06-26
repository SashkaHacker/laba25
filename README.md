# laba25 (4.2)
# Работу выполнил Матвеев Александр Иванович, Вариант - 10
### Перегрузка операций
Когда в классе предоставляются особым образом именованные методы, тогда Python автоматически вызывает их в случае появления экземпляров данного класса в ассоциированных с ними выражениях.

|                                                                |                                           |                                                                                                   |
| -------------------------------------------------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `__init__`                                                     | Конструктор                               | Создание объекта: `X = Class(args)`                                                               |
| `__del__`                                                      | Деструктор                                | Уничтожение объекта `X`                                                                           |
| `__add__`                                                      | Операция `+`                              | `X + Y`, `X += Y`                                                                                 |
| `__or__`                                                       | Операция `\|`                             | `X \| Y`, `X \|= Y`                                                                               |
| `__repr__`<br>`__str__`                                        | Вывод, <br>преобразования                 | `print(x)`, `repr(x)`, `str(x)`                                                                   |
| `__call__`                                                     | Вызовы<br>функций                         | `X(*args, **kargs)`                                                                               |
| `__getattr__`                                                  | Извлечение<br>атрибута                    | `X.atr`                                                                                           |
| `__setattr__`                                                  | Присваивание<br>атрибута                  | `X.any = value`                                                                                   |
| `__delattr__`                                                  | Удаление<br>атрибута                      | `del X.atr`                                                                                       |
| `__gerattribute__`                                             | Извлечение <br>атрибута                   | `X.atr`                                                                                           |
| `__getitem__`                                                  | Индексирование,<br>нарезание,<br>итерация | `x[key], x[i:j]` циклы `for` и другие<br>итерационные конструкции, если<br>отсутствует `__iter__` |
| `__setitem__`                                                  | Присваивание<br>по индексу и срезу        | `x[key] = value`<br>`x[i:j] = iterable`                                                           |
| `__delitem__`                                                  | Удаление по индексу <br>и срезу           | `del x[key], del x[j:j]`                                                                          |
| `__len__`                                                      | Длина                                     | `len(x)`, проверки истинности, если нет <br>`__bool__`                                            |
| `__bool__`                                                     | Булевские проверки                        | `bool(x)`                                                                                         |
| `__lt__`, `__gt__`<br>`__le__`, `__ge__`<br>`__eq__`, `__ne__` | Сравнения                                 | `x < y`, `x > y` и т. д.                                                                          |
| `__radd__`                                                     | Правосторонние<br>операции                | `Other + x`                                                                                       |
| `__iadd__`                                                     | Дополненные на <br>месте операции         | `x += y`                                                                                          |
| `__iter__`<br>`__next__`                                       | Итерационные<br>контексты                 | `i = iter(x), next(i)`                                                                            |
| `__contains__`                                                 | Проверка членства                         | `item in X` (любой итерируемый объект)                                                            |
| `__index__`                                                    | Целочистленное <br>значение               | `hex(x), bin(x), oct(x), list[x], list[0:x]`                                                      |
| `__enter__`<br>`__exit__`                                      | Диспетчер контекста                       | `with obj as var`                                                                                 |
| `__get__`, `__set__`<br>`__delete__`                           | Атрибуты дескриптора                      | `x.attr, x.attr = value`, `del x.attr`                                                            |
| `__new__`                                                      | Создание                                  | Создание объекта перед `__init__`                                                                 |

>[!quote] `__getattr__`
>Перехватывает ссылки на атрибуты. Вызывается с именем атрибута в виде строки каждый раз, когда экземпляр вызывается с несуществующим атрибутом.
>```python
>class Empty:
>	def __getattr__(self, attrname):
>		if attrname == 'age':
>			return 40
>		else:
>			raise AttributeError(attrname)
>x = Empty()
>x.age # -> 40
>x.name # -> такого атрибута не существует
>```

>[!quote] `__setattr__`
>Подобно `__getattr__`, данный метод перехватывает все присваивания значений атрибутам. Если данный метод определен или унаследован, значит вырежение `self.atr = значение -> self.__setattr__('атрибут', значение)`
>Тем не менее, использование метода может привести к бесконечному запуску рекурсии. Т.к. присваивание значений атрибутам каждый раз будут идти через этот метод. В данном случае необходимо реализовать присваивания значений атрибутам экземпляра в виде присваиваний ключам словаря атрибутов. `self.__dict__['name'] = x`, но НИ В КОЕМ СЛУЧАЕ НЕ `self.name = x`
>```python
>class Accesscontrol:
>	def __setattr__(self, attr, value):
>		if attr == 'age':
>			self.__dict__[attr] = value + 10
>		else:
>			raise AttributeError()
>```

>[!quote] `__delattr__`
>Используется для добавления дополнительной логики при удалении атрибутов в классе через конструкцию `del class.name`. Так же как и в методе `__setattr__` необходимо соблюдать осторожность и работать с атрибутами через `del self.__dict__[attr]`. Если метод не определен, то все будет работать и так.

>[!quote] `__call__`
>Вызывается каждый раз, когда мы пишем экземпляр с аргументом (как вызов функции). Можем передавать все что угодно, как обычной функции. Используется часто, когда нам нужно реализовать функцию с фичами классов.
>```python
>class Multiplier:
> 	def __init__(self, factor):
> 		self.factor = factor 
> 	def __call__(self, value):
> 		return value * self.factor 
> 		
> double = Multiplier(2) 
> print(double(5)) # Выведет 10
>```

>[!quote] `__len__ and __bool__`
>Данные методы необходимы для булевой проверки экземпляра. Вот как это работает для `__bool__`. А для `__len__` оно будет давать True, если длина объекта != 0
>```python
>class Truth:
>	def __bool__(self):
>		return True
>		
>x = Truth()
>bool(x) # -> True		
>```

>[!quote] `__del__`
>Удаление экземпляров! Вот так легко и просто определяем этот класс и наслаждаемся какой-то логикой, которая работает, когда ссылка на объект утрачивается.
