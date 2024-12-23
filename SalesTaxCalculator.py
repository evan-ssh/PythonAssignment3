def main():
 while True:
  user_items = GetItems()
  total_of_items = (sum(user_items))
  sales_tax = GetSalesTax(total_of_items)
  total_of_sale = GetTotal(total_of_items, sales_tax)
  print(f"Total: {total_of_items:.2f}")
  print(f"Sales tax: {sales_tax:.2f}")
  print(f"Total After Tax: {total_of_sale:.2f}")

def GetItems():
    items = []
    while True:
        print("Enter items(Enter 0 To End)")
        cost_item = float(input("Enter An Item: "))
        if cost_item == 0:
          break
        items.append(cost_item)
    return items

def GetSalesTax(total_of_items):
  sales_tax = total_of_items * 0.06
  return sales_tax

def GetTotal(total_of_items, sales_tax):
  total_of_sale = total_of_items + sales_tax
  return total_of_sale


main()