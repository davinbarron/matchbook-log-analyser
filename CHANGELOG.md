# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-06-06

### Added

- Created a `LogLoader` utility class using Polars to ingest individual JSON log files or complete directories.
- Introduced custom exception handling for missing paths, empty log folders, and data parsing failures.
- Implemented a complete test suite to validate successful loading paths and error scenarios.
- Created `pyproject.toml` for project configuration

### Changed

- Encapsulated internal file path storage behind a read-only public property.
