# Automate WhatsApp

This repository contains code to automate sending WhatsApp messages using Selenium WebDriver with Python.

## Getting Started

To get started with the project, follow these steps:

### Prerequisites

- Python 3.7 or higher
- Chrome web browser

### Installation

1. Clone the repository:

    ```shell
    git clone https://github.com/kamipakistan/AutomateWhatsapp.git
    ```   
2. Navigate to the project directory:
    ```shell
    cd AutomateWhatsapp
    ```
3. Install the required Python packages:
    ```shell
    pip install -r requirements.txt
    ```
4. Find your Chrome user profile folder. Refer to the following guide for instructions on how to find it: How to Find Your Chrome Profile Folder
    > Instructions for finding the Chrome user profile folder.
    > 
    > Visit: https://www.howtogeek.com/255653/how-to-find-your-chrome-profile-folder-on-windows-mac-and-linux/

5. Update the `CHROME_USER_PROFILE_PATH` variable in the [send_whatsapp_msg.py](send_whatsapp_msg.py) file with the path to your Chrome user profile folder.


### Usage
Open the main.py file and specify the phone number and message content in the phone_number and message variables.

Run the script:
```shell
python send_whatsapp_msg.py
```
This will open a Chrome browser window and automate sending the specified **`Message`** to the provided **`Phone Number`** on WhatsApp Web.

### Contributing
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
