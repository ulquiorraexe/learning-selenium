# Learning Selenium Project

This repository contains various Selenium automation scripts that interact with different websites to perform automated tasks. The project includes four Python files:

- **challenge.py**: Automates filling in a form on a sample website.
- **cookie-clicker.py**: Simulates a bot for the popular game Cookie Clicker.
- **interaction.py**: Automates interaction with the Wikipedia website.
- **main.py**: Automates interactions with Amazon and Python websites.

## Files

### `challenge.py`
This script automates filling in a contact form on a website. The script interacts with input fields for first name, last name, and email, then submits the form. 

#### Features:
- Automates form submission on a demo site.
- Uses Selenium to locate form elements by name and submit data.

#### Usage:
1. Clone the repository.
2. Install required dependencies: `pip install selenium`
3. Run the script: `python challenge.py`

### `cookie-clicker.py`
This script interacts with the Cookie Clicker game on the provided URL. It clicks the cookie button to generate cookies and purchases upgrades when affordable to maximize the cookies per second rate.

#### Features:
- Automates cookie clicking.
- Purchases upgrades when affordable.
- Monitors the cookies per second after running for 5 minutes.

#### Usage:
1. Clone the repository.
2. Install required dependencies: `pip install selenium`
3. Run the script: `python cookie-clicker.py`

### `interaction.py`
This script interacts with the Wikipedia main page. It performs a search for "Python" and navigates to the result page.

#### Features:
- Opens the Wikipedia main page.
- Searches for "Python" and clicks to view the results.

#### Usage:
1. Clone the repository.
2. Install required dependencies: `pip install selenium`
3. Run the script: `python interaction.py`

### `main.py`
This script performs two tasks:
1. **Amazon Price Scraper** (commented out): It scrapes the price of a specific product on Amazon.
2. **Python Events Scraper**: It scrapes upcoming events from the Python website.

#### Features:
- Scrapes the price of a product from Amazon (currently commented out).
- Retrieves and prints upcoming Python events from the Python.org events page.

#### Usage:
1. Clone the repository.
2. Install required dependencies: `pip install selenium`
3. Run the script: `python main.py`

## Installation

To run the scripts, you'll need to have the Selenium package installed.

1. Clone this repository.
2. Install the required dependencies by running the following command:
   ```bash
   pip install selenium
   ```
3. Ensure you have a compatible web driver installed (e.g., ChromeDriver for Chrome).

## Contributing

Feel free to open an issue or submit a pull request for any improvements or fixes.

## License

This project does not have a license.
