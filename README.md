# SeleniumTests

A web application designed to help developers practice and improve their Selenium testing skills through various interactive test scenarios.

## Features

- **Home**: Introduction and navigation to test scenarios
- **E-commerce Test**: Practice testing shopping cart functionality
- **Account Test**: Practice testing user authentication flows

## Project Structure

```
├── src/
│   ├── main.py              # Flask application entry point
│   ├── static/              # Static assets for each section
│   │   ├── account/         # Account section assets
│   │   ├── ecommerce/       # E-commerce section assets
│   │   └── home/           # Home page assets
│   └── templates/           # HTML templates
│       ├── account.html
│       ├── ecommerce.html
│       └── home.html
└── tests/                   # Selenium test scenarios
    ├── account/            # Account testing exercises
    └── ecommerce/         # E-commerce testing exercises
```

## Setup

1. Ensure you have Python installed on your system
2. Install dependencies:
   ```bash
   pdm install
   ```
3. Run the application:
   ```bash
   pdm run python src/main.py
   ```
4. Visit `http://localhost:5000` in your browser

## Writing Tests

The `/tests` directory contains separate sections for different testing scenarios. Each section provides opportunities to practice various Selenium testing techniques:

- **E-commerce Tests**: Practice testing shopping cart interactions, product listings, and checkout flows
- **Account Tests**: Practice testing login forms, registration, and user profile management

## Running Tests

1. Ensure the web application is running
2. Navigate to the specific test directory
3. Run the tests:
   ```bash
   pdm run python tests/[section]/main.py
   ```

For more detailed information about each testing scenario, visit the corresponding sections on the website.
