# Zillow Rental Scraper and Google Forms Autofiller

This project scrapes rental property data from Zillow and automatically fills out a Google Form with the scraped data.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)

## Overview

This project consists of a web scraper that gathers rental property data from Zillow's Los Angeles listings and a script that automatically fills a Google Form with the scraped data. The scraper extracts property prices, addresses, and links to detailed property pages.

## Installation

Clone the repository and Navigate to the project directory::
 ```bash
   git clone https://github.com/Ahmad1015/Zillow-Rental-Scraper-and-Google-Forms-Autofiller.git
   cd Zillow-Rental-Scraper-and-Google-Forms-Autofiller
```
## Usage
- Make sure you have ChromeDriver installed and its path set correctly in the chrome_driver_path variable.
- Run the script:
```python
python main.py
```
## Dependencies
- selenium
- requests
- beautifulsoup4
Install these dependencies using:
```bash
pip install selenium requests beautifulsoup4
```
## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
