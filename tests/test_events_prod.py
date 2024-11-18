import sys
import os
import pytest
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from process_events import process_events

# -- A simple smoke test
def test_data_processing_in_prod():
    try:
        process_events('data/events.csv')
        summary_df = pd.read_csv('data/event_summary.csv')
        assert not summary_df.empty, ">>> event_summary.csv should not be empty <<<"
    except Exception as e:
        pytest.fail(f"Smoke test failed: {str(e)}")
