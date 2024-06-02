# viewer.py

# TODO: implement a GUI viewer
# TODO: implement viewer selection (probably in main?)

def show(article):
    """Show one article"""
    print(article)

def show_list(site, titles):
    """Show list of article titles"""
    print(f"The latest tutorials from {site}")
    for article_id, title in enumerate(titles):
        print(f"{article_id:>3} {title}")