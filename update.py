import requests

url = "https://yowaimo.in/StreamFlexTv/playlist.php?name=SFBRMYCG&token=e1265dd4bee0302fd0fc7d50"

r = requests.get(url)

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(r.text)

print("Playlist updated")
