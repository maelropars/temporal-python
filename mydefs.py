import asyncio
from datetime import datetime, timedelta
from temporalio import workflow, activity
from temporalio.client import Client
from temporalio.worker import Worker

@activity.defn
async def notify(name: str):
    print('in activity')
    print(name)

@workflow.defn
class SayHello:
    @workflow.run
    async def run(self, names: [str]):
        for i in names:
            await workflow.execute_activity(
                notify, i, schedule_to_close_timeout=timedelta(seconds=5)
            )
            await asyncio.sleep(2)
