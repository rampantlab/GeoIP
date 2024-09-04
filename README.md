# GeoIP

This repository contains a Python script for geolocating IP addresses using the [GeoLite2 City](https://dev.maxmind.com/geoip/geolite2-free-geolocation-data) database from MaxMind. The script processes IP addresses and retrieves geographical information such as the city and country for each IP.

## Features

* Processes a list of IP addresses.
* Uses MaxMind's GeoLite2 City database for geolocation.
* Outputs the city and country of each IP address.

## Requirements

* Python 3.x
* The following Python libraries:
  * `geoip2`

You can install the required Python libraries using the following command:

```bash
pip install geoip2
```

## Usage

1. Ensure that you have the latest version of the GeoLite2 City database. You can download it from [MaxMind](https://dev.maxmind.com/geoip/geolite2-free-geolocation-data).
2. Update the path to the database in the script (`db_path` variable).
3. Input your list of IP addresses in the `ip_addresses` variable, ensuring each entry is separated by a newline.
4. Run the script:

```bash
python geolocate_ips.py
```

## Example

The script processes the following sample IP list:

```text
2001:0db8:85a3:0000:0000:8a2e:0370:7334|01-07-2023|19:48:48
2607:f8b0:4005:080b:0000:0000:0000:200e|03-17-2024|11:28:23
2a03:2880:f10d:83:face:b00c:0:25de|12-05-2024|07:45:01
192.158.1.38|01-07-2023|11:57:59
45.67.23.101|03-05-2024|01:50:31
172.217.16.46|04-18-2024|10:24:27
```

For each IP, it will attempt to retrieve the corresponding city and country.

## Notes

* Remember to **download the latest version** of the GeoLite2 City database from MaxMind and update the `db_path` accordingly.
* If geolocation fails for an IP, the script will return `Geolocation failed`.

## License

This project is licensed under the MIT License.
