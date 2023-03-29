import feedparser, datetime

tistory_blog_uri="https://neurai.tistory.com/"
feed = feedparser.parse(tistory_blog_uri+"/rss")

markdown_text = """
[![Typing SVG](https://readme-typing-svg.demolab.com?font=DM+Sans&duration=4000&pause=800&multiline=true&width=435&height=90&lines=Hi%2C+there.;Welcome+to+my+github+page!;Feel+free+to+look+around.)](https://git.io/typing-svg)
## Recent blog posts
""" # list of blog posts will be appended here

markdown_text1 = """
## Interests
<div style="display: flex; justify-content: center;">
    <img src="https://img.shields.io/badge/MNE-3776AB?style=for-the-badge&logo=python&logoColor=white">
    <img src="https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=Google-colab&logoColor=white">
</div>

lst = []


for i in feed['entries']:
    dt = datetime.datetime.strptime(i['published'], "%a, %d %b %Y %H:%M:%S %z").strftime("%b %d, %Y")
    markdown_text += f"[{i['title']}]({i['link']}) - {dt}<br>\n"
    print(i['link'], i['title'])

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.write(markdown_text1)
f.close()
