import requests
import click


# url = "https://github.com/emsalcengiz"

@click.command()
@click.option('--url', help="web sitesi girilir.", required=True, default="https://github.com/emsalcengiz")
def check_website(url):
    try:
        print("girdiğiniz site adresi:", url)
        r = requests.get(url)
        if(r.status_code == 200):
            print("başarılı")
        else:
            print("başarısız :(")

    except Exception as err:
         print(err)


check_website()