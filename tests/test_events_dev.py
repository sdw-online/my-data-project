import sys
import os
import pytest
import pandas as pd

# 0. Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from process_events import process_events



# 1. Unit Test: Check if the events file is readable
def test_read_events_file():
    df = pd.read_csv('data/events.csv')
    assert not df.empty, ">>> events.csv should not be empty <<<"



# 2. Integration Test: Verify event summary generation
def test_event_summary():
    process_events('data/events.csv')
    summary_df = pd.read_csv('data/event_summary.csv')
    assert 'EventType' in summary_df.columns, ">>> 'EventType' column missing <<<"
    assert 'EventCount' in summary_df.columns, ">>> 'EventCount' column missing <<<"
