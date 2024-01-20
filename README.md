# Lorcana Deck PDF Generator

## Introduction
The Lorcana Deck PDF Generator is a Python script designed to create a printable PDF of a Lorcana card deck. It reads a deck configuration from a JSON file, which can be obtained from [Dreamborn](https://dreamborn.ink/), downloads the card images, and arranges them in a grid layout on a PDF file. This tool is perfect for tabletop game enthusiasts who want to print custom decks for their games.

## Features
- **Deck COnfiguration Reading:** Parses a JSON file to obtain deck information.
- **Image Downloading:** Automatically downloads card images from specified URLs.
- **PDF Generation:** Arranges images in a grid layout and generates a PDF file.
- **Customizable Layour:** Supports adjustments in margins, card sizes, and page layout.

## Requirements
- Python 3.x
- Libraries: `json`, `requests`, `tempfile`, `os`, `reportlab`

## Installation
1. Ensure Python 3.x is installed on your system.
2. Install the required Python packages: `pip install requests reportlab`
3. Download the `lorcana.py` script from this repository.

## Obtaining a Deck Configuration
To generate a PDF for a specific deck, you need a deck configuration file in JSON format. You can download this file for any deck from [Dreamborn](https://dreamborn.ink/): 

1. Visit [Dreamborn](https://dreamborn.ink).
2. Find the deck you want to print.
3. Go to the deck's menu and select `Export -> Tabletop Simulator`.
4. Download the JSON file.

## Usage
1. Place your downloaded `deck.json` file in the same directory as the script.
2. Run the script: `python lorcana.py`
3. The script will generate a PDF file named `lorcana_deck.pdf` in the same directory.

## Configuration
- Modify the `tabletop_sim_deck_code` variable in the script with your deck's JSON configuration.
- Adjust `card_width`, `card_height`, `margin_x`, and `margin_y` variables to change the layout.

## Contributing
Contributions to the Lorcana Deck PDF Generator are welcome. Please feel free to fork the repository, make your changes, and create a pull request.

## License
This project is open-source and available under the [MIT License](https://opensource.org/license/mit/).

## Contact
For more information or queries, please contact me at:

- **Email:** [richardpauldev@gmail.com](mailto:richardpauldev@gmail.com)
- **LinkedIn:** [Richard Paul](https://www.linkedin.com/in/richardpauldev/)

Your feedback and contributions are greatly appreciated!
