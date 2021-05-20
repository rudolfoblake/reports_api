def validate_age_range(age: int) -> str:
    if 0 < age <= 13:
        return "0 a 13 anos"
    elif 13 < age <= 16:
        return "14 a 16 anos"
    elif 16 < age <= 25:
        return "18 a 25 anos"
    elif 25 < age <= 30:
        return "26 a 30 anos"
    elif 30 < age <= 40:
        return "31 a 40 anos"
    elif 40 < age <= 50:
        return "41 a 50 anos"
    elif 50 < age <= 60:
        return "51 a 60 anos"
    elif 60 < age <= 120:
        return "maior de 61 anos"
