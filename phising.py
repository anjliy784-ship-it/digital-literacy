import validators 
def detect_phising(message) :
    keywords = [ "urgent" , "click" , "bank" , "otp"]
    for words in keywords :
        if words in message.lower():
            return "⚠️ suspicious message detected ! "
        words = message.split()
        for w in words :
            if validators.url(w) :
                return "⚠️ link detected!"
            return " safe message "