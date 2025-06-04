import time
import requests
import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


nltk.download([
    'punkt',
    'punkt_tab',
    'wordnet',
    'averaged_perceptron_tagger'
])


def type_text(text, delay=0.03):
    """Prints text character-by-character to simulate typing."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    }  
}


for coin in crypto_db:
    print(f"{coin} - Trend: {crypto_db[coin]['price_trend']} | Sustainability: {crypto_db[coin]['sustainability_score']}")


def greet():
    type_text("🌟 CryptoBuddy is online! Let's find you a green and growing crypto!")


def get_crypto_price(crypto_name):
    try:
        response = requests.get(
            "https://api.coingecko.com/api/v3/simple/price", 
            params={
                "ids": crypto_name.lower(),
                "vs_currencies": "usd"
            }
        )
        data = response.json()
        return data[crypto_name.lower()]["usd"]
    except Exception as e:
        return None


def crypto_advice(user_query):
    def safe_reply(text):
        return f"{text}\n\n⚠️ Crypto is risky—always do your own research!"

    user_query = user_query.lower()

    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(user_query)
    lemmas = [lemmatizer.lemmatize(word) for word in tokens]

    trending_keywords = ["trend", "rise", "up", "growing"]
    sustainable_keywords = ["sustain", "green", "eco", "friendly", "long term"]
    buy_keywords = ["buy", "invest", "recommend", "suggest"]
    risk_keywords = ["risk", "danger", "safe", "secure"]

    if any(word in lemma for lemma in lemmas for word in trending_keywords):
        rising_cryptos = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        if rising_cryptos:
            result = ", ".join(rising_cryptos)
            reply = safe_reply(f"📈 These cryptos are trending up: {result}!")
        else:
            reply = safe_reply("❌ Sorry, no cryptocurrencies are currently trending up.")

    elif any(word in lemma for lemma in lemmas for word in sustainable_keywords):
        sustainable_coin = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        score = crypto_db[sustainable_coin]["sustainability_score"] * 10
        reply = safe_reply(f"🌱 Invest in {sustainable_coin}! It has a sustainability score of {score:.1f}/10 and great long-term potential!")

    elif any(word in lemma for lemma in lemmas for word in buy_keywords):
        recommendations = []
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] >= 7 / 10:
                recommendations.append(coin)

        if recommendations:
            reply = safe_reply(f"🚀 Consider investing in {', '.join(recommendations)}! It's rising and highly sustainable.")
        else:
            reply = safe_reply("⚠️ No coins match both high growth and sustainability right now.")

    elif any(word in lemma for lemma in lemmas for word in risk_keywords):
        reply = safe_reply("🚨 Crypto is risky—always do your own research before investing!")

    elif "price" in lemmas or "how much" in lemmas:
        crypto_names = list(crypto_db.keys())
        matched = next((name for name in crypto_names if name.lower() in user_query), None)
        if matched:
            price = get_crypto_price(matched)
            if price:
                reply = safe_reply(f"💰 The current price of {matched} is ${price:,.2f}.")
            else:
                reply = safe_reply(f"❌ Could not fetch the price for {matched}.")
        else:
            reply = safe_reply("🤖 Please specify which cryptocurrency you want the price for.")

    else:
        reply = safe_reply("🤖 Hmm... I didn't understand that. Try asking about trends, sustainability, investment advice, or prices.")

    type_text(reply)

def chat():
    greet()
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            type_text("👋 CryptoBuddy is logging off. Stay safe out there!")
            break
        crypto_advice(user_input)


if __name__ == "__main__":
    chat()
