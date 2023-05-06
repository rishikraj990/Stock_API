# Stock_API

The project is developed by Rishik Raj using Python Flask, HTML, JavaScript, and Bootstrap. It is a web application that fetches financial data from Yahoo Finance and exposes it through a JSON API. Users can make API calls to retrieve the data and even update it using POST requests.

## Table of Contents

- [Project Name](#project-name)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [API Endpoints](#api-endpoints)
  - [Technologies Used](#technologies-used)
  - [Contributing](#contributing)
  - [License](#license)

## Installation

To install and run the project, follow these steps:

1. Clone the repository to your local machine using `git clone https://github.com/rishikraj990/Stock_API.git`.
2. Navigate to the project directory.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run the Flask server using `python app.py`.
5. Access the web application by navigating to `http://127.0.0.1:8000/` in your web browser.

## Usage

Once the web application is running, you can access the home page, API endpoints, and about page by clicking the respective links in the navigation bar. To make an API call, use the endpoint URLs listed in the API Endpoints section below.

Home Page
![plot](./directory_1/directory_2/.../directory_n/plot.png)
API Calling Page
![plot](./directory_1/directory_2/.../directory_n/plot.png)
About Page
![plot](./directory_1/directory_2/.../directory_n/plot.png)

## API Endpoints

The following API endpoints are available:

- `GET /stock-date/<DATE>` - Retrieves the financial data from Yahoo Finance on the basis of DATE.
- `GET /stock-date/<COMPANY CODE>/<DATE>` - Retrieves the financial data from Yahoo Finance on the basis of Company code and DATE.
- `GET /stock-date/<COMPANY CODE>` - Retrieves the financial data from Yahoo Finance on the basis of Company code.
- `POST /stock-update/<COMPANY CODE>/<DATE>` - Updates the financial data on the basis of Company code and DATE.

Both endpoints return data in JSON format.

## Technologies Used

The following technologies were used in the development of this project:

- Python
- Flask
- HTML
- JavaScript
- Bootstrap

## Contributing

Contributions to the project are welcome. To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and commit them with a descriptive commit message.
4. Push your changes to your forked repository.
5. Submit a pull request to the original repository with a description of your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
