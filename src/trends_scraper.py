import pandas as pd
from pytrends.request import TrendReq
import time
import random

class TrendsScraper:
    """Class for scraping data from Google Trends."""
    
    def __init__(self):
        """Initialize the TrendReq client."""
        self.pytrends = TrendReq(
            hl='en-US',
            tz=360,
            timeout=(10,25),
            retries=2,
            backoff_factor=0.1,
            requests_args={'verify': True}
        )
    
    def get_interest_over_time(self, keywords, timeframe="now 7-d", geo=""):
        """
        Get interest over time data for specified keywords.
        
        Args:
            keywords (list): List of keywords to get data for
            timeframe (str): Time frame to retrieve data
            geo (str): Geographic location (defaults to worldwide)
            
        Returns:
            pandas.DataFrame: DataFrame containing interest over time data
        """
        # Build the payload
        self.pytrends.build_payload(keywords, cat=0, timeframe=timeframe, geo=geo, gprop='')
        
        # Add a small delay to avoid rate limiting
        time.sleep(random.uniform(1, 3))
        
        # Get the interest over time data
        interest_over_time_df = self.pytrends.interest_over_time()
        
        # Drop the 'isPartial' column if it exists
        if 'isPartial' in interest_over_time_df.columns:
            interest_over_time_df = interest_over_time_df.drop('isPartial', axis=1)
        
        return interest_over_time_df
    
    def get_related_topics(self, keywords, timeframe="now 7-d", geo=""):
        """
        Get related topics for specified keywords.
        
        Args:
            keywords (list): List of keywords to get data for
            timeframe (str): Time frame to retrieve data
            geo (str): Geographic location (defaults to worldwide)
            
        Returns:
            dict: Dictionary containing related topics data for each keyword
        """
        related_topics = {}
        
        for keyword in keywords:
            # Build the payload with a single keyword
            self.pytrends.build_payload([keyword], cat=0, timeframe=timeframe, geo=geo, gprop='')
            
            # Add a small delay to avoid rate limiting
            time.sleep(random.uniform(1, 3))
            
            # Get the related topics
            try:
                related_topics[keyword] = self.pytrends.related_topics()
            except Exception as e:
                print(f"Error getting related topics for {keyword}: {e}")
                related_topics[keyword] = {}
        
        return related_topics
    
    def get_related_queries(self, keywords, timeframe="now 7-d", geo=""):
        """
        Get related queries for specified keywords.
        
        Args:
            keywords (list): List of keywords to get data for
            timeframe (str): Time frame to retrieve data
            geo (str): Geographic location (defaults to worldwide)
            
        Returns:
            dict: Dictionary containing related queries data for each keyword
        """
        related_queries = {}
        
        for keyword in keywords:
            # Build the payload with a single keyword
            self.pytrends.build_payload([keyword], cat=0, timeframe=timeframe, geo=geo, gprop='')
            
            # Add a small delay to avoid rate limiting
            time.sleep(random.uniform(1, 3))
            
            # Get the related queries
            try:
                related_queries[keyword] = self.pytrends.related_queries()
            except Exception as e:
                print(f"Error getting related queries for {keyword}: {e}")
                related_queries[keyword] = {}
        
        return related_queries
    
    def get_interest_by_region(self, keywords, timeframe="now 7-d", geo="", resolution="COUNTRY"):
        """
        Get interest by region for specified keywords.
        
        Args:
            keywords (list): List of keywords to get data for
            timeframe (str): Time frame to retrieve data
            geo (str): Geographic location (defaults to worldwide)
            resolution (str): Resolution of the data (COUNTRY, REGION, CITY, DMA)
            
        Returns:
            pandas.DataFrame: DataFrame containing interest by region data
        """
        # Build the payload
        self.pytrends.build_payload(keywords, cat=0, timeframe=timeframe, geo=geo, gprop='')
        
        # Add a small delay to avoid rate limiting
        time.sleep(random.uniform(1, 3))
        
        # Get the interest by region data
        interest_by_region_df = self.pytrends.interest_by_region(resolution=resolution, inc_low_vol=True, inc_geo_code=False)
        
        return interest_by_region_df
