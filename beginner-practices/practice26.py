import csv

input_file = "products.csv"
output_file = "products_with_total.csv"

with open(input_file, mode="r", encoding="utf-8") as infile:
    reader = csv.DictReader(infile)

    with open(output_file, mode="w", encoding="utf-8", newline="") as outfile:
        fieldnames = ["Product", "Price", "Quantity", "Total Price"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        writer.writeheader()
        
        for row in reader:
            product = row["Product Name"]
            price = float(row["Price"])
            quantity = int(row["Quantity"])
            total = price * quantity    
        
            writer.writerow({
                "Product": product,
                "Price": price,
                "Quantity": quantity,
                "Total Price": total
            })
    
print("New file created:", output_file)