# Automated Backup Script

A beginner DevOps automation project written in Python to take daily timestamped backups of application files on Linux servers.

## Features
- Validates source directory existence (Fail-Fast design)
- Automates directory creation with current date format (`backup-YYYY-MM-DD/`)
- Idempotent execution (safe to run multiple times)
- Preserves file integrity and metadata using `shutil.copy2`
- Displays clear success/failure execution metrics

## Project Structure
```text
source/
  application.txt
  config.json
backup/
  backup-YYYY-MM-DD/
    application.txt
    config.json
backup.py
README.md# automated-backup-script
