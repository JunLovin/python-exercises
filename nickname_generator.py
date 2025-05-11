def nickname_generator(name):
    if len(name) <= 3:
        return "Error: Name too short"

    vowels = 'aeiou'
    nickname = ''

    if name[2] in vowels:
        nickname = name[:4]
    else:
        nickname = name[:3]
    return nickname

print(nickname_generator('Jimmy'))
