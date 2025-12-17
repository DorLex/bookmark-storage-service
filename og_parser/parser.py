import httpx
from bs4 import BeautifulSoup
from bs4.element import Tag
from fake_headers import Headers
from httpx import Response

from core.enums.url import UrlTypeChoices


class OgParser:
    def __init__(self, url: str) -> None:
        self.url: str = url
        self.header_generator: Headers = Headers(headers=True)
        self.beautiful_soup_obj: BeautifulSoup = self._get_beautiful_soup_obj()
        self.unknown_value: str = 'Unknown'

    def _get_page_html(self, url: str) -> str:
        headers: dict = self.header_generator.generate()
        response: Response = httpx.get(url, headers=headers)
        return response.text

    def _get_beautiful_soup_obj(self) -> BeautifulSoup:
        markup: str = self._get_page_html(self.url)
        return BeautifulSoup(markup, 'html.parser')

    def _get_og_tag(self, tag: str) -> Tag | None:
        return self.beautiful_soup_obj.find(property=f'og:{tag}')

    def _get_content_from_og_tag(self, tag: str) -> str | None:
        og_tag: Tag | None = self._get_og_tag(tag)
        if og_tag:
            return og_tag.get('content')

        return None

    def _get_base_title(self) -> str | None:
        base_title_tag: Tag | None = self.beautiful_soup_obj.title
        if base_title_tag:
            return base_title_tag.string

        return None

    def _get_meta_description(self) -> str | None:
        meta_description_tag: Tag | None = self.beautiful_soup_obj.find('meta', {'name': 'description'})
        if meta_description_tag:
            return meta_description_tag.get('content')

        return None

    @property
    def title(self) -> str:
        og_title: str | None = self._get_content_from_og_tag('title')
        if og_title:
            return og_title

        base_title: str | None = self._get_base_title()
        if base_title:
            return base_title

        return self.unknown_value

    @property
    def description(self) -> str | None:
        og_description: str | None = self._get_content_from_og_tag('description')
        if og_description:
            return og_description

        meta_description: str | None = self._get_meta_description()
        if meta_description:
            return meta_description

        return None

    @property
    def type(self) -> UrlTypeChoices:
        og_type: str | None = self._get_content_from_og_tag('type')
        if og_type not in UrlTypeChoices.values:
            return UrlTypeChoices.website

        return UrlTypeChoices[og_type]

    @property
    def image(self) -> str | None:
        og_image: str | None = self._get_content_from_og_tag('image')
        if og_image:
            return og_image

        return None
