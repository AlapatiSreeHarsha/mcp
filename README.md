# mcp
Here’s a detailed `README.md` template specifically tailored for your GitHub repository:

---

# **MCP Server for Posting Tweets from Google Sheets**

## **Description**
This project is an implementation of an MCP (Model Context Protocol) server that automates the process of posting tweets from a Google Sheet onto X (formerly Twitter) without using the Twitter API. The server integrates with Claude and uses Python for its implementation, leveraging web automation to accomplish the task.

---

## **Features**
1. **Core Functionality**:
   - Reads tweet content from a Google Sheet.
   - Posts tweets on X through web automation using Selenium.
   
2. **Bonus Features**:
   - Tracks and updates the Google Sheet with the status of each tweet (e.g., "Posted").
   - Allows scheduling tweets based on a timestamp column.

---

## **Technologies Used**
- **Language**: Python
- **Libraries**:
  - `selenium` (Web automation)
  - `gspread` (Google Sheets integration)
  - `oauth2client` (Authentication for Google Sheets API)
  - `chromedriver-autoinstaller` (ChromeDriver setup)
  - `pandas` (Optional: CSV handling)
- **Protocol**: [Claude MCP](https://www.claudedesktop.com/)

---

## **Setup Instructions**

### **1. Prerequisites**
- Python 3.10 or above installed on your system.
- A Google Cloud Project with the **Google Sheets API** and **Google Drive API** enabled.
- Service account credentials JSON file downloaded from Google Cloud Console.

### **2. Installation**
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install required Python libraries:
   ```bash
   pip install selenium gspread oauth2client chromedriver-autoinstaller pandas
   ```

3. Place your `credentials.json` file (Google API credentials) in the project directory.

---

## **Usage**
1. **Update Google Sheet Information**:
   - Ensure the Google Sheet is shared with the service account email found in your `credentials.json`.
   - Format the Google Sheet as follows:
     | Tweet Content   | Timestamp (Optional)   |
     |-----------------|-------------------------|
     | Example Tweet 1 | 2024-12-06 10:30:00    |
     | Example Tweet 2 |                         |

2. **Run the Server**:
   ```bash
   python mcp.py
   ```

3. **Automation Process**:
   - The script reads tweets from the Google Sheet.
   - Posts them on X using Selenium.
   - Updates the Google Sheet with the status after posting.

4. **Scheduling** (Optional):
   - If a timestamp is provided, the script will schedule the tweet to be posted at the specified time.

---

## **Demo**
- Watch the project in action in this [demo video](#).
- The video demonstrates:
  1. Reading tweets from the Google Sheet.
  2. Posting on X using web automation.
  3. Updating the Google Sheet with the status.




