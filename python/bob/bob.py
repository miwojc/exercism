def response(hey_bob=""):
    """
    Bob is a lackadaisical teenager. In conversation, his responses are very limited.

    Bob answers 'Sure.' if you ask him a question, such as "How are you?".

    He answers 'Whoa, chill out!' if you YELL AT HIM (in all capitals).

    He answers 'Calm down, I know what I'm doing!' if you yell a question at him.

    He says 'Fine. Be that way!' if you address him without actually saying anything.

    He answers 'Whatever.' to anything else.
    """
    hey_bob = hey_bob.strip()
    if hey_bob.endswith("?") and hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    elif hey_bob.endswith("?"):
        return "Sure."
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    elif hey_bob == "":
        return "Fine. Be that way!"
    else:
        return "Whatever."
