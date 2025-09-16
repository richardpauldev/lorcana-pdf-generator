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

Run the script from the command line:

```bash
python lorcana_proxy_generator.py [options]
```

### Arguments

| Argument               | Description                                | Default            |
| ---------------------- | ------------------------------------------ | ------------------ |
| `-i`, `--input_file`   | Input deck file in JSON format             | `deck.json`        |
| `-o`, `--output_file`  | Output PDF file name                       | `lorcana_deck.pdf` |
| `-or`, `--orientation` | PDF orientation: `portrait` or `landscape` | `portrait`         |

### Example Commands

1. Generate proxies from a deck file named `deck.json` into `lorcana_deck.pdf` (portrait):

       python lorcana_proxy_generator.py

2. Specify a custom input and output:

       python lorcana_proxy_generator.py -i my_deck.json -o test_proxies.pdf

3. Generate the deck in landscape orientation:

       python lorcana_proxy_generator.py -i my_deck.json -o landscape_proxies.pdf -or landscape

## Output

- The script produces a PDF with cards arranged to maximize the number of cards per page.
- Each card is sized to **2.5 x 3.5 inches** (standard TCG size).
- The script automatically deletes downloaded temporary image files after generating the PDF.

## Configuration
- Adjust `card_width`, `card_height`, `margin_x`, `margin_y` and `padding` variables to change the layout.

## Contributing
Contributions to the Lorcana Deck PDF Generator are welcome. Please feel free to fork the repository, make your changes, and create a pull request.

## License
This project is open-source and available under the [MIT License](https://opensource.org/license/mit/).

## Contact
For more information or queries, please contact me at:

- **Email:** [richardpauldev@gmail.com](mailto:richardpauldev@gmail.com)
- **LinkedIn:** [Richard Paul](https://www.linkedin.com/in/richardpauldev/)

Your feedback and contributions are greatly appreciated!
