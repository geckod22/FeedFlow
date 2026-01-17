# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-01-17
### Added
- **Initial Release**: Core MCP server functionality for FeedFlow.
- **MCP Tools**:
    - `add_custom_feed`: Adds a new RSS feed to the database.
    - `remove_feed`: Removes a feed from the database.
	- `list_feeds`: Returns the list of saved RSS feeds.
	- `fetch_rss_feed`: Fetches and displays the latest articles from a given RSS feed URL.
- **MCP Prompts**:
    - `available_feeds_categories`: Returns a list of all unique feed categories.
- **MCP Resources**:
    - `feeds://feeds`: Returns a list of all configured RSS feeds.
    - `feeds://categories`: Returns a list of all unique feed categories.
    - `feeds://feeds/{category}`: Returns a list of RSS feeds filtered by a specific category.
- **Language Detection**:
    - Automatically detects the language of a feed's content if not specified.
- **Data Persistence**:
    - Integrated local SQLite database for storing feed metadata and history.
- **Environment Management**:
    - Project initialization using `uv` for lightning-fast dependency resolution.
    - Automated environment setup scripts (`.bat` files for Windows).
- **Documentation**:
    - Comprehensive `README.md` with installation steps and MCP configuration instructions.
    - Standardized `pyproject.toml` for Python project metadata.

[1.0.0]: https://github.com/geckod22/FeedFlow/releases/tag/v1.0.0

---