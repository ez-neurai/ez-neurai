import feedparser, datetime

tistory_blog_uri="https://neurai.tistory.com/"
feed = feedparser.parse(tistory_blog_uri+"/rss")

# Start the markdown with the image
markdown_text = """
<img width="80%" src="https://github.com/ez-neurai/ez-neurai/assets/62509122/2361b392-ba8f-4edb-ae70-5320739c41a6"/>
<br>
[![Typing SVG](https://readme-typing-svg.demolab.com?font=DM+Sans&duration=4000&pause=800&multiline=true&width=435&height=90&lines=Hi%2C+there.;Welcome+to+my+github+page!;Feel+free+to+look+around.)](https://git.io/typing-svg)
## Recent blog posts
"""

# Parse the RSS feed and append each blog post to the markdown text
for i in feed['entries']:
    dt = datetime.datetime.strptime(i['published'], "%a, %d %b %Y %H:%M:%S %z").strftime("%b %d, %Y")
    markdown_text += f"[{i['title']}]({i['link']}) - {dt}<br>\n"
    print(i['link'], i['title'])

# Write the final markdown text to the README.md file
with open("README.md",mode="w", encoding="utf-8") as f:
    f.write(markdown_text)
