import asyncio
from enum import Enum
from pydantic import BaseModel
from typing import Optional


class Options(Enum):
    cat = "cat"
    dog = "dog"


class ContainerObj(BaseModel):
    choice: Optional[Options] = None


option_obj = ContainerObj()


async def get_input():
    while True:
        user_input = input("Enter the message: ").strip().lower()
        try:
            option_obj.choice = Options(user_input)
        except ValueError:
            print(f"{user_input} is not a valid option. Enter it again")
            continue
        await asyncio.sleep(1)


async def called():
    while True:
        # print(option_obj.choice)
        if option_obj.choice == Options.dog:
            print("Cachorrinho")
        elif option_obj.choice == Options.cat:
            print("ihhhhhh rolou gato")
        else:
            print("Ta estranho papa")
        await asyncio.sleep(1)


async def main():
    while True:
        task1 = asyncio.create_task(get_input())
        task2 = asyncio.create_task(called())

        await task1
        await task2


asyncio.run(main())
