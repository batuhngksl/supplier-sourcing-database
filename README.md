# Supplier Sourcing Database 📦

A structured B2B supplier database built from real sourcing operations in Turkey and Europe. Covers flooring and textile product categories with full contact and location data.

## Background

This database was compiled during active sourcing work for a European B2B distributor (Home-Worx B2B Global, Antwerp), covering supplier visits and evaluations across Turkey's major textile manufacturing hubs — primarily Gaziantep and Istanbul.

## Product Categories

| Category | # Suppliers |
|---|---|
| Chenille Printed Rugs | 6 |
| Cotton Rugs | 7 |
| Regular Rugs | 9 |
| Tufting Rugs | 7 |
| Wool Rugs | 4 |
| Laminate / PVC / SPC / LVT Flooring | 6 |
| Plastic Rugs | 2 |
| Wall-to-Wall Carpet | 7 |
| Yarn | 10 |
| PVC Mat | 1 |

## Data Fields

Each supplier record includes:
- **Company Name**
- **Contact Person & Title**
- **Email**
- **Phone**
- **Products**
- **Address & City**
- **Visit Date** (where applicable)
- **Importance Rating**

## Files

```
supplier-sourcing-database/
├── data/
│   └── suppliers.csv          # Full supplier list (cleaned, all categories)
├── scripts/
│   └── filter_suppliers.py    # Filter by category, city, or keyword
├── README.md
└── requirements.txt
```

## Usage

```bash
pip install -r requirements.txt
python scripts/filter_suppliers.py --category "Cotton Rugs"
python scripts/filter_suppliers.py --city "Gaziantep"
python scripts/filter_suppliers.py --keyword "tufting"
```

## Sample Output

```
Category: Cotton Rugs | City: Gaziantep
----------------------------------------------
İpek Mekik Halı     | Alfiya Kurbanova  | exportsales4@ipekcarpet.com
İlhan Mensucat      | M.Ercan Kalyancıoğlu | info@ilhanmensucat.com
Vahdet Dokuma       | Ömer Özoğlan      | info@vahdetdokuma.com
```

## Notes

- Supplier data reflects market conditions as of early 2025
- Contact information verified through direct outreach and factory visits
- EU quality standards (OEKO-TEX, ISO 9001) were part of the evaluation criteria

---

*Part of a real B2B sourcing workflow — not a demo dataset.*
