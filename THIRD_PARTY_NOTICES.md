# Third-Party Notices and License Map

Realtek AirPort Family is a mixed-license project.

The root `LICENSE` applies **only** to Original Project Work as defined there. It does not relicense third-party source code, headers, firmware, SDK material, or modifications that must remain under an upstream license.

## Linux / rtw88

The source archives vendor an `rtw88-stable` tree derived from the Linux Realtek rtw88 driver. Per-file SPDX identifiers and accompanying license files remain authoritative. Many rtw88 files are marked `GPL-2.0 OR BSD-3-Clause`; other files may use different terms. Those notices must be preserved.

## Feixiao-derived material

The macOS port began from and/or incorporates material derived from the Feixiao project. Files derived from Feixiao retain their existing license notices and SPDX identifiers. The Realtek AirPort Family Project License does not replace those terms.

In particular, notices in `src/compat/` and in Feixiao-derived kext/backend files remain authoritative for those files or portions.

## AirportItlwm / itlwm material

AirPort_RTW88 used AirportItlwm / itlwm as an important reference for AirPort/IO80211 behavior. Any copied or derivative material remains subject to its applicable upstream terms.

Where source distributions include AirportItlwm/Apple reference headers or fixtures, their original notices remain authoritative.

## Apple / MacKernelSDK

MacKernelSDK and Apple-derived headers are third-party material and retain their own license notices. They are not covered by the Realtek AirPort Family Project License.

## Realtek firmware

Realtek firmware blobs remain third-party binary material and are not covered by the Realtek AirPort Family Project License. Any accompanying Realtek firmware license must be preserved with redistributed firmware.

## OpenAWDL / OWL references

Some AWDL work documents behavior, formats, or implementation ideas learned from public OpenAWDL / OWL material. Any actual third-party code or derivative material remains under its applicable upstream license. The custom project license applies only to original material that can lawfully be licensed under it.

## External release dependencies

Release packages may include external kexts such as HS80211Family, IO80211FamilyLegacy, IOSkywalkFamily, and AMFIPass. Those components are not owned by Realtek AirPort Family and retain their respective upstream licenses and notices.

## Important

A file's own copyright/license header takes priority for that file or portion. Do not remove third-party notices merely because the repository also contains the Realtek AirPort Family Project License.
