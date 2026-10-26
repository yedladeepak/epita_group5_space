
import json
import pdb

records = [
    {"volume": "100", "weight": "10"},
    {"volume": "200", "weight": "20"},
    {"volume": "350", "weight": "60"},
    {"volume": "invalid", "weight": "5"},
]

successful_entries = 0
total_volume = 0.0
high_impact_count = 0

for record in records:
    try:
        volume = float(record["volume"])
        weight = float(record["weight"])
    except (ValueError, TypeError):
        continue

    successful_entries += 1
    total_volume += volume

    if weight >= 50:
        high_impact_count += 1

avg_volume = (
    total_volume / successful_entries
    if successful_entries else 0.0
)

result = {
    "successful_entries": successful_entries,
    "total_volume": total_volume,
    "avg_volume": avg_volume,
    "high_impact_count": high_impact_count,
}

print(result)
