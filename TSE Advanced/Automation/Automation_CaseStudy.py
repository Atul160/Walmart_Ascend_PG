def getticketstate():
    import pandas as pd

    incdata= pd.read_csv("Automation_dataset.csv")

    active_incs= incdata[incdata['incident_state']=="Active"]
    completed_incs= incdata[incdata['incident_state'].isin(["Resolved","Closed"])]
    assigned_incs = incdata[~(incdata['assigned_to'].isin(["?",""])) & ~(incdata['incident_state'].isin(["Resolved","Closed"]))]
    pending_incs= incdata[incdata['incident_state'].str.contains("Awaiting")]
    unallocated_incs= incdata[(incdata['incident_state'].str.contains("New")) & (incdata['assigned_to'].isin(["?",""]))]

    print(f"\nTotal Incidents: {len(incdata)}\n\nActive: {len(active_incs)}\nCompleted: {len(completed_incs)}\nPending: {len(pending_incs)}\nAssigned: {len(assigned_incs)}\nUnallocated: {len(unallocated_incs)}\n")

getticketstate()