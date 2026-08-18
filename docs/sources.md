# Sources and evidence policy

This public repository separates three kinds of evidence:

1. **Installed-state observations** from the completed machine.
2. **Receipt-backed acquisition data**, published only after removing location, order, payment, and identifying details.
3. **Manufacturer documentation** for product specifications.

Raw evidence, receipts, hardware identifiers, network information, and unredacted logs are intentionally excluded.

## Project sources

- [Part 1 build article](https://blog.zacharycangemi.com/2026/08/18/my-new-ai-cluster-go-big-or-go-home-part-1/)
- [V1 build article](https://blog.zacharycangemi.com/2026/04/29/48-gb-of-vram-and-a-dream-part-1-the-build/)
- [V1 infrastructure repository](https://github.com/zacangemi/local-llm-infrastructure)
- [Part 3 inference-lab repository](https://github.com/zacangemi/local-llm-inference-lab)

## First-party hardware references

- [AMD Ryzen Threadripper PRO 9955WX specifications](https://www.amd.com/en/products/processors/workstations/ryzen-threadripper/9000-wx-series/amd-ryzen-threadripper-pro-9955wx.html)
- [ASUS Pro WS WRX90E-SAGE SE specifications](https://www.asus.com/us/motherboards-components/motherboards/workstation/pro-ws-wrx90e-sage-se/techspec/)
- [Phanteks Enthoo Pro II Server Edition TG specifications](https://phanteks.com/product/enthoo-pro-2-server-edition-tg/)
- [Phanteks T30-120 specifications](https://phanteks.com/product/t30-120/)
- [Noctua NH-U14S TR5-SP6 specifications](https://www.noctua.at/en/products/nh-u14s-tr5-sp6/specifications)
- [Kingston KF564R32RBEK8-128 data sheet](https://www.kingston.com/datasheets/KF564R32RBEK8-128.pdf)
- [NVIDIA GeForce RTX 3090 specifications](https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090/)
- [Corsair AX1600i specifications](https://www.corsair.com/us/en/p/psu/cp-9020087-na/ax1600i-digital-atx-power-supply-1600-watt-fully-modular-psu-cp-9020087-na)
- [Samsung 9100 PRO 2 TB specifications](https://www.samsung.com/us/business/memory-storage/nvme-ssd/9100-pro-nvme-ssd-sku-mz-vap2t0b-am/)
- [Intel X710-T2L specifications](https://www.intel.com/content/www/us/en/products/sku/189463/intel-ethernet-network-adapter-x710t2l/specifications.html)
- [ASPEED AST2600 specifications](https://www.aspeedtech.com/server_ast2600/)
- [Zero Surge 2R Series product information](https://zerosurge.com/wp-content/uploads/2025/01/2R-Series-01-24-2.pdf)
- [Ubuntu 24.04.4 LTS release notes](https://documentation.ubuntu.com/release-notes/24.04/4/)

## Publication rules used here

- Installed, purchased, planned, and supported are treated as different states.
- Combined physical VRAM is not described as transparently pooled memory.
- Component telemetry is not described as wall power.
- Adapter capability is not described as end-to-end network performance.
- Manufacturer maximums are not described as measured local results.
- Private evidence is summarized or derived, never published raw.
- Known limitations and failed gates remain visible.
