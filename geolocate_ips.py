import geoip2.database
import argparse
import os
import re

# Path to your GeoLite2 database.
db_path = 'GeoLite2-City_20240220/GeoLite2-City.mmdb'

# Function to geolocate an IP address using the GeoLite2 database.
def geolocate_ip(ip_address):
    try:
        with geoip2.database.Reader(db_path) as reader:
            response = reader.city(ip_address)
            country = response.country.name if response.country.name else "Unknown Country"
            city = response.city.name if response.city.name else "Unknown City"
            location = f"{city}, {country}" if city != "Unknown City" else country
            return location
    except Exception as e:
        return "Geolocation failed"

# Function to validate input file format.
def validate_ip_file(input_file):
    ip_pattern = re.compile(r"^(?:\d{1,3}\.){3}\d{1,3}|(?:[a-fA-F0-9:]+)\|\d{2}-\d{2}-\d{4}\|\d{2}:\d{2}:\d{2}$")
    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            if not ip_pattern.match(line):
                print(f"Invalid format: {line}")
                return False
    return True

# Function to process the input file.
def process_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            ip_address = line.split('|')[0].strip()
            location = geolocate_ip(ip_address)
            outfile.write(f"{line.strip()} -> {location}\n")
    print(f"Geolocation results saved to {output_file}")

# Main function to handle command-line arguments and file processing.
def main():
    parser = argparse.ArgumentParser(description="Geolocate IP addresses from a file.")
    parser.add_argument('input_file', help="Path to the input file containing IP addresses.")
    parser.add_argument('output_file', help="Path to the output file to save the geolocation results.")
    args = parser.parse_args()

    # Check if input file exists
    if not os.path.exists(args.input_file):
        print(f"Input file {args.input_file} does not exist.")
        return

    # Validate input file format
    if not validate_ip_file(args.input_file):
        print("Input file is not in the expected format.")
        return

    # Process the file and save results to output file
    process_file(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
