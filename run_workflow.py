import asyncio
from mydefs import SayHello, notify
from datetime import datetime, timedelta
from temporalio import workflow, activity
from temporalio.client import Client, TLSConfig
from temporalio.worker import Worker

async def main():

    # Configure certificates - replace file names below with certificate file references. Be sure to secure private keys in production environment. 
    client_cert_file = "./mtls.pem"
    client_private_key_file = "./mtls.key"

    clientcert = open(client_cert_file, 'rb').read()
    clientprivatekey = open(client_private_key_file, 'rb').read()

    # Replace NAMESPACENAME.ACCOUNTID with appropriate Temporal account and namespace names
    namespacename = "NAMESPACENAME.ACCOUNTID"
    targetdomain = namespacename + ".tmprl.cloud"
    targeturl = "http://" + targetdomain + ":7233"

    # Create client connected to server at the given address
    client = await Client.connect(target_url=targeturl, namespace=namespacename, tls_config=TLSConfig(domain=targetdomain, client_cert=clientcert, client_private_key=clientprivatekey))

    # Client below may be used for Docker self-hosted environment
    # client = await Client.connect(target_url="http://localhost:7233", namespace="default")

    # Execute a workflow
    mylist = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6','user7', 'user8', 'user9']
    await client.execute_workflow(SayHello.run, mylist, id="my-workflow-id", task_queue="my-task-queue")

    print("workflow executed")

if __name__ == "__main__":
    asyncio.run(main())
