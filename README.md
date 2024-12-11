# kobo-export-ui

A simple Python script to generate exports within specific dates or any fields available in the submissions that will appear in your account under Data > Download. This script minimizes the export size and ensures the server does not timeout before the export is processed.

## Instructions

1. **Clone the repository or download the python file**

3. **Replace the necessary information in the script**:

Replace [kpi-url] with your server's URL.
Replace [asset_uid] with your asset's UID.
Replace [your_token_goes_here] with your API key.
Update the start date and time and end date and time as needed.
You can also configure the payload to reflect the settings in KPI:

<img width="802" alt="image" src="https://github.com/user-attachments/assets/2339d392-0f86-4536-882c-1f7096395e37" />

3. **Running the Script**:

    ```bash
    python export_ui.py
    ```

3. **Retrieve the Export**:

After running the script, you will find the export available under the Export section in your account:
<img width="1122" alt="image" src="https://github.com/user-attachments/assets/c1d68ba7-8aa9-4103-8e38-611ca6dcbed2" />

