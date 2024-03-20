import pandas as pd
import sys
import re
import iperf3
from datetime import datetimetime

def run_iperf_test(server_ip, port, duration=15, num_streams=5, bandwidth='5M'):
    client = iperf3.Client()
    client.server_hostname = server_ip
    client.port = port
    client.duration = duration
    client.num_streams = num_streams
    client.bandwidth = bandwidth

    try:
        result = client.run()
        return result

    except Exception as e:
        print(f"Error occurred: {e}")
        return None

    finally:
        client.close()

server_ip = 'ec2-3-137-185-54.us-east-2.compute.amazonaws.com'  # Change this to the IP address of your iperf3 server
port = 32127
data = run_iperf_test(server_ip, port)
now = datetime.now()
location = grand-rapids
formatted_now = now.strftime("%Y-%m-%d_%H-%M-%S")

# Define a regex pattern to match the lines with results
pattern = re.compile(r'\[\s*(\S+)\]\s+(\d+\.\d+-\d+\.\d+)\s+sec\s+(\d+\.?\d*\sK?M?G?Bytes)\s+(\d+\.?\d*\s<?\d*\sK?M?G?bits/sec)(?:\s+(\d+))?\s+(sender|receiver)')


# Prepare lists to hold parsed data
location, times, stream_ids, intervals, transfers, bandwidths = [], [], [], [], [], []

# Parse each line
for line in data:
    match = re.search(pattern, line)
    if match:
        stream_ids.append(match.group(1))
        intervals.append(match.group(2))
        transfers.append(match.group(3))
        bandwidths.append(match.group(4))
        location.append(location)
        times.append(formatted_now)
# Create a DataFrame
df = pd.DataFrame({
    "Times": times,
    "Location": location,
    "Stream ID": stream_ids,
    "Interval": intervals,
    "Transfer": transfers,
    "Bandwidth": bandwidths
})
print(df)
# Save DataFrame to a CSV file
output_file = 'parsed_data.csv'
df.to_csv(output_file, index=False)
print(f"DataFrame saved to {output_file}")
