# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.5.0] - 2026-06-09

### Added

- `get_total_login_count` method to `LogAnalyser` to return the total number of login attempts.
- Streamlit dashboard (`pages/dashboard.py`) with dedicated panels for each `LogAnalyser` method:
  - KPI metrics: total login attempts, unique client connections, most active client IP
  - Login summary status code breakdown chart
  - Top 5 client IPs by request volume chart
  - HTTP method breakdown donut chart for the most active client
  - Traffic volume by country chart
  - Client activity lookup panel with IP search
- Reusable chart and component functions (`render_metric_card`, `render_bar_chart`, `render_donut_chart`, `render_data_table`, `render_search_bar`) to allow components to be shared across panels.

### Changed

- Updated imports to use explicit `src.` prefix (e.g. `from src.columns import LogColumns`).

## [0.4.0] - 2026-06-08

### Added

- `LogAnalyser` class to answer the 7 questions using Polars queries:
  - 1: Can you give a summary of the login endpoint status code responses?
  - 2: How many unique IP addresses did an API call?
  - 3: Can you order those IP addresses by the amount of calls made?
  - 4: What IP address did the most API calls for any API endpoint?
  - 5: Can you give a breakdown of the activity by HTTP method of the IP address from Q4?
  - 6: Can you give a count of requests made by ClientCountry?
  - 7: Can you add functionality for us to be able to input a users IP address and to print out all the activity from that IP?
- `LogColumns` string Enum to manage log schema column mappings.
- `test_log_analyser.py` test suite for methods in `LogAnalyser` .

### Changed

- Updated `pyproject.toml` configuration `pythonpath` from `["."]` to `["src"]`. Doing so fixed issues with imports for tests.

## [0.3.0] - 2026-06-08

### Added

- `get_schema` method added to the YAMLLoader class.
- Schema enforcement support to `LogLoader.load`.

### Changed

- Updated `schema_metadata.yaml` types to use JSON-compatible types `Int64` and `String`.

## [0.2.0] - 2026-06-07

### Added

- `YamlLoader` config utility to securely read and parse metadata.
- Error definitions `YamlLoaderError`, `YamlFileNotFoundError` and `YamlParsingError`.
- `test_yaml_loader.py` for validating path resolution.
- Added `pyyaml` dependency to `pyproject.toml`.

## [0.1.0] - 2026-06-06

### Added

- Created a `LogLoader` utility class using Polars to ingest individual JSON log files or complete directories.
- Introduced custom exception handling for missing paths, empty log folders, and data parsing failures.
- Implemented a complete test suite to validate successful loading paths and error scenarios.
- Created `pyproject.toml` for project configuration

### Changed

- Encapsulated internal file path storage behind a read-only public property.
