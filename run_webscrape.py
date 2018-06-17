from webscrape import export_results
from send_email import send_email

def begin():
    locations = ["San_Francisco", "Peninsula"]
    filename = "housing_results.csv"
    final_csv = export_results("San_Francisco", filename)
    print(final_csv)
    print(send_email(filename))

begin()
