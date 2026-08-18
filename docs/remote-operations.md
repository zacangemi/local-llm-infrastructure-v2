# Remote operations and recovery design

Remote operation was a platform requirement, not an afterthought. The system separates normal administration from hardware-level recovery.

## Normal path

Ubuntu is administered over SSH. This path handles development, model serving, telemetry, service management, and routine shutdown/reboot operations.

## Recovery path

The ASUS motherboard's ASPEED AST2600 BMC remains available independently of Ubuntu and the RTX GPUs. It provides the capabilities needed to:

- view POST and firmware screens;
- enter and change BIOS configuration;
- inspect motherboard-exposed sensors;
- recover when the operating system or normal network path is unavailable; and
- keep both compute GPUs free from display duties.

Management access is isolated behind a separate control path. This repository documents the design principle without publishing addresses, credentials, firewall rules, device identifiers, or physical-location details.

## Power protection state

A Zero Surge 2R15W series-mode protection layer is installed for the server PSU and management relay device. A compatible UPS remains a planned addition. Until that battery-backed layer is installed and validated, the repository does not claim graceful ride-through during an outage.

A UPS will provide ride-through time and controlled shutdown capability. It will not increase the capacity of the household branch circuit.

## Recovery philosophy

1. Use SSH for ordinary work.
2. Use BMC/IPMI when the operating system cannot provide control.
3. Preserve known-good BIOS profiles before changing memory or platform settings.
4. Keep management access private and independent of public services.
5. Test recovery paths before trusting them during a real failure.
6. Treat surge protection, battery backup, smoke detection, telemetry, and human intervention as complementary controls—not substitutes for one another.

The actual recovery drills and their evidence are intentionally reserved for the Part 2 commissioning repository.
