# Owner: @goku_bhai001
# Developer: @goku_bhai001
# Ask Doubt on telegram @goku_bhai001


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "25649636"))
    API_HASH = getenv("API_HASH", "43af470d1c625e603733268b3c2f7b8f")
    BOT_TOKEN = getenv("BOT_TOKEN", "8172435706:AAHvbcHdA9-X6fHxpbbzf4krMJ7zjY8Nxv4")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "0")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "895473497 8193608213").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Goku_bhai001:iS5sYySFKS2xZZpc@cluster0.voj0eyt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Owner: @goku_bhai001
# Developer: @goku_bhai001
# Ask Doubt on telegram @goku_bhai001
