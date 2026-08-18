# Limitations and upgrade path

V2 is operational and intentionally expandable. It is not presented as perfect or complete forever.

## Current limitations

### GPU memory is distributed

Two 24 GB cards provide 48 GB of physical VRAM, but frameworks must partition model weights and work across both devices. There is no transparent 48 GB CUDA device.

### No NVLink

No NVLink bridge is installed. Some fine-tuning or communication-heavy workloads may benefit from it, but support and benefit depend on the framework and workload. It is not required for the inference configurations documented by the project.

### CPU-cooling boundary

CPU-only endurance and dual-GPU endurance passed. The intentionally pathological simultaneous maximum CPU plus dual-GPU synthetic test reached the CPU's 95°C regulation boundary while computation remained correct. That corner is not approved for unrestricted unattended use in the current cooling configuration.

### Memory capacity

128 GB is enough to make large hybrid GPU/system-memory inference useful, but it constrains the largest model/draft combinations. The original target was 256–512 GB.

### CPU-side bandwidth

The 16-core 9955WX provides platform access and strong general performance, but its two CCD/L3 domains do not exploit the full simple arithmetic bandwidth of eight DDR5-6000 channels. A 24-core or 32-core Threadripper PRO is the most interesting future CPU path for memory-heavy MoE inference.

### Storage and backup

The system currently relies on one 2 TB NVMe for the operating system, active projects, and active model weights. Planned high-capacity HDD storage will create a working/archive tier, but internal archive disks alone will not constitute a backup.

### Network capability versus available path

The installed X710 adapter is capable of 10GbE. The current upstream network does not yet provide a validated end-to-end 10GbE path.

### Wall power is unmetered

CPU and GPU telemetry measured roughly 920 W during the extreme combined test. That is not a wall measurement and must not be reported as one. PSU conversion loss, other system components, and transients matter.

## Upgrade order

| Priority | Upgrade | Reason |
|---:|---|---|
| 1 | Compatible UPS behind the installed surge-protection layer | Ride-through and controlled shutdown |
| 2 | High-capacity archival storage plus independent backup | Model and dataset capacity without consuming the active NVMe |
| 3 | Finish remaining cable routing and evaluate the optional fan position | Serviceability and incremental airflow work |
| 4 | 24-core or 32-core Threadripper PRO | More CPU-side opportunity for hybrid MoE decode, if workload frequency justifies it |
| 5 | Higher-memory professional GPU | More capacity per slot and better performance-per-watt than stacking additional 3090s |
| Optional | NVLink bridge | Only after a supported fine-tuning workload demonstrates value |

## Upgrade rule

An upgrade should answer a measured bottleneck, reliability need, or repeated workload—not merely make the parts list more impressive. The WRX90 foundation was purchased so that changes can be made one layer at a time without discarding the rest of the machine.
