import json
import requests
import tempfile
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from io import BytesIO

def read_deck_from_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data["ObjectStates"][0]

data = read_deck_from_file('deck.json')

def download_image(url, image_cache):
    if url in image_cache:
        return image_cache[url]

    response = requests.get(url)
    if response.status_code == 200:
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
        temp_file.write(response.content)
        temp_file.close()
        image_cache[url] = temp_file.name
        return temp_file.name
    return None

pdf_file = "lorcana_deck.pdf"
page_width, page_height = letter
landscape_letter = (page_height, page_width)
c = canvas.Canvas(pdf_file, pagesize=landscape_letter)

card_width, card_height = 2.5 * inch, 3.5 * inch
margin_x, margin_y = 0.5 * inch, 0.5 * inch

cards_per_row = int((landscape_letter[0] - 2 * margin_x) / card_width)
cards_per_column = int((landscape_letter[1] - 2 * margin_y) / card_height)

print(int((page_height - 2 * margin_x) / card_width) * int((page_width - 2 * margin_y) / card_height))

image_cache = {}

current_row = current_column = 0
for deck_id, deck_info in data["CustomDeck"].items():
    face_url = deck_info["FaceURL"]
    image = download_image(face_url, image_cache)
    if image:
        x = margin_x + current_column * card_width
        y = landscape_letter[1] - margin_y - card_height - (current_row * card_height)
        c.drawImage(image, x, y, width=card_width, height=card_height)
        
        current_column += 1
        if current_column >= cards_per_row:
            current_column = 0
            current_row += 1
            if current_row >= cards_per_column:
                c.showPage()
                current_row = 0

c.save()

for temp_file in image_cache.values():
    os.remove(temp_file)

print(f"PDF file '{pdf_file}' has been created with the card images.")
