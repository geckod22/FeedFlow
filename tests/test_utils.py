# tests/test_utils.py
from app.utils import detect_actual_language

def test_detect_actual_language():
	lang = detect_actual_language("this is a test text")
	assert lang == "en"

	lang = detect_actual_language("Questo è un test")
	assert lang == "it"

	false_result = detect_actual_language("")
	assert false_result == False
