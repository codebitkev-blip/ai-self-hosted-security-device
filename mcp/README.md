# Model Context Protocol (MCP)

This project includes an MCP server that exposes security alerts and statistics
as structured tools for Large Language Models (LLMs).

## Purpose

The MCP server allows an AI assistant to:
- Query recent network anomalies
- Retrieve summary security statistics
- Assist with investigation and reporting

## Design Principles

- Read-only access
- Local-only execution
- No packet capture or model control
- Separation from detection pipeline

## Available Tools

- `recent_alerts(limit=10)`
- `alert_statistics()`
