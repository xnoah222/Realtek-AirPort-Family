# Realtek AirPort Family 1.0.1 preview

AirPort_RTW88 2.0.2 and Realtek88LegacyAirport 1.0.1.

Changes:
- PCIe capability registers now use the discovered PCI_EXP capability offset. Previously reads used absolute offsets and writes used 0x100+offset (truncated by the PCI wrapper). This fixes the implementation of CLKREQ/ASPM capability reads and the RTL8821CE completion-timeout workaround.
- Legacy now negotiates supported rates, HT/VHT MCS and WMM from the AP, intersecting hardware capabilities. No invented 2-stream support when a router or RTL8821CE only supports one stream.
- QoS and TX aggregation follow negotiated WMM/HT. Channel width requires AP capability IEs and a valid 80 MHz center.
- Includes the AirPort_RTW88 work developed previously. AWDL/AirDrop remains experimental and unsupported; no new AWDL work is included in this integration task.
- OpCore Simplify integration patch: five PCI IDs, version-dependent drivers/dependencies, Monterey excluded, source/binary asset names kept separate.

Installation matrix (x86_64 PCIe only):
| macOS | Driver/dependencies |
| --- | --- |
| Mojave 10.14–Big Sur 11 | HS80211Family, then Realtek88LegacyAirport |
| Monterey 12 | Unsupported |
| Ventura 13 | AirPort_RTW88 alone |
| Sonoma 14–Tahoe 26 | AMFIPass, IOSkywalkFamily, IO80211FamilyLegacy, then AirPort_RTW88; block native com.apple.iokit.IOSkywalkFamily with Exclude and MinKernel 23.0.0 |

Keep only one Realtek driver active. Ventura needs no injected legacy stack. Kernel ranges: Legacy/HS 18.0.0–20.99.99; modern 22.0.0–25.99.99; injected modern dependencies 23.0.0–25.99.99. Existing project runtime coverage was Ventura 13.7.7/13.7.8 and Sonoma 14.4+; earlier point releases are not newly certified by these builds.

Validation:
- Both x86_64 kexts compile successfully (compiler warnings remain).
- Executable production-helper tests pass for PCIe offsets, missing capability/error handling, 1/2-stream hardware vs 1/2/3-stream APs, 20/40/80 MHz, HT/VHT/rates/WMM and malformed IEs.
- Simplify selection/dependency tests cover Darwin 17–26, with actual bundle ordering and native-stack blocking across the supported families.
- The older PCI family test passes its initial contract checks but cannot complete because the supplied source omits rtw88.xcodeproj/project.pbxproj. This is not an all-tests-green release.
- Physical RTL8822CE and RTL8821CE tests are NOT completed. These changes must not be described as verified repairs of every reported CE failure.
- No before/after throughput claim: prior measurements were on loaded v19 with RTL8822BE/Tahoe, not these new binaries: 25.2 Mbps download, 40.9 Mbps upload; gateway idle 16.7 ms average (0/30 lost), loaded 39.0 ms (1/20 lost). WAN tests also depend on ISP/router/server.

No new kext was installed or EFI modified during development. Keep a working EFI backup when testing. Source ZIPs preserve original third-party notices. Dependencies are unchanged copies from the project's 1.0.0 release; their developers and licenses remain authoritative.
