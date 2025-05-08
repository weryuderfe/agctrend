import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from plotly.subplots import make_subplots

def load_css():
    """Load custom CSS to enhance the appearance of the Streamlit app."""
    st.markdown("""
    <style>
        /* Main container */
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        
        /* Headers */
        h1 {
            color: #1E88E5;
            font-weight: 700;
            margin-bottom: 1.5rem;
        }
        
        h2 {
            color: #0D47A1;
            font-weight: 600;
            margin-top: 1.5rem;
            margin-bottom: 1rem;
        }
        
        h3 {
            color: #1565C0;
            font-weight: 600;
            margin-top: 1rem;
            margin-bottom: 0.75rem;
        }
        
        /* Sidebar */
        .sidebar .sidebar-content {
            background-color: #f8f9fa;
        }
        
        /* Button styling */
        .stButton>button {
            border-radius: 4px;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        
        /* Data frame styling */
        .dataframe {
            font-size: 0.9rem;
        }
        
        /* Charts and visualizations */
        .stPlotlyChart {
            margin-top: 1rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
            border-radius: 8px;
            padding: 1rem;
            background-color: white;
        }
        
        /* Tabs styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 2px;
        }
        
        .stTabs [data-baseweb="tab"] {
            padding: 10px 16px;
            background-color: #f1f3f4;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: #1E88E5;
            color: white;
        }
        
        /* Article styling */
        .article-container {
            background-color: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
            line-height: 1.6;
        }
        
        /* Spinner animation */
        .stSpinner > div > div > div {
            border-color: #1E88E5 !important;
        }
        
        /* Input fields */
        div[data-baseweb="input"] {
            border-radius: 4px;
        }
        
        div[data-baseweb="select"] > div {
            border-radius: 4px;
        }
    </style>
    """, unsafe_allow_html=True)

def get_plotly_chart(df):
    """
    Create a Plotly visualization for trends data.
    
    Args:
        df (pandas.DataFrame): DataFrame containing trends data
        
    Returns:
        plotly.graph_objects.Figure: Plotly figure object
    """
    # Create figure
    fig = go.Figure()
    
    # Get list of keywords (columns)
    keywords = df.columns.tolist()
    
    # Add a trace for each keyword
    for keyword in keywords:
        fig.add_trace(
            go.Scatter(
                x=df.index,
                y=df[keyword],
                mode='lines',
                name=keyword,
                hovertemplate='<b>%{x}</b><br>Interest: %{y}<extra></extra>'
            )
        )
    
    # Customize the layout
    fig.update_layout(
        title={
            'text': 'Google Trends Interest Over Time',
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title='Date',
        yaxis_title='Search Interest',
        hovermode='x unified',
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1
        ),
        margin=dict(l=40, r=40, t=60, b=40),
        height=500,
        plot_bgcolor='rgba(245, 247, 249, 0.8)',
        paper_bgcolor='white',
        font=dict(
            family='Arial, sans-serif',
            size=12,
            color='rgb(50, 50, 50)'
        )
    )
    
    # Update axes properties
    fig.update_xaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(230, 230, 230, 0.8)'
    )
    
    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(230, 230, 230, 0.8)',
        range=[0, 105]  # Google Trends data is 0-100
    )
    
    return fig

def create_comparison_chart(df1, df2, title1, title2):
    """
    Create a side-by-side comparison chart of two datasets.
    
    Args:
        df1 (pandas.DataFrame): First DataFrame
        df2 (pandas.DataFrame): Second DataFrame
        title1 (str): Title for first subplot
        title2 (str): Title for second subplot
        
    Returns:
        plotly.graph_objects.Figure: Plotly figure object with subplots
    """
    # Create subplots
    fig = make_subplots(rows=1, cols=2, subplot_titles=(title1, title2))
    
    # Add traces for the first dataset
    for column in df1.columns:
        fig.add_trace(
            go.Bar(x=df1.index, y=df1[column], name=column),
            row=1, col=1
        )
    
    # Add traces for the second dataset
    for column in df2.columns:
        fig.add_trace(
            go.Bar(x=df2.index, y=df2[column], name=column),
            row=1, col=2
        )
    
    # Update layout
    fig.update_layout(
        height=400,
        showlegend=False,
        margin=dict(l=40, r=40, t=60, b=40)
    )
    
    return fig