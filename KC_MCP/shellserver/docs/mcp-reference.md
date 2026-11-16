
# MCP Development References

## Purpose

This document provides official references for developing
Model Context Protocol (MCP) servers using Python, FastMCP,
and the uv package manager.

## 1. Official MCP Documentation

URL: https://modelcontextprotocol.io/docs

Use this documentation to understand:
- MCP architecture and concepts
- MCP clients and servers
- MCP tools, resources, and prompts
- MCP transports (stdio and Streamable HTTP)
- MCP server development
- MCP security and best practices

## 2. Official MCP GitHub

URL: https://github.com/modelcontextprotocol

Use this source for:
- Official MCP repositories
- Protocol specifications
- SDK implementations
- Examples and reference implementations
- Latest SDK updates

## 3. Python MCP SDK

URL: https://github.com/modelcontextprotocol/python-sdk

Use this repository for:
- Python MCP server development
- FastMCP implementation
- Tool registration using @mcp.tool()
- Resource registration using @mcp.resource()
- Prompt registration using @mcp.prompt()
- Server initialization and execution
- MCP Inspector testing

## 4. Python Package Management

URL: https://docs.astral.sh/uv/

Use uv for:
- Python project initialization
- Virtual environment management
- Package installation
- Dependency management
- Running Python applications

## 5. Development Guidelines

When generating MCP server code:

1. Follow the official MCP Python SDK.
2. Prefer FastMCP for simple MCP implementations.
3. Use uv for Python dependency management.
4. Write clean, modular, reusable Python code.
5. Add type hints and docstrings.
6. Validate tool input and handle errors.
7. Follow current MCP security best practices.
8. Use Windows PowerShell commands.
9. Avoid outdated MCP APIs and deprecated methods.
10. Verify uncertain API details against the latest
    official documentation.

## 6. Cursor Agent Instructions

When asked to implement an MCP server:

- Read this reference document first.
- Consult relevant official online documentation.
- Prioritize official sources over third-party examples.
- Explain MCP architecture before complex implementation.
- Generate working Python examples using FastMCP.
- Clearly identify required dependencies.
- Provide instructions for testing the MCP server.
- Explain how to connect it to Cursor or Claude Desktop.

Note: These URLs are references, not locally indexed
documentation. Fetch their content when needed.
