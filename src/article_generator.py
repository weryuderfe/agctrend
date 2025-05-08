import pandas as pd
import random
from datetime import datetime

class ArticleGenerator:
    """Class for generating articles based on Google Trends data."""
    
    def __init__(self):
        """Initialize the ArticleGenerator with templates."""
        self.templates = {
            'informative': {
                'intro': [
                    "Recent data from Google Trends reveals a significant increase in interest for {keyword}. Let's explore what's driving this trend and why it matters.",
                    "Google Trends has highlighted {keyword} as a topic of growing interest. In this article, we'll analyze the data and provide insights on this trend.",
                    "{keyword} has been gaining traction according to recent Google Trends data. We'll break down what this means and why it's important to be aware of this trend."
                ],
                'body': [
                    "The data shows that interest in {keyword} has been {trend_direction} over {timeframe}. This suggests that {insight}.",
                    "When examining related topics such as {related_topic1} and {related_topic2}, we can see a correlation with the interest in {keyword}.",
                    "It's worth noting that searches for {related_query1} have also {query_trend}, indicating a broader interest in this subject area.",
                    "Industry experts suggest that the {trend_direction} interest in {keyword} could be attributed to {reason}.",
                    "The geographical distribution of interest shows that {geo_insight}, which may reflect regional differences in adoption or awareness."
                ],
                'conclusion': [
                    "As interest in {keyword} continues to evolve, staying informed about these trends can provide valuable insights for researchers, businesses, and consumers alike.",
                    "Monitoring these trends in {keyword} will be crucial for understanding future developments in this area and their potential impact.",
                    "Whether you're a professional in the field or simply curious about {keyword}, these trends offer a glimpse into the collective interests and priorities of online users."
                ]
            },
            'analytical': {
                'intro': [
                    "This analytical examination of Google Trends data reveals compelling patterns regarding {keyword}. The following analysis breaks down the key metrics and their implications.",
                    "An in-depth analysis of {keyword} based on Google Trends data demonstrates noteworthy patterns that warrant closer examination. Let's explore the numbers and their significance.",
                    "The quantitative assessment of {keyword} through Google Trends reveals statistically significant trends. This analysis will decompose the data to extract actionable insights."
                ],
                'body': [
                    "Examining the trend coefficient for {keyword}, we observe a {trend_direction} with a notable correlation to {related_topic1}. This statistical relationship suggests {insight}.",
                    "When performing comparative analysis between {keyword} and adjacent search terms like {related_query1}, we detect a pattern that indicates {pattern_insight}.",
                    "The temporal distribution of search interest demonstrates cyclical patterns with peaks occurring around {peak_insight}. This periodicity may be attributed to {reason}.",
                    "Regional variance analysis shows a standard deviation of interest across different geographical areas, with particular concentration in {geo_insight}.",
                    "Correlation coefficients between {keyword} and {related_topic2} suggest a causal relationship that merits further investigation, particularly regarding {specific_aspect}."
                ],
                'conclusion': [
                    "The data-driven insights regarding {keyword} point to several strategic implications that stakeholders should consider when formulating long-term strategies.",
                    "This analytical framework for understanding {keyword} trends provides a foundation for predictive modeling and anticipatory planning in related domains.",
                    "Continued quantitative monitoring of these metrics will be essential for maintaining an accurate understanding of how interest in {keyword} evolves over time."
                ]
            },
            'persuasive': {
                'intro': [
                    "The dramatic rise in interest for {keyword} revealed by Google Trends cannot be ignored. This shift represents a crucial opportunity that forward-thinking individuals and organizations must embrace.",
                    "Google Trends has uncovered a compelling story about {keyword} that demands attention. The data clearly shows why this topic should be at the forefront of your consideration.",
                    "If you're not paying attention to {keyword}, you're missing out on a significant trend. Google's search data reveals why this topic deserves your immediate focus."
                ],
                'body': [
                    "The evidence is clear: interest in {keyword} has {trend_direction} by a remarkable margin. This isn't just a temporary blip—it's a fundamental shift that will reshape how we think about {broader_category}.",
                    "Consider how {related_topic1} connects with {keyword}. This relationship highlights an unmistakable pattern that savvy observers are already leveraging to their advantage.",
                    "When people search for {related_query1}, they're expressing a genuine need. The {query_trend} in these searches demonstrates the growing importance of addressing this topic.",
                    "Leaders in this space are already capitalizing on the growing interest in {keyword}. Those who hesitate to acknowledge this trend risk being left behind as the landscape evolves.",
                    "The regional data is particularly telling—{geo_insight} shows that this isn't just a localized phenomenon but a widespread movement gaining momentum across diverse areas."
                ],
                'conclusion': [
                    "The time to act on these {keyword} trends is now. As interest continues to grow, early adopters will secure the advantages that come with foresight and decisive action.",
                    "Don't allow your competitors to monopolize the opportunities presented by the rising interest in {keyword}. Use these insights to position yourself at the forefront of this important development.",
                    "The Google Trends data makes a compelling case: {keyword} represents not just a passing interest but a significant shift that will continue to influence preferences and behaviors moving forward."
                ]
            },
            'entertaining': {
                'intro': [
                    "Well, well, well... looks like {keyword} is having quite the moment in the spotlight! Google Trends has caught this rising star, and we're here for the gossip.",
                    "Hold onto your search bars, folks! {keyword} is trending faster than celebrity scandals. Let's dive into this Google Trends phenomenon with a smile.",
                    "In today's episode of 'What's Breaking the Internet?' we have {keyword} stealing the show. Google Trends has the receipts, and we've got the story."
                ],
                'body': [
                    "The trend line for {keyword} is going {trend_direction} faster than my motivation on a Monday morning. This sudden fame might be because {humorous_reason}.",
                    "People are also searching for {related_query1}, which is like the quirky sidekick to our main character {keyword}. They go together like awkward small talk and elevator rides.",
                    "Interestingly, {related_topic1} is riding on the coattails of {keyword}'s newfound popularity. It's the classic 'I knew them before they were famous' situation.",
                    "The geographical data shows that folks in {geo_insight} are particularly obsessed. Perhaps they have less exciting things to Google? No judgment here!",
                    "If {keyword} were a celebrity, its publicist would be popping champagne right now. Its rise to fame has been more dramatic than the plot twists in my favorite binge-worthy shows."
                ],
                'conclusion': [
                    "Whether {keyword} is having its fifteen minutes of fame or settling in for a long-term relationship with the limelight, one thing's certain: it's more popular than my attempts at home haircuts during quarantine.",
                    "So there you have it—{keyword} is trending, and now you're in the loop. Feel free to casually drop this knowledge at your next social gathering to appear both informed and effortlessly cool.",
                    "Will {keyword} continue its reign of search supremacy, or will it join the ranks of forgotten trends like planking and fidget spinners? Only time (and Google Trends) will tell!"
                ]
            },
            'conversational': {
                'intro': [
                    "Have you noticed how {keyword} seems to be everywhere these days? It's not just you—Google Trends confirms this topic is gaining serious traction. Let's chat about what's going on.",
                    "So, I was looking at Google Trends the other day and couldn't help but notice that {keyword} is really taking off. I thought we might explore why that is and what it means for us.",
                    "Hey there! Wondering why everyone's suddenly talking about {keyword}? Google's search data shows there's a real surge of interest, and I think it's worth unpacking together."
                ],
                'body': [
                    "You know how trends come and go, right? Well, with {keyword}, we're seeing something interesting—interest has been {trend_direction} steadily. My take is that {conversational_insight}.",
                    "What's really caught my attention is how {related_topic1} ties into all this. It's like when you start thinking about one thing, and it naturally leads you to another connected idea.",
                    "People are also asking about {related_query1} a lot more. Does that surprise you? I find it makes sense because when you're exploring {keyword}, that question naturally comes up.",
                    "Between you and me, I think the reason we're seeing this trend might be {reason}. What do you think? Does that resonate with your experience?",
                    "It's fascinating to see that people in {geo_insight} are particularly interested in this topic. I wonder if that's because of {regional_reason} or if it's just coincidence."
                ],
                'conclusion': [
                    "At the end of the day, whether {keyword} is just having a moment or becoming a lasting part of our conversations, it's always interesting to see what captures our collective attention, isn't it?",
                    "So what do you make of all this? Is {keyword} something that matters in your world, or is it just another trending topic that will fade away? I'd love to hear your thoughts!",
                    "As we keep an eye on how interest in {keyword} develops, I think it's worth considering how these trends reflect our changing priorities and interests as a society. Just some food for thought!"
                ]
            }
        }
    
    def generate_article(self, keyword, related_topics_data, related_queries_data, tone="informative", length="medium"):
        """
        Generate an article based on trends data.
        
        Args:
            keyword (str): The main keyword for the article
            related_topics_data (dict): Dictionary containing related topics data
            related_queries_data (dict): Dictionary containing related queries data
            tone (str): Tone of the article (informative, analytical, persuasive, entertaining, conversational)
            length (str): Length of the article (short, medium, long)
            
        Returns:
            str: Generated article
        """
        # Default to informative if tone not found
        if tone not in self.templates:
            tone = "informative"
        
        # Select template
        template = self.templates[tone]
        
        # Extract related topics if available
        related_topics = []
        if 'top' in related_topics_data and related_topics_data['top'] is not None:
            related_topics = related_topics_data['top']['topic_title'].tolist() if 'topic_title' in related_topics_data['top'].columns else []
        elif 'rising' in related_topics_data and related_topics_data['rising'] is not None:
            related_topics = related_topics_data['rising']['topic_title'].tolist() if 'topic_title' in related_topics_data['rising'].columns else []
        
        # Extract related queries if available
        related_queries = []
        if 'top' in related_queries_data and related_queries_data['top'] is not None:
            related_queries = related_queries_data['top']['query'].tolist() if 'query' in related_queries_data['top'].columns else []
        elif 'rising' in related_queries_data and related_queries_data['rising'] is not None:
            related_queries = related_queries_data['rising']['query'].tolist() if 'query' in related_queries_data['rising'].columns else []
        
        # Create placeholders
        replacements = {
            'keyword': keyword,
            'trend_direction': random.choice(['increasing', 'rising', 'growing', 'surging', 'climbing']),
            'timeframe': random.choice(['the past week', 'recent months', 'the last quarter', 'this year']),
            'insight': random.choice([
                'there is growing public interest in this area', 
                'this topic is becoming increasingly relevant in today\'s context', 
                'more people are seeking information on this subject',
                'this represents a shift in public awareness and curiosity'
            ]),
            'related_topic1': related_topics[0] if related_topics else 'related subjects',
            'related_topic2': related_topics[1] if len(related_topics) > 1 else 'similar topics',
            'related_query1': related_queries[0] if related_queries else 'common questions',
            'query_trend': random.choice(['increased', 'grown', 'expanded', 'risen']),
            'reason': random.choice([
                'recent developments in the field', 
                'increased media coverage', 
                'growing awareness of its importance',
                'changing consumer preferences',
                'technological advancements'
            ]),
            'geo_insight': random.choice([
                'certain regions show notably higher interest', 
                'interest varies significantly by location', 
                'some areas show disproportionately high engagement',
                'interest is concentrated in specific geographical areas'
            ]),
            'broader_category': random.choice([
                'this industry', 
                'this field', 
                'related sectors',
                'the market',
                'consumer behavior'
            ]),
            'humorous_reason': random.choice([
                'everyone suddenly decided to become an expert overnight', 
                'it\'s the internet\'s new obsession',
                'we all collectively decided it was worth our attention',
                'it\'s more entertaining than watching paint dry'
            ]),
            'conversational_insight': random.choice([
                'people are genuinely curious to learn more about it', 
                'it touches on something many of us are experiencing right now',
                'it addresses a common challenge or opportunity',
                'it connects to broader changes happening in our society'
            ]),
            'pattern_insight': random.choice([
                'a growing ecosystem of related interests', 
                'shifting priorities among searchers',
                'an evolution in how people think about this topic',
                'emerging connections between previously separate domains'
            ]),
            'peak_insight': random.choice([
                'specific events or announcements', 
                'seasonal factors',
                'cyclical industry developments',
                'media coverage spikes'
            ]),
            'specific_aspect': random.choice([
                'user adoption patterns', 
                'market development stages',
                'information-seeking behaviors',
                'public perception shifts'
            ]),
            'regional_reason': random.choice([
                'local policies or initiatives', 
                'cultural factors',
                'regional economic conditions',
                'community interests'
            ])
        }
        
        # Generate intro paragraph
        intro = random.choice(template['intro'])
        for key, value in replacements.items():
            intro = intro.replace(f"{{{key}}}", value)
        
        # Generate body paragraphs based on length
        if length == "short":
            num_paragraphs = random.randint(2, 3)
        elif length == "medium":
            num_paragraphs = random.randint(4, 6)
        else:  # long
            num_paragraphs = random.randint(7, 10)
        
        body_paragraphs = []
        # Ensure we don't exceed the template's body paragraphs
        num_paragraphs = min(num_paragraphs, len(template['body']))
        
        for _ in range(num_paragraphs):
            paragraph = random.choice(template['body'])
            for key, value in replacements.items():
                paragraph = paragraph.replace(f"{{{key}}}", value)
            body_paragraphs.append(paragraph)
        
        # Generate conclusion
        conclusion = random.choice(template['conclusion'])
        for key, value in replacements.items():
            conclusion = conclusion.replace(f"{{{key}}}", value)
        
        # Assemble the article
        current_date = datetime.now().strftime("%B %d, %Y")
        title = f"Trending Insights: Understanding the Rise of {keyword}"
        
        article = f"# {title}\n\n"
        article += f"*Published on {current_date}*\n\n"
        article += f"{intro}\n\n"
        article += "\n\n".join(body_paragraphs) + "\n\n"
        article += f"{conclusion}\n\n"
        article += f"*This article was generated based on Google Trends data for '{keyword}'.*"
        
        return article