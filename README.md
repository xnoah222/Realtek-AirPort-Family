# Realtek AirPort Family for macOS

Native-style Realtek Wi-Fi support for macOS.

## 1.0.1 — Wi-Fi and OpCore Simplify

[Download release](https://github.com/xnoah222/Realtek-AirPort-Family/releases/tag/v1.0.1) · [Changes and validation](RELEASE-NOTES-1.0.1.md) · [OpCore Simplify integration](integration/opcore-simplify/README.md)

The release contains one ZIP with `LegacyAirport`, `Airport_RTW88` and `Sonoma - Tahoe` folders.

Includes AirPort_RTW88 **2.0.1** and Realtek88LegacyAirport **1.0.1**. Fixes PCIe capability addressing and AP capability negotiation. CE runtime validation remains pending; this is not a verified fix for every RTL8822CE/RTL8821CE problem. AirDrop remains unsupported. The two root source archives correspond to these release binaries.

**Realtek AirPort Family** provides native-style AirPort support for selected Realtek PCIe Wi-Fi adapters across multiple generations of macOS.

The project currently includes two drivers:

- **Realtek88LegacyAirport** — macOS Mojave through Big Sur (Realtek88LegacyAirport.kext + HS80211Family.kext)
- **AirPort_RTW88** — macOS Ventura through Tahoe (On Sonoma and Later you need to use Legacy Stack)

> **Realtek Wi-Fi. From Mojave to Tahoe.**

---

## Supported Hardware

Currently supported PCIe adapters:

- Realtek RTL8822BE
- Realtek RTL8822CE
- Realtek RTL8821CE

> [!NOTE]
> USB and SDIO Realtek Wi-Fi adapters are not supported.

---

## Compatibility

| macOS | Driver | Status |
|---|---|---|
| Mojave 10.14 | Realtek88LegacyAirport | ✅ Supported |
| Catalina 10.15 | Realtek88LegacyAirport | ✅ Supported |
| Big Sur 11 | Realtek88LegacyAirport | ✅ Supported |
| Monterey 12 | — | ❌ Not supported |
| Ventura 13.7.7 – 13.7.8 | AirPort_RTW88 | ✅ Supported |
| Sonoma 14.4+ | AirPort_RTW88 | ✅ Supported |
| Sequoia 15 | AirPort_RTW88 | ✅ Supported |
| Tahoe 26 | AirPort_RTW88 | ✅ Supported |

> [!IMPORTANT]
> macOS Monterey is currently not supported.

---

# Installation

## macOS Mojave – Big Sur

Required:

- `HS80211Family.kext`
- `Realtek88LegacyAirport.kext`

Copy both kexts to:

```text
EFI/OC/Kexts/
```

and enable them under:

```text
Kernel -> Add
```

`HS80211Family.kext` must load before `Realtek88LegacyAirport.kext`.

---

## macOS Ventura

Required:

- `AirPort_RTW88.kext`

Copy the kext to:

```text
EFI/OC/Kexts/
```

and enable it under:

```text
Kernel -> Add
```

No legacy Skywalk stack is required on Ventura.

---

## macOS Sonoma – Tahoe

Required:

- `AirPort_RTW88.kext`
- `IO80211FamilyLegacy.kext`
- `IOSkywalkFamily.kext`
- `AMFIPass.kext`

The required dependencies are included in the release package for convenience.

Copy the kexts to:

```text
EFI/OC/Kexts/
```

and enable them under:

```text
Kernel -> Add
```

### Blocking native IOSkywalkFamily

On macOS Sonoma and newer, the native `IOSkywalkFamily` must be blocked so the legacy `IOSkywalkFamily.kext` can be loaded.

Configure the block under:

```text
Kernel -> Block
```

> [!IMPORTANT]
> Blocking the native IOSkywalkFamily is required on Sonoma and newer. An incorrect configuration may prevent the Wi-Fi stack from loading.

### OpenCore Configuration Example

![IOSkywalkFamily Kernel Block](Images/Kernel-Block.png)

---

# Current Status

Both drivers target core Wi-Fi functionality. The latest preview is compiled and software-tested; physical verification of RTL8822CE/RTL8821CE and the full macOS matrix remains pending.

Supported core functionality includes:

- Wi-Fi scanning
- Network association
- 2.4 GHz and 5 GHz networks
- Network switching
- Sustained network traffic

AirPort_RTW88 also supports sleep/wake recovery.

---

## AWDL / AirDrop

AWDL support in **AirPort_RTW88** is currently experimental.

Partial AWDL functionality exists, but AirDrop and other AWDL-dependent features should not currently be considered supported.

**Realtek88LegacyAirport does not support AWDL.**

AWDL is separate from the core Wi-Fi stability status of AirPort_RTW88.

---

# Previous AirPort_RTW88 Releases

AirPort_RTW88 previously existed as a standalone experimental project.

The releases published in the original repository were early development builds and contained stability and connectivity issues.

Those releases are now **deprecated and do not represent the current state of AirPort_RTW88**.

With the migration to Realtek AirPort Family, the AirPort_RTW88 version number has been reset.

The first AirPort_RTW88 release distributed as part of this project starts at:

**2.0.0**

This release should not be confused with the historical AirPort_RTW88 1.0.0 release from the deprecated repository.

---

# Included Dependencies

Some external kexts are included in the release packages to make installation easier.

These components are **not developed or owned by Realtek AirPort Family** and remain the work of their respective developers and projects.

### Mojave – Big Sur

- `HS80211Family.kext`

### Sonoma – Tahoe

- `IO80211FamilyLegacy.kext`
- `IOSkywalkFamily.kext`
- `AMFIPass.kext`

Original licenses, notices and credits should be preserved.

---

# Credits

Realtek AirPort Family would not exist without the work and research of several open-source projects.

### Driver Development

- **Linux rtw88** — Realtek Wi-Fi driver used as the main reference and basis for Realtek hardware support.
- **OpenIntelWireless / AirportItlwm** — major reference for implementing native AirPort integration on macOS.
- **Feixiao** — upstream macOS Realtek driver material used by this project.
- **MacKernelSDK** — kernel development resources used for macOS driver development.

### External Kexts

- **HS80211Family.kext** — from the `sXmpwn/atheros-ke` project.
- **IO80211FamilyLegacy.kext / IOSkywalkFamily.kext** — legacy Wi-Fi stack distributed through `Edwardwich/BCM-WIFI-Sequoia`.
- **AMFIPass.kext** — distributed through `kaoskinkae/AMFIPass`.

All credit for these external components belongs to their respective developers and contributors.

---

# Source Code

Source code for Realtek AirPort Family is provided with the project.

The source distribution preserves applicable copyright notices and licenses from the projects on which the drivers are based.

---

# Disclaimer

Realtek AirPort Family is an independent community project.

It is not affiliated with, endorsed by, or supported by Apple Inc. or Realtek Semiconductor Corp.

Hackintosh configurations can vary significantly between systems.

**Always keep a working EFI backup before modifying kexts or your OpenCore configuration.**

---

# License

Realtek AirPort Family is a **mixed-license** repository.

Original Project Work for **AirPort_RTW88** and **Realtek88LegacyAirport** is licensed under the custom **Realtek AirPort Family Project License 1.0**, but only where the project has the legal right to apply it. The license permits use, modification, redistribution and commercial distribution while requiring modified distributions that rely on Covered Original Project Work to use a distinct project identity rather than presenting themselves as official AirPort_RTW88 or Realtek88LegacyAirport releases.

Third-party code and data are **not relicensed**. Linux/rtw88, Feixiao-derived material, AirportItlwm/itlwm material, Apple/MacKernelSDK material, Realtek firmware and other third-party components retain their own notices and license terms.

See:

- `LICENSE` — Realtek AirPort Family Project License 1.0
- `THIRD_PARTY_NOTICES.md` — third-party license map
- `ORIGINAL_WORK_NOTICE.md` — scope of the project's original work
- individual source-file headers and license files inside the source archives

---

**Realtek Wi-Fi. From Mojave to Tahoe.**
