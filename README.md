# AZ-204

## Serverless

Design First Technologies:

- **Logic Apps** - draw out complex workflows (can edit code)
- **Microsoft Power Automate/Microsoft flow** - built on top of Logic Apps, 
only GUI targeted at non-IT people. There is no option to edit code.

Code First Technologies;

 - **WebJobs/WebJobs SDK** - part of Azure App Service, use if code is part
   of existing App Service appliaction. You pay for entrie VM, or App Service plan that hosts the job.
 - **Azure Functions** - simpler administration and more flexible, this
   is what you want to use in most cases. Run on a consumption plan.

## Azure Functions

* by default limited to 5 minutes, can be extended to 10.
* **durable functions** alow to orchestrate execution of multipe functions without any timeout.
* it might be cheaper to host your service on a VM when you expect your function to be executed continously.
* service plans:
    * **consumption service plan**: automatic scalling, bills you when functions are running (default 5 mins timeout).
    * **Azure App Service Plan**: can run continously on a VM that you define, not really serverless, you are responsible for managing the VM. 
* must be linked to a storage account: logging function executions, manage execution triggers.
* functions are event driven, an evant that starts a function is called **trigger** (blob storage, cosmos db, event grid, http, queue storage, service bus, timer), it is a special type of input binding that has the additional capability of initiating execution
* **Bindings** - declarative way to connect data and services, you don't have to write code in your function to connect to data sources and manage connections. Each binding has a direction: *input* / *output*
* **Binding Properties**: name, type, direction, connection
* **Access**:
  * anonymous
  * function (http request must provide a key)
  * admin (similar to function, but with an admin key that can be used to trigger any function in the function app)

### Durable Functions

Long-lasting, stateful operations in serverless environment, retain state between calls.

Types:
* client - entry point for creating an instance of Durable Functions (triggered by events like http request arriving)
* orhcestrator - describe how actions are executed, and the order in which they are run. Functions can be called synchronosuly, or asynchronosuly, output is saved locally in variables and can be used in subsequent function calls.
* activity  - basic unit of work, contains the actual work performed by the tasks being orchestrated. 

workflow:
* function chaining
* fan out/fan in - run in parallel and wait to finish.
* async HTTP Apis - redirect client to a status endpoint, client can learn when the operation is finished by polling it.
* monitor - reccurring process in a workflow, for example poll until condition is met.
* human interaction - for example an approval process.

Durable functions provides timers for use in orchestrator functions. They can impelement delays or setup timeouts for asynchronous actions. 

### Azure Functions Core Tools

* generate files and folders you need to develop functions locally
* run functions locally, so you can test & debug
* pubish functions to Azure

Tools are packages as a single command line utility `func`.

Two most critical projet files are:
* **host.json** - stores runtime configuration values (like logging options)
* **local.settings.json** - local runtime settings & custom application settings 

1. Create project: `func init`
2. Create a new function: `func new`
3. Start function locally: `func start` 
4. Publish: `func azure functionapp publish "$FUNCTIONAPP"`

Before you can use the Core Tools to publish a project, you need to create a function app in Azure. Core tools don't ask you to sign in to azure. Instead, they use your subscription and resources by loading your session information from Azure CLI or Azure PowerShell - if you do not have an active seesion in one of those tools, publishing will fail!

When you publish, any functions already present in the target app are stopped and deleted before the contents of your project are deployed. You can't combine functions from multiple projects into one app by publishing them in sequence - all of the functions you want in the app must be in one project.
