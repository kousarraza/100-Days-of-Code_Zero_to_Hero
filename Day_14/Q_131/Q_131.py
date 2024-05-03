# 131. Write a python program to replace first occurrence of a character with another in a string.

text = "Hello, world!"
old_char = 'o'
new_char = 'X'
if text.index('') == -1:
        text
elif text.index('')== 0:
    new_char + text[1:]

modified_text=text[:text.index('')] + new_char + text[text.index('')+1:]

print(f"Original text: {text}")
print(f"Modified text: {modified_text}")