import sys
import os
import time
import pytest
import pandas as pd

# 0. Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from process_events import process_events


# 1. End-to-End Test: Validate the entire event processing flow
def test_end_to_end_event_processing():
    process_events('data/events.csv')
    summary_df = pd.read_csv('data/event_summary.csv')
    assert not summary_df.empty, ">>> event_summary.csv should not be empty <<<"



# 2. Performance Test: Check if event processing runs within acceptable time
def test_performance_event_processing():
    start_time = time.time()
    process_events('data/events.csv')
    end_time = time.time()
    assert (end_time - start_time) < 1, ">>> Event processing took too long <<<"
