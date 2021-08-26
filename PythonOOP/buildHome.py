# Строим дом

class House:
    """класс дома"""  # Первая строка считается описанием класса/метода. Стандарт PEP8
    house_size: int
    house_weight: int
    
    def window(size:int, weight:int):
        """окно"""
        return size, weight


def checkAttr(className: object, attrName: str, desc: str = "") -> str:
    """проверяет значение атрибута, если имеется, то выводит о нем информацию, если нет, то выводит информацию о том, что его нет

    - className - объект класса, в котором делаем проверку (required parameter type: object)
    - attrName - имя атрибута (required parameter type: string)
    - desc - описание атрибута (parameter type: string)"""

    if hasattr(className, attrName):
        if desc != "": 
            return "Атрибут {} {}: {}".format(attrName, desc, getattr(className, attrName))
        else: 
            return "Атрибут {} имеет значение: {}".format(attrName, getattr(className, attrName))
    else: 
        info = "Атрибут {} не найден".format(attrName) 
        return info
    

print("Описание класса:", House.__doc__)  
print("Имя класса:", House.__name__)  
print("Полный набор данных класса:", dir(House)) 

h = House()
h.house_size = 100  # Размер дома: атрибут или свойство класса
h.house_weight = 15  # Ширина дома: атрибут или свойство класса
print("Список локальных переменных:", h.__dict__) 

# Возвращаем значение атрибута
print(checkAttr(h, "house_size", "размер дома"))
print(checkAttr(h, "house_weight", "ширина дома"))
print(checkAttr(h, "house_height", "высота дома"))

# Добавляем атрибут и значение
setattr(h, "house_height", 10)
print(checkAttr(h, "house_height", "высота дома"))

# Удаляем атрибут высота дома
delattr(h, "house_height")
print(checkAttr(h, "house_height", "высота дома"))

# Принадлежность экземпляра к тому или иному классу
print(isinstance(h, House))