'''
Unit Testing with pytest
Ensure robust data pipelines.
'''
import pytest

def preprocess_data(df):
    return df.dropna()

def test_preprocess_data():
    df = pd.DataFrame({'A': [1, None, 3]})
    result = preprocess_data(df)
    assert len(result) == 2


'''
Logging
Track pipeline execution.
'''

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_data(df):
    logger.info("Starting data processing")
    result = df.dropna()
    logger.info(f"Processed {len(result)} rows")
    return result