age = 11
has_fairy = True

if age >= 11 and has_fairy:
    print("Hey! Listen!")
    print("Hey! Listen!")
    # ...
    print("Hey! Listen!")
elif has_fairy:
    print("Hey! Listen!")
else:
    print("Silence")

print("This will always print")

certificate = '12A'  # U,PG,12,12A,15,18
certificate = certificate.upper()

if certificate == 'U':
    print("Suitable for all ages")
elif certificate == 'PG':
    print("Follow parental guidance")
elif certificate in ('12', '12A'):
    print("For twelve and above")
elif certificate == '15':
    print("Fifteen years or older")
elif certificate == '18':
    print("Adults only")
else:
    print("Certification not recognized")
