import json, subprocess, sys, time

# Start the MCP server process
server = subprocess.Popen(
    [sys.executable, "weather_server.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True
)

def send(obj):
    server.stdin.write(json.dumps(obj) + "\n")
    server.stdin.flush()

def recv(timeout=5):
    t0 = time.time()
    while time.time() - t0 < timeout:
        line = server.stdout.readline()
        if not line:
            continue
        line = line.strip()
        if line.startswith("{") and line.endswith("}"):
            return json.loads(line)
    return None

# 1) Initialize
send({
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2024-11-05",
        "capabilities": {"roots": {"listChanged": True}, "sampling": {}},
        "clientInfo": {"name": "test-client", "version": "1.0.0"}
    }
})
print("initialize ->", recv())

# 2) Confirm initialization (no output expected)
send({"jsonrpc": "2.0", "method": "notifications/initialized"})

# 3) List tools
send({"jsonrpc": "2.0", "id": 2, "method": "tools/list"})
print("tools/list ->", recv())

# 4) Call get_weather for Berlin
send({
    "jsonrpc": "2.0",
    "id": 3,
    "method": "tools/call",
    "params": {
        "name": "get_weather",  # <TODO1> is get_weather
        "arguments": {"city": "Berlin"}  # <TODO2> is "city": "Berlin"
    }
})
print("get_weather ->", recv())


""" output
initialize -> {'jsonrpc': '2.0', 'id': 1, 'result': {'protocolVersion': '2024-11-05', 'capabilities': {'experimental': {}, 'prompts': {'listChanged': False}, 'resources': {'subscribe': False, 'listChanged': False}, 'tools': {'listChanged': True}}, 'serverInfo': {'name': 'Demo 🚀', 'version': '1.12.4'}}}
tools/list -> {'jsonrpc': '2.0', 'id': 2, 'result': {'tools': [{'name': 'get_weather', 'description': 'Retrieves the temperature for a specified city.\n\nParameters:\n    city (str): The name of the city for which to retrieve weather data.\n\nReturns:\n    float: The temperature associated with the city.', 'inputSchema': {'properties': {'city': {'title': 'City', 'type': 'string'}}, 'required': ['city'], 'type': 'object'}, 'outputSchema': {'properties': {'result': {'title': 'Result', 'type': 'number'}}, 'required': ['result'], 'title': '_WrappedResult', 'type': 'object', 'x-fastmcp-wrap-result': True}, '_meta': {'_fastmcp': {'tags': []}}}, {'name': 'set_weather', 'description': "Sets the temperature for a specified city.\n\nParameters:\n    city (str): The name of the city for which to set the weather data.\n    temp (float): The temperature to associate with the city.\n\nReturns:\n    str: A confirmation string 'OK' indicating successful update.", 'inputSchema': {'properties': {'city': {'title': 'City', 'type': 'string'}, 'temp': {'title': 'Temp', 'type': 'number'}}, 'required': ['city', 'temp'], 'type': 'object'}, 'outputSchema': {'properties': {'result': {'title': 'Result', 'type': 'string'}}, 'required': ['result'], 'title': '_WrappedResult', 'type': 'object', 'x-fastmcp-wrap-result': True}, '_meta': {'_fastmcp': {'tags': []}}}]}}
get_weather -> {'jsonrpc': '2.0', 'id': 3, 'result': {'content': [{'type': 'text', 'text': '20.0'}], 'structuredContent': {'result': 20.0}, 'isError': False}}
"""