""" Module to create watson translator instance and translate between english and french """
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

# create an instance of the IBM Watson Language translator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-01-30',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """ A function to translate text from english to french """
    french_text = ""
    # if the input non-empty
    if english_text:
        french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()['translations'][0]['translation']

    return french_text

def french_to_english(french_text):
    """ A function to translate text from french to english """
    english_text = ""
    # if the input non-empty
    if french_text:
        english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()['translations'][0]['translation']

    return english_text
