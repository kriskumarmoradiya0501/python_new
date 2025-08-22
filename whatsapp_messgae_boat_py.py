import pandas as pd
import pywhatkit as kit
import time

# Load the CSV file
df = pd.read_csv('D:/1.csv')  # Make sure '1.csv' is in the same directory or provide the full path

# Assuming the CSV has a column named 'contact' with the mobile numbers
contacts = df['contact'].tolist()

# Message to send
message = "Your common message here."

# Sending messages
for contact in contacts:
    # Send message using pywhatkit
    kit.sendwhatmsg(contact, message, 9, 2)  # This will open WhatsApp at 15:00 (3:00 PM), change as needed
    
    # Wait for 20 seconds before sending the next message
    time.sleep(20)