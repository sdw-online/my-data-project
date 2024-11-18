import pandas as pd

def process_events(filepath):
    df = pd.read_csv(filepath)

    # Summarize events by type
    event_summary = df.groupby('EventType').agg({'Description': 'count'}).reset_index()
    event_summary.columns = ['EventType', 'EventCount']

    # Save the summary report
    event_summary.to_csv('data/event_summary.csv', index=False)
    print("Event summary generated and saved.")
