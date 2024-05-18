import argparse
import sys
import threading
from urllib.parse import urlparse
from queue import Queue
from tqdm import tqdm

#Ensure the URL has a scheme (http/https), defaulting to http
def ensure_http_scheme(url):
    if not urlparse(url).scheme:
        return "http://" + url
    return url
    
#Function to request URLs from the queue and process responses
def request_url(queue, base_url, timeout, success_codes, headers, output_file, progress_bar, results):
    while not queue.empty():
        word = queue.get()
        url = base_url + word.strip()
        try:
            response = requests.get(url, timeout=timeout, headers=headers)
            if response.status_code in success_codes:
                # Store successful results
                results.append((url, response.status_code))
                # Display progress with tqdm
                tqdm.write(f"[+] Found: [{url}] (Status: {response.status_code})")
                if output_file:
                    # Save results to file if specified
                    with open(output_file, 'a') as f:
                        f.write(f"[+] [{url}] (Status: {response.status_code})\n")
        except requests.exceptions.RequestException:
            pass  # Ignore all types of request exceptions
        finally:
            # Mark task as done and update progress
            queue.task_done()
            progress_bar.update(1)
# Perform directory brute-forcing on the given base URL.
def brute_force_directories(base_url, wordlist, timeout, success_codes, headers, threads, output_file):
    base_url = ensure_http_scheme(base_url)
    if not base_url.endswith('/'):
        base_url += '/'

    queue = Queue()
    for word in wordlist:
        # Add directory paths to queue, ignoring comments and empty lines
        if word.strip() and not word.strip().startswith("#"):
            queue.put(word)

    progress_bar = tqdm(total=queue.qsize(), desc="Progress", unit="req")
    results = []

    # Start worker threads to request URLs
    for _ in range(threads):
        thread = threading.Thread(target=request_url, args=(queue, base_url, timeout, success_codes, headers, output_file, progress_bar, results))
        thread.start()

    # Wait for all threads to finish
    queue.join()
    # Close progress bar
    progress_bar.close()

    if not results:
        print("No results found")

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Brute force directory paths on a given base URL.")
    parser.add_argument("base_url", help="The base URL to brute force directories on.")
    parser.add_argument("--timeout", type=float, default=1.0, help="Request timeout in seconds (default: 1.0).")
    parser.add_argument("--wordlist", type=str, help="Path to a file containing the wordlist. If not provided, reads from stdin.")
    parser.add_argument("--success-codes", type=int, nargs='+', default=[200], help="HTTP status codes to consider as success (default: [200]).")
    parser.add_argument("--headers", type=str, nargs='*', help="Custom headers for the requests (e.g., 'User-Agent: custom').")
    parser.add_argument("--threads", type=int, default=5, help="Number of concurrent threads (default: 5).")
    parser.add_argument("--output", type=str, help="File to save successful results.")

    args = parser.parse_args()

    if args.headers:
        headers = dict(header.split(':', 1) for header in args.headers)
    else:
        headers = {}

    if args.wordlist:
        with open(args.wordlist, 'r', encoding='utf-8') as f:
            wordlist = [line.strip() for line in f]
    else:
        wordlist = [line.strip() for line in sys.stdin]

    brute_force_directories(args.base_url, wordlist, args.timeout, args.success_codes, headers, args.threads, args.output)

if __name__ == "__main__":
    main()
