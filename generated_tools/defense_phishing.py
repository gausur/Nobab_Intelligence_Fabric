#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-15 06:29:14.273474

import re
import smtplib

def is_phishing_url(url):
    if not re.match(r"^https?://", url):
        return False
    parsed = urlparse(url)
    if not parsed.hostname:
        return False
    hostname = parsed.hostname.lower()
    if "google" in hostname or "facebook" in hostname or "twitter" in hostn[5D[K
hostname:
        return True
    else:
        return False

def is_phishing_email(sender, subject):
    if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", se[2D[K
sender):
        return False
    if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", su[2D[K
subject):
        return False
    if "phishing" in subject.lower() or "fraudulent" in subject.lower():
        return True
    else:
        return False

def main(argv):
    parser = argparse.ArgumentParser(description="Detect and mitigate phish[5D[K
phishing attacks")
    parser.add_argument("--url", help="URL to check for phishing", required[8D[K
required=True)
    parser.add_argument("--email", help="Email address to check for phishin[7D[K
phishing", required=True)
    args = parser.parse_args(argv[1:])

    if is_phishing_url(args.url):
        print("Phishing URL detected!")
        return 1
    elif is_phishing_email(args.sender, args.subject):
        print("Phishing email detected!")
        return 1
    else:
        print("No phishing detected.")
        return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))