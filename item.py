class Item:
  def __init__(self, vendor, barcode, size, weight):
    self.vendor = vendor
    self.barcode = barcode
    self.size = size
    self. weight = weight
  
  def display_info(self):
    print(f"Vendor: {self.vendor}")
    print(f"Barcode: {self.barcode}")
    print(f"Size: {self.size}")
    print(f"Weight: {self.weight}")