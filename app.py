import os
import instaloader
from datetime import datetime


def download_instagram_content(username):
    L = instaloader.Instaloader()

    # Login (optional)
    # L.interactive_login("your_username") # If you want to login to access private profiles

    try:
        profile = instaloader.Profile.from_username(L.context, username)

        # Create a folder to store the downloaded content
        folder_name = f"{username}_content"
        os.makedirs(folder_name, exist_ok=True)

        # Download all content
        L.download_profile(profile.username, profile_pic_only=False)

        # Create or append to a change log file
        change_log_file = f"{folder_name}/change_log.txt"
        with open(change_log_file, "a+") as log:
            log.write(f"Content downloaded/updated on: {datetime.now()}\n")

        print("Content downloaded successfully.")
    except instaloader.exceptions.ProfileNotExistsException:
        print("Profile not found.")


if __name__ == "__main__":
    username = input("Enter Instagram username: ")
    download_instagram_content(username)
