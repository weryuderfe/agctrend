import pandas as pd
import requests
import json
from datetime import datetime, timedelta
import time
import random

class TrendsScraper:
    """Class for scraping data from Google Trends web URL."""
    
    def __init__(self):
        """Initialize the scraper with base URL and headers."""
        self.base_url = "https://trends.google.com/trends/api/explore"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    
    def _build_payload(self, keywords, timeframe="now 7-d", geo="US"):
        """Build the request payload."""
        req = {
            "comparisonItem": [
                {
                    "keyword": kw.strip(),
                    "geo": geo,
                    "time": timeframe
                } for kw in keywords
            ],
            "category": 0,
            "property": ""
        }
        return {"hl": "en-US", "tz": "-120", "req": json.dumps(req)}
    
    def _clean_json(self, response_text):
        """Clean the response text by removing garbage prefix."""
        return json.loads(response_text[5:])  # Remove ")]}'" prefix
    
    def get_interest_over_time(self, keywords, timeframe="now 7-d", geo="US"):
        """
        Get interest over time data for specified keywords.
        
        Args:
            keywords (list): List of keywords to get data for
            timeframe (str): Time frame to retrieve data
            geo (str): Geographic location (defaults to US)
            
        Returns:
            pandas.DataFrame: DataFrame containing interest over time data
        """
        try:
            # Convert keywords to list if string
            if isinstance(keywords, str):
                keywords = [keywords]
            
            # Make request
            payload = self._build_payload(keywords, timeframe, geo)
            response = requests.get(self.base_url, params=payload, headers=self.headers)
            
            if response.status_code != 200:
                print(f"Error: Status code {response.status_code}")
                return pd.DataFrame()
            
            # Parse response
            data = self._clean_json(response.text)
            
            # Create empty DataFrame
            df = pd.DataFrame()
            
            # Add timestamp as index
            if 'timelineData' in data['default']['timelineData']:
                timestamps = [int(point['time']) for point in data['default']['timelineData']]
                df.index = pd.to_datetime(timestamps, unit='s')
                
                # Add data for each keyword
                for i, kw in enumerate(keywords):
                    values = [point['value'][i] for point in data['default']['timelineData']]
                    df[kw] = values
            
            return df
            
        except Exception as e:
            print(f"Error fetching data: {str(e)}")
            return pd.DataFrame()
    
    def get_related_topics(self, keywords, timeframe="now 7-d", geo="US"):
        """
        Get related topics for specified keywords.
        
        Args:
            keywords (list): List of keywords to get data for
            timeframe (str): Time frame to retrieve data
            geo (str): Geographic location (defaults to US)
            
        Returns:
            dict: Dictionary containing related topics data for each keyword
        """
        # For now, return empty dict as related topics requires different endpoint
        return {}
    
    def get_related_queries(self, keywords, timeframe="now 7-d", geo="US"):
        """
        Get related queries for specified keywords.
        
        Args:
            keywords (list): List of keywords to get data for
            timeframe (str): Time frame to retrieve data
            geo (str): Geographic location (defaults to US)
            
        Returns:
            dict: Dictionary containing related queries data for each keyword
        """
        # For now, return empty dict as related queries requires different endpoint
        return {}
    
    def get_interest_by_region(self, keywords, timeframe="now 7-d", geo="US", resolution="COUNTRY"):
        """
        Get interest by region for specified keywords.
        
        Args:
            keywords (list): List of keywords to get data for
            timeframe (str): Time frame to retrieve data
            geo (str): Geographic location (defaults to US)
            resolution (str): Resolution of the data (COUNTRY, REGION, CITY, DMA)
            
        Returns:
            pandas.DataFrame: DataFrame containing interest by region data
        """
        # For now, return empty DataFrame as regional data requires different endpoint
        return pd.DataFrame()
