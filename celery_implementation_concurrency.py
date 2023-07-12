from fastapi import FastAPI
from celery import Celery
import time
import asyncio
import uvicorn

app = FastAPI()
celery_app = Celery(
    "myapp", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0"
)


@celery_app.task
def synchronous_blocking_operation(identifier: str, blocking_time: int):
    time.sleep(blocking_time)
    return f"Finished: {identifier} - time: {blocking_time}"


@app.get("/concurrency-test/{_id}/{time_block}")
async def example_endpoint(_id: str, time_block: int):
    result = synchronous_blocking_operation.delay(_id, time_block)
    while not result.ready():
        await asyncio.sleep(0.1)
    return result.result


if __name__ == "__main__":
    uvicorn.run("single_file_celery_test:app", host="0.0.0.0", reload=True, port=8000)


# $ python -m single_file_celery_test
# $ python -m celery -A single_file_celery_test.celery_app worker --loglevel=info
# $ curl -X GET http://localhost:8000/concurrency-test/heavy_task/30
# $ curl -X GET http://localhost:8000/concurrency-test/light_task/5
