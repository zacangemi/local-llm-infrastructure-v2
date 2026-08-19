# Airflow and cooling design

> Companion narrative: [My New AI Cluster: Go Big or Go Home, Part 1](https://blog.zacharycangemi.com/2026/08/18/my-new-ai-cluster-go-big-or-go-home-part-1/)

The cooling objective was sustained, remote operation with simple serviceability. The machine is entirely air-cooled: ten Phanteks T30-120 chassis fans plus the two NF-A15 fans supplied with the Noctua CPU cooler.

<p align="center">
  <img src="../assets/images/airflow-layout.jpg" width="580" alt="Annotated airflow direction through the completed V2 server">
</p>

## Final fan layout

| Group | Count | Direction | Function |
|---|---:|---|---|
| Front T30 bank | 4 | Intake | Feeds fresh air across the board and GPU region |
| Side/rear T30 bank | 2 | Intake | Adds direct air beside the GPU stack |
| Top T30 bank | 3 | Exhaust | Removes rising GPU and CPU heat |
| Upper-left CPU-area T30 | 1 | Exhaust | Supports the CPU-area exhaust path |
| Noctua NF-A15 pair | 2 | Through heatsink toward top exhaust | Push/pull CPU-tower airflow |

The chassis therefore has six intake and four exhaust fans, producing a design intended for mild positive pressure. Including the CPU-cooler pair, the machine contains twelve rotating fans.

## Why T30-120

The T30 uses a 30 mm frame rather than the more common 25 mm format. Phanteks specifies three physical PWM profiles. Every installed fan is switched to Advanced mode, which permits up to 3,000 RPM. This makes the higher performance envelope available to the motherboard's curves; it does not mean every fan constantly runs at full speed.

The fan choice was driven by airflow and static-pressure capability through a dense multi-GPU chassis, not silence or RGB aesthetics.

## Why air cooling

Liquid cooling could provide more peak CPU thermal margin. Air cooling was selected because this server is intended to run remotely and remain straightforward to inspect and service. Removing pumps, tubing, and liquid-bearing components fit the preferred reliability model.

That is a tradeoff, not a universal recommendation. The Noctua tower is appropriate for the intended GPU-dominant workload, but the commissioning campaign found the boundary of the CPU-cooling configuration under deliberately simultaneous maximum CPU and dual-GPU synthetic load. The full measurements and operating rule belong in Part 2.

## What the build can and cannot claim

Supported by the final installed state:

- all ten chassis fans are installed and respond through their fan chains;
- all switches are set to Advanced mode;
- dual-GPU, GPU-dominant, and CPU-only workloads passed their intended gates; and
- the one-slot gap materially improves the upper card's access to intake air compared with V1.

Not claimed here:

- a controlled pre/post fan temperature delta;
- direct GDDR6X junction temperatures under Linux;
- unlimited unattended operation at simultaneous maximum CPU and GPU power; or
- that air cooling is categorically safer or better for every system.
