BRANCHES = {
    "mumbai": "Mumbai Main Branch - Nariman Point",
    "pune": "Pune Branch - Shivaji Nagar",
    "delhi": "Delhi Branch - Connaught Place"
}


def locate_branch(city):

    city = city.lower()

    return BRANCHES.get(
        city,
        "No branch found for this city."
    )