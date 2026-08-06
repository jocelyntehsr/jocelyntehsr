import re
import urllib.request

SCHOLAR_ID = "fTTCTdIAAAAJ"

def fetch_stats():
    url = f"https://scholar.google.com/citations?user={SCHOLAR_ID}&hl=en"
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            
            # Find citation counts table from HTML
            matches = re.findall(r'<td class="gsc_rsb_std">(\d+)</td>', html)
            
            citations = matches[0] if len(matches) > 0 else "N/A"
            h_index = matches[2] if len(matches) > 2 else "N/A"
            i10_index = matches[4] if len(matches) > 4 else "N/A"

            # Create SVG Card
            svg_content = f'''<svg fill="none" width="400" height="120" xmlns="http://www.w3.org/2000/svg">
  <style>
    .header {{ font: 600 16px 'Segoe UI', Roboto, sans-serif; fill: #4285F4; }}
    .stat-label {{ font: 400 13px 'Segoe UI', Roboto, sans-serif; fill: #8b949e; }}
    .stat-val {{ font: 600 18px 'Segoe UI', Roboto, sans-serif; fill: #58a6ff; }}
    .bg {{ fill: #0d1117; stroke: #30363d; stroke-width: 1px; rx: 8px; }}
  </style>
  <rect width="100%" height="100%" class="bg" />
  <text x="20" y="35" class="header">🎓 Google Scholar Stats</text>
  
  <text x="20" y="70" class="stat-label">Citations</text>
  <text x="20" y="95" class="stat-val">{citations}</text>
  
  <text x="160" y="70" class="stat-label">h-index</text>
  <text x="160" y="95" class="stat-val">{h_index}</text>
  
  <text x="280" y="70" class="stat-label">i10-index</text>
  <text x="280" y="95" class="stat-val">{i10_index}</text>
</svg>'''

            with open("scholar-stats.svg", "w", encoding="utf-8") as f:
                f.write(svg_content)
            print("Successfully updated scholar-stats.svg")

    except Exception as e:
        print(f"Error scraping stats: {e}")
        # Build SVG with direct values as fallback so build never fails
        svg_content = '''<svg fill="none" width="400" height="120" xmlns="http://www.w3.org/2000/svg">
  <style>
    .header { font: 600 16px 'Segoe UI', Roboto, sans-serif; fill: #4285F4; }
    .stat-label { font: 400 13px 'Segoe UI', Roboto, sans-serif; fill: #8b949e; }
    .stat-val { font: 600 18px 'Segoe UI', Roboto, sans-serif; fill: #58a6ff; }
    .bg { fill: #0d1117; stroke: #30363d; stroke-width: 1px; rx: 8px; }
  </style>
  <rect width="100%" height="100%" class="bg" />
  <text x="20" y="35" class="header">🎓 Google Scholar Stats</text>
  <text x="20" y="70" class="stat-label">Citations</text>
  <text x="20" y="95" class="stat-val">15</text>
  <text x="160" y="70" class="stat-label">h-index</text>
  <text x="160" y="95" class="stat-val">2</text>
  <text x="280" y="70" class="stat-label">Publications</text>
  <text x="280" y="95" class="stat-val">3</text>
</svg>'''
        with open("scholar-stats.svg", "w", encoding="utf-8") as f:
            f.write(svg_content)

if __name__ == "__main__":
    fetch_stats()