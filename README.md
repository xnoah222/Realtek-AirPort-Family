# Realtek-AirPort-Family
Realtek Wi-Fi drivers for macOS Mojave through Tahoe, built around Apple’s AirPort networking stack.
# Realtek AirPort Family for macOS

### Native-style Realtek Wi-Fi support across generations of macOS.

Realtek AirPort Family is a collection of Wi-Fi drivers designed to bring selected Realtek RTL88xx wireless adapters into Apple's AirPort networking stack.

From **macOS Mojave to macOS Tahoe**, the project provides different drivers adapted to each generation of Apple's Wi-Fi frameworks instead of forcing a single implementation across incompatible networking stacks.

One family. Three drivers. Twelve years of macOS.

---

## The Driver Family

### Realtek88LegacyAirport

**macOS Mojave 10.14 → macOS Big Sur 11.7.11**

The legacy branch of Realtek AirPort Family.

Designed around the classic AirPort / IO80211 networking stack used by older versions of macOS.

**Status:** Stable

- Wi-Fi scanning
- Association and authentication
- 2.4 GHz networks
- 5 GHz networks
- Network switching
- Sleep / Wake
- Sustained network traffic

**Known limitations**

- Hibernation is not supported
- AWDL is not supported

---

### RTL88_Airport21

**macOS Monterey 12**

A dedicated driver for Darwin 21 and the Monterey generation of Apple's AirPort stack.

Rather than extending either the Legacy or Modern driver beyond the environment they were designed for, Monterey receives its own implementation.

**Status:** Stable

- Wi-Fi scanning
- Association and authentication
- 2.4 GHz networks
- 5 GHz networks
- Network switching
- Sleep / Wake
- Hibernation support
- Sustained network traffic

AWDL is not currently guaranteed.

---

### AirPort_RTW88

**macOS Ventura 13 → macOS Tahoe 26**

The modern branch of Realtek AirPort Family and the continuation of the original AirPort_RTW88 project.

Built for newer generations of Apple's Wi-Fi stack, with a focus on stability under everyday use and sustained network traffic.

**Status:** Stable

- Wi-Fi scanning
- Association and authentication
- 2.4 GHz networks
- 5 GHz networks
- Network switching
- Sleep / Wake
- Hibernation support
- Sustained network traffic

AWDL support is experimental and is not considered part of the core stability guarantee.

---

## macOS Compatibility

| macOS | Version | Driver | Status |
| --- | --- | --- | --- |
| Mojave | 10.14 | Realtek88LegacyAirport | ✅ Stable |
| Catalina | 10.15 | Realtek88LegacyAirport | ✅ Stable |
| Big Sur | 11.0 – 11.7.11 | Realtek88LegacyAirport | ✅ Stable |
| Monterey | 12.x | RTL88_Airport21 | ✅ Stable |
| Ventura | 13.x | AirPort_RTW88 | ✅ Stable |
| Sonoma | 14.x | AirPort_RTW88 | ✅ Stable |
| Sequoia | 15.x | AirPort_RTW88 | ✅ Stable |
| Tahoe | 26.x | AirPort_RTW88 | ✅ Stable |

---

## Supported Hardware

Realtek AirPort Family currently targets:

- **Realtek RTL8822BE**
- **Realtek RTL8822CE**
- **Realtek RTL8821CE**

PCIe devices only.

USB and SDIO Realtek Wi-Fi adapters are not supported.

---

## Why three drivers?

Apple's Wi-Fi architecture changed substantially across macOS generations.

Trying to maintain one increasingly patched driver for every version of macOS would introduce unnecessary complexity and compromise stability.

Realtek AirPort Family instead uses three purpose-built implementations:

```text
Mojave ─ Catalina ─ Big Sur
              │
     Realtek88LegacyAirport

           Monterey
              │
        RTL88_Airport21

Ventura ─ Sonoma ─ Sequoia ─ Tahoe
              │
         AirPort_RTW88
```

Each branch can evolve around the networking architecture it was designed to support while remaining part of the same project.

---

## Stability

The primary goal of Realtek AirPort Family is not simply getting a Realtek adapter detected by macOS.

A working driver should remain working.

Core Wi-Fi functionality is tested around:

- Extended network usage
- Sustained network traffic
- Repeated network switching
- 2.4 GHz ↔ 5 GHz switching
- Disconnect / reconnect cycles
- Sleep / Wake
- Connection recovery

Experimental functionality such as AWDL is kept separate from the stability status of normal Wi-Fi operation.

---

## AWDL, AirDrop and Continuity

AWDL is **not currently guaranteed across Realtek AirPort Family**.

Experimental AWDL functionality may be present in some driver and macOS combinations, but it should not currently be considered a supported feature.

The absence or instability of AWDL does not affect the supported status of standard Wi-Fi connectivity.

---

## Installation

Installation requirements depend on the macOS generation being used.

Some versions of macOS require additional networking components that are **not distributed as part of Realtek AirPort Family**.

Detailed installation instructions and required upstream dependencies are provided with each release.

Do not mix drivers intended for different macOS generations.

---

## Source Code

Source code corresponding to public releases is provided separately with the project releases.

Realtek AirPort Family contains and adapts work from multiple open-source projects. Original copyright and licensing notices are preserved where applicable.

See the included license and source documentation for additional information.

---

## Credits

Realtek AirPort Family would not exist without the work of the open-source wireless and Hackintosh communities.

Special thanks to:

- **OpenIntelWireless / AirportItlwm** — research, architecture and implementation reference for integrating third-party Wi-Fi hardware with Apple's AirPort stack.
- **Linux rtw88 developers** — Realtek RTL88xx hardware support and documentation.
- **Dortania / OpenCore Legacy Patcher** — legacy macOS networking research and infrastructure.
- Everyone testing Realtek hardware across different Macs, Hackintoshes and macOS versions.

---

## Project History

Realtek AirPort Family grew out of **AirPort_RTW88**, originally created to bring Realtek RTL88xx PCIe Wi-Fi hardware to modern versions of macOS.

What started as a single experimental driver eventually became a larger effort to support multiple generations of Apple's networking stack.

AirPort_RTW88 now lives here as the Modern branch of a broader driver family.

---

## License

Realtek AirPort Family is distributed under the **GNU General Public License v2.0**.

Individual incorporated components remain subject to their respective copyright and licensing terms.

---

**Realtek AirPort Family for macOS**

*Realtek Wi-Fi. From Mojave to Tahoe.*
