import asyncio

from fastmcp import Client

client = Client("http://127.0.0.1:8000/mcp")

async def get_tools_from_sercer():
    async with client:
        tools = await client.list_tools()

        for tool in tools:
            print(tool.name)

    return tools

async def create_task_using_mcp():
    async with client:
        result = await client.call_tool(
            "create_task",
            {
                "title": "Implement FastMCP server",
                "description": "Implement a FastMCP server that can handle tasks and their statuses.",
                "priority": "high"
            }
        )
        print(result.data)
    return result.data

async def update_task_status_from_mcp():
    async with client:
        result = await client.call_tool(
            "update_task_status",
            {
                "task_id": "1",
                "status": "in progress"
            }
        )
        print(result.data)
    return result.data

async def list_tasks_using_mcp():
    async with client:
        result = await client.call_tool("list_tasks")
        print(result.data)
    return result.data


if __name__ == "__main__":
    # asyncio.run(create_task_using_mcp())
    asyncio.run(list_tasks_using_mcp())
    asyncio.run(update_task_status_from_mcp())
    asyncio.run(list_tasks_using_mcp())

