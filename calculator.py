from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("calculator")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract two numbers."""
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')

