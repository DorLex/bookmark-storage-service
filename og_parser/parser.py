from bs4 import BeautifulSoup

from core.enums.choices import UrlTypeChoices


class Parser:
    def __init__(self, page_html: str) -> None:
        self.page_html: str = page_html
        self.parsed_html = self.get_parsed_html(self.page_html)
        self.unknown: str = 'Unknown'

    def get_parsed_html(self, markup: str) -> BeautifulSoup:
        return BeautifulSoup(markup, 'html.parser')

    def get_og_tag(self, tag: str) -> BeautifulSoup | None:
        return self.parsed_html.find(property=f'og:{tag}')

    def get_og_content(self, tag: str) -> str:
        og_tag = self.get_og_tag(tag)
        if og_tag:
            return og_tag.get('content')

        return None

    def get_base_title(self) -> str:
        base_title_tag = self.parsed_html.title
        if base_title_tag:
            return base_title_tag.string

        return None

    def get_meta_description(self) -> str:
        meta_description_tag = self.parsed_html.find('meta', {'name': 'description'})
        if meta_description_tag:
            return meta_description_tag.get('content')

        return None

    @property
    def title(self) -> str:
        og_title = self.get_og_content('title')
        if og_title:
            return og_title

        base_title = self.get_base_title()
        if base_title:
            return base_title

        return self.unknown

    @property
    def description(self) -> str:
        og_description = self.get_og_content('description')
        if og_description:
            return og_description

        meta_description = self.get_meta_description()
        if meta_description:
            return meta_description

        return self.unknown

    @property
    def type(self) -> UrlTypeChoices:
        og_type = self.get_og_content('type')
        if og_type not in UrlTypeChoices.values:
            return UrlTypeChoices.website

        return og_type

    @property
    def image(self) -> str | None:
        og_image = self.get_og_content('image')
        if og_image:
            return og_image

        return None
