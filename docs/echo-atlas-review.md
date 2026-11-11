# Echo and Atlas documentation review — 10 November 2026

Authoring notes; this file is not a customer manual chapter.

## Scope and evidence

Reviewed all eight customer chapters for each product and the legacy API/User Interface redirects. Customer-facing manual changes are in `docs/echo/` and `docs/atlas/`, with shared illustrations and styling under `docs/assets/`; the initial review did not change firmware or DIRAC Field. The follow-up below also closes automatic-power-off gaps in firmware and clarifies the app editor.

The current firmware checkout is `C:/Users/han/Documents/Projects/Echo2Atlas/source`, at commit `f16de77df0a0b08e261d9296b747985b43cfbdfe`. Relevant sources were read directly:

| Subject | Source |
|---|---|
| Menu entries and navigation | `components/ui/menudata.cpp`, `pagemenu.cpp`, `pageduration.cpp`, `input.cpp` |
| Self-test display and interpretation | `components/ui/pageselftest.cpp`, `components/signals/SelfTestService.cpp`, `components/status/settings.cpp` |
| Speaker output prerequisite | `components/signals/player.cpp`: output routing applies to self-test playback as well as ordinary playback |
| Self-test API semantics | `components/status/StateManager.cpp`, `components/api/apiHandler.cpp` |
| Echo/Atlas transport and gain | `components/ui/pagemain.cpp`, `pageatlas.cpp`, `pageechosignal.cpp`, `pageatlassignal.cpp` |
| Signal types, modes, lengths and levels | `components/status/SignalValidator.cpp`, `components/signals/SignalPathBuilder.cpp` |
| Station selection, fallback, passwords | `components/ui/pagenetwork.cpp`, `components/network/network.cpp` |
| Power, auto-off and standby | `components/power/power.cpp`, `components/status/monitor.cpp` |
| Local software update | `components/ui/pageota.cpp` |

The supplied `Echo-Atlas Power & Signal Control 260718.pdf` and `Echo V2 + Atlas V1 260618.pdf` were checked for power conditions, the protected 4000 mAh cell and Atlas's 45 W high-power condition. The more recent power document takes precedence. Existing product photographs, annotated Atlas views and OLED illustrations were retained.

## Changes made

- Added the self-test procedure, speaker-output preparation, three-pass progress, Pass/Fail meanings, Fr/difference interpretation and return-to-Service action to both System Menu pages.
- Added self-test troubleshooting and links from Quick Start; distinguished a failed comparison from a test that produced no result.
- Explained local update, standby, auto-off, playback timer and editor cancellation.
- Standardised customer-facing app naming to DIRAC Field and linked app-specific procedures to its guide.
- Added the Echo Sine source, omitted the engineering-only USB audio sources from both customer manuals, distinguished intermittent stimulus duration from the displayed sequence period, and documented Atlas's local-versus-app gain control locations.
- Expanded network troubleshooting, per-network Auto-reconnect, fallback hotspot and shared device-password explanations.
- Removed copied Echo mass, dimensions, battery runtime and electrical ratings from Atlas specifications. Retained the confirmed mounting, connectors and common battery information; made the remaining specification-review boundary explicit.
- Replaced generic copied-draft notices on Atlas Troubleshooting and Release Notes with reviewed content. Kept a specific notice on incomplete Atlas specifications. No release dates or version histories were invented.

## Display images received and integrated — 11 November 2026

The supplied Echo photos were reconstructed with the echo-display-renderer skill, using the firmware fonts and layout. Each new illustration has a reproducible JSON specification, a 128 × 64 native PNG, an enlarged preview and an SVG in `docs/assets/echo/`.

| Supplied photo | Illustration | Placement |
|---|---|---|
| `codex-clipboard-71cac8f4-5647-444a-9817-4106776b9539.jpg` | `self-test-progress.svg` — Test 2/3 | Both System Menu self-test sections |
| `codex-clipboard-f71fafa0-8795-45d7-b4bd-246f3730460f.jpg` | `self-test-pass.svg` — Pass, Fr: 134.0 Hz (-6.0) | Both System Menu self-test sections |
| `codex-clipboard-64c76944-1640-4a92-8b90-c4f039c81994.jpg` | `self-test-fail.svg` — Fail, Fr: 122.0 Hz (-18.0) | Both System Menu self-test sections |
| `codex-clipboard-65f55bdf-b0d7-4261-b78f-a34a6144b647.png` | Existing `signal-level.svg` matches the photo | Echo Signal Setup: STIPA front-panel level choices |

Han explicitly authorised use of the Echo self-test image in the Atlas guide because a complete Atlas with all twelve loudspeakers was unavailable. The Atlas page identifies these as shared Echo examples; they do not establish a physical Atlas test result or its correct reference setting. No separate Atlas Pass photo is outstanding. No further display photo is required for these sections.

## Remaining factual checks

- **Atlas hardware ratings:** confirm mass, dimensions, BNC input/output ratings and measured acoustic output. The former 1.0 kg, 100 × 105 × 170 mm and 24/8 h figures were copied from Echo and were not substantiated for Atlas. Confirm Atlas runtime at stated signals, gains and power conditions before adding numerical values.
- **Echo ratings:** existing mass, dimensions, runtime and calibration tolerance were retained from its original specifications; this review did not remeasure or independently certify them.
- **Echo local versus remote level limits:** the current front-panel code offers a custom STIPA editor from 40 to 80 dBA; shared REST validation caps STIPA at 70 dBA and advertises no custom-level choice. The supplied DIRAC Field screenshot shows its 60/70 dBA presets. The hardware guide now identifies its table as local front-panel settings; no firmware/API change was made. The supplied local STIPA photograph confirms that the front panel includes User alongside 60 and 70 dB. It confirms the custom-level entry point; its numerical range remains based on firmware rather than that photograph. The remote/local difference remains an implementation decision.
- **Self-test reference:** the shared defaults are 140 Hz and an 8 Hz tolerance, but stored settings can differ. Han confirmed that the reference and tolerance are factory settings and cannot be changed by the user. The manuals identify them accordingly without asserting the shared defaults for every unit. Factory/service configuration remains outside the customer instructions.
- **Remote self-test:** API `success`/`completed` describe acquisition success, not the OLED Pass/Fail tolerance comparison. A remote client must compare measured frequency with the stored reference and tolerance. The customer manuals do not imply that DIRAC Field already exposes a self-test control.

## Validation boundary

The review is grounded in source and supplied documents. No self-test, update or acoustic measurement was performed on physical Echo/Atlas hardware. Static link/anchor checks and desktop/phone browser checks validate the documentation, not the hardware.

Validation completed: 20 HTML pages including redirects, 403 local references and unique anchors passed. All 16 customer chapters were checked at 1280 px and 390 px widths, with no page overflow or broken images. The mobile chapter menu collapsed correctly. `git diff --check` passed.

Illustration validation on 11 November 2026: all three native screens are 128 × 64 and match their SVG lit-pixel counts. All 417 local references in the Echo/Atlas pages resolve. The two System Menu pages and Echo Signal Setup have no page/figure overflow at 1280 px and 390 px; paired results become one column on phones. The SVG display and STIPA menu render in the browser.

## Follow-up corrections — 11 November 2026

- Removed USB audio input from customer-facing Echo, Atlas and DIRAC Field pages; the hidden engineering capability remains in firmware.
- Clarified that DIRAC Field will play the stimulus during soundfield buildup before recording.
- Added the supplied password-backspace example to both System Menu pages using firmware glyph 127. Its JSON, SVG, native PNG and preview are in `docs/assets/echo/password-backspace*`.
- Documented the five-minute minimum enabled auto-off timeout, with zero disabled; firmware settings normalize older short values and the local editor shows the minimum before confirmation. Both REST APIs reject invalid types, fractional seconds and shorter enabled values; the app already enforces whole minutes and now states the minimum in its editor.
- Specified a quiet self-test environment and factory-only reference/tolerance.
- Identified Atlas's built-in power amplifier, recommended MiFi/phone hotspots for multiple-device systems across all relevant connection guides, and centered the Echo control-panel illustration.

Follow-up validation: 25 HTML pages and 617 local references passed link/anchor checks. The backspace native PNG is 128 × 64; its 904 lit pixels match the SVG. Echo Overview and both text-entry pages have no overflow or broken images at 1280 px and 390 px; the Echo control-panel center offset is zero apart from subpixel rounding. Aether status and Echo/Atlas status/UI components compiled with ESP-IDF. Both sanitized timeout host regressions, the Aether network-mode regression and Echo/Atlas signal/settings regression passed. The Windows DIRAC Field build and 132 focused tests passed. No firmware was flashed; physical auto-off timing and front-panel interaction remain to be verified on devices.
