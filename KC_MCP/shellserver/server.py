"""A simple MCP server that exposes a terminal tool and a README resource."""

import subprocess
import sys
from pathlib import Path

from mcp.server.mcpserver import MCPServer

mcp = MCPServer("shellserver")

TIMEOUT_SECONDS = 30
SHELL = ["powershell", "-NoProfile", "-Command"] if sys.platform == "win32" else ["bash", "-c"]
README_PATH = Path.home() / "Desktop" / "mcpreadme.md"


@mcp.resource(
    "file:///desktop/mcpreadme.md",
    name="mcpreadme",
    description="The mcpreadme.md file from the Desktop directory.",
    mime_type="text/markdown",
)
def mcpreadme() -> str:
    """Return the contents of mcpreadme.md on the Desktop."""
    return README_PATH.read_text(encoding="utf-8")


@mcp.tool()
def terminal_tool(command: str) -> str:
    """Run a shell command (PowerShell on Windows, bash elsewhere) and return its output (stdout, stderr and exit code)."""
    if not command.strip():
        return "Error: command must not be empty."

    try:
        result = subprocess.run(
            [*SHELL, command],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        return f"Error: command timed out after {TIMEOUT_SECONDS} seconds."

    return (
        f"exit code: {result.returncode}\n"
        f"stdout:\n{result.stdout}\n"
        f"stderr:\n{result.stderr}"
    )


if __name__ == "__main__":
    mcp.run(transport="stdio")
