from toneAnalyzer import callWatson
from apiCall import getUserTweets, dMUser

# Analyzes users tweets and returns a cumulative score of users emotions and sentiment based on the tweet
def toneAnalyzer(userId):
    Emotions = {}
    Anger = 0
    Fear = 0
    Joy = 0
    Sadness = 0
    Analytical = 0
    Confident = 0
    Tentative = 0
    textDump = getUserTweets(userId)
    for text in textDump:
        res = callWatson(text)
        for tones in res['document_tone']['tones']:
            if tones['tone_id'] == 'sadness':
                Sadness += float(tones['score'])
            elif tones['tone_id'] == 'anger':
                Anger += float(tones['score'])
            elif tones['tone_id'] == 'tentative':
                Tentative += float(tones['score'])
            elif tones['tone_id'] == 'joy':
                Joy += float(tones['score'])
            elif tones['tone_id'] == 'fear':
                Fear += float(tones['score'])
            elif tones['tone_id'] == 'analytical':
                Analytical += float(tones['score'])
            elif tones['tone_id'] == 'confident':
                Confident += float(tones['score'])
            else:
                continue

    strongestEmotion = max(Anger, Fear, Anger, Fear,
    Joy, Sadness, Analytical, Confident, Tentative)

    Emotions = {'Anger':Anger, 'Fear': Fear, 'Joy': Joy, 'Sadness':Sadness,
    'Analytical':Analytical, 'Confident':Confident, 'Tentative': Tentative}

    for k, v in list(Emotions.items()):
        if float(v) < strongestEmotion:
            del Emotions[k]

    print("From the users most recent tweets the users emotional scores were:")
    print("Sadness: " + str(Sadness))
    print("Anger: " + str(Anger))
    print("Analytical: " + str(Analytical))
    print("Confident: " + str(Confident))
    print("Joy: " + str(Joy))
    print("Tentative: " + str(Tentative))
    print("Fear: " + str(Fear))
    print("The most dominant emotions are/were:")
    for k, v in Emotions.items():
        print(str(k) + ": " + str(Emotions[k]))
        if k == 'Sadness':
            dMUser('emoAnalysisBot')
