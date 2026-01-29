from mcp.server.fastmcp import FastMCP
from mcp.tools import get_alerts, get_alert_stats

mcp = FastMCP("AI Self-Hosted Security Device")

@mcp.tool()
def recent_alerts(limit: int = 10):
    """Fetch recent detected security anomalies."""
    return get_alerts(limit)

@mcp.tool()
def alert_statistics():
    """Fetch summary statistics of detected anomalies."""
    return get_alert_stats()

if __name__ == "__main__":
    mcp.run()
