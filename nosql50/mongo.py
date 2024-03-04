from pymongo import MongoClient
from query import pipeline

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

# Execute aggregation pipeline
result = list(db.project.aggregate(pipeline))

# Expected results
expected_result = [
    {"project_id": 1, "average_experience_years": 2.0},
    {"project_id": 2, "average_experience_years": 2.5}
]

# Test the results
assert compare_results(expected_result, result), "Test failed: Results do not match expected"

print("Test passed: Results match expected")