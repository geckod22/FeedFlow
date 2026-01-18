
# tests/test_utils.py
from feedflow.main import mcp

def test_mcp_config():
    """Verify that the MCP instance in main.py is configured correctly."""
    assert mcp.name == "FeedFlow"
    assert mcp.version == "1.0.0"
    
