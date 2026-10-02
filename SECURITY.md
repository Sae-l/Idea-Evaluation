# Security policy

The maintained skill version is 2.1. Version 2.0 predates the input-validation and formula-text protections; use the current version for exports.

Treat imported idea data as untrusted. The exporter reads a local JSON file and writes the explicitly requested output path. It does not contact external services. Generated XLSX files contain intentional scoring formulas, while supplied text is stored literally; CSV formula-like text is prefixed with an apostrophe.

For a security concern, use GitHub private vulnerability reporting if enabled, or contact the maintainer through an available private channel. Do not include secrets, confidential idea descriptions or exploit payloads in a public issue. No response-time guarantee is stated.
