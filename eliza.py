import re
import random
import database
from langdetect import detect
from google_trans_new import google_translator


class Eliza():
  """Added support for language translation.
  Eliza will aim to understand different languages via text and respond on the go."""

  def __init__(self):
    self.keys = list(map(lambda x: re.compile(x[0], re.IGNORECASE), database.database_regexp_response))
    self.values = list(map(lambda x: x[1], database.database_regexp_response))

  def translate(self, text, vocabulary):
    """Take a string, replace any words found in vocabulary.keys()
    with the corresponding vocabulary.values()"""

    words = text.lower().split()
    keys = vocabulary.keys();
    for i in range(0, len(words)):
      if words[i] in keys:
        words[i] = vocabulary[words[i]]
    return ' '.join(words)

  def response(self, text):
    """Take a string, a set of regexps, and a corresponding
    set of response lists; find a match, and return a randomly
    chosen response from the corresponding list."""

    for i in range(0, len(self.keys)):
      match = self.keys[i].match(text)
      if match:
        resp = random.choice(self.values[i])
        pos = resp.find('%')
        while pos > -1:
          num = int(resp[pos+1:pos+2])
          resp = resp[:pos] + \
            self.translate(match.group(num), database.database_reflection) + \
            resp[pos+2:]
          pos = resp.find('%')
        if resp[-2:] == '?.': resp = resp[:-2] + '.'
        if resp[-2:] == '??': resp = resp[:-2] + '?'
        return resp
    return None

def main():
  """Main function for eliza.py"""

  print('\n************** Chat with Eliza **************\n')
  print('[Eliza]: Hi! How can I help you?')
  translator = google_translator()
  sentence = ''
  speaker = Eliza()

  while sentence != 'q':
    try:
      sentence = input('[You]: ')
      curr_lang = detect(sentence)
      #curr_lang = translator.detect(sentence) # Does not work
      print('\n[Info] Your input language is:', curr_lang)
      translated_sentence = translator.translate(sentence, lang_tgt = 'en')
    except EOFError:
      translated_sentence = 'q'
    while translated_sentence[-1] in '!.':
      translated_sentence = translated_sentence[:-1]

    res = speaker.response(translated_sentence)
    print("\n[Eliza]: ", res, '|', f"(In {curr_lang}: {translator.translate(res, lang_tgt = curr_lang)}")

if __name__ == "__main__":
  main()
