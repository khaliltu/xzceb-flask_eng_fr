import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

language_translator.set_disable_ssl_verification(True)


def english_to_french(english_text):
    translations = language_translator.translate(
        text=english_text, model_id='en-fr').get_result()
    translations = json.dumps(translations, ensure_ascii=False)
    translations = json.loads(translations)
    translation = translations["translations"][0]
    french_text = translation["translation"]
    return french_text


def french_to_english(french_text):
    translations = language_translator.translate(
        text=french_text, model_id='fr-en').get_result()
    translations = json.dumps(translations, ensure_ascii=False)
    translations = json.loads(translations)
    translation = translations["translations"][0]
    english_text = translation["translation"]
    return english_text
