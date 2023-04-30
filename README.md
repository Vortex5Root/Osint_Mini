# Osint_Mini_CLI Documentation

## Usage
This is a command-line tool for Open Source Intelligence (OSINT) gathering. The tool provides two options:
- `cmd_Intraface.py -full <Base_DNS>`: Generates a report with all vulnerabilities of the subdomains of a given base DNS.
- `cmd_Intraface.py -simple <sub_dns/dns>`: Generates a report with information about an unexplored subdomain or DNS.

## Class
### `run`
This class includes the following methods:

#### `Sub_DNS_Lookup(alvo)`
This method performs a DNS lookup using `Dns_Dumpter` to retrieve subdomains of a given base DNS.

##### Parameters
- `alvo`: a string representing the base DNS.

##### Returns
- a list of subdomains.

#### `Extenal_Nmap_Scan(subdns, alvo, speed=1)`
This method performs an external Nmap scan using `Nmap_API` to retrieve information about open ports.

##### Parameters
- `subdns`: a list of subdomains.
- `alvo`: a string representing the base DNS.
- `speed`: an integer representing the scanning speed (default is 1).

## Properties
### `cmd`
This class includes the following properties:

#### `at`
This property is an instance of `__arts__` from the `Arts` module.

#### `tool`
This property is an instance of `run` class.

## Example
```cmd_Intraface.py -full <Base_DNS>```

This generates a report with all vulnerabilities of the subdomains of a given base DNS.

```cmd_Intraface.py -simple <sub_dns/dns>```

This generates a report with information about an unexplored subdomain or DNS.
