import itertools
import os
import time


class factory(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(factory, cls).__call__(*args, **kwargs)
            return cls._instances[cls]
        print('Ошибка: нельзя создать ещё одного робота!')
        return None


class Robot(metaclass=factory):
    serial_number: str = 'АА001221-56'
    name: str = None
    place: str = None

    def build_house(self) -> str:
        return None

    def build_barn(self) -> str:
        return None

    def add_floor(self) -> str:
        return None

    def demolish_floor(self) -> str:
        return None

    def __str__(self) -> str:
        funs = []
        for fun in [self.build_house, self.build_barn,
                    self.add_floor, self.demolish_floor]:
            funs.append(fun())
        funs = list(filter(None, funs))
        funs = 'Отсутствуют' if len(funs) == 0 else ', '.join(funs).capitalize()

        return f'Серийный номер: {self.serial_number}.\n' + \
               f'Имя: {self.name}.\n' + \
               f'Место пребывания: {self.place}.\n' + \
               f'Функции: {funs}.'


class RobotV(Robot):
    def __init__(self):
        self.name = 'В'
        self.place = 'Робозавод'


class RobotDecorator(Robot):
    robot: Robot

    def __init__(self, robot):
        self.robot = robot

    def build_house(self) -> str:
        return self.robot.build_house()

    def build_barn(self) -> str:
        return self.robot.build_barn()

    def add_floor(self) -> str:
        return self.robot.add_floor()

    def demolish_floor(self) -> str:
        return self.robot.demolish_floor()


class RobotVita(RobotDecorator):
    def __init__(self, robot):
        super().__init__(robot)
        self.name = 'Вита'
        self.place = 'Робошкола'

    def build_house(self) -> str:
        return 'постройка домов'

    def build_barn(self) -> str:
        return 'постройка сараев'


class RobotVitaliy(RobotDecorator):
    def __init__(self, robot):
        super().__init__(robot)
        self.name = 'Виталий'
        self.place = 'Предприятие "ООО Кошмарик"'

    def add_floor(self) -> str:
        return 'добавление этажей к постройкам'

    def demolish_floor(self) -> str:
        return 'снос верхних этажей у построек'


def print_loading(text: str):
    os.system('cls')
    print(text, end='')
    it = itertools.cycle(['.'] * 3 + ['\b \b'] * 3)
    for i in range(30):
        time.sleep(.3)
        print(next(it), end='', flush=True)
    os.system('cls')


def print_info(header: str, robot: Robot):
    os.system('cls')
    print(header.capitalize() + '!\n')
    print(str(robot) + '\n')
    input('Нажмите enter для продолжения...')
    os.system('cls')


if __name__ == '__main__':
    print_loading('Создание робота')
    robot = RobotV()
    print_info(header='робот создан', robot=robot)

    print_loading('Первичное обучение')
    robot = RobotVita(robot)
    print_info(header='робот прошел первичное обучение', robot=robot)

    print_loading('Практика на предприятии')
    robot = RobotVitaliy(robot)
    print_info(header='робот окончил практику на предприятии', robot=robot)