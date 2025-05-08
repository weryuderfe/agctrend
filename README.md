# Google Trends Article Generator

A Streamlit application that scrapes Google Trends data and automatically generates articles based on trending topics.

## Features

- Search for multiple keywords on Google Trends
- Select time range and geographical region for data collection
- View comprehensive trends data and visualizations
- Explore related topics and queries
- Generate articles with customizable tone and length
- Download trend data as CSV and articles as text files

## Installation

1. Clone this repository
2. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:

```bash
streamlit run app.py
```

2. Enter keywords in the sidebar (comma-separated)
3. Select time range and region
4. Choose article parameters (tone and length)
5. Click "Get Trends Data" to fetch and display the data
6. Navigate to the "Generated Articles" tab
7. Select a keyword and click "Generate Article"
8. Download the article or trend data as needed

## Data Sources

This application uses the PyTrends library to access Google Trends data, including:

- Interest over time
- Related topics
- Related queries

## Customization

You can customize the article generation by:

- Selecting different tones (Informative, Persuasive, Entertaining, Analytical, Conversational)
- Choosing article length (Short, Medium, Long)
- Adding your own templates in the `article_generator.py` file

## License

This project is licensed under the MIT License.