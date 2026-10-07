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
    total_volume = 0.0
    for part in bom:
        total_volume += part["quantity"] * part["volume_cm3"]  # cm3
    return total_volume


# Calculate the total cost.
def total_cost(bom):
    total_cost = 0.0
    for part in bom:
        total_cost += part["quantity"] * part["unit_cost"]
    return total_cost


# Calculate the totals per material.
def totals_by_materials(bom):
    materials = [part["material"] for part in bom]
    unique_materials = list(dict.fromkeys(materials))
    materials_totals = {material: {} for material in unique_materials}
    for material in unique_materials:
        material_bom = [part for part in bom if part["material"] == material]
        materials_totals[material]["total_parts"] = total_parts(material_bom)
        materials_totals[material]["total_volume"] = total_volume(material_bom)
        materials_totals[material]["total_cost"] = total_cost(material_bom)
    return materials_totals


print(total_parts(bom))
print(f"${total_cost(bom):.2f}")
print(f"{total_volume(bom):.1f} cm\u00b3")
results = totals_by_materials(bom)
for material, totals in results.items():
    print(material)
    print(f"Parts: {totals['total_parts']}")
    print(f"Volume: {totals['total_volume']:.1f} cm\u00b3")
    print(f"Cost: ${totals['total_cost']:.2f}")
