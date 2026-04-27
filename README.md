# Transport Cost Calculator 🚛

A road freight cost estimation tool for cross-border raw material logistics. Originally built to automate trucking cost calculations for DRI (Direct Reduced Iron) shipments on the **Turkey–Iran corridor**.

## Background

Built during procurement work at Vertra Steel (Adana, Turkey) to automate the manual cost breakdown for sourcing raw materials via road transport. The tool replaced a manual spreadsheet process and provides instant cost estimates per route.

## What It Calculates

Given a route (origin → destination with km distance), the calculator outputs:

| Cost Component | Input |
|---|---|
| ⛽ Fuel Cost | Distance, fuel price (TRY/Iran rate), consumption rate |
| 🛡️ Insurance | Monthly insurance cost, prorated per trip |
| 🔧 Maintenance | Annual maintenance cost, prorated per km |
| 🚗 Tires | Annual tire cost, prorated per km |
| 👤 Driver & Other | Monthly driver cost per round trip |
| 🛣️ HGS (Tolls) | Fixed toll cost per route |
| **📊 Total Cost (TRY)** | Full round trip cost |
| **💰 Cost per Ton** | Based on truck capacity |
| **📦 Cost per km** | Efficiency metric |

## Route Example (used in production)

```
Vertra Steel (Ceyhan OSB, Adana) → Kapıköy Customs → Ardekan, Iran
Total Distance: ~1,470 km (one way)
Round Trip: ~2,940 km
```

## Files

```
transport-cost-calculator/
├── calculator.py         # Main cost calculation script
├── config.py             # Default parameters (fuel price, insurance, etc.)
├── sample_output.txt     # Example calculation output
├── README.md
└── requirements.txt
```

## Usage

```bash
pip install -r requirements.txt
python calculator.py --distance-one-way 1470 --capacity 24
```

### Or with custom parameters:

```bash
python calculator.py \
  --distance-one-way 1470 \
  --capacity 24 \
  --fuel-price-try 60 \
  --fuel-price-iran 2 \
  --driver-cost-monthly 150000 \
  --insurance-monthly 20000
```

## Sample Output

```
====================================================
  TRANSPORT COST ESTIMATE — Round Trip
====================================================
  Route Distance (one-way) : 1,470 km
  Round Trip Distance       : 2,940 km
  Truck Capacity            : 24 tons

  Fuel Cost                 : 10,036 TRY
  Insurance                 : 10,000 TRY
  Tire Cost                 : 17,500 TRY
  Maintenance               : 971 TRY
  Driver & Other            : 75,000 TRY
  HGS (Tolls)              : 520 TRY
  ------------------------------------
  Total Round Trip Cost     : 114,027 TRY
  Cost per Ton              : 4,751 TRY/ton
  Cost per km               : 38.78 TRY/km
====================================================
```

## Notes

- Fuel consumption rates: full truck = 1L/3km, empty truck = 1L/4.5km
- Iranian fuel price and Turkish fuel price are configurable separately
- All costs in Turkish Lira (TRY)

---

*Built from real procurement data — not a simulation.*
