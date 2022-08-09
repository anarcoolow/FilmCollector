import requests


def download_film(request_url: str):
	data = requests.get(request_url)
	print(data.text)
