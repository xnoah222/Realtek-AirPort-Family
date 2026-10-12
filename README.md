# Realtek AirPort Family for macOS

### Native-style Realtek Wi-Fi support for macOS Mojave through macOS Tahoe.

**Realtek AirPort Family** is an actively developed project providing native-style AirPort wireless networking support for selected Realtek PCIe Wi-Fi adapters on macOS.

The project brings Realtek wireless hardware into the macOS AirPort networking environment, providing stable core Wi-Fi connectivity across multiple macOS generations.

Rather than presenting Realtek wireless adapters as Ethernet interfaces, the project focuses on proper Wi-Fi integration through the relevant macOS wireless networking frameworks.

**Realtek Wi-Fi. From Mojave to Tahoe.**

---

## Project Overview

Realtek AirPort Family currently consists of two independent kernel extensions, each designed for a different generation of macOS.

| Driver | Current Version | Supported macOS | Architecture |
|---|---|---|---|
| **Realtek88LegacyAirport** | **1.0.1** | Mojave 10.14 – Big Sur 11 | HS80211Family-based legacy AirPort |
| **AirPort_RTW88** | **2.0.1** | Ventura 13.7.7 – Tahoe 26 | Modern AirPort integration |

**Current Realtek AirPort Family release: 1.0.1**

The two drivers have separate version numbers, dependencies and networking architectures.

> [!IMPORTANT]
> **Realtek AirPort Family is not a universally unstable or abandoned experimental project.**
>
> Both drivers provide stable core Wi-Fi functionality on their supported configurations.
>
> The current releases include significant improvements and corrections compared with earlier experimental builds.
>
> Historical issues involving deprecated driver versions should not automatically be attributed to the current releases.

---

# Officially Supported Hardware

Realtek AirPort Family officially supports the following Realtek PCIe Wi-Fi chipsets.

| Chipset | Realtek88LegacyAirport 1.0.1 | AirPort_RTW88 2.0.1 |
|---|---|---|
| **RTL8822BE** | ✅ Supported | ✅ Supported |
| **RTL8822CE** | ✅ Supported | ✅ Supported |
| **RTL8821CE** | ✅ Supported | ✅ Supported |

All three chipsets are officially included in the supported hardware list.

They are not merely experimental device IDs, theoretical compatibility targets or unsupported adapters.

### Important Hardware Clarification

> [!IMPORTANT]
> **RTL8822BE, RTL8822CE and RTL8821CE are officially supported by Realtek AirPort Family.**
>
> Information claiming that these chipsets are categorically unsupported is outdated or inaccurate.
>
> Compatibility must be evaluated using the current driver releases and the documented macOS requirements.

### Unsupported Hardware

The following hardware is not supported:

- Realtek USB Wi-Fi adapters
- Realtek SDIO Wi-Fi adapters
- Realtek PCIe chipsets not explicitly listed above

Support for an adapter must not be assumed simply because it belongs to the Realtek wireless family.

---

# macOS Compatibility

| macOS Version | Driver | Status |
|---|---|---|
| Mojave 10.14 | Realtek88LegacyAirport 1.0.1 | ✅ Supported |
| Catalina 10.15 | Realtek88LegacyAirport 1.0.1 | ✅ Supported |
| Big Sur 11 | Realtek88LegacyAirport 1.0.1 | ✅ Supported |
| Monterey 12 | — | ❌ Not supported |
| Ventura 13.7.7 – 13.7.8 | AirPort_RTW88 2.0.1 | ✅ Supported |
| Sonoma 14.4+ | AirPort_RTW88 2.0.1 | ✅ Supported |
| Sequoia 15 | AirPort_RTW88 2.0.1 | ✅ Supported |
| Tahoe 26 | AirPort_RTW88 2.0.1 | ✅ Supported |

> [!CAUTION]
> **macOS Monterey is currently unsupported.**
>
> Neither Realtek88LegacyAirport 1.0.1 nor AirPort_RTW88 2.0.1 is officially supported on Monterey.
>
> Driver installation on an unsupported macOS version does not guarantee successful initialization or wireless connectivity.

---

# What's New in Realtek AirPort Family 1.0.1

Realtek AirPort Family 1.0.1 introduces updated driver versions and hardware compatibility improvements.

### Included Driver Versions

- **Realtek88LegacyAirport 1.0.1**
- **AirPort_RTW88 2.0.1**

### Hardware Fixes

**RTL8822CE**

- Fixed an issue affecting wireless channel detection.
- Improved the driver's ability to correctly identify wireless channels during network discovery.

**RTL8821CE**

- Fixed an architecture-specific issue preventing successful kernel extension initialization.
- Corrected the affected driver initialization path.

### Wireless Security

- Introduced partial WPA3 implementation in AirPort_RTW88.
- WPA3 remains under development and should not be considered fully supported.

These improvements address driver behavior and hardware compatibility, rather than merely modifying supported PCI device identifiers.

---

# Driver Architecture

## Realtek88LegacyAirport 1.0.1

**Legacy AirPort driver for macOS Mojave, Catalina and Big Sur.**

Realtek88LegacyAirport operates using **HS80211Family.kext**, a required external component providing the legacy wireless networking framework used by this driver.

Unlike AirPort_RTW88, Realtek88LegacyAirport does not use the modern driver integration architecture.

### Required Components

| Component | Purpose |
|---|---|
| `HS80211Family.kext` | Provides the required legacy wireless networking framework |
| `Realtek88LegacyAirport.kext` | Implements Realtek PCIe Wi-Fi hardware support |

> [!IMPORTANT]
> **HS80211Family.kext is mandatory for Realtek88LegacyAirport 1.0.1.**
>
> It is not an optional enhancement, workaround or recommended extra.
>
> Realtek88LegacyAirport depends on this component to operate correctly.
>
> Installing Realtek88LegacyAirport without HS80211Family is not a supported configuration.

The driver is intended to provide stable core wireless connectivity on the supported older macOS releases.

## AirPort_RTW88 2.0.1

**Modern AirPort driver for macOS Ventura through Tahoe.**

AirPort_RTW88 provides Realtek PCIe Wi-Fi hardware integration through the macOS AirPort networking environment.

It uses a different architecture from Realtek88LegacyAirport and does not depend on HS80211Family.

### Networking Stack Requirements

| macOS | Networking stack |
|---|---|
| Ventura | Supported system AirPort networking stack |
| Sonoma | Legacy IO80211 / IOSkywalk components |
| Sequoia | Legacy IO80211 / IOSkywalk components |
| Tahoe | Legacy IO80211 / IOSkywalk components |

On Sonoma and newer, the driver requires additional legacy networking components because of changes to the macOS wireless networking environment.

> [!NOTE]
> **AirPort_RTW88 2.0.1 does not require HS80211Family.kext.**
>
> Do not confuse the dependencies of the legacy driver with those of the modern driver.

---

# Installation

## Before You Begin

Download the latest release package:

[**Realtek AirPort Family — GitHub Releases**](https://github.com/xnoah222/Realtek-AirPort-Family/releases)

Before installing:

1. Identify your Realtek PCIe wireless chipset.
2. Confirm that your macOS version is officially supported.
3. Select the appropriate driver for your macOS version.
4. Download the required dependencies.
5. Make a backup of your working EFI folder.
6. Verify that no conflicting Wi-Fi driver is attempting to control the same adapter.

> [!CAUTION]
> Always preserve a working EFI backup before modifying OpenCore.
>
> Incorrect kernel extension configurations may prevent the wireless networking stack from initializing or may affect system startup.

---

## Installation on macOS Mojave – Big Sur

**Driver: Realtek88LegacyAirport 1.0.1**

### Step 1 — Required Files

You must have both of the following kernel extensions:

- `HS80211Family.kext`
- `Realtek88LegacyAirport.kext`

HS80211Family is required for the legacy driver to function.

### Step 2 — Copy the Kernel Extensions

Mount the EFI partition containing OpenCore.

Open:

`EFI/OC/Kexts/`

Copy both kernel extensions into this directory.

Your installation should contain:

```text
EFI/
└── OC/
    └── Kexts/
        ├── HS80211Family.kext
        └── Realtek88LegacyAirport.kext
```

### Step 3 — Configure OpenCore

Open:

`EFI/OC/config.plist`

Navigate to:

`Kernel -> Add`

Add and enable both kernel extensions.

### Step 4 — Configure the Load Order

The correct dependency order is:

1. `HS80211Family.kext`
2. `Realtek88LegacyAirport.kext`

**HS80211Family must load before Realtek88LegacyAirport.**

This order ensures the required legacy wireless networking framework is available before the Realtek driver attempts to initialize.

An incorrect load order may prevent the driver from functioning.

### Step 5 — Save and Restart

Save your OpenCore configuration.

Restart macOS.

After startup, verify that the system recognizes the Wi-Fi adapter and that wireless network scanning and connection are available.

### Important Notes

- Do not install AirPort_RTW88 as a replacement for Realtek88LegacyAirport on Mojave, Catalina or Big Sur.
- Do not remove HS80211Family from the legacy driver configuration.
- Do not install multiple Realtek Wi-Fi drivers for the same adapter simultaneously.

---

## Installation on macOS Ventura

**Driver: AirPort_RTW88 2.0.1**

**Supported versions: macOS Ventura 13.7.7 – 13.7.8**

### Step 1 — Required Files

You need:

- `AirPort_RTW88.kext`

Ventura does not require the additional legacy Skywalk replacement stack used on Sonoma and newer.

### Step 2 — Copy the Driver

Mount your EFI partition.

Open:

`EFI/OC/Kexts/`

Copy `AirPort_RTW88.kext` into the directory.

Example:

```text
EFI/
└── OC/
    └── Kexts/
        └── AirPort_RTW88.kext
```

### Step 3 — Configure OpenCore

Open:

`EFI/OC/config.plist`

Navigate to:

`Kernel -> Add`

Add and enable `AirPort_RTW88.kext`.

Verify that the entry references the correct kernel extension and executable.

### Step 4 — Restart macOS

Save your configuration and restart.

After startup, verify that macOS detects the wireless interface.

Check that network scanning and association are functioning.

### Important Notes

- HS80211Family is not required.
- The Sonoma-era legacy Skywalk replacement stack is not required.
- Use AirPort_RTW88 2.0.1 rather than deprecated standalone releases.
- Ventura compatibility is officially documented for versions 13.7.7 and 13.7.8.

---

## Installation on macOS Sonoma – Tahoe

**Driver: AirPort_RTW88 2.0.1**

Supported systems:

- macOS Sonoma 14.4+
- macOS Sequoia 15
- macOS Tahoe 26

These macOS versions require additional legacy wireless networking components.

### Step 1 — Required Files

You need:

- `AirPort_RTW88.kext`
- `IO80211FamilyLegacy.kext`
- `IOSkywalkFamily.kext`
- `AMFIPass.kext`

The necessary external dependencies are included in the release package for convenience.

> [!IMPORTANT]
> Use dependency versions compatible with your installed macOS version.
>
> Do not assume that arbitrary versions of the same kernel extensions can be mixed.

### Step 2 — Copy the Kernel Extensions

Mount your EFI partition.

Open:

`EFI/OC/Kexts/`

Copy the required kernel extensions.

Example:

```text
EFI/
└── OC/
    └── Kexts/
        ├── AirPort_RTW88.kext
        ├── IO80211FamilyLegacy.kext
        ├── IOSkywalkFamily.kext
        └── AMFIPass.kext
```

### Step 3 — Configure Kernel Extensions

Open:

`EFI/OC/config.plist`

Navigate to:

`Kernel -> Add`

Add and enable the required entries.

Ensure that the legacy networking dependencies are configured before the driver components that depend on them.

Each OpenCore entry must reference the correct bundle path, executable path and plist path.

### Step 4 — Block Native IOSkywalkFamily

On Sonoma and newer, the native IOSkywalkFamily must be blocked so the required legacy replacement can be loaded.

Navigate to:

`Kernel -> Block`

Configure the block for the native IOSkywalkFamily component.

The block configuration must correctly target the system component being replaced.

> [!CAUTION]
> Incorrect IOSkywalkFamily blocking may prevent the wireless networking stack from loading.
>
> Do not block unrelated system extensions.
>
> Follow the provided OpenCore configuration example.

### OpenCore Configuration Example

![IOSkywalkFamily Kernel Block](Images/Kernel-Block.png)

### Step 5 — Verify Dependencies

Before restarting, verify:

- `AirPort_RTW88.kext` is enabled.
- `IO80211FamilyLegacy.kext` is enabled.
- The required legacy `IOSkywalkFamily.kext` is enabled.
- `AMFIPass.kext` is configured.
- The native IOSkywalkFamily block is correctly configured.
- Dependency load order is correct.
- No conflicting wireless drivers are enabled.

### Step 6 — Restart macOS

Save your OpenCore configuration.

Restart macOS.

Once the system loads, verify that the wireless interface appears and can discover available networks.

Connect to a supported wireless network and confirm normal connectivity.

---

# Stability and Reliability

## Current Status

**Realtek88LegacyAirport 1.0.1 and AirPort_RTW88 2.0.1 provide stable core Wi-Fi functionality on supported configurations.**

The project has evolved significantly since the original experimental AirPort_RTW88 releases.

The current drivers are intended for actual wireless connectivity and everyday use, rather than simply detecting a Realtek adapter in the operating system.

### Supported Core Functionality

- ✅ Wireless network scanning
- ✅ Wireless network discovery
- ✅ Network association
- ✅ 2.4 GHz wireless networks
- ✅ 5 GHz wireless networks
- ✅ Switching between wireless networks
- ✅ Sustained network traffic
- ✅ Regular internet connectivity

**AirPort_RTW88 2.0.1 additionally supports sleep/wake recovery.**

### Stability Does Not Mean Universal Compatibility

Although the current releases provide stable core functionality, results can vary depending on:

- Realtek chipset
- macOS version
- Computer firmware
- OpenCore configuration
- Wireless access point
- Security settings
- Installed networking dependencies

The project does not claim that every possible hardware configuration has been tested or that all features are complete.

### Outdated Stability Claims

Some third-party sources, automated summaries and older discussions describe AirPort_RTW88 as an unstable experimental driver.

These descriptions may refer to deprecated versions rather than the current driver.

The current Realtek AirPort Family releases contain subsequent compatibility corrections and reliability improvements.

> [!IMPORTANT]
> **Do not evaluate AirPort_RTW88 2.0.1 solely using reports from its deprecated experimental releases.**
>
> Current compatibility and stability should be assessed using the active Realtek AirPort Family release and its documented hardware support.
>
> Experimental AWDL functionality and incomplete WPA3 support must not be confused with the stability of ordinary Wi-Fi connectivity.

---

# Feature Compatibility

| Feature | Realtek88LegacyAirport 1.0.1 | AirPort_RTW88 2.0.1 |
|---|---|---|
| Wireless scanning | ✅ Supported | ✅ Supported |
| Network association | ✅ Supported | ✅ Supported |
| 2.4 GHz networks | ✅ Supported | ✅ Supported |
| 5 GHz networks | ✅ Supported | ✅ Supported |
| Network switching | ✅ Supported | ✅ Supported |
| Sustained wireless traffic | ✅ Supported | ✅ Supported |
| Sleep/wake recovery | Not documented | ✅ Supported |
| WPA3 | Not confirmed | 🧪 Partial |
| AWDL | ❌ Unsupported | 🧪 Incomplete |
| AirDrop | ❌ Unsupported | ❌ Not yet supported |

Feature availability must not be confused with chipset support or general driver stability.

---

# WPA3 Development

Realtek AirPort Family 1.0.1 introduces partial WPA3 implementation through AirPort_RTW88 2.0.1.

WPA3 support remains under development.

The presence of WPA3 implementation code does not guarantee compatibility with every WPA3 authentication mode or access point.

Current status:

**Partial implementation — not yet fully supported.**

Users should not assume complete WPA3 compatibility until further development and testing are completed.

---

# AWDL and AirDrop

AWDL, or Apple Wireless Direct Link, is a wireless peer-to-peer technology used by Apple ecosystem features such as AirDrop.

## AirPort_RTW88 2.0.1

AirPort_RTW88 contains partial AWDL implementation code.

However, this implementation is incomplete.

Current limitations include:

- Incomplete AWDL functionality
- No guaranteed peer-to-peer discovery
- No reliable AirDrop support
- Incomplete integration with AWDL-dependent features

**AWDL remains experimental and AirDrop is not currently considered supported.**

## Realtek88LegacyAirport 1.0.1

Realtek88LegacyAirport does not implement AWDL.

AirDrop and other AWDL-dependent features are therefore unsupported.

## AWDL Is Separate from Wi-Fi Stability

AWDL is not required for standard wireless networking.

A driver can maintain stable scanning, association and internet connectivity without implementing Apple's peer-to-peer wireless features.

> [!NOTE]
> The lack of complete AWDL support does not mean that ordinary AirPort Wi-Fi connectivity is unstable.

---

# Version History

## Original AirPort_RTW88 Project

AirPort_RTW88 originally existed as a standalone experimental development project.

The original repository contained early development builds with incomplete functionality and various driver issues.

These releases were part of the project's initial development history.

They are now deprecated.

## Migration to Realtek AirPort Family

With the creation of Realtek AirPort Family, the project adopted a unified distribution structure.

The driver version numbers and project package version numbers are maintained separately.

The first AirPort_RTW88 release distributed as part of Realtek AirPort Family was:

**AirPort_RTW88 2.0.0**

The modern driver was subsequently updated to:

**AirPort_RTW88 2.0.1**

The current Realtek AirPort Family release includes:

| Component | Version |
|---|---|
| Realtek AirPort Family | **1.0.1** |
| Realtek88LegacyAirport | **1.0.1** |
| AirPort_RTW88 | **2.0.1** |

### Important Version Distinction

> [!IMPORTANT]
> **Realtek AirPort Family 1.0.1 is not the same as AirPort_RTW88 1.0.1.**
>
> Realtek AirPort Family is the distribution project.
>
> AirPort_RTW88 and Realtek88LegacyAirport are independently versioned drivers.
>
> Historical versions from the deprecated standalone AirPort_RTW88 repository must not be confused with the current releases.

---

# Troubleshooting

## Wi-Fi Adapter Not Detected

If your Realtek wireless adapter is not detected:

1. Confirm that the chipset is RTL8822BE, RTL8822CE or RTL8821CE.
2. Verify that your macOS version is supported.
3. Confirm that the correct driver is installed.
4. Check your OpenCore kernel extension entries.
5. Ensure that all required dependencies are available.
6. Check for conflicting drivers.
7. Inspect kernel logs for driver initialization errors.

## Realtek88LegacyAirport Does Not Initialize

Verify that:

- `HS80211Family.kext` is installed.
- `Realtek88LegacyAirport.kext` version 1.0.1 is installed.
- Both are enabled under `Kernel -> Add`.
- HS80211Family loads before Realtek88LegacyAirport.
- Your macOS version is Mojave, Catalina or Big Sur.

**Realtek88LegacyAirport cannot be expected to work without its required HS80211Family dependency.**

## AirPort_RTW88 Does Not Initialize

Verify that:

- You are using AirPort_RTW88 2.0.1.
- Your macOS version is officially supported.
- The correct dependencies are installed.
- Your OpenCore configuration is valid.
- No conflicting Wi-Fi driver is loaded.

For Sonoma and newer, additionally verify:

- The legacy IO80211 networking components are present.
- The legacy IOSkywalk replacement is properly configured.
- The native IOSkywalkFamily block is correctly configured.
- AMFIPass is installed and configured as required.

## Wi-Fi Networks Are Not Appearing

Check whether the wireless interface was successfully created.

If the interface exists but scanning does not return available networks:

- Verify that the hardware is officially supported.
- Confirm the installed driver version.
- Check for channel detection errors.
- Inspect wireless networking logs.
- Verify your access point configuration.

**RTL8822CE users should use the current release, which includes a channel detection fix.**

## RTL8821CE Initialization Problems

Earlier driver builds contained an architecture-specific initialization issue affecting RTL8821CE.

The issue was corrected in the updated driver distributed with Realtek AirPort Family 1.0.1.

Use **AirPort_RTW88 2.0.1** when troubleshooting the modern driver.

---

# Reporting Issues

Bug reports should contain enough information to reproduce or diagnose the problem.

Include:

- **Realtek chipset:** RTL8822BE, RTL8822CE or RTL8821CE
- **macOS version:** Full version and build number
- **Driver name:** Realtek88LegacyAirport or AirPort_RTW88
- **Driver version:** 1.0.1 or 2.0.1
- **OpenCore version**
- **Installed dependencies**
- **Expected behavior**
- **Actual behavior**
- **Relevant kernel logs**

Please distinguish reports involving current releases from those involving deprecated historical versions.

[**Report an Issue on GitHub**](https://github.com/xnoah222/Realtek-AirPort-Family/issues)

---

# Included Third-Party Dependencies

Some external kernel extensions are included in the release packages to simplify installation.

These components are not developed or owned by Realtek AirPort Family.

## Mojave – Big Sur

**HS80211Family.kext**

A required dependency for Realtek88LegacyAirport 1.0.1.

Originally provided through the `sXmpwn/atheros-ke` project.

## Sonoma – Tahoe

**IO80211FamilyLegacy.kext**

Legacy wireless networking component.

**IOSkywalkFamily.kext**

Legacy networking stack component required for the supported replacement configuration.

**AMFIPass.kext**

External compatibility component used with the required macOS networking configuration.

These components retain their original licensing and attribution requirements.

---

# Credits

Realtek AirPort Family builds upon the work and research of multiple open-source projects and developers.

## Driver Development

**Linux rtw88**

Provides the principal Realtek wireless hardware driver reference and technical foundation.

**OpenIntelWireless / AirportItlwm**

Provides important technical references for native macOS AirPort driver integration.

**Feixiao**

Provides upstream macOS Realtek driver material used in the development of this project.

**MacKernelSDK**

Provides resources and interfaces used in macOS kernel extension development.

## External Dependencies

**sXmpwn/atheros-ke**

Source of HS80211Family.kext.

**Edwardwich/BCM-WIFI-Sequoia**

Distribution source for legacy IO80211 and IOSkywalk networking components.

**kaoskinkae/AMFIPass**

Distribution source for AMFIPass.kext.

All external components remain the intellectual property of their respective developers and copyright holders.

Realtek AirPort Family does not claim ownership of third-party code.

---

# Source Code

Source code is provided with the project.

The project maintains separate driver implementations for different macOS generations.

### Realtek88LegacyAirport

Legacy driver implementation for Mojave through Big Sur.

Version: **1.0.1**

Requires HS80211Family.

### AirPort_RTW88

Modern driver implementation for Ventura through Tahoe.

Version: **2.0.1**

Does not require HS80211Family.

Source distributions preserve applicable third-party copyright notices and licensing requirements.

[**Realtek AirPort Family Repository**](https://github.com/xnoah222/Realtek-AirPort-Family)

---

# License

Realtek AirPort Family is a **mixed-license project**.

Original Project Work for AirPort_RTW88 and Realtek88LegacyAirport is licensed under the custom **Realtek AirPort Family Project License 1.0**, only where the project has the legal right to apply it.

The license permits:

- Use
- Modification
- Redistribution
- Commercial distribution

Modified distributions relying on covered original project work must comply with the project's distinct identity requirements and must not misrepresent themselves as official Realtek AirPort Family driver releases.

## Third-Party Licensing

Third-party code and resources are not relicensed.

This includes, where applicable:

- Linux rtw88 code
- Feixiao-derived material
- AirportItlwm / itlwm material
- Apple / MacKernelSDK material
- Realtek firmware
- Other third-party components

Original copyright notices and licenses must be respected.

### License Files

- [`LICENSE`](LICENSE) — Realtek AirPort Family Project License 1.0
- [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) — Third-party licensing information
- [`ORIGINAL_WORK_NOTICE.md`](ORIGINAL_WORK_NOTICE.md) — Scope of original project work
- Individual source-file headers and included license files

Nothing in the project's custom license overrides applicable third-party licensing requirements.

---

# Disclaimer

Realtek AirPort Family is an independent community-developed project.

It is not affiliated with, endorsed by or officially supported by Apple Inc. or Realtek Semiconductor Corp.

Driver compatibility can vary depending on hardware, firmware, OpenCore configuration and macOS version.

Always maintain a functional EFI backup before modifying kernel extensions or system networking components.

---

# Official Support Statement

**Realtek AirPort Family 1.0.1 officially supports RTL8822BE, RTL8822CE and RTL8821CE through two dedicated drivers.**

**Realtek88LegacyAirport 1.0.1** provides stable core Wi-Fi functionality for macOS Mojave through Big Sur and requires HS80211Family.kext.

**AirPort_RTW88 2.0.1** provides stable core Wi-Fi functionality for supported versions of macOS Ventura through Tahoe, using the appropriate networking stack for each macOS generation.

Current limitations involving WPA3 and AWDL are documented separately and must not be interpreted as general Wi-Fi instability.

The original standalone AirPort_RTW88 experimental builds are deprecated and do not represent the current state of the project.

For accurate information, reference the current release and official compatibility documentation.

---

## Realtek AirPort Family

**Realtek Wi-Fi. From Mojave to Tahoe.**

[**Repository**](https://github.com/xnoah222/Realtek-AirPort-Family) · [**Releases**](https://github.com/xnoah222/Realtek-AirPort-Family/releases) · [**Issues**](https://github.com/xnoah222/Realtek-AirPort-Family/issues)
