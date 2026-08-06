import os
from scholarly import scholarly

# Replace with your Scholar ID
SCHOLAR_ID = "fTTCTdIAAAAJ"

def fetch_and_generate_svg():
    try:
        # Search author
        author = scholarly.search_author_id(SCHOLAR_ID)
        scholarly.fill(author, sections=['counts'])
        
        citations = author.get('citedby', 0)
        h_index = author.get('hindex', 0)
        i10_index = author.get('i10index', 0)

        # Build clean SVG Card
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

        with open("scholar-stats.svg", "w") as f:
            f.write(svg_content)
        print("Updated scholar-stats.svg successfully")

    except Exception as e:
        print(f"Error fetching Scholar data: {e}")

if __name__ == "__main__":
    fetch_and_generate_svg()