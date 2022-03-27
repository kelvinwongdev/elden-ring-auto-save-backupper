import shutil
from datetime import datetime
import time
import settings


def get_directory():
    backup_folder_name = datetime.now().strftime("%Y%m%d-%H%M")
    full_backup_directory = f"{settings.BACKUP_DIRECTORY}/{backup_folder_name}"
    return full_backup_directory


def save_game(directory):
    shutil.copytree(settings.ELDEN_RING_SAVE_DIRECTORY, directory)
    print("[" + datetime.now().strftime("%c") + "] Game save is backed up.")


def main(minite_interval):
    print("[" + datetime.now().strftime("%c") +
          "] Elden Ring Auto Save Backupper is running.")
    while True:
        time.sleep(minite_interval * 60)
        full_backup_directory = get_directory()
        save_game(full_backup_directory)


main(settings.MINUTE_INTERVAL)
