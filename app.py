import streamlit as st
from src.trends_scraper import TrendsScraper
from src.article_generator import ArticleGenerator
from src.utils import load_css, get_plotly_chart
import pandas as pd

def main():
    # Load custom CSS
    load_css()
    
    # Page configuration
    st.set_page_config(
        page_title="Trends to Articles Generator",
        page_icon="📈",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Header
    st.title("Google Trends Article Generator")
    st.markdown("Transform trending topics into well-crafted articles with just a few clicks.")
    
    # Sidebar for inputs
    with st.sidebar:
        st.header("Search Parameters")
        
        # Keyword input
        keywords = st.text_input("Enter keywords (comma separated)", "AI, machine learning, data science")
        
        # Time range selection
        timeframe_options = {
            "Past hour": "now 1-H",
            "Past 4 hours": "now 4-H", 
            "Past day": "now 1-d",
            "Past 7 days": "now 7-d",
            "Past 30 days": "now 30-d",
            "Past 90 days": "now 90-d",
            "Past 12 months": "now 12-m",
            "Past 5 years": "today 5-y"
        }
        timeframe = st.selectbox("Select time range", list(timeframe_options.keys()))
        
        # Region selection
        region_options = {
            "Worldwide": "",
            "United States": "US",
            "United Kingdom": "GB",
            "Canada": "CA",
            "Australia": "AU",
            "India": "IN",
            "Germany": "DE",
            "France": "FR",
            "Japan": "JP"
        }
        region = st.selectbox("Select region", list(region_options.keys()))
        
        # Article parameters
        st.header("Article Parameters")
        
        article_tone_options = ["Informative", "Persuasive", "Entertaining", "Analytical", "Conversational"]
        article_tone = st.selectbox("Article Tone", article_tone_options)
        
        article_length_options = ["Short (300-500 words)", "Medium (500-800 words)", "Long (800-1200 words)"]
        article_length = st.selectbox("Article Length", article_length_options)
        
        # Search button
        search_button = st.button("Get Trends Data", type="primary")
    
    # Initialize session state variables if they don't exist
    if 'trends_data' not in st.session_state:
        st.session_state.trends_data = None
    if 'related_topics' not in st.session_state:
        st.session_state.related_topics = None
    if 'related_queries' not in st.session_state:
        st.session_state.related_queries = None
    if 'articles' not in st.session_state:
        st.session_state.articles = {}
    
    # Process search when button is clicked
    if search_button:
        with st.spinner("Fetching trends data..."):
            # Prepare search parameters
            kw_list = [k.strip() for k in keywords.split(",")]
            tf = timeframe_options[timeframe]
            geo = region_options[region]
            
            # Initialize scraper and get trends data
            scraper = TrendsScraper()
            try:
                trends_data = scraper.get_interest_over_time(kw_list, tf, geo)
                related_topics = scraper.get_related_topics(kw_list, tf, geo)
                related_queries = scraper.get_related_queries(kw_list, tf, geo)
                
                # Store in session state
                st.session_state.trends_data = trends_data
                st.session_state.related_topics = related_topics
                st.session_state.related_queries = related_queries
                
                st.success("Data fetched successfully!")
            except Exception as e:
                st.error(f"Error fetching trends data: {str(e)}")
    
    # Display trends data if available
    if st.session_state.trends_data is not None:
        # Display the data in tabs
        tab1, tab2, tab3, tab4 = st.tabs(["Trends Overview", "Related Topics", "Related Queries", "Generated Articles"])
        
        with tab1:
            st.header("Trends Overview")
            trends_df = st.session_state.trends_data
            
            # Create visualization
            fig = get_plotly_chart(trends_df)
            st.plotly_chart(fig, use_container_width=True)
            
            # Show the data table
            st.subheader("Trends Data")
            st.dataframe(trends_df, use_container_width=True)
            
            # Download button for trends data
            csv = trends_df.to_csv(index=True)
            st.download_button(
                label="Download Trends Data as CSV",
                data=csv,
                file_name="trends_data.csv",
                mime="text/csv"
            )
        
        with tab2:
            st.header("Related Topics")
            if st.session_state.related_topics:
                for keyword in st.session_state.related_topics:
                    st.subheader(f"Topics related to '{keyword}'")
                    
                    # Rising topics
                    if 'rising' in st.session_state.related_topics[keyword]:
                        st.write("Rising Topics")
                        rising_df = st.session_state.related_topics[keyword]['rising']
                        if rising_df is not None and not rising_df.empty:
                            st.dataframe(rising_df, use_container_width=True)
                        else:
                            st.info("No rising topics found.")
                    
                    # Top topics
                    if 'top' in st.session_state.related_topics[keyword]:
                        st.write("Top Topics")
                        top_df = st.session_state.related_topics[keyword]['top']
                        if top_df is not None and not top_df.empty:
                            st.dataframe(top_df, use_container_width=True)
                        else:
                            st.info("No top topics found.")
            else:
                st.info("No related topics data available.")
        
        with tab3:
            st.header("Related Queries")
            if st.session_state.related_queries:
                for keyword in st.session_state.related_queries:
                    st.subheader(f"Queries related to '{keyword}'")
                    
                    # Rising queries
                    if 'rising' in st.session_state.related_queries[keyword]:
                        st.write("Rising Queries")
                        rising_df = st.session_state.related_queries[keyword]['rising']
                        if rising_df is not None and not rising_df.empty:
                            st.dataframe(rising_df, use_container_width=True)
                        else:
                            st.info("No rising queries found.")
                    
                    # Top queries
                    if 'top' in st.session_state.related_queries[keyword]:
                        st.write("Top Queries")
                        top_df = st.session_state.related_queries[keyword]['top']
                        if top_df is not None and not top_df.empty:
                            st.dataframe(top_df, use_container_width=True)
                        else:
                            st.info("No top queries found.")
            else:
                st.info("No related queries data available.")
        
        with tab4:
            st.header("Generated Articles")
            st.info("Select a keyword to generate an article about.")
            
            # Get keyword list
            kw_list = [k.strip() for k in keywords.split(",")]
            
            # Two columns for selection and generation
            col1, col2 = st.columns([1, 2])
            
            with col1:
                # Article controls
                selected_keyword = st.selectbox("Select keyword for article", kw_list)
                
                # Extract article parameters
                if article_length == "Short (300-500 words)":
                    word_count = "short"
                elif article_length == "Medium (500-800 words)":
                    word_count = "medium"
                else:
                    word_count = "long"
                
                # Generate button
                generate_btn = st.button("Generate Article", type="primary")
                
                if generate_btn:
                    with st.spinner("Generating article..."):
                        # Get the related data for context
                        related_topics_data = st.session_state.related_topics.get(selected_keyword, {})
                        related_queries_data = st.session_state.related_queries.get(selected_keyword, {})
                        
                        # Initialize article generator
                        article_gen = ArticleGenerator()
                        
                        # Generate the article
                        article = article_gen.generate_article(
                            selected_keyword,
                            related_topics_data,
                            related_queries_data,
                            tone=article_tone.lower(),
                            length=word_count
                        )
                        
                        # Store in session state
                        st.session_state.articles[selected_keyword] = article
            
            with col2:
                # Display the generated article if available
                if selected_keyword in st.session_state.articles:
                    article = st.session_state.articles[selected_keyword]
                    
                    # Article display
                    st.subheader(f"Article about {selected_keyword}")
                    st.markdown(article)
                    
                    # Download button for article
                    st.download_button(
                        label="Download Article as Text",
                        data=article,
                        file_name=f"{selected_keyword.replace(' ', '_')}_article.txt",
                        mime="text/plain"
                    )
                else:
                    st.info("No article generated yet. Click 'Generate Article' to create one.")

if __name__ == "__main__":
    main()