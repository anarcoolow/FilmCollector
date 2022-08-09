from pprint import pprint

from selenium import webdriver

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
