#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-14 09:24:06.958624

import re
import smtplib

def is_phishing_url(url):
    pattern = r"^(?:http|https)://\S+"
    return bool(re.match(pattern, url))

def send_email(recipient, subject, body):
    server = smtplib.SMTP("smtp.example.com")
    server.sendmail("no-reply@example.com", recipient, f"Subject: {subject}[9D[K
{subject}\n\n{body}")
    server.quit()

def detect_phishing(url):
    if not is_phishing_url(url):
        return False
    try:
        request = urllib.request.urlopen(url)
        response = request.read()
        soup = BeautifulSoup(response, "html.parser")
        if soup.title and soup.title.string == "Phishing Site":
            send_email("admin@example.com", "Possible Phishing Attack", f"U[3D[K
f"URL: {url}")
            return True
    except (URLError, ValueError):
        pass
    return False

if __name__ == "__main__":
    urls = ["http://www.phishingsite1.com", "https://phishingsite2.net"]
    for url in urls:
        if detect_phishing(url):
            print("Phishing attack detected!")