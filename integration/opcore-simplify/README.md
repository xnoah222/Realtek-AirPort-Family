# Proposed upstream OpCore Simplify integration

This patch is prepared for the upstream commit in BASE_COMMIT. It has not been merged into the original OpCore Simplify catalog. Publishing a release does not register drivers in that catalog.

The contribution adds AirPort_RTW88, Realtek88LegacyAirport and HS80211Family, selects them by Darwin version and PCI IDs, and downloads all three products from the single Realtek-AirPort-Family-1.0.1.zip asset. It does not disable or alter the upstream application updater.

- Darwin 18–20: Realtek88LegacyAirport + HS80211Family.
- Darwin 21: unsupported.
- Darwin 22: AirPort_RTW88 alone.
- Darwin 23–25: AirPort_RTW88 + legacy stack and its dependencies.

PCI IDs: 10EC:B822, C822, C82F, C821, B821. AWDL/AirDrop unsupported. CE runtime validation remains pending.
