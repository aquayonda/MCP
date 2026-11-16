# shellserver

A simple MCP server, built with the [Python MCP SDK](https://github.com/modelcontextprotocol/python-sdk), that exposes one tool for running terminal commands.

## Tool

| Tool | Parameter | Description |
|------|-----------|-------------|
| `terminal_tool` | `command` (string) | Runs a shell command (PowerShell on Windows, bash on Linux/in the Docker image) and returns its exit code, stdout and stderr. |

Behavior:
- On Windows, commands run through `powershell -NoProfile -Command <command>`; on Linux (including the Docker image) through `bash -c <command>`.
- Commands time out after 30 seconds.
- An empty command returns an error message.

## Requirements

- Windows with PowerShell
- Python 3.15 or newer
- [uv](https://docs.astral.sh/uv/)

## Project layout

```
shellserver/
├── server.py          # the MCP server (MCPServer + terminal_tool)
├── pyproject.toml     # dependencies (mcp[cli]>=2.3.0)
├── docs/mcp-reference.md   # MCP development references
└── .cursor/python.mdc      # Cursor rules for Python MCP development
```

## How it works

`server.py` creates an `MCPServer` (the high-level API in mcp 2.x; older SDKs call it `FastMCP`), registers `terminal_tool` with the `@mcp.tool()` decorator, and runs over the stdio transport. The client (Cursor) starts the server as a subprocess and talks to it over stdin/stdout, so the server must not print anything else to stdout.

## Setup

```powershell
uv sync
```

## Run and test

Run the server directly (it waits for a client on stdio):

```powershell
uv run server.py
```

Test it interactively with the MCP Inspector:

```powershell
uv run mcp dev server.py
```

## Connect to Cursor

Add this to `.cursor/mcp.json` (in the project, or in your home `.cursor` folder):

```json
{
  "mcpServers": {
    "shellserver": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\Users\\thetkc\\Desktop\\MCP\\KC_MCP\\shellserver",
        "run",
        "server.py"
      ]
    }
  }
}
```

Cursor then lists `terminal_tool` and calls it when the agent needs to run a command.

## Security

`terminal_tool` runs any command it receives with your user's permissions. There is no allowlist or sandbox.

- Keep Cursor's tool-approval prompt on and review each command.
- Do not expose this server over a network.
- To restrict it, add an allowlist of permitted commands before running.

## Verification

A test client using the SDK listed one tool (`terminal_tool`), and calling it with `echo hello` returned `hello` with exit code 0.
