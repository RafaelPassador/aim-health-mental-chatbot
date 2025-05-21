BLOCKED_KEYWORDS = ["suicídio", "remédio", "matar", "morte", "automutilação"]

def check_guardrails(user_input):
    for word in BLOCKED_KEYWORDS:
        if word in user_input.lower():
            return f"Aviso: não posso responder sobre '{word}'. Procure um profissional de saúde."
    return None
