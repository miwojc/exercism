def response(hey_bob=""):
    """
    Bob is a lackadaisical teenager. In conversation, his responses are very limited.

    Bob answers 'Sure.' if you ask him a question, such as "How are you?".

    He answers 'Whoa, chill out!' if you YELL AT HIM (in all capitals).

    He answers 'Calm down, I know what I'm doing!' if you yell a question at him.

    He says 'Fine. Be that way!' if you address him without actually saying anything.

    He answers 'Whatever.' to anything else.
    """
    if hey_bob.isupper():
        if hey_bob.endswith("?"):
            response = "Calm down, I know what I'm doing!"
        else:
            response = "Whoa, chill out!"
    elif hey_bob.endswith("?"):
        response = "Sure."
    elif hey_bob == "":
        response = "Fine. Be that way!"
    else:
        response = "Whatever."
    return response
