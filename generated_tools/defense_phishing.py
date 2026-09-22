#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-22 05:42:21.146859

import re
import ssl

class PhishingDetector:
    def __init__(self, email_text):
        self.email_text = email_text

    def is_phishing(self):
        # Check for obvious phishing URLs
        phishing_urls = ['https://www.phishingwebsite.com', 'https://phishi[15D[K
'https://phishingwebsite.com']
        for url in phishing_urls:
            if url in self.email_text:
                return True

        # Check for suspicious URLs
        suspicious_urls = ['https://www.suspiciouswebsite.com', 'https://su[11D[K
'https://suspiciouswebsite.com']
        for url in suspicious_urls:
            if url in self.email_text:
                return True

        # Check for suspicious domain names
        suspicious_domain_names = ['suspiciouswebsite.com', 'phishingwebsit[15D[K
'phishingwebsite.com']
        for domain_name in suspicious_domain_names:
            if domain_name in self.email_text:
                return True

        # Check for suspicious email addresses
        suspicious_email_addresses = ['phishing@suspiciouswebsite.com', 'ph[3D[K
'phishing@phishingwebsite.com']
        for email_address in suspicious_email_addresses:
            if email_address in self.email_text:
                return True

        # Check for suspicious IP addresses
        suspicious_ip_addresses = ['1.2.3.4', '5.6.7.8']
        for ip_address in suspicious_ip_addresses:
            if ip_address in self.email_text:
                return True

        # Check for suspicious SSL certificates
        try:
            ssl.get_server_certificate(self.email_text)
            return False
        except ssl.SSLError:
            return True

    def mitigate(self):
        if self.is_phishing():
            print("This email is a phishing attack!")
        else:
            print("This email is legitimate.")

if __name__ == '__main__':
    email_text = input("Enter the email text: ")
    detector = PhishingDetector(email_text)
    detector.mitigate()