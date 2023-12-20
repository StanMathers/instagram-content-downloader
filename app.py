import os
import instaloader
from datetime import datetime


def download_instagram_content(username: str, download_path: str, instagram_login: str = None):
    L = instaloader.Instaloader(dirname_pattern=f"{download_path}/{username}")

    # Login (optional)
    if instagram_login:
        L.interactive_login(instagram_login)

    try:
        profile = instaloader.Profile.from_username(L.context, username)

        # Create a folder to store the downloaded content
        folder_name = f"{download_path}/{username}_content"
        os.makedirs(folder_name, exist_ok=True)

        # Download all content
        L.download_profile(profile.username, profile_pic_only=False, fast_update=True)

        # Create or append to a change log file
        change_log_file = f"{folder_name}/change_log.txt"
        with open(change_log_file, "a+") as log:
            log.write(f"Content downloaded/updated on: {datetime.now()}\n")

        print("Content downloaded successfully.")
    except instaloader.exceptions.ProfileNotExistsException:
        print("Profile not found.")


if __name__ == "__main__":
    # If required, change None to your Instagram login. Example: instagram_login = "your_username"
    # Example use case: If you want to download private profiles, you need to login
    instagram_login = None

    download_path = "public"  # Change this to your desired download path
    username = input("Enter Instagram username: ")
    download_instagram_content(username, download_path, instagram_login)
