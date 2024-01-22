languages = {
    "Hazik" : {
        "favourite languages" : ["java","python","c"]
    },
    "Faik" : {
        "favourite games" : ["IT TAKES 2","VALORANT"]
    }
}
print(languages)

nested = {
    "BGMI" : {
        "ID" : {
            "LEVEL" : 75,
            "NAME" : "FAIK",
            "KD" : 5
        }
    },
    "VALORANT" : {
        "VID" : {
            "NAME" : "RAY",
            "LEVEL" : 70,
            "KD" : 1.2
        }
    }
}
print(nested)

def add_new_user(name, langs, exp):
    newu = {}
    newu["user_name"] = name
    newu["favourite_languages"] = langs
    newu["experience"] = exp
    programming_language.append(newu)
    print(newu)
programming_language = [
    {"user_name" : "Elshad",
     "favorite_languages" : ["Python", "Java", "C#"],
     "experience": 10
    },
    {"user_name":"Renad",
     "favorite_languages" : ["Scratch","Python"],
     "experience" : 2
    },
]

add_new_user("Edy", ["Java", "Kotlin", "Swift"], 10)