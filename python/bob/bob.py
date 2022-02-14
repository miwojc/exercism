def response(hey_bob=""):
    """
    Bob is a lackadaisical teenager. In conversation, his responses are very limited.

    Bob answers 'Sure.' if you ask him a question, such as "How are you?".

    He answers 'Whoa, chill out!' if you YELL AT HIM (in all capitals).

    He answers 'Calm down, I know what I'm doing!' if you yell a question at him.

    He says 'Fine. Be that way!' if you address him without actually saying anything.

    He answers 'Whatever.' to anything else.
    """
    message = hey_bob.strip()
    if not message:
        return "Fine. Be that way!"
    elif message.endswith("?") and message.isupper():
        return "Calm down, I know what I'm doing!"
    elif message.endswith("?"):
        return "Sure."
    elif message.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."
