from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from config import Config

credential = AzureKeyCredential(Config.key)
text_analytics_client = TextAnalyticsClient(endpoint=Config.endpoint, credential=credential)

def is_negative_comment(comment_text):
    try:
        return get_sentiment(comment_text) == "negative"
    except Exception as e:
        print("Eroare analiză sentiment:", e)
        return False

def get_sentiment(text):
    response = text_analytics_client.analyze_sentiment([text])[0]

    return response.sentiment