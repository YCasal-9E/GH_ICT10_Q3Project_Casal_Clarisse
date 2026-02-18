from pyscript import display, document

def check_eligibility(event):
    document.getElementById('result').innerHTML = ""

    registered = document.getElementById("registered").checked
    medical = document.getElementById("medical").checked
    grade_value = document.getElementById("grade").value
    section = document.getElementById("section").value
    result = document.getElementById("result")

    if grade_value == "" or section == "":
        result.innerHTML = "Please select a grade level and section."
        return

    if not registered and not medical:
        result.innerHTML = "You are not eligible. You must register and secure medical clearance."
        return
    
    if not registered:
        result.innerHTML = "You are not eligible. Please register online."
        return

    if not medical:
        result.innerHTML = "You are not eligible. Please secure a medical clearance."
        return

    grade = int(grade_value)

    team = ""
    image = ""

    if (grade == 7 and section == "Sapphire") or \
       (grade == 8 and section == "Topaz") or \
       (grade == 9 and section == "Sapphire") or \
       (grade == 10 and section == "Sapphire"):
        team = "Green Hornets"
        image = "https://i.postimg.cc/rp9GFMdL/Image-20260129-073102-367.jpg"

    elif (grade == 7 and section == "Topaz") or \
         (grade == 8 and section == "Sapphire") or \
         (grade == 9 and section == "Topaz") or \
         (grade == 10 and section == "Emerald"):
        team = "Yellow Tigers"
        image = "https://i.postimg.cc/CK4CLSZT/Image-20260129-073102-389.jpg"

    elif (grade == 7 and section == "Emerald") or \
         (grade == 8 and (section == "Emerald" or section == "Ruby")) or \
         (grade == 9 and section == "Emerald") or \
         (grade == 10 and section == "Ruby"):
        team = "Blue Bears"
        image = "https://i.postimg.cc/jjh6dtDF/blue-bears-(1).jpg"

    elif (grade == 7 and section == "Ruby") or \
         (grade == 8 and section == "Jade") or \
         (grade == 9 and section == "Ruby") or \
         (grade == 10 and section == "Topaz"):
        team = "Red Bulldogs"
        image = "https://i.postimg.cc/pdBQXR9H/Image-20260129-073102-405.jpg"

    else:
        result.innerHTML = "No team assignment found."
        return

    result.innerHTML = (
        "Congratulations! You are eligible to join the Intramurals.<br>"
        f"Assigned Team: <strong>{team}</strong><br>"
        f"<img src='{image}'>"
    )


from pyscript import document

def verify_account(event):
    document.getElementById('result').innerHTML = ""

    user_val = document.getElementById("username").value
    pass_val = document.getElementById("password").value
    result = document.getElementById("result")

    if user_val == "" or pass_val == "":
        result.innerHTML = "<b>Please enter both username and password.</b>"
        return

    if len(user_val) < 7:
        remaining = 7 - len(user_val)
        result.innerHTML = f"<b>Username must be at least 7 characters long. Please enter {remaining} more character(s).</b>"
        return

    if len(pass_val) < 10:
        remaining = 10 - len(pass_val)
        result.innerHTML = f"<b>Password must be at least 10 characters long. Please enter {remaining} more character(s).</b>"
        return

    has_letter = False
    has_number = False

    for char in pass_val:
        if char.isalpha():
            has_letter = True
        if char.isdigit():
            has_number = True

    if not has_letter:
        result.innerHTML = "<b>Password must contain at least one letter.</b>"
        return

    if not has_number:
        result.innerHTML = "<b>Password must contain at least one number.</b>"
        return

    result.innerHTML = "<b>Account created successfully!</b>"


def showPlayers(event):
    result_div = document.getElementById("result")
    result_div.innerHTML = ""

    players = [
        "Abayon", "Antes", "Apostol", "Banaag", "Barrientos",
        "Casal", "Coeli", "David", "De Mata", "Dela Cruz, F.",
        "Dela Cruz, J.", "Dellejero", "Fukuda", "Gozum", "Ibay",
        "Lim", "Lozano", "Mamauag", "Navarro", "Precones",
        "Ramos", "Sidhu", "Tiu", "Villamayor", "Zaragoza"
    ]

    output = ""

    for player in players:
        output += f"- {player}<br>"

    result_div.innerHTML = output