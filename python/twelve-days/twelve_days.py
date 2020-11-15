def recite(start_verse, end_verse):
    days = (
        'first',
        'second',
        'third',
        'fourth',
        'fifth',
        'sixth',
        'seventh',
        'eighth',
        'ninth',
        'tenth',
        'eleventh',
        'twelfth'
    )
    gifts = (
        'twelve Drummers Drumming, ',
        'eleven Pipers Piping, ',
        'ten Lords-a-Leaping, ',
        'nine Ladies Dancing, ',
        'eight Maids-a-Milking, ',
        'seven Swans-a-Swimming, ',
        'six Geese-a-Laying, ',
        'five Gold Rings, ',
        'four Calling Birds, ',
        'three French Hens, ',
        'two Turtle Doves, ',
        'and a Partridge in a Pear Tree.'
    )
    results = []
    for verse in range(start_verse, end_verse+1):
        result=[f"On the {days[verse-1]} day of Christmas my true love gave to me: "]
        if verse >1:
            result.extend(gifts[12-verse:12])
        else:
            result.append('a Partridge in a Pear Tree.')
        results.append("".join(result))
    return results
