from fastapi import FastAPI
import asyncio
import re

app = FastAPI()


async def le():
    message = None
    i = 0
    while True:
        with open("sample.txt") as f:
            content = f.readlines()
        flag = re.sub(r"\W+", "", content[0]) if content else None
        print(i, flag)
        if flag == "done":
            message = {"message": "sucesso"}
            break
        i += 1
        await asyncio.sleep(2)
    return message


async def de_boa(recebe=False):
    while True:
        if not recebe:
            print("So de boa")
        else:
            break
        await asyncio.sleep(2)
    print("Ate que enfim")
    return None


@app.get("/")
def ret():
    return {"message": "nada"}


@app.get("/volta")
async def espera():
    _le = asyncio.create_task(le())
    _de_boa = asyncio.create_task(de_boa())

    await _le
    await _de_boa
    return _le
