import requests
import json
import os

# Step 1: Create a new directory for the project
project_dir = "CurelinkMealQueryProcessor"
os.makedirs(project_dir, exist_ok=True)

# Step 2: Navigate to the new directory
os.chdir(project_dir)

# Step 3: Download the JSON file from the provided URL
url = "https://clchatagentassessment.s3.ap-south-1.amazonaws.com/queries.json"
response = requests.get(url)

# Step 4: Load the JSON data from the response
if response.status_code == 200:
    queries = response.json()  # Parse the JSON content
    print("Downloaded and loaded the queries successfully!")
else:
    print(f"Failed to download the file. Status code: {response.status_code}")
    queries = []  # If the download fails, start with an empty list

# Step 5: Process each query
output = []
for query in queries:
    # Emulate the generation of a response (placeholder)
    generated_response = "This is a placeholder response for the meal picture."

    # Construct the output object
    output_item = {
        "ticket_id": query.get("chat_context", {}).get("ticket_id"),
        "latest_query": query.get("latest_query"),
        "generated_response": generated_response,
        "ideal_response": query.get("ideal_response")
    }

    # Append the output to the results list
    output.append(output_item)

# Step 6: Save the results in a JSON file
output_file = "output.json"
with open(output_file, "w") as f:
    json.dump(output, f, indent=4)

print(f"Generated responses saved in {output_file}")
