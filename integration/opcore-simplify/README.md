# OpCore Simplify integration

This is a tested patch for upstream commit in `BASE_COMMIT`, not a claim that upstream has merged support.

```sh
git clone https://github.com/lzhoang2801/OpCore-Simplify.git
git -C OpCore-Simplify checkout $(cat BASE_COMMIT)
git -C OpCore-Simplify apply /absolute/path/to/realtek-airport.patch
```

Run the patched copy normally. Updating/replacing it from upstream can remove this integration.

PCI IDs: 10EC:B822, C822, C82F, C821, B821. USB/SDIO IDs are not mapped to AirPort drivers.

- Darwin 18–20: Realtek88LegacyAirport + HS80211Family.
- Darwin 21: unavailable (Monterey).
- Darwin 22: AirPort_RTW88 alone.
- Darwin 23–25: AirPort_RTW88 + IO80211FamilyLegacy + IOSkywalkFamily + AMFIPass (and its Lilu dependency in Simplify's catalog).
- Future Darwin versions: not enabled implicitly.

The installer retains its existing dependency sort and native IOSkywalkFamily block at MinKernel 23.0.0. The drivers conflict with Feixiao and with each other. Download names retain AirPort_RTW88's underscore; Source ZIPs cannot replace the binary product.

Requires the new release's separately named `AirPort_RTW88-…-RELEASE.zip`, `Realtek88LegacyAirport-…-RELEASE.zip`, and `HS80211Family-…-RELEASE.zip` assets. The old combined 1.0.0 archive does not expose these products to Simplify.

AirDrop/AWDL is unsupported. Runtime confirmation is still needed on RTL8822CE/RTL8821CE and the older macOS versions.
