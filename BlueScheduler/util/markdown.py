import markdown


def convert_markdown_html(markdown_content):
    exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.tables',
            'markdown.extensions.toc']
    html = markdown.markdown(markdown_content, extensions=exts)
    return html
