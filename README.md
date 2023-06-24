# python_azure_function_pipenv_virtual_env

Creating azure function and running in virtual environment created by pipenv

find more details how to create pipenv virtual environment in https://kenanhancer.com/2023/06/23/python-azure-function-debugging-in-pipenv-virtual-environment/?preview=true

## How to create virtual environment with pipenv

https://kenanhancer.com/2023/06/19/how-to-create-virtual-environment-with-pipenv/

## Creating virtual environment

```shell
$ mkdir python_demo
$ cd python_demo
```

```shell
$ pyenv local 3.9.16
$ pipenv --python $(pyenv which python)
```

## Activating virtual environment

```shell
$ pipenv shell
```

## Creating Azure Function Project

```shell
$ func init --python -m V2
```

## Creating Azure Function Triggers

> Creating HTTP trigger function named HttpExample

```shell
$ func new --name HttpExample --template "HTTP trigger" --authlevel "anonymous"
```

> Creating Timer trigger function named TimerTrigger

```shell
$ func new --name TimerTrigger --template "Timer trigger"
```

> Creating Queue trigger function named QueueTrigger

```shell
$ func new --name QueueTrigger --template "Queue trigger" --authlevel "anonymous"
```

> Creating Blob trigger function named BlobTrigger

```shell
$ func new --name BlobTrigger --template "Blob trigger"
```

> Creating Cosmos DB trigger function named CosmosDBTrigger

```shell
$ func new --name CosmosDBTrigger --template "Cosmos DB trigger"
```

> Creating Service Bus Queue trigger function named ServiceBusQueueTrigger

```shell
$ func new --name ServiceBusQueueTrigger --template "Service Bus Queue trigger"
```

> Creating Service Bus Topic trigger function named ServiceBusTopicTrigger

```shell
$ func new --name ServiceBusTopicTrigger --template "Service Bus Topic trigger"
```

> Creating Event Hub trigger function named EventHubTrigger

```shell
$ func new --name EventHubTrigger --template "Event Hub trigger"
```

> Creating Event Grid trigger function named EventGridTrigger

```shell
$ func new --name EventGridTrigger --template "Event Grid trigger"
```

> Creating IoT Hub (Event Hub) trigger function named IoTHubTrigger

```shell
$ func new --name IoTHubTrigger --template "IoT Hub (Event Hub) trigger"
```

> Creating SignalR Service trigger function named SignalRTrigger

```shell
$ func new --name SignalRTrigger --template "SignalR Service trigger"
```

> Creating Durable Functions orchestrator trigger function named DurableOrchestratorTrigger

```shell
$ func new --name DurableOrchestratorTrigger --template "Durable Functions orchestrator trigger"
```

> Creating Durable Functions activity trigger function named DurableActivityTrigger

```shell
$ func new --name DurableActivityTrigger --template "Durable Functions activity trigger"
```

> Creating Durable Functions HTTP starter trigger function named DurableHTTPStarter

```shell
$ func new --name DurableHTTPStarter --template "Durable Functions HTTP starter"
```

> Creating RabbitMQ trigger function named RabbitMQTrigger

```shell
$ func new --name RabbitMQTrigger --template "RabbitMQ trigger"
```

> Creating Kafka trigger function named KafkaTrigger

```shell
$ func new --name KafkaTrigger --template "Kafka trigger"
```

## VSCode config files

### .vscode/launch.json

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Attach to Python Functions",
      "type": "python",
      "request": "attach",
      "port": 9091,
      "preLaunchTask": "func: host start"
    }
  ]
}
```

### .vscode/tasks.json

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "func: host start",
      "type": "shell",
      "command": "func host start --language-worker -- '-m ptvsd --host 127.0.0.1 --port 9091'",
      "problemMatcher": "$func-python-watch",
      "isBackground": true,
      "dependsOn": "pip install (functions)"
    },
    {
      "label": "pip install (functions)",
      "type": "shell",
      "osx": {
        "command": "${config:azureFunctions.pythonVenv}/bin/python -m pip install -r requirements.txt"
      },
      "windows": {
        "command": "${config:azureFunctions.pythonVenv}\\Scripts\\python -m pip install -r requirements.txt"
      },
      "linux": {
        "command": "${config:azureFunctions.pythonVenv}/bin/python -m pip install -r requirements.txt"
      },
      "problemMatcher": []
    },
    {
      "label": "Run Azurite",
      "type": "shell",
      "command": "azurite",
      "isBackground": true,
      "problemMatcher": "$tsc"
    }
  ]
}
```

### .vscode/settings.json

>update value of **azureFunctions.pythonVenv** to your environment name. Just update python_demo-3.9 to your virtual environment name.

```json
{
  "azureFunctions.deploySubpath": ".",
  "azureFunctions.scmDoBuildDuringDeployment": true,
  "azureFunctions.pythonVenv": "/Users/kenanhancer/.local/share/virtualenvs/python_demo-3.9",
  "azureFunctions.projectLanguage": "Python",
  "azureFunctions.projectRuntime": "~4",
  "debug.internalConsoleOptions": "neverOpen",
  "azureFunctions.projectLanguageModel": 2
}
```

### .vscode/extensions.json

```json
{
  "recommendations": [
    "ms-azuretools.vscode-azurefunctions",
    "ms-python.python"
  ]
}
```

## Start Azurite for local emulator

>Azurite is local emulator of Azure. Azure function needs azurite so that when we run func host start , azure function app will connect to Azurite storage acount, so click **CMD+SHIFT+P** in VSCode and type azurite: start and enter.

![](./images/image1.png)

## Debugging Azure Function locally

>Click **CMD+SHIFT+P** and type Debug: Start Debugging as shown in below screenshot or just click **F5** shortcut.

![](./images/image2.png)

>VSCode will ask for storage account, so select Use Local Emulator for local development.

![](./images/image3.png)

### local.settings.json

```json
{
    "IsEncrypted": false,
  "Values": {
      "FUNCTIONS_WORKER_RUNTIME": "python",
    "AzureWebJobsFeatureFlags": "EnableWorkerIndexing",
    "AzureWebJobsStorage": "UseDevelopmentStorage=true"
  }
}
```

>This will update line 6 in **local.settings.json**

![](./images/image4.png)

## Testing Azure HTTP and Webhook Triggered Functions Locally

>GET request
```shell
$ curl http://localhost:7071/api/HttpExample\?name=Azure
```

>POST request
```shell
$ curl -X POST -H "Content-Type: application/json" -d '{ "name": "Azure" }' http://localhost:7071/api/HttpExample
```

## Testing Azure Non-HTTP Triggered Functions Locally

>POST request
```shell
$ curl --request POST -H "Content-Type: application/json" --data '{"input":"sample queue data"}' http://localhost:7071/admin/functions/QueueFunc
```

## Deactivating virtual environment

```shell
$ exit
```