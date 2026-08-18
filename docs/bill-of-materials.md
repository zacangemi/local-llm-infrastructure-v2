# Public bill of materials

This ledger reproduces the cost scope used by the published Part 1 article. Store locations, receipt/order identifiers, payment details, serial numbers, and private evidence paths are intentionally omitted.

## Accounting definitions

- **Item price:** hardware price before a separately listed paid protection plan, shipping, and tax.
- **Pre-tax total:** item price plus protection plan and shipping.
- **Post-tax total:** the historical amount paid for that row.
- **V2-acquired:** components obtained specifically for V2, including the gifted NVMe at its paid acquisition value.
- **V1 carryover:** hardware moved from V1, valued at its original paid acquisition amount. The two historical GPU plans are included to match the published article.
- **Tracked acquisition value:** historical accounting across different purchase dates. It is not current resale value or replacement cost.

## Component ledger

| Component | Origin | Date | Vendor | Item | Plan | Shipping | Pre-tax | Tax | Post-tax |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| Noctua NH-U14S TR5-SP6 CPU cooler | New for V2 | 2026-01-13 | Micro Center | $139.99 | $0.00 | $0.00 | $139.99 | $12.08 | $152.07 |
| ASUS Pro WS WRX90E-SAGE SE | New for V2 | 2026-02-03 | Micro Center | $1,199.99 | $139.99 | $0.00 | $1,339.98 | $115.64 | $1,455.62 |
| Phanteks Enthoo Pro II Server Edition TG | New for V2 | 2026-01-06 | Phanteks | $189.99 | $0.00 | $40.00 | $229.99 | $0.00 | $229.99 |
| AMD Ryzen Threadripper PRO 9955WX | New for V2 | 2026-05-06 | Micro Center | $1,499.99 | $139.99 | $0.00 | $1,639.98 | $141.53 | $1,781.51 |
| Kingston FURY Renegade Pro 128 GB kit | New for V2 | 2026-05-22 | CDW | $3,686.48 | $0.00 | $50.98 | $3,737.46 | $322.35 | $4,059.81 |
| 10× Phanteks T30-120 fan order | New for V2 | 2026-03-12 | Phanteks | $384.96 | $0.00 | $0.00 | $384.96 | $0.00 | $384.96 |
| 1× Phanteks T30-120 add-on/spare | New for V2 | 2026-04-21 | Phanteks | $39.99 | $0.00 | $5.00 | $44.99 | $4.00 | $48.99 |
| Samsung 9100 PRO 2 TB NVMe | Gifted for V2 | 2025-12-18 | Amazon | $304.97 | $0.00 | $0.00 | $304.97 | $21.35 | $326.32 |
| RTX 3090 FE — GPU 0 | V1 carryover | 2024-11-03 | Micro Center | $629.96 | $79.99 | $0.00 | $709.95 | $61.27 | $771.22 |
| RTX 3090 FE — GPU 1 | V1 carryover | 2024-11-26 | Micro Center | $699.99 | $79.99 | $0.00 | $779.98 | $54.60 | $834.58 |
| Corsair AX1600i | V1 carryover | 2024-11-10 | Micro Center | $609.99 | $0.00 | $0.00 | $609.99 | $52.61 | $662.60 |
| Corsair 12-pin GPU cable — GPU 0 | V1 carryover | 2024-11-11 | Corsair | $19.99 | $0.00 | $9.99 | $29.98 | $2.59 | $32.57 |
| Corsair 12-pin GPU cable — GPU 1 | V1 carryover | 2024-11-29 | Corsair | $16.99 | $0.00 | $9.99 | $26.98 | $2.33 | $29.31 |

## Reconciled totals

| Cost scope | Items | Plans | Shipping | Pre-tax | Tax | Post-tax |
|---|---:|---:|---:|---:|---:|---:|
| V2-acquired components | $7,446.36 | $279.98 | $95.98 | $7,822.32 | $616.95 | $8,439.27 |
| V1 carryover and paid plans | $1,976.92 | $159.98 | $19.98 | $2,156.88 | $173.40 | $2,330.28 |
| **Total tracked machine acquisition value** | **$9,423.28** | **$439.96** | **$115.96** | **$9,979.20** | **$790.35** | **$10,769.55** |

Of the V2-acquired total, $326.32 is the value of a gifted NVMe rather than operator out-of-pocket spending. Therefore:

- V2-specific cash purchases: **$8,112.95**
- gifted V2 hardware value: **$326.32**
- V2-acquired total: **$8,439.27**

Support infrastructure—networking accessories, surge protection, and future battery backup—is tracked separately and is not included in the machine total above.

## Reproducibility

The table is backed by [data/bill-of-materials.csv](../data/bill-of-materials.csv). Run the repository validator to recalculate every row and the three public summary scopes:

~~~bash
python3 scripts/validate_repo.py
~~~
