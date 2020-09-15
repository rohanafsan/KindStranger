import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator



# Call to the Watson Api to get it initiated
authenticator = IAMAuthenticator('')
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    authenticator=authenticator
)

tone_analyzer.set_service_url('')

# Call to the Watson Api to analyze emotions in text
def callWatson(tweetText):
    tone_analysis = tone_analyzer.tone(
        {'text': tweetText},
        content_type='application/json'
        ).get_result()
    return tone_analysis
