import requests
import plotly.express as px

# Make an API call and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process overall results.
response_dict = r.json()
print(f"Complete Results: {not response_dict['incomplete_results']}")

# Process repository information.
repo_dicts = response_dict['items']
repo_links, stars, hovered_texts = [], [], []
for repo_dict in repo_dicts:
    # Turn repo names into active links.
    repo_link = f"<a href='{repo_dict['html_url']}'>{repo_dict['name']}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    # Build hover texts.
    hovered_text = f"{repo_dict['owner']['login']}<br />{repo_dict['description']}"
    hovered_texts.append(hovered_text)

# Make visualization.
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hovered_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)

fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

fig.show()