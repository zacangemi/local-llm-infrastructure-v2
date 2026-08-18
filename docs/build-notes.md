# Build notes

This is the public assembly record for Part 1. It describes the build process without exposing receipt identifiers, hardware serials, network details, or private evidence paths.

## Before assembly

1. The empty Phanteks chassis was inspected, vacuumed, and wiped down. Plastic shavings and manufacturing debris were removed before any electronics entered the case.
2. The motherboard was placed flat on a protected surface.
3. Board switches and documented defaults were checked while they were still easy to reach.
4. The BIOS was updated with ASUS BIOS FlashBack before first boot because the board's original firmware predated native Threadripper PRO 9000 WX support. ASUS lists the 9955WX as supported beginning with BIOS 1106.

## Bench assembly

The installation order was:

1. Threadripper PRO CPU and carrier;
2. all eight ECC RDIMMs, one per memory channel;
3. Noctua mounting hardware and the NH-U14S TR5-SP6;
4. both NF-A15 fans through the supplied PWM splitter to CPU_FAN;
5. Samsung 9100 PRO in M.2_1 under the motherboard heatsink; and
6. a one-GPU bench/first-boot configuration.

The loaded EEB motherboard—board, CPU, memory, storage, and cooler—was then lowered into the chassis with the case lying flat. This reduced the chance of losing control of a large and expensive assembly during mounting.

<p align="center">
  <img src="../assets/images/bench-assembly.jpg" width="720" alt="Bench assembly before installation in the chassis">
</p>

## Power connections

The final single-PSU build uses:

- the 24-pin motherboard power connection;
- both required CPU EPS power feeds;
- both supplemental PCIe board-power inputs used for multi-GPU stability; and
- one dedicated Corsair CP-8920274 cable per RTX 3090 FE.

Each GPU cable uses two PSU-side 8-pin connections and one GPU-side Founders Edition 12-pin connection.

Modular PSU cables are not interchangeable merely because their plugs fit. Only cables verified for the exact PSU family and purpose were used.

## Chassis completion

After the motherboard and power feeds were secured:

1. the ten T30 fans were placed in their final intake/exhaust groups;
2. the physical mode switch on every T30 was set to Advanced, making the 3,000 RPM ceiling available to the fan curves;
3. chassis wiring and fan chains were routed;
4. GPU 0 was installed in slot 3;
5. GPU 1 was installed in slot 7; and
6. the one-slot airflow gap and all power connections were physically rechecked.

<p align="center">
  <img src="../assets/images/gpu-slot-gap.jpg" width="520" alt="Close view of the one-slot gap between both RTX 3090 Founders Edition cards">
</p>

## What was deliberately not installed

- no NVLink bridge;
- no anti-sag bracket;
- no second NVMe or HDD yet;
- no liquid CPU cooler;
- no additional accelerator; and
- no UPS yet.

Eleven T30s were purchased, but ten are installed. The remaining fan is a spare/future option and is not counted as active cooling.

## First boot and software direction

The machine was initially brought up with one GPU. Ubuntu was installed and the platform was stabilized before the second card returned to the final lower slot.

Ubuntu was chosen because the CUDA, NCCL, vLLM, llama.cpp, container, telemetry, and model-serving ecosystems are Linux-first. SSH is the normal administration path; the BMC remains independent recovery infrastructure.

## Lessons from build day

- Update workstation-board firmware before a difficult chassis installation when CPU support depends on it.
- Read the motherboard's power diagrams closely; professional multi-GPU boards can require supplemental connections that consumer builds do not.
- Populate memory channels intentionally, not merely DIMM slots opportunistically.
- Treat card dimensions and slot spacing as thermal design inputs.
- Verify modular PSU cable compatibility by exact PSU family.
- Keep the first boot configuration minimal, then add the second GPU after the base platform is stable.
- Record installed state separately from plans. Purchased, planned, and installed are not interchangeable words.
