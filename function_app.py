import azure.functions as func
import logging

app = func.FunctionApp()


# curl http://localhost:7071/api/HttpExample?name=Azure
# curl -X POST -H "Content-Type: application/json" -d '{ "name": "Azure" }' http://localhost:7071/api/HttpExample
@app.route(route="HttpExample", auth_level=func.AuthLevel.ANONYMOUS)
def HttpExample(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

# curl --request POST -H "Content-Type: application/json" --data '{"input":"sample queue data"}' http://localhost:7071/admin/functions/QueueFunc
@app.function_name("QueueFunc")
@app.queue_trigger(arg_name="azqueue", queue_name="myqueue",
                               connection="AzureWebJobsStorage") 
def QueueTrigger(azqueue: func.QueueMessage):
    logging.info('Python Queue trigger processed a message: %s',
                azqueue.get_body().decode('utf-8'))
