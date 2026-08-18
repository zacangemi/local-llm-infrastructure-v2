# Architecture and platform decisions

## The central decision

V2 was designed around the platform rather than around a new GPU purchase. The two RTX 3090 Founders Edition cards remained useful, but V1 showed that consumer-platform lane allocation, physical spacing, memory capacity, operating-system friction, and recovery options could limit otherwise capable accelerators.

The rebuild therefore prioritized WRX90, Threadripper PRO, eight-channel ECC RDIMM, a server-oriented chassis, and out-of-band management.

## Compute and memory topology

The AMD Ryzen Threadripper PRO 9955WX provides:

- 16 Zen 5 cores and 32 threads;
- eight DDR5 RDIMM memory channels;
- ECC support enabled by default;
- 148 native PCIe lanes, 144 usable, with up to 128 at PCIe 5.0;
- a 350 W default TDP; and
- the sTR5 platform needed by the WRX90 motherboard.

The motherboard exposes six PCIe 5.0 x16 slots plus a seventh physical x16 slot operating at x8, four PCIe 5.0 x4 M.2 sockets, two SlimSAS connections, dual 10 Gb Ethernet, and a dedicated management interface.

The installed GPUs are PCIe Gen4 devices. GPU 0 occupies motherboard slot 3 and GPU 1 occupies slot 7. Both negotiated Gen4 x16 under load during commissioning. Their three-slot bodies retain one physical slot-width between them.

## Why all eight DIMMs are populated

The installed Kingston kit contains eight matched 16 GB ECC RDIMMs. One DIMM occupies each channel from A through H, exposing the full physical channel width of the platform.

The kit is rated for DDR5-6400. The active production configuration is the kit's factory EXPO Profile #2 at DDR5-6000, 32-38-38-80. The reason for stopping at 6000—and the qualification history behind that decision—belongs to the commissioning project.

ECC improves fault detection and correction; it is not inherently faster than non-ECC memory. It was selected for reliability in a remotely operated, sustained-load system.

## GPU memory semantics

Each RTX 3090 provides 24 GB of GDDR6X. The machine therefore contains 48 GB of physical VRAM, but that capacity is not automatically pooled into one address space. The inference or training framework must explicitly partition models and work across both devices.

No NVLink bridge is installed. Communication between the cards depends on the backend and host/PCIe path selected by the workload.

## Storage and networking

The active root and working drive is a Samsung 9100 PRO 2 TB installed in the motherboard's M.2_1 socket. The device is PCIe 5.0 x4—not x16.

An Intel X710-T2L provides two copper Ethernet ports capable of up to 10GbE. Adapter capability and current end-to-end network speed are deliberately kept distinct: the present upstream path does not yet operate at 10GbE.

## Console and recovery plane

The motherboard's ASPEED AST2600 BMC provides a console independent of Ubuntu and the RTX GPUs. That keeps both 3090s display-free and enables POST, BIOS, sensor, and recovery access even if the operating system is unavailable.

Normal administration uses SSH. The BMC is the recovery path, not the everyday workload interface. Public documentation intentionally omits addresses, credentials, relay details, and physical-location information.

## Installed-state diagram

~~~mermaid
flowchart LR
    cpu[Threadripper PRO 9955WX]
    ram[8×16 GB ECC RDIMM<br/>8 channels / DDR5-6000]
    board[WRX90 platform]
    g0[RTX 3090 FE<br/>GPU 0 / Gen4 x16]
    g1[RTX 3090 FE<br/>GPU 1 / Gen4 x16]
    ssd[9100 PRO 2 TB<br/>Gen5 x4]
    lan[X710-T2L<br/>dual 10GBASE-T]
    bmc[AST2600 BMC]

    cpu <--> ram
    cpu <--> board
    board <--> g0
    board <--> g1
    board <--> ssd
    board <--> lan
    bmc -. out-of-band control .-> board
~~~

## Why this foundation matters

GPUs are expected to change over the life of the system. The foundation is intended to survive those changes. The motherboard, memory architecture, chassis, power supply, cooling layout, Linux environment, and recovery plane create a platform in which future accelerators can be evaluated without rebuilding the entire machine first.
