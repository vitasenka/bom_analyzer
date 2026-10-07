bom = [
    {
        "name": "Bracket",
        "material": "PLA",
        "quantity": 2,
        "volume_cm3": 18.5,
        "unit_cost": 0.42,
    },
    {
        "name": "Cover",
        "material": "PETG",
        "quantity": 1,
        "volume_cm3": 32.0,
        "unit_cost": 0.73,
    },
    {
        "name": "Spacer",
        "material": "PLA",
        "quantity": 6,
        "volume_cm3": 2.4,
        "unit_cost": 0.08,
    },
]


# Calculate the total number of parts.
def total_parts(bom):
    total = 0
    for part in bom:
        total += part["quantity"]
    return total


# Calculate the total volume.
def total_volume(bom):
    total = 0.0
    for part in bom:
        total += part["quantity"] * part["volume_cm3"]  # cm3
    return total


# Calculate the total cost.
def total_cost(bom):
    total = 0.0
    for part in bom:
        total += part["quantity"] * part["unit_cost"]
    return total


# Calculate the totals per material.
def totals_by_material(bom):
    materials = [part["material"] for part in bom]
    unique_materials = list(dict.fromkeys(materials))
    materials_totals = {material: {} for material in unique_materials}
    for material in unique_materials:
        material_bom = [part for part in bom if part["material"] == material]
        materials_totals[material]["total_parts"] = total_parts(material_bom)
        materials_totals[material]["total_volume"] = total_volume(material_bom)
        materials_totals[material]["total_cost"] = total_cost(material_bom)
    return materials_totals


# Print the report.
def print_report(parts, cost, volume, materials):
    print(parts)
    print(f"${cost:.2f}")
    print(f"{volume:.1f} cm\u00b3")
    for material, totals in materials.items():
        print(material)
        print(f"Parts: {totals['total_parts']}")
        print(f"Volume: {totals['total_volume']:.1f} cm\u00b3")
        print(f"Cost: ${totals['total_cost']:.2f}")


# Main function to run the report.
def main(bom):
    parts = total_parts(bom)
    cost = total_cost(bom)
    volume = total_volume(bom)
    materials = totals_by_material(bom)
    print_report(parts, cost, volume, materials)


if __name__ == "__main__":
    main(bom)
