import os
from io import StringIO
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import time
import schedule
import smtplib
from email.message import EmailMessage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename

load_dotenv()

key = os.getenv("FILE_ENCRPTION_KEY")
if key is None:
    key = Fernet.generate_key()
    with open(".env", "a") as env_file:
        env_file.write(f"\nFILE_ENCRPTION_KEY={key.decode()}\n")

# Defing paths to poll for incident data files
wd = 'C:/Users/a0p063p/Desktop/Ascend- Product Engineering/CapStone Project'
os.chdir(wd)
source_paths = [f'{wd}/Input/Source1', f'{wd}/Input/Source2', f'{wd}/Input/Source3']
output_path = f'{wd}/Output'

###################################
# Defining functions for encryption
###################################
# Encryption object with 
cipher_suite = Fernet(key)

# Function to encrypt data
def encrypt(data):
    return cipher_suite.encrypt(data.encode())

# # Function to decrypt data
def decrypt(encrypted_data):
    return cipher_suite.decrypt(encrypted_data).decode()

##############################################
# Defining Email Functions (GMAIL and Outlook)
##############################################
# Function to send email via GMAIL
def send_email_gmail(subject, body, receiver, attachment= None):
    # Set up email details
    sender = os.getenv("gmail_sender")
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver
    # msg.set_content(body)
    msg.set_content(body,subtype='html')
    # msg.attach(MIMEText(body, 'plain'))
    
    if attachment:
        # Add fiile attachments to the email
        for f in attachment:
            with open(f, 'rb') as content_file:
                content = content_file.read()
                msg.add_attachment(content, maintype='application', filename=f)
    
    try:
        # Connect to SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
            smtp.starttls()  # Enable TLS encryption
            smtp.login(sender, os.getenv('gmail_app_password'))  # Login to SMTP server
            smtp.send_message(msg)
            # smtp.sendmail(msg)
            smtp.quit()
        print(f'Email sent successfully! ({subject})')
    except Exception as e:
        print(f'Failed to send email (Subject: {subject}). Error: {e}')
    
    # send_email_gmail("TEST", "Test Body\nNext Line", "cool.cool.atul@gmail.com", sender_email, smtp_server , "587", sender_email, sender_password)

# Function to send email via OUTLOOK
def send_email_outlook(subject, body , receiver , attachment= None):
    # Set up email details
    sender = os.getenv("outlook_sender")
    smtp_server = "smtp.wal-mart.com"
    smtp_port = 25
    
    # Create message object
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    
    # Attach body to the message
    msg.attach(MIMEText(body, "html"))
    
    if attachment:
        # Add fiile attachments to the email
        for f in attachment:
            with open(f, "rb") as fil:
                part = MIMEApplication(fil.read(),Name=basename(f))
            # After the file is closed
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
            msg.attach(part)

    try:
        # Connect to SMTP server and send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.sendmail(sender, receiver, msg.as_string())
            server.quit()
        print(f'Email sent successfully! ({subject})')
    except Exception as e:
        print(f'Failed to send email (Subject: {subject}). Error: {e}')

# DateTime handler function
def convertto_date(date_str):
    try:
        return datetime.strptime(date_str, "%m/%d/%Y %H:%M")
    except:
        try:
            return datetime.strptime(date_str, "%d/%m/%Y %H:%M")
        except:    
            try:
                return datetime.strptime(date_str,"%d-%m-%Y %H:%M")
            except:
                try:
                    return datetime.strptime(date_str,"%m-%d-%Y %H:%M")
                except:
                    return date_str

# Bold Dataframe Columns
def bold_df(df,columns):
    # return df.style.set_properties(subset=columns,**{'font-weight':'bold'})
    for column in columns:
        print(column)
        df[column] = [f'<b>{x}</b>' for x in df[column]]
    return df

#######################################################
# Function to check for the existence of incident files
#######################################################
def check_for_incident_files():
    print("Validating Source Paths")
    files_found = []
    for path in source_paths:
        try:
            files = os.listdir(path)
            print(f"Found : {path}",end=None)
            for file in files:
                if file.endswith('.csv') or file.endswith('.xlsx'):
                    print(f"        {os.path.join(path, file)}")
                    files_found.append(os.path.join(path, file))
        except Exception as e:
            print(e)
            
    return files_found

####################################
# Function to process incident files
####################################
def process_incident_files(incident_files):
    # Create an empty list to store DataFrames
    data_frames = []
    
    print("\nProcessing Incident Files (Source)\n")
    
    # Reading all Incident files
    for file in incident_files:
        # Read CSV or Excel file using pandas
        if 'csv' in file:
            df = pd.read_csv(file, low_memory=False)
        elif 'xls' in file:
            df = pd.read_excel(file, low_memory=False)
        else:
            continue
        data_frames.append(df)
    
    # Continue if reading files was successful
    if len(data_frames) > 0:
        merged_df = pd.concat(data_frames, ignore_index=True).dropna().drop_duplicates(subset='number')
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
        
        # Exporting merged data to a local working file 
        merged_df.to_csv(f'{output_path}/merged_data.csv', index=False)
        
        # Segregate data into 5 output files based on priority
        for priority, group in merged_df.groupby('priority_label'):
            try:
                # file_name = f'{output_path}/incident_priority_{priority}.csv'
                file_name = f'{output_path}/incident_priority_{priority}.bin'
                if os.path.exists(file_name):
                    os.remove(file_name)
                
                # group.to_csv(file_name,index=False)
                csv = group.to_csv(index=False)
                encrypted_csv= encrypt(csv)
                
                with open(file_name, "wb") as file:
                    file.write(encrypted_csv)
                print("File created: ",file_name, " [Encrypted]")
            except:
                continue
    else:
        print("Could not read from source files. Aborting!")
        exit()

##########################################
# Function to handle file absence scenario
##########################################
def handle_file_absence():
    datetime_now = datetime.now()
    print(f"\nIncident files were not found during the scheduled polling at {datetime_now}. Retrying in 1 hour.")
    
    count = 1
    # Notify Process Manager about missing files
    # send_email_gmail(f"Incident File Not Found (Attempt {count})", f"Incident files were not found during the scheduled polling at {datetime_now}. Retrying in 1 hour.","cool.cool.atul@gmail.com")
    send_email_outlook(f"Incident File Not Found (Attempt {count})", f"Incident files were not found during the scheduled polling at {datetime_now}. Retrying in 1 hour.","atul.pahlazani@walmart.com")
    
    incident_files = None

    while not incident_files and count < 3:
        count+=1    # increment count by 1
        # Wait for an hour before retrying
        # time.sleep(3600)  # 1 hour
        time.sleep(5)  # 5 seconds, for demo purpose
        print(f"\nAttempt No. {count}")
        incident_files = check_for_incident_files()     # Retrying check for incident files in source paths
    
    return incident_files

# Function for generating summaries and insights
def generate_summaries_and_insights():
    
    # Create resolver performance summary and send mail notification
    summary_data = calculate_resolver_performance()
    
    # Preparing graphical representation of summary_data using "matplotlib"
    
    # plt.ion()   # Enable interactive mode, which shows / updates the figure after every plotting command, so that calling show() is not necessary
    plt.bar(summary_data['inc_summary']['Priority'],summary_data['inc_summary']['Resolved_INCs'])
    plt.title('Distribution of Incident Priorities')
    plt.xlabel('PRIORITY')
    plt.ylabel('Count') 
    plt.savefig(f"{output_path}/inc_prioritwise.jpg",format='jpg')
    # plt.show()
    
    for i, group in summary_data['top5_resolvers'].groupby('Priority'): 
        fig,ax = plt.subplots()   
        ax.set_title(f"Top 5 Resolvers {i}")
        group[['Name','INC_Resolved']].plot(kind='bar', x='Name', y='INC_Resolved', ax=ax, color='green')
        fig.savefig(f"{output_path}/{i}_top5_resolvers.jpg",format='jpg')
    
    for i, group in summary_data['top5_resolvers_holiday'].groupby('Priority'): 
        fig,ax = plt.subplots()   
        ax.set_title(f"Top 5 Resolvers {i}")
        group[['Name','INC_Resolved']].plot(kind='bar', x='Name', y='INC_Resolved', ax=ax, color='green')
        fig.savefig(f"{output_path}/{i}_top5_resolvers_holiday.jpg",format='jpg')
    
    for i, group in summary_data['inc_exceed_sla'].groupby('priority_label'): 
        fig,ax = plt.subplots()   
        ax.set_title(f"Top 5 Incidents exceeded SLA {i}")
        group[['number','ttr_hrs']].plot(kind='bar', x='number', y='ttr_hrs', ax=ax, color='green')
        fig.savefig(f"{output_path}/{i}_top5_inc_exceeded_sla.jpg",format='jpg')
    
    
    # Preparing summary and insights to be sent as HTML Body via Email
    
    top5_resolvers = "<h3>Top 5 Resolvers</h3>"
    for p, group in summary_data['top5_resolvers'].groupby('Priority'):
        top5_resolvers += f"<br><h4>Priority: {p}</h4>"
        top5_resolvers += group.to_html(index=False)
    
    top5_resolvers_holiday = "<h3>Top 5 Resolvers during Holiday Season</h3>"
    for p, group in summary_data['top5_resolvers_holiday'].groupby('Priority'):
        top5_resolvers_holiday += f"<br><h4>Priority: {p}</h4>"
        top5_resolvers_holiday += group.to_html(index=False)
        
    inc_exceed_sla = "<h3>Top 5 Incidents exceeded SLA</h3>"
    for p, group in summary_data['inc_exceed_sla'].groupby('priority_label'):
        inc_exceed_sla += f"<br><h4>Priority: {p}</h4>"
        inc_exceed_sla += group.to_html(index=False)
        
    resolution_summary = "<h3>Resolver Performance Summary</h3>"
    for p, group in summary_data['resolution_summary'].groupby('Priority'):
        resolution_summary += f"<br><h4>Priority: {p}</h4>"
        resolution_summary += group.to_html(index=False)
    
    
    summary = {
        "top5_resolvers" : top5_resolvers ,
        "top5_resolvers_holiday" : top5_resolvers_holiday,
        "inc_exceed_sla" : inc_exceed_sla,
        "inc_summary" : f"<h3>Incident Summary</h3><br><br>{summary_data['inc_summary'].to_html(index=False)}",
        "resolution_summary" : resolution_summary,
    }
    
    return summary

############################################
# Function to calculate resolver performance
############################################
def calculate_resolver_performance():
    # Calculate resolver performance metrics (e.g., resolution rates within SLA)
    # Aggregate data from the 5 output files and calculate resolver performance
    
    priority_files = os.listdir(output_path)
    
    sla_definitions = {
        'P1': 4,    # 4 Hours
        'P2': 12,   # 12 Hours
        'P3': 3 * 24,   # 3 days in hours  
        'P4': 7 * 24,   # 7 days in hours
        'P5': 14 * 24,   # 14 days in hours
    }
    
    holiday_dates= ['3/3/2016','6/4/2016','7/3/2016']
    
    resolution_summary = []
    incident_summary = pd.DataFrame(columns=['Priority','Active_INCs','Resolved_INCs','Resolvers_Count'])
    top5_inc_exceed_sla_arr= []
    top5_resolvers_arr= []
    top5_resolvers_holiday_arr=[]
    
    
    print("\nDecrypting and processing priority wise files \n")
    print("Resolution performance and summary:\n")
    
    # Iterating each Priority file to gather resolution performance and summary.
    for pfile in priority_files:   
        try:
            # Read the CSV file into Pandas Dataframe and remove duplicates
            # pdf = pd.read_csv(os.path.join(output_path, pfile), low_memory=False, index_col=False).drop_duplicates(subset='number')
            with open(os.path.join(output_path, pfile), "rb") as file:
                # incident_priority = os.path.splitext(os.path.basename(file.name))[0]
                encrypted_data_read = file.read()

            decrypted_data = decrypt(encrypted_data_read)
            pdf = pd.read_csv(StringIO(decrypted_data))
            
            # Filter out rows with empty/ invalid values at 'resolved_at' and 'opened_at' columns
            active_incs = pdf[(pdf['resolved_at'] =='?') | (pdf['resolved_at'] =='') | (pdf['opened_at'] =='?') | (pdf['opened_at'] =='')]
            pdf = pdf[(pdf['resolved_at'] !='?') & (pdf['resolved_at'] !='') & (pdf['opened_at'] !='?') & (pdf['opened_at'] !='')]            
            
            # Fetching all Resolvers list from the Dataframe
            resolvers = pdf.resolved_by.value_counts().index.tolist()
            
            resolver_summary= pd.DataFrame(columns=['Priority','Name','AVG_TTR','INC_Resolved','INC_MetSLA','INC_ExceedSLA','Resolution_Rate'])
            priority = pfile.split('_')[-1].split('.')[0]        
            sla_hours = sla_definitions[priority]
            
            # Collecting data for INC Summary      
            incident_summary = pd.concat([incident_summary, pd.DataFrame({'Priority':[priority],'Active_INCs':[len(active_incs)],'Resolved_INCs':[len(pdf)],'Resolvers_Count':[len(resolvers)]})], ignore_index=True)
            
            # Iterate through each INC to calculate resolution time and SLA breach
            for i, data in pdf.iterrows():
                inc_open_date = convertto_date(data.opened_at)
                inc_close_date = convertto_date(data.resolved_at)
                try:
                    inc_resolution_time = inc_close_date - inc_open_date
                    inc_resolution_hrs = round((inc_resolution_time).total_seconds()/3600,2)
                    
                    pdf.loc[i, 'ttr'] = inc_resolution_time
                    pdf.loc[i, 'ttr_hrs'] = inc_resolution_hrs
                    pdf.loc[i, 'sla_hrs'] = sla_hours
                    pdf.loc[i, 'sla_breached'] = inc_resolution_hrs > sla_hours    
                    pdf.loc[i, 'holiday'] = data.resolved_at.split(" ")[0] in holiday_dates         
                except Exception as e:
                    print(e)
            
            # Filtering out rows with negative resolution time (Data cleaning)
            pdf = pdf[(pdf['ttr_hrs'] > 0)]
                
            # Fetching Top 5 Incidents exceeded SLA
            top5_inc_exceed_sla = pdf[pdf['ttr_hrs'] > sla_hours].sort_values(by='ttr_hrs',ascending=False)[:5][['number','priority_label','resolved_by','opened_at','resolved_at','ttr','ttr_hrs','sla_hrs','sla_breached']]
            top5_inc_exceed_sla_arr.append(top5_inc_exceed_sla)
            
            # Fetching Top 5 Incident Resolvers
            top5_resolvers = resolvers[:5]
            
            # Fetching Top 5 Incident Resolvers
            resolvers_holiday = pdf[pdf['holiday'] == True].resolved_by.value_counts().index.tolist()
            top5_resolvers_holiday = resolvers_holiday[:5]
            
            print(f"{priority}")
            print(f"Top 5 resolvers : {', '.join(top5_resolvers)}")
            print(f"Top 5 Incidents (SLA Breached) : {', '.join(top5_inc_exceed_sla.number)}\n")
            
            # Procesng data of Top 5 resolvers sequentially
            for resolver in resolvers:
                try:
                    # Get resolver incident data where resolved_at is not empty
                    resolver_data = pdf[(pdf['resolved_by'] == resolver)]
                    
                    inc_exceed_sla = resolver_data[resolver_data['sla_breached']==True]
                    inc_met_sla = resolver_data[resolver_data['sla_breached']==False]
                    
                    # Calculating resolution rate ( ratio of the number of incidents resolved within SLA to the total number of incidents handled by the resolver)
                    resolver_rate = round(len(inc_met_sla) / len(resolver_data),2)
                    
                    # Calculating average resolution time 
                    avg_resolution_time = pd.to_timedelta(resolver_data['ttr']).mean()
                    
                    # Appending resolver data to Pandas Dataframe
                    resolver_summary_df = pd.DataFrame({'Priority':[priority],'Name':[resolver],'AVG_TTR':[avg_resolution_time],'INC_Resolved':[len(resolver_data)],'INC_MetSLA':[len(inc_met_sla)],'INC_ExceedSLA':[len(inc_exceed_sla)],'Resolution_Rate':[resolver_rate]})
                    resolver_summary = pd.concat([resolver_summary, resolver_summary_df], ignore_index=True)
                
                    if resolver in top5_resolvers:
                        top5_resolvers_arr.append(resolver_summary_df)
                    
                    if resolver in top5_resolvers_holiday:
                        top5_resolvers_holiday_arr.append(resolver_summary_df)
                except:
                    continue
            
            resolution_summary.append(resolver_summary.sort_values(by='Resolution_Rate',ascending=False))
        except Exception as e:
            # print(e)
            continue
    
    inc_summary = pd.concat([incident_summary, pd.DataFrame({'Priority':['Total'],'Active_INCs':[incident_summary.Active_INCs.sum()],'Resolved_INCs':[incident_summary.Resolved_INCs.sum()],'Resolvers_Count':[incident_summary.Resolvers_Count.sum()]})], ignore_index=True)
    top5_inc_exceed_sla_arr = pd.concat(top5_inc_exceed_sla_arr).dropna()
    resolution_summary = pd.concat(resolution_summary).dropna()
    top5_resolvers_arr = pd.concat(top5_resolvers_arr).dropna()
    top5_resolvers_holiday_arr =  pd.concat(top5_resolvers_holiday_arr).dropna()
    
    final_summary = {"inc_summary": inc_summary, "inc_exceed_sla": top5_inc_exceed_sla_arr, "resolution_summary" : resolution_summary, "top5_resolvers": top5_resolvers_arr, 'top5_resolvers_holiday' : top5_resolvers_holiday_arr}
    
    return final_summary

# Function to Delete Source Files
def delete_incident_files(incident_files):
    for file in incident_files:
        try:
            print(f"Removing File: {file}")
            os.remove(file)
        except OSError as e:
            print(e)

###############
# Main process
###############
def main_process():
    today = datetime.now()
    # Check if today is the first Monday of the month at 10 AM
    if (today.weekday() == 0 and 1 <= today.day <= 7 and today.hour == 10 and today.minute == 0) or True:
        incident_files = check_for_incident_files()
        if not incident_files:
            # Handle file absence scenario
            incident_files = handle_file_absence()
        
        if incident_files:
            # Process the incident files
            process_incident_files(incident_files)

            # Placeholder: Generate and collect summary data
            summary_data = generate_summaries_and_insights()
            
            top5_plots = []
            top5_plots_files = os.listdir(output_path)
            for file in top5_plots_files:
                if file.endswith('.jpg') and 'top5' in file:
                    top5_plots.append(os.path.join(output_path, file))
            
            # Send notification to Process Head with summary data
            # send_email_gmail("Top 5 Summary", f"{summary_data['top5_resolvers']}<br><br>{summary_data['inc_exceed_sla']}",os.getenv("gmail_receiver"))
            # send_email_gmail("INC Overview and Resolution Summary", f"{summary_data['inc_summary']}<br><br>{summary_data['resolution_summary']}",os.getenv("gmail_receiver"))
            
            send_email_outlook("Top 5 Summary", f"{summary_data['top5_resolvers']}<br><br>{summary_data['top5_resolvers_holiday']}<br><br>{summary_data['inc_exceed_sla']}",os.getenv("outlook_receiver"),top5_plots)
            send_email_outlook("INC Overview and Resolution Summary", f"{summary_data['inc_summary']}<br><br>{summary_data['resolution_summary']}",os.getenv("outlook_receiver"))
            # Delete incident files
            delete_incident_files(incident_files)
        else:
            print('\nIncident files were not found during the scheduled polling time (3 attempts with a gap of 1hour). Aborting the process!')
    else:
        print(f"Today is {today}, not 1st Monday of month at 10:00 AM. Aborting!!")


main_process()
# Schedule the main_process to run every minute for demonstration purposes
# schedule.every(30).seconds.do(main_process)

# # Run the scheduler
# while True:
#     schedule.run_pending()
#     time.sleep(1)
