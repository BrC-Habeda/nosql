from pymongo import MongoClient
import os

# Function to compare results
def compare_results(expected_results, actual_results):
    # Check if lengths are equal
    if len(expected_results) != len(actual_results):
        return False
    # Check if all elements are equal
    for expected, actual in zip(expected_results, actual_results):
        if expected != actual:
            return False
    return True

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['testdb']  # Replace 'testdb' with your actual database name

# Get all query files in the current directory
query_files = [file for file in os.listdir() if file.endswith('.js')]

# Iterate over each query file
for query_file in query_files:
    # Import the query pipeline and expected result from the file
    query_module = __import__(query_file[:-3])  # Remove '.js' extension
    pipeline = query_module.pipeline
    expected_result = query_module.expected_result
    
    # Execute aggregation pipeline
    result = list(db.project.aggregate(pipeline))
    
    # Test the results
    assert compare_results(expected_result, result), f"Test for {query_file} failed: Results do not match expected"

    print(f"Test for {query_file} passed: Results match expected")
