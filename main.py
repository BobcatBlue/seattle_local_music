from ticketmaster_shows import get_shows
import pandas as pd


df = pd.read_csv("Seattle_ticketmaster_venues - Sheet1.csv")
body = ""
shows_tonight = {
    "venue": [],
    "show": [],
    "date": []
}

x = 0
for index, row in df.iterrows():
    venue, bands, date = get_shows(row["Venue Name"], row["vID"])

    shows_tonight["venue"].append(venue)
    shows_tonight["show"].append(bands)
    shows_tonight["date"].append(date)

df_show_data = pd.DataFrame(shows_tonight)
print(df_show_data.to_string())

# for index, row in df.iterrows():
#     venue, bands, date = get_shows(row["Venue Name"], row["vID"])
#     print(venue, bands, date)
#
#     body = body + venue + "\n"
#     all_bands = []
#
#     for b in bands:
#         if "w/" in b:
#             all_bands.extend([nb.strip() for nb in b.split('w/')])
#             bands = all_bands
#         else:
#             pass
#
#     for x, band in enumerate(bands):
#         if x:
#             body = body + band + ", "
#         body = body + band
#
#     body = body + "\n" + date + 2*"\n"

#print(body)