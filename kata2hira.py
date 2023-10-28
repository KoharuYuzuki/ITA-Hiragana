import re
import os
import jaconv

transcript_file_path = './transcript.txt'
transcript_pattern = re.compile('^(?P<name>.+):(?P<text>.+),(?P<yomi>.+)$', re.M | re.I)

with open(transcript_file_path, mode='r', encoding='utf-8') as transcript_file:
  transcript = transcript_file.read()

matches = [x.groupdict() for x in re.finditer(transcript_pattern, transcript)]
os.makedirs('./txt', exist_ok=True)

for match in matches:
  katakana = match['yomi']
  katakana = katakana.replace('。', '')
  katakana = katakana.replace('？', '')

  txt_file_path = os.path.join('./txt', F'{match["name"]}.txt')

  with open(txt_file_path, mode='w', encoding='utf-8') as txt_file:
    hiragana = jaconv.kata2hira(katakana)
    txt_file.write(hiragana)
