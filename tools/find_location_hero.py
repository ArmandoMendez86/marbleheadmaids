#!/usr/bin/env python3
import re
import urllib.request

url = "https://madtownmaids.com/locations/sun-prairie"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")

for match in re.findall(r'(?:src|href|url)=["\']([^"\']+)["\']', html):
    if any(x in match.lower() for x in (".jpg", ".webp", ".png", "image", "hero", "location")):
        print(match)

for match in re.findall(r"background-image:\s*url\(([^)]+)\)", html):
    print("bg:", match)
