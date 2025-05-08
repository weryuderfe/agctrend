import pandas as pd
import requests
from datetime import datetime, timedelta
import time
import random
from bs4 import BeautifulSoup

class TrendsScraper:
    """Class for fetching Google Trends data."""
    
    def __init__(self):
        """Initialize the scraper."""
        self.base_url = "https://trends.google.com/trends/explore"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
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
            # For demonstration purposes, generate sample data
            # In production, you would parse the actual response from Google Trends
            end_date = datetime.now()
            start_date = end_date - timedelta(days=7)
            dates = pd.date_range(start=start_date, end=end_date, freq='D')
            
            df = pd.DataFrame(index=dates)
            
            if isinstance(keywords, str):
                keywords = [keywords]
            
            for keyword in keywords:
                # Generate realistic-looking trend data
                base_value = 65  # Living room typically has moderate-high interest
                values = []
                for _ in range(len(dates)):
                    # Add some natural variation
                    daily_value = base_value + random.randint(-15, 15)
                    # Ensure values stay within 0-100 range
                    daily_value = max(0, min(100, daily_value))
                    values.append(daily_value)
                
                df[keyword] = values
            
            return df
            
        except Exception as e:
            print(f"Error fetching trends data: {str(e)}")
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
        # Sample related topics for "living room"
        sample_topics = {
            'living room': {
                'rising': pd.DataFrame({
                    'topic_title': [
                        'Modern living room',
                        'Living room furniture',
                        'Living room decor',
                        'Small living room',
                        'Living room design'
                    ],
                    'value': [
                        'Breakout',
                        '+250%',
                        '+180%',
                        '+150%',
                        '+120%'
                    ]
                }),
                'top': pd.DataFrame({
                    'topic_title': [
                        'Living room furniture',
                        'Living room decor',
                        'Modern living room',
                        'Small living room ideas',
                        'Living room design'
                    ],
                    'value': [
                        100,
                        95,
                        80,
                        75,
                        70
                    ]
                })
            }
        }
        
        return sample_topics
    
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
        # Sample related queries for "living room"
        sample_queries = {
            'living room': {
                'rising': pd.DataFrame({
                    'query': [
                        'living room ideas 2024',
                        'modern farmhouse living room',
                        'coastal living room',
                        'living room paint colors',
                        'living room curtains'
                    ],
                    'value': [
                        'Breakout',
                        '+200%',
                        '+180%',
                        '+150%',
                        '+130%'
                    ]
                }),
                'top': pd.DataFrame({
                    'query': [
                        'living room ideas',
                        'small living room ideas',
                        'modern living room',
                        'living room furniture',
                        'living room decor'
                    ],
                    'value': [
                        100,
                        90,
                        85,
                        80,
                        75
                    ]
                })
            }
        }
        
        return sample_queries
    
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
        # Sample regional data for US states
        states = [
            'California', 'Texas', 'Florida', 'New York', 'Illinois',
            'Pennsylvania', 'Ohio', 'Georgia', 'North Carolina', 'Michigan'
        ]
        
        values = [random.randint(60, 100) for _ in states]
        
        df = pd.DataFrame({
            'region': states,
            'interest': values
        }).set_index('region')
        
        return df
