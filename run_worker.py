import asyncio
from mydefs import SayHello, notify
from datetime import datetime, timedelta
from temporalio import workflow, activity
from temporalio.client import Client
from temporalio.worker import Worker


async def main():
    # Create client connected to server at the given address
    client = await Client.connect("http://localhost:7233")

    # Run the worker
    worker = Worker(client, task_queue="my-task-queue", workflows=[SayHello], activities=[notify])
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
