
# System-Design Reminder

This Python project is designed to send a daily reminder to read a random engineering blog from a curated list. The reminder is shown through a desktop notification, and the link to the blog is opened in the browser automatically.
## Features

- **Daily Blog Reminder**: Based on the current day, a unique blog URL from a list is selected and displayed.
- **Desktop Notification**: A notification is triggered with the title "Blog Reminder" and the blog URL.
- **Automatic Browser Launch**: After showing the notification, the project will automatically open the selected blog URL in the default web browser.
## Requirements

- **Python 3.x**
- **Plyer** (for notifications)
- **Webbrowser** (built-in Python library)
- **OS** (built-in Python library)
- **datetime** (built-in Python library)

```bash
pip install plyer
```
## Run Locally

- Save the Python script BlogReminder.pyw on your system.
- Run the script using:

```bash
  python "C:\path\to\BlogReminder.pyw"
```
- The script will execute, sending a desktop notification with the blog URL and opening it in your default web browser.

## Set Up Daily Task with Windows Task Scheduler:

To make the script run automatically every day, use **Windows Task Scheduler** to execute the script daily. Here's how to add the task:

### Step-by-Step Guide:

1. **Open Task Scheduler**:
   - Type "Task Scheduler" in the Windows search bar and open it.

2. **Create a New Task**:
   - In the Task Scheduler window, click on **Create Basic Task** in the right panel.

3. **Set Task Name and Trigger**:
   - Provide a name for the task (e.g., "Blog Reminder").
   - Choose "Daily" and set the time when you want the task to run (for example, you can set it to run at 9:00 AM daily).

4. **Action: Run the Script**:
   - Select **Start a Program** as the action.
   - In the "Program/script" field, browse to your **bash script** (e.g., `run_blog_reminder.bat`) that runs the Python file.

5. **Save the Task**:
   - Once the task is created, click **Finish**. The task will now run the Python script at the scheduled time, triggering the notification and opening the blog in the browser.

### Notes:
- The list of blogs is hardcoded into the script, and it picks a blog URL based on the day of the month.
- The notification and blog URL are displayed only once a day, depending on when the script is run.

## Authors

- [@ronitahuja](https://github.com/ronitahuja)

