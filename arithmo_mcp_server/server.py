# your MCP server code
from mcp.server.fastmcp import FastMCP
from .calculator import perform_operation

mcp = FastMCP("arithmo_mcp_server")

@mcp.tool()
async def perform_calculation(operation: str, a: float, b: float) -> str:
    return perform_operation(operation, a, b)

if __name__ == "__main__":
    mcp.run(transport='tcp', host='0.0.0.0', port=8000)
