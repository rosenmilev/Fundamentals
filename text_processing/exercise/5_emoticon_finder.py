# text = input().split(":")
# text = text[1:]
#
# if text[0] != "":
#     for num in text:
#         if num != "":
#             if num[0] != " ":
#                 print(f":{num[0]}")

text = input()

emoticons = [text[i:i + 2] for i in range(len(text)) if text[i] == ":" and text[i + 1] != " "]
print("\n".join(emoticons))
