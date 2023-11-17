import os
import pandas as pd
import datetime
import schedule
import time
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

# Paths to poll for incident data files
# os.getcwd()
wd = 'C:/Users/a0p063p/Desktop/Ascend- Product Engineering/CapStone Project'
os.chdir(wd)
source_paths = [f'{wd}/Source1', f'{wd}/Source2', f'{wd}/Source3']

# Replace with your email configuration
smtp_server = 'smtp.yourserver.com'
sender_email = 'your_email@domain.com'
password=os.getenv("gmail_app_password")

# Function to send email
def send_email(subject, body, to_email, from_email, smtp_server, smtp_port, username, password):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    msg.set_content(body)
    try:
        # Connect to SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
            smtp.starttls()  # Enable TLS encryption
            smtp.login(username, password)  # Login to SMTP server
            smtp.send_message(msg)
        print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email. Error: {e}')

# send_email("TEST", "Test Body", "cool.cool.atul@gmail.com", "atulunique8892@gmail.com", "smtp.gmail.com", "587", "atulunique8892", "")

# Function to check for the existence of incident files
def check_for_incident_files():
    files_found = []
    for path in source_paths:
        files = os.listdir(path)
        for file in files:
            if file.endswith('.csv') or file.endswith('.xlsx'):
                files_found.append(os.path.join(path, file))
    return files_found

# Function to handle file absence scenario
def handle_file_absence():
    # Notify Process Manager about missing files
    notification_msg = "Incident files not found. Retrying in 1 hour."
    send_notification_to_manager(notification_msg)
    # Wait for an hour before retrying
    time.sleep(3600)  # 1 hour

# Function to process incident files
def process_incident_files(incident_files):
    # Placeholder functions for data processing and categorization
    
    # Create an empty list to store DataFrames
    data_frames = []

    for file in incident_files:
        # Example: Read CSV or Excel file using pandas
        df = pd.read_csv(file,low_memory=False)
        data_frames.append(df)
        
    merged_df = pd.concat(data_frames, ignore_index=True).dropna()
    
    # Categorize data based on priority definitions
    # Define priority definitions
    priority_definitions = {
        'P1': 'Critical',
        'P2': 'High',
        'P3': 'Moderate',
        'P4': 'Low',
        'P5': 'Very Low'
    }

    # Map priority definitions to create a new column 'Priority_Label'
    merged_df['Priority_Label'] = merged_df['priority_label'].map(priority_definitions)

    # Segregate data into 5 output files based on priority
    for priority, group in merged_df.groupby('priority_label'):
        file_name = f'incident_priority_{priority}.csv'
        group.to_csv(file_name, index=False)

    # Placeholder for generating summaries and insights
    generate_summaries_and_insights()

# Placeholder function for generating summaries and insights
def generate_summaries_and_insights():
    # Calculate various metrics as described (e.g., resolver performance, incidents exceeding SLA)

    # Example calculations:
    # Top 5 incident resolvers with their average time to resolve
    # Top 5 incident resolvers with their average time to resolve during holiday season
    # Top 5 incidents exceeding SLA

    # Create resolver performance summary and send mail notification
    resolver_summary = calculate_resolver_performance()
    # send_notification_to_process_head(resolver_summary)
    send_email("Resolver Performance Summary", f"Resolver Performance Summary:\n{resolver_summary}", "cool.cool.atul@gmail.com", "atulunique8892@gmail.com", "smtp.gmail.com", "587", "atulunique8892", password)

# Function to calculate resolver performance
def calculate_resolver_performance():
    # Calculate resolver performance metrics (e.g., resolution rates within SLA)
    # Aggregate data from the 5 output files and calculate resolver performance

    # Example calculation:
    # resolver_summary = {resolver_name: resolution_rate}

    return resolver_summary

# Function to notify the Process Manager if incident files are not found
def send_notification_to_manager():
    # Send an informational notification to the Process Manager
    msg = EmailMessage()
    msg['Subject'] = 'Incident File Not Found'
    msg['From'] = sender_email
    msg['To'] = 'process_manager@example.com'
    msg.set_content('Incident files were not found during the scheduled polling.')

    # Connect to SMTP server and send email
    with smtplib.SMTP(smtp_server, 587) as smtp:
        smtp.starttls()
        smtp.login('your_email@example.com', 'your_password')
        smtp.send_message(msg)

# Function to send email notification to Process Head
def send_notification_to_process_head(summary_data):
    msg = EmailMessage()
    msg['Subject'] = 'Resolver Performance Summary'
    msg['From'] = sender_email
    msg['To'] = 'process_head@example.com'

    # Craft the email body with the summary data
    email_body = "Resolver Performance Summary:\n"
    email_body += summary_data  # Include the actual summary data here

    msg.set_content(email_body)

    with smtplib.SMTP_SSL(smtp_server, 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, 'your_password')  # Replace with your email password
        smtp.send_message(msg)

# Function to handle the main process
def main_process():
    today = datetime.now()
    # Check if today is the first Monday of the month at 10 AM
    if today.weekday() == 0 and 1 <= today.day <= 7 and today.hour == 10 and today.minute == 0:
        incident_files = check_for_incident_files()
        if not incident_files:
            # Handle file absence scenario
            handle_file_absence()
        else:
            # Process the incident files
            process_incident_files(incident_files)
            # Placeholder: Generate and collect summary data
            summary_data = "Summary data for resolver performance."
            # Send notification to Process Head with summary data
            send_notification_to_process_head(summary_data)
    else:
        print(f"Today is {today}")

# Schedule the main_process to run every minute for demonstration purposes
schedule.every().minute.do(main_process)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
