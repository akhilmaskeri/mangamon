import os
import unittest
from pathlib import Path

from mangamon.download import MangaDownloader

class DownloadTastCases(unittest.TestCase):

	def test_download_chapter_bad_manga_name(self):
		download = MangaDownloader()
		self.assertRaises(ValueError, download.download_chapter, "", 1, "/")
		self.assertRaises(ValueError, download.download_chapter, None, 1, "/")
		self.assertRaises(ValueError, download.download_chapter, 1, 1, "/")

	def test_download_chapter_bad_chapter_number(self):
		download = MangaDownloader()
		self.assertRaises(ValueError, download.download_chapter, "coolest-manga", -1, "/")
		self.assertRaises(ValueError, download.download_chapter, "coolest-manga", 0, "/")
		self.assertRaises(ValueError, download.download_chapter, "coolest-manga", "1", "/")

	def test_download_chapter_non_existant_download_location(self):
		download = MangaDownloader()
		self.assertRaises(FileNotFoundError, download.download_chapter, "coolest-manga", 1, Path("XYZ://whatever"))

	def test_download_chapter_download_location_not_directory(self):
		download = MangaDownloader()
		self.assertRaises(FileNotFoundError, download.download_chapter, "coolest-manga", 1, Path(__file__))


	def test_save_image_empty_soup(self):
		pass

	def test_save_image_bad_chapter(self):
		pass

	def test_save_image_bad_page(self):
		pass

	def test_save_image_bad_destination(self):
		pass
