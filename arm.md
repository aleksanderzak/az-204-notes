# ARM templates

ARM template file structure

When writing an ARM template, you need to understand all the parts that make up
the template and what they do. The template files are made up of the following
elements:
* schema: A required section that defines the location of the JSON schema file
  that describes the structure of JSON data. The version number you use depends
  on the scope of the deployment and your JSON editor.
* contentVersion: A required section that defines the version of your template
  (such as 1.0.0.0). You can use this value to document significant changes in
  your template to ensure you're deploying the right template.
* apiProfile: An optional section that defines a collection of API versions for
  resource types. You can use this value to avoid having to specify API versions
  for each resource in the template.
* parameters: An optional section where you define values that are provided
  during deployment. These values can be provided by a parameter file, by
  command-line parameters, or in the Azure portal.
* variables: An optional section where you define values that are used to
  simplify template language expressions.
* functions: An optional section where you can define user-defined functions
  that are available within the template. User-defined functions can simplify
  your template when complicated expressions are used repeatedly in your
  template.
* resources: A required section that defines the actual items you want to deploy
  or update in a resource group or a subscription.
* output: An optional section where you specify the values that will be returned
  at the end of the deployment.

```
az deployment group create \
  --name blanktemplate \
  --resource-group myResourceGroup \
  --template-file $templateFile
```

```
az deployment group create \
  --resource-group elo \
  --template-file arm/azuredeploy.json \
  --parameters arm/azuredeploy.parameters.dev.js
```

```
az deployment group create \
  --resource-group elo \
  --template-file arm/azuredeploy.json \
  --parameters storagePrefix=elo
```

**Expressions** are values that are evaluated when the template is deployed. They
start and end with brackets, [ and ], and can return a string, integer, Boolean,
array, or object.

An ARM template **variable** is a construct that holds a value for later use.
Template variables are specified in camel case. Don't use the reference function
in the variables section of a template. The reference function is resolved at
runtime, and variables are resolved when the template is parsed. Also, don't use
variables for apiVersion on a resource. The API version determines the schema of
the resource, and often you can't change the version without changing the
properties for the resource. 

**Functions**
* Array functions for working with arrays. For example, `first` and `last`.
* Comparison functions for making comparisons in your templates. For example,
  `equals` and `greater`.
* Date functions for working with dates. For example, `utcNow` and
  `dateTimeAdd`.
* Deployment value functions for getting values from sections of the template
  and values related to the deployment. For example, `environment` and
  `parameters`.
* Logical functions for working with logical conditions. For example, `if` and
  `not`.
* Numeric functions for working with integers. For example, `max` and `mod`.
* Object functions for working with objects. For example, `contains` and
  `length`.
* Resource functions for getting resource values. For example, `resourceGroup`
  and `subscription`.
* String functions for working with strings. For example, `length` and
  `startsWith`.