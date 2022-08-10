from pprint import pprint

from selenium import webdriver

import downloader
import page_analyzer

if __name__ == "__main__":
	options = webdriver.ChromeOptions()
	options.add_argument("--headless")
	chrome_prefs = {"profile.managed_default_content_settings.images": 2}
	options.add_experimental_option("prefs", chrome_prefs)
	browser = webdriver.Chrome(options=options)

	test_url = "http://fanseries.tv/serials/273-silicon-valley-64/1-season/1-episode.html"
	# browser.get(test_url)
	# time.sleep(2)
	# audio_tracks = browser.find_elements(By.XPATH, "//div[@class='slick-track']/div")
	# text_of_audio_tracks = [track.text for track in audio_tracks]
	# print(list(zip(range(len(text_of_audio_tracks)), text_of_audio_tracks)))
	# download_film(test_url)

	audio_tracks = page_analyzer.get_titles_of_audio_tracks(test_url)
	film_name = page_analyzer.get_name(test_url)
	pprint(film_name)
	pprint(audio_tracks)

	test_file_url = "http://osmium.stream.voidboost.cc/5/7/7/1/5/fdf07f15dda5da3795e5ae7f4e0e048e:2022081013:OXBOQkxLU2NXR3l1NFQ3UllISmFiUE5KZFhpSWQ3M0NVdHV2a0lvdERSWk9RMUZrKzRWNXhFVk5CZWRra0U3cHZaT2NERERlcDhjN29OZ1hnZ2FFczJxaE5vTkgwdEVTbnNVUjAxNVJEaUU9/7g5rw.mp4:hls:manifest.m3u8"

	downloader.download_film(test_file_url)
