import paralleldots
paralleldots.set_api_key("g3HKhLRm4rCMYcteWGrdpqlxxTJNFRRV9Kzoiy8LAvg")

def ner(text):
    ner = paralleldots.ner(text)
    return ner
