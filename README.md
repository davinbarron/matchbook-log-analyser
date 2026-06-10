# Matchbook Log Analyser

A log analysis tool for parsing and inspecting Matchbook system activity logs, with an interactive dashboard for exploring metrics and client behaviour.

## Docs

- [Setup Guide](docs/setup.md)
- [Anomaly Findings](docs/anomaly_findings.md)

## Usage

The dashboard provides the following views:

- **Total Login Attempts**: count of all login requests and their status codes
- **Unique Client Connections**: number of distinct IP addresses seen in the logs
- **Most Active Client IP**: the IP address with the highest request volume
- **Login Summary**: status code breakdown for login endpoint requests
- **Top Client IPs**: the five highest-volume IP addresses by request count
- **HTTP Method Breakdown**: method distribution for the most active client
- **Traffic by Country**: request counts grouped by client country
- **Client Activity Lookup**: search by IP address to view all activity for that client
