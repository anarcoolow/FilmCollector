from urllib.request import urlopen

from lxml import etree


def get_titles_of_audio_tracks(url: str):
	response = urlopen(url)
	htmlparser = etree.HTMLParser()
	tree = etree.parse(response, htmlparser)

	result = [title.text for title in tree.xpath("//div[@class='sounds-list']/div")]
	return result


def get_name(url: str):
	response = urlopen(url)
	htmlparser = etree.HTMLParser()
	tree = etree.parse(response, htmlparser)

	return tree.xpath("//h1[@class='page-title']")[0].text
