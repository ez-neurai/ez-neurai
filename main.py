import feedparser, datetime

# URI of the tistory blog
tistory_blog_uri="https://neurai.tistory.com/"
feed = feedparser.parse(tistory_blog_uri+"/rss")

# Markdown for profile image and typing SVG
markdown_profile = """
<img width="40%" src="https://github.com/ez-neurai/ez-neurai/assets/62509122/2361b392-ba8f-4edb-ae70-5320739c41a6"/>
<br>
[![Typing SVG](https://readme-typing-svg.demolab.com?font=DM+Sans&duration=4000&pause=800&multiline=true&width=435&height=90&lines=Hi%2C+there.;Welcome+to+my+github+page!;Feel+free+to+look+around.)](https://git.io/typing-svg)
<br>
"""


# Markdown for blog posts
markdown_blog_posts = "## Recent blog posts\n"

# Append each blog post to markdown_blog_posts string
for i in feed['entries']:
    dt = datetime.datetime.strptime(i['published'], "%a, %d %b %Y %H:%M:%S %z").strftime("%b %d, %Y")
    markdown_blog_posts += f"[{i['title']}]({i['link']}) - {dt}<br>\n"

# Combine both markdowns
full_markdown = markdown_profile + markdown_blog_posts

# Write the markdown to README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(full_markdown)