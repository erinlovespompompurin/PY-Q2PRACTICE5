from pyscript import document, display

def check_country(e):
    country = {
        "ph" : "Philippines",
        "au" : "Australia",
        "jp" : "Japan",
        "sg" : "Singapore",
        "fr" : "France"
    }

    country_code = document.getElementById("countries").value

    display(country.get(country_code, "Country code not found"), target = "output1")