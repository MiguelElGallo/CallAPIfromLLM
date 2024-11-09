# LLM models calling APIs

Chat flow is designed for conversational application development, building upon the capabilities of standard flow and providing enhanced support for chat inputs/outputs and chat history management. With chat flow, you can easily create a chatbot that handles chat input and output.

In this simple example it is illustrated how you can tell a model to call a Python function, which in turn calls an API from <https://api.open-meteo.com/v1/forecast>

The Python code for that function and API call is here: [](Chat_call_API/test_use_function.py)

## Create connection for LLM tool to use

You can follow these steps to create a connection required by a LLM tool.

Currently, there are two connection types supported by LLM tool: "AzureOpenAI" and "OpenAI". If you want to use "AzureOpenAI" connection type, you need to create an Azure OpenAI service first. Please refer to [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/cognitive-services/openai-service/) for more details. If you want to use "OpenAI" connection type, you need to create an OpenAI account first. Please refer to [OpenAI](https://platform.openai.com/) for more details.

```bash
# Create azure open ai connection
pf connection create --file azure_openai.yaml --set api_key=<your_api_key> api_base=<your_api_base> --name miguel_azure_open_ai
```

Note in [the Flow](Chat_call_API/flow.dag.yaml) we are using a connection named `miguel_azure_open_ai`.

```bash
# show registered connection
pf connection show --name miguel_azure_open_ai
```

Please refer to connections [document](https://promptflow.azurewebsites.net/community/local/manage-connections.html) and [example](https://github.com/microsoft/promptflow/tree/main/examples/connections) for more details.

## Executing the prompt flow

### Python requirements

1. Navigate to the Chat_call_API directory:

    ```bash
    cd Chat_call_API
    ```

2. Create a virtual environment named `env`:

    ```bash
    python3 -m venv env
    ```

3. Activate the virtual environment:

    ```bash
    source env/bin/activate
    ```

4. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

### Run the flow

Execute:

```bash
pf flow test --flow ./flow.dag.yaml --interactive
```

You will see:

```log
============================================================
Welcome to chat flow, Ask the model to call the weather API.
Press Enter to send your message.
You can quit with ctrl+C.
============================================================
User: 
```

Enter a question like: "Give me the temperature at latitude 10, longitude 10"

The model will get the latitude and longitude from your question and call the weather API, and reply with the temperature.
