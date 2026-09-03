#!/usr/bin/env python3
"""
Automated Backup Script
DevOps Training Assignment - Project 3
"""

import os
import shutil
from datetime import datetime


def perform_backup(source_dir="source", backup_base_dir="backup"):
    print("=" * 55)
    print("        AUTOMATED SERVER BACKUP PROCESS")
    print("=" * 55)

    # 1. Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"[FAILED] Source directory '{source_dir}' does not exist!")
        return False

    # 2. Get today's date formatted as YYYY-MM-DD
    current_date = datetime.now().strftime("%Y-%m-%d")
    destination_folder = os.path.join(backup_base_dir, f"backup-{current_date}")

    try:
        # 3. Create the backup destination folder
        os.makedirs(destination_folder, exist_ok=True)

        # 4. Copy all files from source to backup folder
        files = os.listdir(source_dir)
        if not files:
            print("[WARNING] Source directory is empty. Nothing to back up.")
            return False

        copied_count = 0
        for file_name in files:
            source_file = os.path.join(source_dir, file_name)
            destination_file = os.path.join(destination_folder, file_name)

            if os.path.isfile(source_file):
                shutil.copy2(source_file, destination_file)
                print(f" -> Backed up: {file_name}")
                copied_count += 1

        # 5. Display success confirmation
        print("-" * 55)
        print(f"[SUCCESS] Backup completed successfully!")
        print(f" Date        : {current_date}")
        print(f" Source      : {source_dir}/")
        print(f" Destination : {destination_folder}/")
        print(f" Files Saved : {copied_count} file(s)")
        print("=" * 55)
        return True

    except Exception as e:
        print("-" * 55)
        print(f"[FAILED] Backup process encountered an error: {e}")
        print("=" * 55)
        return False


if __name__ == "__main__":
    perform_backup()
