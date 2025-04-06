from operator import itemgetter

import requests
import plotly.express as px

# Make an API call, and store the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    try:
        # Build a dictionary for each article.
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
        submission_dicts.append(submission_dict)
    except KeyError:
        continue

submission_dicts = sorted(
    submission_dicts, 
    key=itemgetter('comments'), 
    reverse=True
)

# Prepare data for plot
submission_links, comments = [], []

for submission in submission_dicts:
    # Turn repo names into active links.
    submission_link = f"<a href='{submission['hn_link']}'>{submission['title']}</a>"
    submission_links.append(submission_link)
    comments.append(submission['comments'])

# Make visualization.
title = "Most active discussions currently on Hacker News."
labels = {'x': 'Submission ID', 'y': 'Comments'}
fig = px.bar(x=submission_links, y=comments, title=title, labels=labels)

fig.show()