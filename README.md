# create custom Server 

> Get started building your own server to use in Claude for Desktop and other clients.

In this tutorial, we'll build a simple MCP calculator server and connect it to a host, Claude for Desktop.
## What is MCP?

**MCP** stands for **Model Context Protocol** — it’s a protocol that allows developers to extend AI assistants (like Claude) with custom tools and servers.

- Think of it like giving your AI assistant **extra powers**.
- These servers expose tools or functionalities that the assistant can use during a conversation.
- For example: you can build weather servers, calculators, finance assistants, or anything you imagine.

### What we'll be building

We'll build a server that exposes four tools: `add`, `subtract`, `multiply`, and `divide`. Then we'll connect the server to an MCP host (in this case, Claude for Desktop):

<Note>
    Servers can connect to any client. We've chosen Claude for Desktop here for demonstration purposes.
</Note>

<Accordion title="Why Claude for Desktop and not Claude.ai?">
    Because servers are locally run, MCP currently only supports desktop hosts.
</Accordion>

### Core MCP Concepts

MCP servers can provide three main types of capabilities:

1. **Resources**: File-like data that can be read by clients (like API responses or file contents)
2. **Tools**: Functions that can be called by the LLM (with user approval)
3. **Prompts**: Pre-written templates that help users accomplish specific tasks

This tutorial will primarily focus on tools.

<Tabs>
    <Tab title="Python">
        Let's get started with building our calculator server! [You can find the complete code for what we'll be building here.](https://github.com/varunidealabs/simple-calculator-mcp-server.git)

        ### Prerequisite knowledge

        This quickstart assumes you have familiarity with:

        * Python
        * LLMs like Claude

        ### System requirements

        * Python 3.10 or higher installed.
        * You must use the Python MCP SDK 1.2.0 or higher.

        ### Set up your environment

        First, let's install `uv` and set up our Python project and environment:

        <CodeGroup>
            ```bash MacOS/Linux
            curl -LsSf https://astral.sh/uv/install.sh | sh
            ```

            ```powershell Windows
            powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
            ```
        </CodeGroup>

        Make sure to restart your terminal afterwards to ensure that the `uv` command gets picked up.

        Now, let's create and set up our project:

        <CodeGroup>
            ```bash MacOS/Linux
            # Create a new directory for our project
            uv init calculator
            cd calculator

            # Create virtual environment and activate it
            uv venv
            source .venv/bin/activate

            # Install dependencies
            uv add "mcp[cli]"

            # Create our server file
            touch calculator.py
            ```

            ```powershell Windows
            # Create a new directory for our project
            uv init calculator
            cd calculator

            # Create virtual environment and activate it
            uv venv
            .venv\Scripts\activate

            # Create our server file
            new-item calculator.py
            ```
        </CodeGroup>

        Now let's dive into building your server.

        ## Building your server

        ### Importing packages and setting up the instance

        Add these to the top of your `calculator.py`:

        ```python
        from mcp.server.fastmcp import FastMCP

        # Initialize FastMCP server
        mcp = FastMCP("calculator")
        ```

        ### Implementing tool execution

        The tool execution handler is responsible for actually executing the logic of each tool. Let's add it:

        ```python
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
        ```

        ### Running the server

        Finally, let's initialize and run the server:

        ```python
        if __name__ == "__main__":
            # Initialize and run the server
            mcp.run(transport='stdio')
        ```

        Your server is complete! Run `uv run calculator.py` to confirm that everything's working.

        Let's now test your server from an existing MCP host, Claude for Desktop.

        ## Testing your server with Claude for Desktop

        <Note>
            Claude for Desktop is not yet available on Linux.
        </Note>

        We'll need to configure Claude for Desktop for whichever MCP servers you want to use. To do this, open your Claude for Desktop App configuration at `~/Library/Application Support/Claude/claude_desktop_config.json` in a text editor. Make sure to create the file if it doesn't exist.

        <Tabs>
            <Tab title="MacOS/Linux">
                ```bash
                code ~/Library/Application\ Support/Claude/claude_desktop_config.json
                ```
            </Tab>

            <Tab title="Windows">
                ```powershell
                code $env:AppData\Claude\claude_desktop_config.json
                ```
            </Tab>
        </Tabs>

        You'll then add your servers in the `mcpServers` key. The MCP UI elements will only show up in Claude for Desktop if at least one server is properly configured.

        In this case, we'll add our single calculator server like so:

        <Tabs>
            <Tab title="MacOS/Linux">
                ```json Python
                {
                    "mcpServers": {
                        "calculator": {
                            "command": "uv",
                            "args": [
                                "--directory",
                                "/ABSOLUTE/PATH/TO/PARENT/FOLDER/calculator",
                                "run",
                                "calculator.py"
                            ]
                        }
                    }
                }
                ```
            </Tab>

            <Tab title="Windows">
                ```json Python
                {
                    "mcpServers": {
                        "calculator": {
                            "command": "uv",
                            "args": [
                                "--directory",
                                "C:\\ABSOLUTE\\PATH\\TO\\PARENT\\FOLDER\\calculator",
                                "run",
                                "calculator.py"
                            ]
                        }
                    }
                }
                ```
            </Tab>
        </Tabs>

        <Warning>
            You may need to put the full path to the `uv` executable in the `command` field. You can get this by running `which uv` on MacOS/Linux or `where uv` on Windows.
        </Warning>

        <Note>
            Make sure you pass in the absolute path to your server.
        </Note>

        This tells Claude for Desktop:

        1. There's an MCP server named "calculator"
        2. To launch it by running `uv --directory /ABSOLUTE/PATH/TO/PARENT/FOLDER/calculator run calculator.py`

        Save the file, and restart **Claude for Desktop**.
    </Tab>
</Tabs>

<Note>
    Since this calculator supports basic arithmetic operations, it can be used for addition, subtraction, multiplication, and division.
</Note>

For more info: [MCP Official Docs](https://modelcontextprotocol.io/quickstart/server)
