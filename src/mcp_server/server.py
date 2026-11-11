from fastmcp import FastMCP
from mcp_server.database import (
    get_all_tasks,
    update_task_status_in_db,
    save_task
)

mcp = FastMCP("My MCP Server", "1.0.0")

@mcp.tool(name="create_task", description="this tool is created to create new tasks")
def create_task(title: str, description: str, priority: str = "medium") -> dict:
    """
    this function creates new tasks in our database
    """
    task_id = str(uuid4())
    status = "todo"
    task = {
        "task_id": task_id,
        "title": title,
        "description": description,
        "priority": priority,
        "status": status
    }
    save_task(task)
    return task

@mcp.tool(name="update_task_status", description="this tool is created to update the status of existing tasks")
def update_task_status(task_id: str, status: Literal["todo", "in_progress", "completed"]) -> dict:
    """
    this function will update the status of a specific task based on its task_id
    """
    return update_task_status_in_db(task_id, status)

@mcp.tool(name="list_tasks", description="this tool provide all the list of tasks in our database")
def list_tasks() -> list[dict]:
    """
    this function returns all the tasks in our database
    """
    return get_all_tasks()

if __name__ == "__main__":
    mcp.run(transport=http, port=8000)
    # create_task(
    #     title="Implement FastMCP server",
    #     description="Implement a FastMCP server that can handle tasks and their statuses.",
    #     priority="high"
    # )