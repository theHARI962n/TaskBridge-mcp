import asyncio 
from uuid import uuid4

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.mcp import MCPAdapter
from langchain.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

mcp_adapter = MCPAdapter("http://127.0.0.1:8000/mcp")

async def main():
    async with mcp_adapter:
        tools = await mcp_adapter.list_tools()

        agent = create_agent(
            model="gpt-6-luna",
            tools=tools,
            system_prompt="you are a helpful task management assistant",
            checkpointer=InMemorySaver()
        )

        config = {"configurable": {"thread_id": str(uuid4())}}
        human_question = "can u help me ?"

        while human_question != "exit":

            print("Agent is thinking...")
            result = await agent.ainvoke({"messages": [HumanMessage(content=human_question)], "config": config})

            print(result["messages"][-1].text)

            human_question = input("type message (q to exit): \n")

if __name__ == "__main__":
    asyncio.run(main())