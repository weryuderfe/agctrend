from pytrends.request import TrendReq
import pandas as pd
import time
import random

class TrendsScraper:
    """Class for fetching real Google Trends data using specific URL format."""
    
    def __init__(self):
        """Initialize the TrendReq client with US locale."""
        self.pytrends = TrendReq(
            hl='en-US',
            tz=360,
            timeout=(10,25),
            retries=2,
            backoff_factor=0.1
        )
    
    def get_interest_over_time(self, keywords, timeframe="now 7-d", geo="US"):
        """
        Get interest over time data using format: trends.google.com/trends/explore?geo=US&q=keywords
        
        Args:
            keywords (list): List of keywords to get data for
            timeframe (str): Time frame to retrieve data
            geo (str): Geographic location (always US)
            
        Returns:
            pandas.DataFrame: DataFrame containing interest over time data
        """
        try:
            if isinstance(keywords, str):
                # Convert comma-separated string to list
                keywords = [k.strip() for k in keywords.split(',')]
            
            # Ensure geo is always US to match the URL format
            geo = "US"
            
            # Build the payload
            self.pytrends.build_payload(keywords, cat=0, timeframe=timeframe, geo=geo)
            
            # Add a small delay to avoid rate limiting
            time.sleep(random.uniform(1, 2))
            
            # Get the interest over time data
            df = self.pytrends.interest_over_time()
            
            # Drop isPartial column if it exists
            if 'isPartial' in df.columns:
                df = df.drop('isPartial', axis=1)
            
            return df
            
        except Exception as e:
            print(f"Error fetching trends data: {str(e)}")
            return pd.DataFrame()
    
    def get_related_topics(self, keywords, timeframe="now 7-d", geo="US"):
        """
        Get related topics using format: trends.google.com/trends/explore?geo=US&q=keywords
        
        Args:
            keywords (list): List of keywords to get data for
            timeframe (str): Time frame to retrieve data
            geo (str): Geographic location (always US)
            
        Returns:
            dict: Dictionary containing related topics data for each keyword
        """
        related_topics = {}
        
        if isinstance(keywords, str):
            keywords = [k.strip() for k in keywords.split(',')]
        
        # Ensure geo is always US
        geo = "US"
        
        for keyword in keywords:
            try:
                # Build the payload
                self.pytrends.build_payload([keyword], cat=0, timeframe=timeframe, geo=geo)
                
                # Add a small delay to avoid rate limiting
                time.sleep(random.uniform(1, 2))
                
                # Get related topics
                topics = self.pytrends.related_topics()
                related_topics[keyword] = topics.get(keyword, {})
                
            except Exception as e:
                print(f"Error fetching related topics for {keyword}: {str(e)}")
                related_topics[keyword] = {}
        
        return related_topics
    
    def get_related_queries(self, keywords, timeframe="now 7-d", geo="US"):
        """
        Get related queries using format: trends.google.com/trends/explore?geo=US&q=keywords
        
        Args:
            keywords (list): List of keywords to get data for
            timeframe (str): Time frame to retrieve data
            geo (str): Geographic location (always US)
            
        Returns:
            dict: Dictionary containing related queries data for each keyword
        """
        related_queries = {}
        
        if isinstance(keywords, str):
            keywords = [k.strip() for k in keywords.split(',')]
        
        # Ensure geo is always US
        geo = "US"
        
        for keyword in keywords:
            try:
                # Build the payload
                self.pytrends.build_payload([keyword], cat=0, timeframe=timeframe, geo=geo)
                
                # Add a small delay to avoid rate limiting
                time.sleep(random.uniform(1, 2))
                
                # Get related queries
                queries = self.pytrends.related_queries()
                related_queries[keyword] = queries.get(keyword, {})
                
            except Exception as e:
                print(f"Error fetching related queries for {keyword}: {str(e)}")
                related_queries[keyword] = {}
        
        return related_queries
    
    def get_interest_by_region(self, keywords, timeframe="now 7-d", geo="US", resolution="REGION"):
        """
        Get interest by region using format: trends.google.com/trends/explore?geo=US&q=keywords
        
        Args:
            keywords (list): List of keywords to get data for
            timeframe (str): Time frame to retrieve data
            geo (str): Geographic location (always US)
            resolution (str): Resolution of the data (COUNTRY, REGION, CITY, DMA)
            
        Returns:
            pandas.DataFrame: DataFrame containing interest by region data
        """
        try:
            if isinstance(keywords, str):
                keywords = [k.strip() for k in keywords.split(',')]
            
            # Ensure geo is always US
            geo = "US"
            
            # Build the payload
            self.pytrends.build_payload(keywords, cat=0, timeframe=timeframe, geo=geo)
            
            # Add a small delay to avoid rate limiting
            time.sleep(random.uniform(1, 2))
            
            # Get interest by region
            df = self.pytrends.interest_by_region(resolution=resolution, inc_low_vol=True)
            
            return df
            
        except Exception as e:
            print(f"Error fetching regional data: {str(e)}")
            return pd.DataFrame()
