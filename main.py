from slack import RTMClient
from chatgpt import ChatGPT
from dotenv import load_dotenv
import os
load_dotenv()

# 自足的に Slack メッセージ tracking
@RTMClient.run_on(event="message")
def chatgptbot(**payload):
    data = payload["data"]
    web_client = payload["web_client"]
    bot_id = data.get("bot_id", "")
    subtype = data.get("subtype", "")
    origin_text = data.get("text", "")
    tag_code = origin_text.split(" ")[0]

    # メッセージ情報把握
    print(data)
    # Botのメッセージではない場合、ChatGPTが返事
    if bot_id == "" and subtype == "" and ">" in tag_code:
        channel_id = data["channel"]
        # Extracting message send by the user on the slack
        text = data.get("text", "")
        text = text.split(">")[-1].strip()
        # 入力時間を把握、返事をするようにする
        message_ts = data["ts"]

        # もらったテキストをChatGPTに送る、ChatGPTの返事をセーブ
        
        response = ChatGPT(text)
        # Slackにメッセージ送る
        web_client.chat_postMessage(channel=channel_id, username = "きらきらきらり", icon_url="https://pbs.twimg.com/profile_images/1617171924316221443/vlmR21L2_400x400.jpg" ,text=response, thread_ts=message_ts)

if __name__ == "__main__":
    try:
        # RTMクライアントcallおよびstart
        rtm_client = RTMClient(token=os.environ.get("BOT_TOKEN"))
        print("Starter Bot connected and running!")
        rtm_client.start()
    except Exception as err:
        print(err)
