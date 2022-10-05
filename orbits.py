# Import InfluxDB and other needed Libraries
import influxdb_client 
from influxdb_client.client.write_api import SYNCHRONOUS
import math
import time


# InfluxDB connection parameters. You will need to change these to match your InfluxDB settings.
bucket = "Orbits"
org = "CRC"
token = "wFJ2FDuaUkXIU0O6wlAJIF_YLF5rul540I61bO-EvurC3fHwpXu27-hxHvS8b43hTI-lJ1mVf8z9cka_SmLvVQ=="
url="http://localhost:8086"


# Create a connection to InfluxDB
client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

# Test the InfluxDB
testConnection = client.health()

if (testConnection.status == 'pass'):
    print('\n\nInfluxDB connection established!\n\n')
    
else:
    print(f'\n\nInfluxDB connection failed: {testConnection.message}\nCheck connection settings, verify InfluxDB is running and try again.\n\n')
    exit()
    
# Create Write Client    
write_api = client.write_api(write_options=SYNCHRONOUS)

# Latitude and Longitude of Vandenberg SFB
# 34.7420° N, 120.5724° W
lat0 = 34.7420 * math.pi / 180
lon0 = 120.5724 * math.pi / 180

restTime = 1 #second
orbitTime = 7200 #seconds (2 hours)
radPerStep = 2 * math.pi / orbitTime
step = lon0

while(1):
    
    while(step <= (2*math.pi)):
        latRad = lat0 * math.sin(step)
        latDeg = latRad * 180 / math.pi
    
        if(step <= math.pi):
            lonRad = step
        else:
            lonRad = -2*math.pi + step
        
        lonDeg= lonRad * 180 / math.pi
        step += radPerStep
        influxdb_client.DateTimeLiteral
        
        latWrite = influxdb_client.Point("FLTA100").tag("launch_site", "Vandenberg").field("lat", latDeg)
        lonWrite = influxdb_client.Point("FLTA100").tag("launch_site", "Vandenberg").field("lon", lonDeg)
        write_api.write(bucket=bucket, org=org, record=latWrite)
        write_api.write(bucket=bucket, org=org, record=lonWrite)
        time.sleep(0.01)
        
    step = 0
    
