import json
import urllib.request

# Replace with your Semantic Scholar Author ID
AUTHOR_ID = "fTTCTdIAAAAJ"

def fetch_and_generate_svg():
    url = f"https://api.semanticscholar.org/graph/v1/author/{AUTHOR_ID}?fields=name,citationCount,hIndex,paperCount"
    
    req = urllib.request.Request(url, headers={'User-Agent': 'GitHub-Action-Stats'})
    
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            
            citations = data.get('citationCount', 0)
            h_index = data.get('hIndex', 0)
            papers = data.get('paperCount', 0)

            # Build clean SVG Card
            svg_content = f'''<svg fill="none" width="400" height="120" xmlns="http://www.w3.org/2000/svg">
  <style>
    .header {{ font: 600 16px 'Segoe UI', Roboto, sans-serif; fill: #4285F4; }}
    .stat-label {{ font: 400 13px 'Segoe UI', Roboto, sans-serif; fill: #8b949e; }}
    .stat-val {{ font: 600 18px 'Segoe UI', Roboto, sans-serif; fill: #58a6ff; }}
    .bg {{ fill: #0d1117; stroke: #30363d; stroke-width: 1px; rx: 8px; }}
  </style>
  <rect width="100%" height="100%" class="bg" />
  <text x="20" y="35" class="header">🎓 Academic & Scholar Stats</text>
  
  <text x="20" y="70" class="stat-label">Citations</text>
  <text x="20" y="95" class="stat-val">{citations}</text>
  
  <text x="160" y="70" class="stat-label">h-index</text>
  <text x="160" y="95" class="stat-val">{h_index}</text>
  
  <text x="280" y="70" class="stat-label">Publications</text>
  <text x="280" y="95" class="stat-val">{papers}</text>
</svg>'''

            with open("scholar-stats.svg", "w") as f:
                f.write(svg_content)
            print("Successfully created scholar-stats.svg")

    except Exception as e:
        print(f"Failed to fetch stats: {e}")
        # Create a fallback SVG so git add never throws code 128
        fallback_svg = '''<svg fill="none" width="400" height="120" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#0d1117" rx="8"/>
  <text x="20" y="60" fill="#8b949e" font-family="sans-serif">Scholar Stats Unavailable</text>
</svg>'''
        with open("scholar-stats.svg", "w") as f:
            f.write(fallback_svg)

if __name__ == "__main__":
    fetch_and_generate_svg()