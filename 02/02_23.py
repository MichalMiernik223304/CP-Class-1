vat_tax_rate = 23
amount = float(input("Enter amount:"))
vat = round(amount * vat_tax_rate/(100+vat_tax_rate), 2)

print(f"Amount: {amount}zł\nVAT 23%: {vat}")
