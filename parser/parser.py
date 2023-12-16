from bs4 import BeautifulSoup


class Parser:
    def __init__(self, page_html):
        self.page_html = page_html
        self.parsed_html = self.get_parsed_html(self.page_html)

    def get_parsed_html(self, markup):
        parsed_html = BeautifulSoup(markup, 'html.parser')
        return parsed_html

    @property
    def title(self):
        og_title_tag = self.parsed_html.head.find(property=r'og:title')
        if og_title_tag:
            og_title = og_title_tag.get('content')
            if og_title:
                return og_title

        title = self.parsed_html.head.title
        if title:
            return title.string

        return 'unknown'

    @property
    def description(self):
        description = self.parsed_html.head.find(property=r'og:description')
        return description
