import random

def pass_generator():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    elem_for_pass = alphabet + numbers
    password = ''

    for _ in range(0, random.randint(8, 15)):
        password += elem_for_pass[random.randint(0, len(elem_for_pass) - 1)]

    return password

def at_mail_domain_generator():
    mails = ["gmail", "inbox", "rambler", "unecon", "ya", "yandex", "live"]
    domains = ["re", "su", "com", "net", "org", "edu"]

    return '@' + mails[random.randint(0, 6)] + '.' + domains[random.randint(0, 5)]

def username_generator():
    names = ["Chris", "Mark", "Chris", "Scarlett", "Jeremy", "Don", "Paul", "Brie", "Karen", "Danai", "Benedict", "Jon",
             "Bradley", "Gwyneth", "Josh", "Benedict", "Tom", "Zoe", "Elizabeth", "Dave", "Evangeline", "Tessa", "Rene",
             "Tilda"]
    surnames = ["Evans", "Ruffalo", "Hemsworth", "Johansson", "Renner", "Cheadle", "Rudd", "Larson", "Gillan", "Gurira",
                "Wong", "Favreau", "Cooper", "Paltrow", "Brolin", "Cumberbatch", "Holland", "Saldana", "Olsen",
                "Bautista",
                "Lilly", "Thompson", "Russo", "Swinton"]

    return names[random.randint(0, 23)] + '_' + surnames[random.randint(0, 23)]


print_out = open('email.txt', 'w')

for _ in range(0, 1000):
    print(username_generator() + at_mail_domain_generator() + ' ' + pass_generator(), file = print_out)