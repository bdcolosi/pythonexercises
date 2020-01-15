bill_amount = int(input("How much was the bill? "))

service_level = input("Level of service? ")
    
def service(service_level):
    if service_level == "good":
        print((.2 * bill_amount) + bill_amount)
    if service_level == "fair":
        print((.15 * bill_amount)+ bill_amount)
    if service_level == "bad":
        print((.1 * bill_amount)+ bill_amount)

service(service_level)