import os
import time
import schedule
import logging
import random
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

logging.basicConfig(level=logging.DEBUG)

def sendMessage(slack_client, msg):
  # make the POST request through the python slack client
  
  # check if the request was a success
  try:
    slack_client.chat_postMessage(
      channel='#chanel-name',
      text=msg
    )#.get()
  except SlackApiError as e:
    logging.error('Request to Slack API Failed: {}.'.format(e.response.status_code))
    logging.error(e.response)

if __name__ == "__main__":
  SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
  slack_client = WebClient(SLACK_BOT_TOKEN)
  logging.debug("authorized slack client")

  letters = ['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ', 'た', 
           'ち', 'つ', 'て', 'と', 'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ひ', 'ふ', 'へ', 'ほ', 'ま', 'み', 
           'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん', 'が', 'ぎ',
           'ぐ', 'げ', 'ご', 'ざ', 'じ', 'ず', 'ぜ', 'ぞ', 'だ', 'ぢ', 'づ', 'で', 'ど', 'ば', 'び', 'ぶ',
           'べ', 'ぼ', 'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ']
  
  expressions = ['ohayo-gozaimasu', 'konnichiwa', 'kombanwa', 'oyasumi', 'sayonara', 'ja mata / dewa mata', 'hajimemashute', 'yoroshiku', 'arigato', 'do itashimashute', 'gomen nasaii', 'sumimasen', 
                 'ittekimasu', 'itterasshai', 'tadaiima', 'okaeri nasai', 'irasshaimase', 'ojamashimasu', 'ojamashimasu', 'ojamashimashita', 'itadakimasu', 'gochisousamadeshita', 'omedeto', 'ganbatte', 
                 'kiotsukete', 'chotto matte', 'genki desuka', 'daijobu desuka', 'ii desuka', 'hisashiburi', 'odaijini', 'osakini dozo', 'shitsurei shimasu', 'otsukare sama', 'moshimoshi', 'kanpai', 
                 'wakarimasen', 'wakarimashuta', 'moichido onegaishimasu', 'yukkuri onegaishimasu']
  
  num = list(range(1, 1000001))
  
  user = ['<@MemberID>', '<@MemberID>', '<@MemberID>']

  # Choose a random user
  chosen_user = random.sample(user, 1)
  # Choose 2 random numbers
  chosen_num = random.sample(num, 2)
  # Choose three random letter
  chosen_letters = random.sample(letters, 3)
  # choose three random expressions
  chosen_express = random.sample(expressions, 3)

  msg = f"Konnichiwa {chosen_user[0].strip('[]')} kyo wa moji desu, ganbatte kudasai: {chosen_letters[0]}, {chosen_letters[1]}, {chosen_letters[2]}"
  msg2 = f"Soshite {chosen_user[0].strip('[]')}, kotaete kudasai: {chosen_express[0]}, {chosen_express[1]}, {chosen_express[2]}"
  msg3 = f"Soretomo {chosen_user[0].strip('[]')}, kazu wa nandesuka: {chosen_num[0]}, {chosen_num[1]}"
  schedule.every().day.at("12:32").do(lambda: sendMessage(slack_client, msg))
  schedule.every().day.at("13:35").do(lambda: sendMessage(slack_client, msg2))
  schedule.every().day.at("14:00").do(lambda: sendMessage(slack_client, msg3))

  logging.info("entering loop")

  while True:
    schedule.run_pending()
    time.sleep(5) # sleep for 5 seconds between checks on the scheduler
