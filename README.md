# HDC Scraping

HDC Scraping is a Python-based project designed to extract data from the Health Data Center (HDC) system. This tool automates the retrieval of health-related data, facilitating analysis and reporting.

## Features

- **Automated Data Extraction**: Streamlines the process of collecting health data from the HDC system.
- **Data Parsing**: Processes and structures the extracted data for easy analysis.
- **Error Handling**: Implements robust error handling to ensure reliable data retrieval.

## Prerequisites

Before using this tool, ensure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Ramathibodi-HPSR/HDC_scraping.git
   cd HDC_scraping
   ```

2. **Install Required Packages**:

   It's recommended to use a virtual environment to manage dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

   Then, install the necessary packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Scraper**:

   Update the information in `scraping.ipynb` file with your specific settings, such as login credentials and target URLs.


2. **Access Extracted Data**:

   The extracted data will be saved in the `downloads` directory in your specified format (e.g., CSV, JSON).

## Contributing

We welcome contributions to enhance the functionality of this project. To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m 'Add YourFeature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

We appreciate the support from the Ramathibodi Health Policy and Systems Research team and all contributors who have assisted in the development of this tool.
