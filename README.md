# Dir-Brute

The **dirbrute.py** script is a command-line tool designed to perform directory brute-force attacks on a specified base URL. It takes a list of potential directory paths as input and checks each one against the target URL to determine if it exists. This tool can be invaluable for discovering hidden directories or files on web servers.

## Features

- **Multi-threaded Scanning:** Utilizes multiple threads for simultaneous directory brute-forcing, speeding up the scanning process.
- **Customizable Timeout:** Allows you to set a custom timeout for controlling request duration, ensuring efficient scanning.
- **Custom Headers:** Option to specify custom HTTP headers for requests, enabling flexibility in request customization.
- **Multiple Success Codes:** Ability to specify multiple HTTP status codes to consider as success, accommodating various server configurations.
- **Output Results:** Option to save successful results to a file for further analysis and reporting.

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/dev-angelist/Dir-Brute.git
    ```

2. Navigate to the directory:

    ```bash
    cd Dir-Brute
    ```

## Usage

```bash
usage: dirbrute.py [-h] [--timeout TIMEOUT]
                   [--success-codes SUCCESS_CODES [SUCCESS_CODES ...]]
                   [--headers HEADERS [HEADERS ...]] [--threads THREADS]
                   [--output OUTPUT]
                   base_url wordlist

Brute force directory paths on a given base URL.

positional arguments:
  base_url              The base URL to brute force directories on.
  wordlist              Path to a file containing the wordlist.

optional arguments:
  -h, --help            show this help message and exit
  --timeout TIMEOUT     Request timeout in seconds (default: 1.0).
  --success-codes SUCCESS_CODES [SUCCESS_CODES ...]
                        HTTP status codes to consider as success (default: [200]).
  --headers HEADERS [HEADERS ...]
                        Custom headers for the requests (e.g., 'User-Agent: custom').
  --threads THREADS     Number of concurrent threads (default: 5).
  --output OUTPUT       File to save successful results.
```

### Additional Resources:

- A comprehensive list of directory paths, is just present cloning current repository into path /directories_list
- For an extensive collection of wordlists, visit [kkrypt0nn/wordlists](https://github.com/kkrypt0nn/wordlists).

## Contributing

If you wish to contribute to this project, follow these steps:

1. Fork this repository.
2. Create a branch for your contribution (`git checkout -b feature/your-contribution`).
3. Commit your changes (`git commit -am 'Add feature X'`).
4. Push your branch (`git push origin feature/your-contribution`).
5. Open a pull request.

## Author

@dev-angelist ([GitHub profile](https://github.com/dev-angelist)) 


## Legal Disclaimer

Please note that conducting port scanning activities may be illegal in some jurisdictions without proper authorization. Before using this tool, ensure that you have the necessary permissions to perform scanning activities on the target network. Unauthorized port scanning can potentially violate laws and regulations related to computer security and privacy.

It is your responsibility to comply with all applicable laws and regulations in your jurisdiction. The author of this script does not condone or endorse any illegal or unauthorized use of this tool.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

--- 
