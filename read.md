Prerequisites
Python installed on your machine.
SQLite3 included in your Python installation.
Setup Instructions
Install Python:

Ensure Python is installed on your system. You can download it from python.org.
Verify the installation by running:
bash
Copy code
python --version
Install SQLite3:

SQLite3 should be included with your Python installation. You can verify this by running:
bash
Copy code
sqlite3 --version
Create Python Script:

Create a file named youtube_manager.py.
Copy and paste the provided code into this file.
Running the Script:

Open a terminal or command prompt.
Navigate to the directory containing youtube_manager.py.
Run the script using the following command:
bash
Copy code
python youtube_manager.py
Using the Application
Launching the Application:

After running the script, you will see the main menu with options to list, add, update, delete, and exit.
List All YouTube Videos:

Select option 1 to list all videos. If the table is empty, it will indicate that the table is empty.
Add a YouTube Video:

Select option 2 to add a new video.
Enter the video's name and time when prompted.
Update a YouTube Video:

Select option 3 to update an existing video.
Enter the video ID, new name, and new time when prompted.
Delete a YouTube Video:

Select option 4 to delete a video.
Enter the video ID to delete when prompted.
Exit the Application:

Select option 5 to exit the application.
Code Summary
Database Connection:

Connects to a SQLite database named youtube_video.
Creates a table videos if it does not exist with columns id, name, and time.
Functions:

all_videos(): Lists all videos from the videos table.
add_video(name, time): Adds a new video to the videos table.
update_video(video_id, new_name, new_time): Updates a video's name and time based on its ID.
delete_video(video_id): Deletes a video from the videos table based on its ID.
Main Loop:

Provides a text-based menu to interact with the database.
Users can choose to list, add, update, delete videos, or exit the application.
Notes
Ensure the SQLite database file (youtube_video) is in the same directory as the script, or provide the correct path.
This application is a simple command-line interface for managing YouTube video entries in a SQLite database.