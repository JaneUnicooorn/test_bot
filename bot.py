import requests

TOKEN = '704001319:AAHwbOYzZoHaRCN73XGEEhAF2aN_wAb61Pw'
MAIN_URL = f'https://api.telegram.org/bot{TOKEN}/'


r = requests.post(f'{MAIN_URL}getUpdates')

print(r.json())