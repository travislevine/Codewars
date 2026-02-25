languages_dict = {
    "english": "Welcome",
    "czech": "Vitejte",
    "danish": "Velkomst",
    "dutch": "Welkom",
    "estonian": "Tere tulemast",
    "finnish": "Tervetuloa",
    "flemish": "Welgekomen",
    "french": "Bienvenue",
    "german": "Willkommen",
    "irish": "Failte",
    "italian": "Benvenuto",
    "latvian": "Gaidits",
    "lithuanian": "Laukiamas",
    "polish": "Witamy",
    "spanish": "Bienvenido",
    "swedish": "Valkommen",
    "welsh": "Croeso"
}

def greet(language):
    if not isinstance(language, str):
        return languages_dict["english"]
    normalised = language.lower()
    if normalised in languages_dict:
        return languages_dict[normalised]
    else:
        return languages_dict["english"]
print(greet("fleMish"))
#You have passed all of the tests! :)
#https://www.codewars.com/kata/577ff15ad648a14b780000e7/train/python