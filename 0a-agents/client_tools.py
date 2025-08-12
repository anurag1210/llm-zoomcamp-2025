# client_tools.py
import asyncio
from fastmcp import Client

async def main():
    async with Client("weather_server.py") as mcp_client:
        tools_resp = await mcp_client.list_tools()
        print("tools/list ->")
        print(tools_resp)

if __name__ == "__main__":
    asyncio.run(main())