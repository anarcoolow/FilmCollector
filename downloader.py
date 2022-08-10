import requests


def download_film(m3u8_file_url: str):
	data = requests.get(m3u8_file_url).text
	data = data.split('\n')
	segments = []
	for segment in segments:
		if ".ts" in segment:
			pass

	print(data)

# url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
# r = requests.get(url)
# with open('/Users/scott/Downloads/cat3.jpg', 'wb') as f:
# 	f.write(r.content)
