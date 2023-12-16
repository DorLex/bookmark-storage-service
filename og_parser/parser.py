from bs4 import BeautifulSoup


class Parser:
    def __init__(self, page_html):
        self.page_html = page_html
        self.parsed_html = self.get_parsed_html(self.page_html)
        self.unknown = 'Unknown'

    def get_parsed_html(self, markup):
        parsed_html = BeautifulSoup(markup, 'html.parser')
        return parsed_html

    def get_og_tag(self, tag):
        og_tag = self.parsed_html.head.find(property=f'og:{tag}')
        return og_tag

    def get_og_content(self, tag):
        og_tag = self.get_og_tag(tag)
        if og_tag:
            og_content = og_tag.get('content')
            return og_content

    def get_base_title(self):
        base_title_tag = self.parsed_html.head.title
        if base_title_tag:
            return base_title_tag.string

    def get_meta_description(self):
        meta_description_tag = self.parsed_html.head.find('meta', {'name': 'description'})
        if meta_description_tag:
            return meta_description_tag.get('content')

    @property
    def title(self):
        og_title = self.get_og_content('title')
        if og_title:
            return og_title

        base_title = self.get_base_title()
        if base_title:
            return base_title

        return self.unknown

    @property
    def description(self):
        og_description = self.get_og_content('description')
        if og_description:
            return og_description

        meta_description = self.get_meta_description()
        if meta_description:
            return meta_description

        return self.unknown
