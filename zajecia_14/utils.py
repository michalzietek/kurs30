import requests


def retrieve_data_from_api(country_name):
    url_address = f"https://restcountries.com/v3.1/name/{country_name}?fullText=true"
    response = requests.get(url_address)

    if response.status_code == 200:
        print("Hura udało się pobrać!")
        return parse_data_from_response_to_valid_dict(response_body=response.json())
    else:
        print("Niestety nie ma takiego kraju. Może polecisz na wakacje do San Escobar z Witoldem Waszczykowskim?")


def parse_data_from_response_to_valid_dict(response_body):
    return {
        "name": response_body[0].get("name").get("common"),
        "capital": response_body[0].get("capital")[0],
        "region": response_body[0].get("region"),
        "subregion": response_body[0].get("subregion"),
        "languages": response_body[0].get("languages"),
        "currency": response_body[0].get("currencies"),
        "flag": response_body[0].get("flag")
    }

