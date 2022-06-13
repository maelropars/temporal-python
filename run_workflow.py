import asyncio
from mydefs import SayHello, notify
from datetime import datetime, timedelta
from temporalio import workflow, activity
from temporalio.client import Client
from temporalio.worker import Worker

async def main():
    # Create client connected to server at the given address
    client = await Client.connect("http://localhost:7233")

    # Execute a workflow
    mylist = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6','user7', 'user8', 'user9']
    await client.execute_workflow(SayHello.run, mylist, id="my-workflow-id", task_queue="my-task-queue")

    print("workflow executed")

if __name__ == "__main__":
    asyncio.run(main())
