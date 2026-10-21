# Realtek AirPort Family for macOS

**Native-style AirPort Wi-Fi support for selected Realtek PCIe adapters, from macOS Mojave to macOS Tahoe.**

Realtek AirPort Family brings together separate macOS Wi-Fi driver projects built around different generations of Realtek hardware and macOS networking interfaces.

The family includes three projects:

- **Realtek88LegacyAirport** — legacy AirPort support for macOS Mojave, Catalina, and Big Sur.
- **AirPort_RTW88** — modern AirPort integration for selected Realtek RTL88xx PCIe adapters.
- **AirPort_RTW89** — AirPort integration for selected Realtek RTL89xx PCIe adapters.

Each driver has its own supported hardware, implementation, requirements, limitations, and licensing terms. Being part of the same family does not mean that all three drivers support the same adapters or macOS releases.

> **Realtek Wi-Fi. From Mojave to Tahoe.**

---

## Table of contents

- [Overview](#overview)
- [macOS compatibility](#macos-compatibility)
- [Realtek88LegacyAirport](#realtek88legacyairport)
- [AirPort_RTW88](#airport_rtw88)
- [AirPort_RTW89](#airport_rtw89)
- [Hardware compatibility](#hardware-compatibility)
- [Networking architecture](#networking-architecture)
- [Installation requirements](#installation-requirements)
- [Known limitations](#known-limitations)
- [Troubleshooting](#troubleshooting)
- [Credits](#credits)
- [External dependencies](#external-dependencies)
- [Licensing](#licensing)
- [Disclaimer](#disclaimer)
- [Project links](#project-links)

## Overview

Realtek AirPort Family aims to provide Wi-Fi through macOS's native AirPort networking interface instead of exposing the wireless adapter as a conventional Ethernet interface or requiring a separate application to manage connections.

Depending on the driver and macOS version, this allows wireless networking to integrate with the system's Wi-Fi interface and related networking services.

The family is divided into three projects because the legacy and modern macOS networking stacks require different approaches.

| Project | Hardware family | macOS versions |
|---|---|---|
| Realtek88LegacyAirport 1.0.1 | Selected RTL88xx PCIe adapters | Mojave 10.14 – Big Sur 11 |
| AirPort_RTW88 2.0.1 | Selected RTL88xx PCIe adapters | Ventura 13.7.7–13.7.8, Sonoma 14.4+, Sequoia 15.x, Tahoe 26.x |
| AirPort_RTW89 | Selected RTL89xx PCIe adapters | Ventura 13, Sonoma 14.4+, Sequoia 15.x, Tahoe 26.x |

**macOS Monterey 12 is not supported by the current family compatibility matrix.**

These compatibility ranges describe operating-system support, not a guarantee that every adapter listed in a driver's source code has been tested on every macOS release. Hardware support and testing status are documented separately below.

## macOS compatibility

The following table summarizes the intended division between the three drivers.

| macOS release | Realtek88LegacyAirport | AirPort_RTW88 | AirPort_RTW89 |
|---|---|---|---|
| Mojave 10.14 | Supported | Not supported | Not supported |
| Catalina 10.15 | Supported | Not supported | Not supported |
| Big Sur 11 | Supported | Not supported | Not supported |
| Monterey 12 | Not supported | Not supported | Not supported |
| Ventura 13 | Not supported | 13.7.7–13.7.8 | Supported |
| Sonoma 14 | Not supported | 14.4 and later | 14.4 and later |
| Sequoia 15 | Not supported | Supported | Supported |
| Tahoe 26 | Not supported | Supported | Supported |

The drivers are not interchangeable. Install the project intended for your adapter and macOS version, and follow that project's own installation documentation.

## Realtek88LegacyAirport

**Version:** 1.0.1

Realtek88LegacyAirport provides legacy AirPort support for selected Realtek PCIe Wi-Fi adapters on macOS Mojave, Catalina, and Big Sur.

It uses the legacy `HS80211Family` networking framework, which distinguishes it from the newer AirPort_RTW88 implementation.

### Compatibility

- macOS Mojave 10.14
- macOS Catalina 10.15
- macOS Big Sur 11

### Supported adapters

- Realtek RTL8822BE
- Realtek RTL8822CE
- Realtek RTL8821CE

These are the adapters listed as supported by the project; other chipsets should not be assumed to work.

### Architecture

Realtek88LegacyAirport depends on `HS80211Family.kext` for its legacy AirPort implementation.

The framework is an essential part of this driver's architecture rather than an optional component that can be omitted without considering compatibility.

### Important notes

- This driver is intended for the legacy macOS range listed above.
- It is a separate implementation from AirPort_RTW88, not simply an older release of the same modern driver.
- Its compatibility should not be extended to Monterey or later without explicit project support.

## AirPort_RTW88

**Version:** 2.0.1

Repository: [xnoah222/Airport_RTW88](https://github.com/xnoah222/Airport_RTW88)

AirPort_RTW88 provides modern AirPort integration for selected Realtek RTL88xx PCIe Wi-Fi adapters.

It is intended to make compatible Realtek wireless hardware available through macOS's native Wi-Fi interface, with network discovery and connection management integrated into the operating system.

### Compatibility

- macOS Ventura 13.7.7–13.7.8
- macOS Sonoma 14.4 and later
- macOS Sequoia 15.x
- macOS Tahoe 26.x

macOS Monterey 12 is unsupported.

### Supported adapters

- **RTL8822BE** — PCIe
- **RTL8822CE** — PCIe
- **RTL8821CE** — PCIe

USB and SDIO variants are not supported by this project.

### Changes in version 2.0.1

Version 2.0.1 includes fixes and improvements involving:

- RTL8822CE channel detection.
- RTL8821CE architecture-specific initialization.
- Partial WPA3 implementation.

WPA3 support remains partial and should not be interpreted as complete compatibility with every WPA3 network configuration.

### Networking features

The project is designed around native macOS AirPort networking rather than a separate Wi-Fi management application.

Available functionality depends on the adapter, operating-system release, and networking configuration. Support for the native Wi-Fi interface does not imply that every Apple wireless feature is available.

### Requirements for newer macOS releases

On Sonoma 14.4 and later, the driver uses legacy-compatible networking components to work with the relevant macOS Wi-Fi stack.

The setup may require:

- `AMFIPass.kext`
- `IO80211FamilyLegacy.kext`
- A compatible legacy `IOSkywalkFamily.kext`

The native `IOSkywalkFamily` may need to be blocked in OpenCore so the intended compatible version can load. Follow the project's installation instructions for the exact configuration and load order.

Do not mix arbitrary versions of these components. They must be compatible with the macOS release and with one another.

### Known limitations

- WPA3 implementation is partial.
- AWDL-related functionality is not considered fully supported.
- AirDrop and other features that depend on AWDL should not be expected to work.
- USB and SDIO adapters are outside the project's supported hardware scope.
- macOS Monterey is unsupported.

## AirPort_RTW89

**Repository:** [FranciumOS-org/Airport_RTW89](https://github.com/FranciumOS-org/Airport_RTW89)

AirPort_RTW89 brings native-style macOS AirPort integration to selected Realtek RTL89xx PCIe wireless adapters. It is a separate driver project from AirPort_RTW88 and uses the Linux `rtw89` driver as its principal hardware-driver reference.

### Compatibility

- macOS Ventura 13
- macOS Sonoma 14.4 and later
- macOS Sequoia 15.x
- macOS Tahoe 26.x

macOS Monterey 12 is unsupported.

### Hardware support and testing status

The following list distinguishes adapters with working or tested status from those whose support is present in the project but remains untested.

| Adapter | Device ID(s) | Status |
|---|---|---|
| RTL8852BE | `B852`, `B85B` | Working; development hardware |
| RTL8852BTE | `B520` | Included; untested |
| RTL8851BE | `B851` | Included; untested |
| RTL8852AE | `8852`, `A85A` | Tested on macOS Tahoe 26 |
| RTL8852CE | `C852` | Tested on macOS Tahoe 26; WPA3 not yet supported |
| RTL8922AE | `8922`, `892B` | Included; untested |
| RTL8922DE | `892D`, `882D`, `895D` | Tested on macOS Tahoe 26 |

The table records the project's reported status. An adapter marked *included; untested* should not be treated as verified hardware support.

USB and SDIO adapters are not supported.

### Networking functionality

The project documents the following functionality, subject to the adapter and configuration:

- Open Wi-Fi networks.
- WPA2-Personal.
- WPA2-Enterprise, including a tested 802.1X PEAP configuration.
- Joining networks through the macOS Wi-Fi interface.
- Scanning for networks while connected.
- Saving network credentials and reconnecting to known networks.
- Connecting to an iPhone Personal Hotspot using supported Wi-Fi security configurations.
- Wi-Fi 6 operation, with up to 80 MHz channel width and two spatial streams on compatible hardware.
- OpenCore-based startup and normal system shutdown.

The project has reported approximately 500 Mbps download performance in a 5 GHz, 80 MHz configuration. Actual results vary with the adapter, access point, radio environment, and system configuration.

### Security and wireless limitations

- WPA3 support is limited; a network offering WPA2/WPA3 transition mode may connect using WPA2.
- The RTL8852CE does not currently have WPA3 support.
- Sleep and wake handling exists in the driver, but broader testing is still needed.
- AWDL, AirDrop, and Apple peer-to-peer Continuity features are not supported.
- Support status for untested adapters must be confirmed through actual hardware testing.

### Networking stack requirements

Newer macOS releases may require compatible legacy Wi-Fi networking components, including:

- `IOSkywalkFamily`
- `IO80211FamilyLegacy`
- `AMFIPass`

The required versions and OpenCore configuration depend on the macOS release. Use the instructions provided by AirPort_RTW89 rather than copying settings from an unrelated configuration.

## Hardware compatibility

The family supports selected **PCIe** wireless adapters only. A chipset appearing in an upstream Linux driver does not automatically mean that the corresponding macOS driver supports it.

| Hardware type | Family support |
|---|---|
| RTL8822BE PCIe | Realtek88LegacyAirport and AirPort_RTW88 |
| RTL8822CE PCIe | Realtek88LegacyAirport and AirPort_RTW88 |
| RTL8821CE PCIe | Realtek88LegacyAirport and AirPort_RTW88 |
| Listed RTL89xx PCIe adapters | AirPort_RTW89, according to the individual adapter's testing status |
| Realtek USB Wi-Fi adapters | Not supported |
| Realtek SDIO Wi-Fi adapters | Not supported |
| Other unlisted PCIe adapters | Not guaranteed |

**Before installing a driver, identify the exact wireless chipset and PCI device ID.** Similar model names do not necessarily indicate the same hardware or driver compatibility.

Bluetooth functionality, where present on a combo wireless card, is separate from these Wi-Fi drivers and is not provided by Realtek AirPort Family.

## Networking architecture

The family uses different approaches according to the target macOS generation.

### Legacy AirPort

Realtek88LegacyAirport uses `HS80211Family.kext` for its legacy implementation on Mojave, Catalina, and Big Sur.

### Modern AirPort

AirPort_RTW88 and AirPort_RTW89 target newer macOS releases and integrate with the system's AirPort/IO80211 networking architecture.

For Sonoma and later, compatibility with the legacy Wi-Fi networking stack may require additional components and OpenCore configuration.

The goal is native-style Wi-Fi integration: the adapter should be managed through the system's Wi-Fi interface instead of relying on an unrelated connection utility.

This does not mean that all macOS wireless services are implemented. Features such as AWDL, AirDrop, and other peer-to-peer services have their own requirements and are not supported simply because ordinary Wi-Fi connectivity works.

## Installation requirements

Installation instructions differ between the three projects. Consult the documentation supplied by the specific driver you intend to install.

Before changing your configuration:

1. Confirm the exact Realtek chipset and device ID.
2. Verify that your macOS version is listed as supported for that driver.
3. Back up your working OpenCore EFI.
4. Check the required kext versions and their load order.
5. Follow the project's own instructions for any required legacy networking components.
6. Test ordinary Wi-Fi connectivity before relying on the system for essential network access.

For Sonoma and later, pay particular attention to the required `IO80211FamilyLegacy`, `IOSkywalkFamily`, and `AMFIPass` configuration where applicable.

Do not install all three drivers together merely because they belong to the same family. Select the driver that matches your hardware and operating-system version, and follow its own documentation.

## Known limitations

The family does not promise complete support for every Realtek adapter or every macOS wireless feature.

Known limitations across the projects include:

- macOS Monterey 12 is not supported by the current compatibility matrix.
- USB and SDIO Wi-Fi adapters are outside the supported hardware scope.
- Hardware support varies by driver and testing status.
- WPA3 functionality varies and remains incomplete in the documented implementations.
- AWDL, AirDrop, and related Apple peer-to-peer features are not supported by the modern drivers as documented.
- Sleep, wake, roaming, and other behaviors may require additional testing depending on the driver and adapter.

A successful boot or a visible Wi-Fi menu does not, by itself, establish that every networking feature is working correctly.

## Troubleshooting

### The wireless adapter does not appear

- Verify the chipset and PCI device ID.
- Check that you installed the correct family driver.
- Confirm that the driver supports your macOS release.
- Review the OpenCore kext configuration and dependency load order.
- Check whether the required legacy Wi-Fi components are loading.

### The driver loads but cannot find networks

- Check whether the adapter is explicitly supported by that driver.
- Confirm that the required firmware and driver components are available.
- Test in an environment with a known working access point.
- Consult the relevant project's issue tracker and troubleshooting documentation.

### The Wi-Fi menu works, but a network cannot be joined

Check the network's security mode and the driver's current protocol support. In particular, WPA3 and WPA2/WPA3 transition configurations may not work as expected with all adapters.

### Wi-Fi works, but AirDrop or Continuity does not

Ordinary Wi-Fi connectivity and AWDL-based Apple features are different capabilities. AirDrop and other peer-to-peer functions are not supported by the modern drivers as documented.

### A macOS update breaks Wi-Fi

Review the updated macOS version against the compatibility table. Recheck the legacy networking stack requirements and the versions of all related kexts before making further changes.

For driver-specific problems, report the issue in the appropriate project's issue tracker with the macOS version, adapter model, device ID, and relevant diagnostic information. Avoid publishing private identifiers or a complete EFI containing personal information.

## Credits

Realtek AirPort Family builds on the work of upstream projects, researchers, and developers. The following credits identify important sources and technical references; they do not imply that those projects maintain or officially endorse Realtek AirPort Family.

### AirPort_RTW88 and legacy driver work

- **Linux `rtw88`** — principal reference for Realtek wireless hardware-driver functionality.
- **OpenIntelWireless (`itlwm` and `AirportItlwm`)** — technical references for integrating wireless drivers with macOS's IO80211/AirPort architecture.
- **Feixiao** — upstream macOS Realtek driver material used during development.
- **MacKernelSDK** — interfaces and resources for macOS kernel-extension development.

### AirPort_RTW89

- **Linux `rtw89`** — upstream Realtek hardware-driver implementation and reference.
- **Linux `mac80211` and `cfg80211`** — references for wireless subsystem behavior and APIs.
- **AirPort_RTW88 and Realtek AirPort Family** — related compatibility work, Linux API shims, and macOS driver-integration references.
- **OpenIntelWireless** — reference for native-style macOS wireless-driver integration.
- **OpenCore Legacy Patcher and Acidanthera** — relevant work and tooling around OpenCore, Lilu, and legacy macOS wireless networking components.
- **hostap** — wireless authentication and networking components used in the RTW89 project.
- **Mbed TLS** — cryptographic library used in the RTW89 project.
- **Realtek and the Linux firmware project** — firmware provenance for supported hardware.

All upstream authors and contributors retain credit for their work under the applicable terms.

## External dependencies

Some functionality depends on components maintained or distributed by other projects.

| Component or source | Role |
|---|---|
| `sXmpwn/atheros-ke` | Source of `HS80211Family.kext` used by the legacy driver |
| `Edwardwich/BCM-WIFI-Sequoia` | Distribution source for legacy `IO80211` and `IOSkywalk` networking components |
| `kaoskinkae/AMFIPass` | Distribution source for `AMFIPass.kext` |
| OpenCore | Bootloader and kext configuration for Hackintosh systems |
| Lilu | Dependency where required by the selected driver |
| Linux `rtw88` and `rtw89` | Upstream hardware-driver references and code, subject to their respective licenses |
| `hostap` and Mbed TLS | Components used by AirPort_RTW89, subject to their respective licenses |

These dependencies are not automatically owned by Realtek AirPort Family. Follow each upstream project's terms and obtain components from their appropriate sources.

## Licensing

Realtek AirPort Family contains projects and components with different licensing terms. **The family name does not replace, override, or unify the individual licenses.**

### Realtek AirPort Family Project License 1.0

Original work covered by the custom **Realtek AirPort Family Project License 1.0** may be used, modified, redistributed, and commercially distributed under the terms of that license, where legally applicable.

Modified distributions that rely on covered original work must comply with the license's project-identity requirements and must not misrepresent themselves as official releases of the original project.

The custom license applies only to work it can legally cover. It does not automatically relicense third-party code or override the rights of upstream authors.

### AirPort_RTW89 and third-party code

AirPort_RTW89 includes code governed by **GPL-2.0** and other applicable third-party licenses. The relevant source files and components must be handled under their applicable terms.

In particular, the Linux `rtw89` code and other vendored or adapted components retain the licensing obligations that apply to them. The family license cannot be used to remove those obligations.

### Third-party notices

Third-party code, firmware, SDKs, and macOS networking components remain subject to their original ownership and applicable licenses.

Do not assume that a component can be redistributed simply because it is required to run a driver. Preserve relevant copyright notices and license texts, and consult the applicable upstream project before redistributing its work.

## Disclaimer

Realtek AirPort Family is an independent community project. It is not affiliated with, endorsed by, or supported by Apple or Realtek.

macOS and the referenced third-party projects remain the property of their respective owners. Compatibility and feature availability depend on the adapter, macOS release, firmware, and system configuration.

Use these drivers at your own risk. Maintain a recoverable OpenCore configuration before changing kernel extensions or system networking components.

## Project links

- **Realtek AirPort Family:** https://github.com/xnoah222/Realtek-Airport-Family
- **AirPort_RTW88:** https://github.com/xnoah222/Airport_RTW88
- **AirPort_RTW89:** https://github.com/FranciumOS-org/Airport_RTW89
- **Family releases:** https://github.com/xnoah222/Realtek-Airport-Family/releases
- **Family issue tracker:** https://github.com/xnoah222/Realtek-Airport-Family/issues

For driver-specific installation guidance, compatibility questions, and bug reports, consult the corresponding driver repository.
