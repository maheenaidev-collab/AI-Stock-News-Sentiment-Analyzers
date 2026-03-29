from transformers import pipeline

sentiment = pipeline("sentiment-analysis")

news = [
    "Bitcoin price is expected to rise this year",
    "Crypto market crashed heavily today",
    "Investors are bullish on Ethereum"
]

for n in news:
    result = sentiment(n)
    print(n, result)
