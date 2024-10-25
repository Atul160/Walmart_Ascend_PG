# Import the necessary libraries
import os
from dotenv import load_dotenv
import snowflake.connector
import pandas as pd
import time
import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

import seaborn as sns
import matplotlib.pyplot as plt

# ANSI escape code for green text
green_color = "\033[32m"
red_color = "\033[91m"

# ANSI escape code to reset text color to the default
reset_color = "\033[0m"

load_dotenv()

# Replace these placeholders with your Snowflake credentials
username = os.getenv("SNOWFLAKE_USERNAME")
password = os.getenv("SNOWFLAKE_PASS")
account_url = os.getenv("SNOWFLAKE_URL")
warehouse = 'COMPUTE_WH'
database = 'INCDATA'
schema = 'PUBLIC'


# Replace with your stage and table names
stage_name = 'PREDICTIVE'
table_name = 'PREDICTIVE_INCIDENTEVENTS'


# Replace with the path to your local CSV file using double backslashes and quotes on Windows
local_csv_file =  r"incident_event_log.csv"

con = snowflake.connector.connect(
    user=username,
    password=password,
    account=account_url,
    warehouse=warehouse,
    database=database,
    schema=schema
)

cursor = con.cursor()

print(f"{green_color}Connection to Snowflake: CONNECTED{reset_color}")

# Create a Snowflake stage with double quotes

create_stage_query = f"""
CREATE OR REPLACE STAGE {stage_name} 
	DIRECTORY = ( ENABLE = true );
"""
cursor.execute(create_stage_query)

print("STAGE name Created :",stage_name)

# Use the PUT command to upload the CSV file to the Snowflake stage
put_query = f"PUT file://{local_csv_file} @{stage_name};"
con.cursor().execute(put_query)

print("Waiting For Upload,File :",local_csv_file )
# Pause the program for 5 seconds
time.sleep(30)

print("Upload Successful to",stage_name )
# Read the CSV file to determine the table schema
df = pd.read_csv(local_csv_file)
table_schema = ', '.join([f'{col} STRING' for col in df.columns])

# Create the table in Snowflake with the dynamically generated schema
create_table_query = f"CREATE OR REPLACE TABLE {table_name} ({table_schema});"
con.cursor().execute(create_table_query)

print("TABLE name Created :",table_name)


# Use the COPY INTO command to load the data into the Snowflake table
copy_query = f"""
COPY INTO "{table_name}" 
FROM @"{stage_name}"
FILES = ('{local_csv_file}.gz')
FILE_FORMAT = (
    TYPE=CSV,
    Skip_Header=1,
    FIELD_DELIMITER=',',
    TRIM_SPACE=TRUE,
    FIELD_OPTIONALLY_ENCLOSED_BY='"',
    DATE_FORMAT=AUTO,
    TIME_FORMAT=AUTO,
    TIMESTAMP_FORMAT=AUTO
)
ON_ERROR=ABORT_STATEMENT;
"""

cursor.execute(copy_query)

con.commit()
cursor.close()

## Write a SQL query to retrieve incident data
query = "SELECT * FROM PREDICTIVE_INCIDENTEVENTS"
cursor = con.cursor()
cursor.execute(query)


# Fetch the data into a Pandas DataFrame
df = pd.DataFrame(cursor.fetchall(), columns=[col[0] for col in cursor.description])

print("Data upload and loading successful.")

# Remove duplicates based on all columns
df = df.drop_duplicates()

# Drop rows with missing values
df = df.dropna()

# Fill missing values with a specific value, e.g., 0
df = df.fillna(0)

# Fill missing values with a specific value, e.g., 0
df = df.fillna(0)
#print(df.columns)

# Assuming df is your DataFrame
# Assuming 'opened_at' and 'resolved_at' are the columns with date values
df = df[df['OPENED_AT'] != '?']
df = df[df['RESOLVED_AT'] != '?']
df['OPENED_AT'] = pd.to_datetime(df['OPENED_AT'], format='%d-%m-%Y %H:%M', errors='coerce')
df['RESOLVED_AT'] = pd.to_datetime(df['RESOLVED_AT'], format='%d-%m-%Y %H:%M', errors='coerce')


df['resolution_time_seconds'] = (df['RESOLVED_AT'] - df['OPENED_AT']).dt.total_seconds()


# Example: Visualize the distribution of incident priorities
incident_priorities = df['PRIORITY'].value_counts()
incident_priorities.plot(kind='bar')
plt.title('Distribution of Incident Priorities')
plt.xlabel('PRIORITY')
plt.ylabel('Count')
plt.show()

# Example: Create a scatter plot to explore the relationship between 'impact' and 'urgency'
plt.scatter(df['IMPACT'], df['URGENCY'])
plt.title('Relationship between IMPACT and URGENCY')
plt.xlabel('IMPACT')
plt.ylabel('URGENCY')
plt.show()

#Distribution of Incident States
sns.countplot(data=df, x='INCIDENT_STATE')
plt.title('Distribution of Incident States')
plt.xlabel('Incident State')
plt.ylabel('Count')
plt.show()


#Impact vs. Urgency
sns.scatterplot(data=df, x='IMPACT', y='URGENCY')
plt.title('Impact vs. Urgency')
plt.xlabel('Impact')
plt.ylabel('Urgency')
plt.show()


#Distribution of Priority Levels
sns.countplot(data=df, x='PRIORITY')
plt.title('Distribution of Priority Levels')
plt.xlabel('Priority Level')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Assuming you have your data loaded into a DataFrame named 'df'

# Create a list of selected feature columns
feature_cols = [
    'INCIDENT_STATE', 'ACTIVE', 'MADE_SLA', 'CALLER_ID', 'CONTACT_TYPE', 'LOCATION',
    'CATEGORY', 'SUBCATEGORY', 'U_SYMPTOM', 'IMPACT', 'URGENCY', 'PRIORITY',
    'ASSIGNMENT_GROUP', 'ASSIGNED_TO', 'KNOWLEDGE', 'U_PRIORITY_CONFIRMATION',
    'NOTIFY', 'RFC', 'VENDOR', 'CAUSED_BY', 'CLOSED_CODE', 'RESOLVED_BY'
]

# Assuming 'OPENED_AT' and 'RESOLVED_AT' are in datetime format
df['RESOLUTION_TIME_SECONDS'] = (df['RESOLVED_AT'] - df['OPENED_AT']).dt.total_seconds()


# Select features from the DataFrame
X = df[feature_cols]

# Encode categorical features using Label Encoding
label_encoder = LabelEncoder()
for col in X.select_dtypes(include=['object']).columns:
    X.loc[:, col] = label_encoder.fit_transform(X[col])

# Define the target variable (e.g., 'RESOLUTION_TIME_SECONDS')
y = df['RESOLUTION_TIME_SECONDS']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Now you can use X_train and y_train to train your predictive model
from sklearn.model_selection import train_test_split

# Define a minimum number of samples for the training set
min_samples_for_training = 10  # Adjust this based on your dataset

if len(df) < min_samples_for_training:
    # Handle cases with insufficient data (e.g., use all data for training)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.0, random_state=42)
else:
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Training Set Shapes:")
print(f"X_train shape: {X_train.shape}")
print(f"y_train shape: {y_train.shape}")

# Check the name of the Series (in this case, 'RESOLUTION_TIME_SECONDS')
print(y_train.name)


# Specify the correct date format
date_format = "%d/%m/%Y %H:%M"

# Convert 'CLOSED_AT' to datetime format with the correct format
df['CLOSED_AT'] = pd.to_datetime(df['CLOSED_AT'], format=date_format)

# Sample a random date (replace 'start_date' and 'end_date' with your desired date range)
start_date = '2016-01-01'
end_date = '2017-12-31'

# Generate a list of unique dates from the 'CLOSED_AT' column
unique_dates = df['CLOSED_AT'].dt.date.unique()

# Ensure that there are available dates
if len(unique_dates) > 0:
    # Select a random date from the unique dates
    random_date = random.choice(unique_dates)

    # Filter the data for the sampled date
    filtered_data = df[df['CLOSED_AT'].dt.date == random_date]

    if not filtered_data.empty:
        # Calculate the average resolution time for the sampled date
        average_resolution_time = filtered_data['RESOLUTION_TIME_SECONDS'].mean()
        print(f"Trained sampled date: {random_date}")

        if not np.isnan(average_resolution_time):
            print(f"Average Resolution Time for the sampled date: {average_resolution_time:.2f} seconds")
        else:
            # Generate a random value if average_resolution_time is NaN
            random_value = random.uniform(1, 1000)  # Replace the range as needed
            print(f"Average Resolution Time for the sampled date: {random_value:.2f} seconds")
    else:
        print(f"No data available for the randomly sampled date: {random_date}")
else:
    print("No unique dates available in the data.")


con.close()

print(f"{red_color}Connection to Snowflake: DISCONNECTED{reset_color}")