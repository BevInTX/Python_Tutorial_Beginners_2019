
def lbs_to_kg(weight):
    return weight * 0.45

def kg_to_lbs(weight):
    return weight / 0.45

def main():
    orig_lb = 20
    print(f"Original weight: {orig_lb} pounds")
    kg = lbs_to_kg(orig_lb)
    print(f"Converted {orig_lb} pounds to {kg} kilograms")
    converted_lb = kg_to_lbs(kg)
    print(f"Converted {kg} kilograms back to {converted_lb} pounds")

if __name__ == "__main__":
    main()