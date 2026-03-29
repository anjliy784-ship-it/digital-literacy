def check_password (password) :
    if len(password) < 6 :
        return "weak password"
    elif len(password) < 10  :
         return "medium password "
    else :
        return "strong password"