
address = "Lovely Close"

streets = ["street", "road", "drive", "avenue", "boulevard", "close", "crescent"]
if len(address) <= 50 and any(street in address.lower() for street in streets):
    print("Yes")
else:
    print("No")