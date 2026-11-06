# DIRAC Field manual — illustrations to provide

This is an authoring checklist, not a chapter in the customer manual. The manual text is drafted; the numbered comments in its HTML mark suggested illustration locations. Screenshots have not been invented or substituted with mockups.

## Capture instructions

- Prefer original PNG screenshots at the phone/tablet's native resolution, in portrait orientation, with the whole app page visible. Use one consistent platform and display scale for the first set.
- Keep app labels, menus, status indicators and transport controls readable. For a long page, provide consecutive screenshots rather than a reduced full-page image.
- Use representative names and data, for example Project “Room survey”, Group “Room A”, source “Source 1” and receiver “Receiver 1”. Keep those names consistent across related screenshots.
- Conceal actual passwords. A password field should be masked or empty; use fictitious values if a visible example is needed.
- Record the DIRAC Field version, platform and connected device software versions with the batch. Include the selected device type in the filename where indicated.
- The filenames below are proposed delivery names. Keep images unannotated: numbers, arrows and captions can be added separately.
- “Core” images establish the main user journey. “Supporting” images explain less frequent actions or a second state and can follow later.
- Several requests have a/b/c states. Keep them as separate native images; they can be combined into a labelled comparison later.
- No factory reset, firmware installation or fault needs to be performed solely to obtain a screenshot. Capture the setup/confirmation screen, or use an existing example of a progress/error state when available.
- The Aether/AEM-01 product illustration is already available and does not need to be supplied again.

## General navigation and measurement workflow

| ID | Priority | Proposed filename(s) | What to show | Manual location / purpose |
|---|---|---|---|---|
| DF-01 | Core | df-01-app-menu.png | Open the app menu on Devices; show Devices, Projects, Settings, Help and About. | [Overview — navigation](index.html#navigation). Establish the shared navigation and its context. |
| DF-02 | Core | df-02-destination-picker.png | “Save the next measurement to” open from Save to; include existing project/group choices and creation choices. | [Quick Start — destination](quick-start/index.html#destination), reused for project/destination instructions. |
| DF-03 | Core | df-03-devices.png | Devices list with Aether, Echo, Atlas, HBK 2755 and HBK 2255 if available; readable names and connection/battery states. Multiple screens are fine if the list is long. | [Connecting Devices — discovery](connecting-devices/index.html#discovery), also the device-role overview. |
| DF-04 | Supporting | df-04-add-device.png | Add Device IP-address prompt, with a representative address and its confirm/cancel actions. | [Connecting Devices — manual address](connecting-devices/index.html#manual-address). |
| DF-05 | Core | df-05-device-authentication.png | Device authentication prompt for a representative device, password concealed, with connection actions visible. | [Connecting Devices — authentication](connecting-devices/index.html#authentication). |
| DF-06 | Core | df-06-projects.png | Projects page with two or more named projects, their counts and New/Edit/Export/Delete actions visible as applicable. | [Projects — create or edit](projects-and-groups/index.html#projects). |
| DF-07 | Core | df-07-project-editor.png | New/Edit project with name, temperature, pressure and humidity, plus Save and Cancel. | [Projects — create or edit](projects-and-groups/index.html#projects). Show defaults and their units. |
| DF-08 | Core | df-08-project-groups.png | One project showing several groups and its active group, including Use/Edit/Export/Delete and New group. | [Projects — groups](projects-and-groups/index.html#groups). |
| DF-09 | Core | df-09a-group-measurements.png; df-09b-group-selection.png | First the group with actual saved measurement summaries; then Select mode with two selected measurements and Move/Export/Delete actions. | [Projects — inspect, move and delete](projects-and-groups/index.html#measurements). |
| DF-10 | Core | df-10-measurement-metadata.png | Edit Measurement Metadata showing name, type, receiver distance and speech/noise controls. Use a multi-receiver example if available; provide scrolling panels for a long form. | [Projects — metadata](projects-and-groups/index.html#metadata). |
| DF-11 | Core | df-11a-capture-progress.png; df-11b-retrieval-progress.png | A source-triggered measurement during capture and then retrieval/processing, with the real stage text, progress and available Stop/Cancel controls. | [Measurement workflow — run](measurement-workflow/index.html#run). Reused for recorder progress explanations. |

## Device control pages

| ID | Priority | Proposed filename(s) | What to show | Manual location / purpose |
|---|---|---|---|---|
| DF-12 | Core | df-12a-aether-slm-live.png; df-12b-aether-leq-final.png | Aether in SLM mode with a live parameter and Start/Stop state; then a completed timed Leq with its interval and final status visible. | [Aether — control page](device-controls/aether/index.html#page) and [SLM](device-controls/aether/index.html#slm). |
| DF-13 | Core | df-13-aether-recording.png | Aether in Recording mode, idle and ready, showing Save to, input indication, duration and Record. | [Aether — control page](device-controls/aether/index.html#page) and recording steps. |
| DF-14 | Core | df-14a-aether-slm-configuration.png; df-14b-aether-leq-configuration.png | SLM configuration with L and its weighting controls; a second image with Leq selected so the missing time-weighting field is apparent. Include Apply/Cancel. An expanded selector can be an additional inset. | [Aether — SLM](device-controls/aether/index.html#slm). |
| DF-15 | Core | df-15-aether-calibration-start.png | Calibrate Aether dialog before Start, including the calibrator-level field and dB unit. | [Aether — calibration](device-controls/aether/index.html#calibration). |
| DF-16 | Supporting | df-16a-aether-calibration-progress.png; df-16b-aether-calibration-result.png | Actual calibration progress and a successful result. Include a failure example only if one already exists. | [Aether — calibration](device-controls/aether/index.html#calibration). |
| DF-17 | Supporting | df-17a-aether-recovery-options.png; df-17b-aether-password-restoration.png | Recovery options reached from a recovery-mode card, then Restore factory password with an empty/masked entry. | [Aether — recovery](device-controls/aether/index.html#recovery). |
| DF-18 | Supporting | df-18a-aether-reset-confirmation.png; df-18b-aether-reset-physical-confirmation.png | Factory-reset data-loss/setup screen and the physical-confirmation instructions. If safely available, include the final Erase and reset screen without executing it. | [Aether — recovery](device-controls/aether/index.html#recovery). Distinguish reset from password restoration. |
| DF-19 | Core | df-19-echo-control.png | Echo ready with a representative Pink MLS/e-Sweep selection, Play/Stop and the measurement action, plus Save to with an eligible receiver available. | [Echo/Atlas — control page](device-controls/echo-atlas/index.html#page). |
| DF-20 | Core | df-20-atlas-control.png | Atlas ready with PMLS-RA or ESWP-RA, its gain knob/readout, transport controls and Save to. | [Echo/Atlas — control page](device-controls/echo-atlas/index.html#page). Make the difference from Echo visible. |
| DF-21 | Core | df-21a-echo-signal-setup.png; df-21b-echo-stipa-setup.png | Echo Pink MLS/e-Sweep configuration with mode, length and level choices; then STIPA showing its supported preset-level choices. Include Apply/Cancel. | [Echo/Atlas — configuration](device-controls/echo-atlas/index.html#configure) and [Echo](device-controls/echo-atlas/index.html#echo). |
| DF-22 | Core | df-22-atlas-signal-setup.png | Atlas PMLS-RA/ESWP-RA configuration showing type, offered modes, length and custom gain. Include Apply/Cancel. | [Echo/Atlas — configuration](device-controls/echo-atlas/index.html#configure) and [Atlas](device-controls/echo-atlas/index.html#atlas). |
| DF-23 | Supporting | df-23-echo-atlas-user-signals.png | User configuration with two or more stored audio names, selector, Upload/Delete and transfer indication if available. Either AE source can demonstrate the shared controls; note the device used. | [Echo/Atlas — user signals](device-controls/echo-atlas/index.html#user-signals). |
| DF-24 | Core | df-24-hbk2755-control.png | HBK 2755 with one of White/Pink/User active, gain and knob visible, plus measurement controls with an eligible receiver available. | [HBK 2755 — signal controls](device-controls/hbk2755/index.html#signals). |
| DF-25 | Core | df-25-hbk2755-user-signals.png | User Signals page opened by holding User, with file selection, Set as User, Upload and Delete visible. | [HBK 2755 — user signals](device-controls/hbk2755/index.html#user-signals). |
| DF-26 | Core | df-26-hbk2255-control.png | HBK 2255 recording page with input-level indication, destination, duration selector and Record. | [HBK 2255 — control page](device-controls/hbk2255/index.html#page). |
| DF-27 | Supporting | df-27-hbk2255-eligibility.png | Device card showing an existing “BZ-7351 missing or inactive” or “status not verified” message. Do not alter a working licence just to capture this. | [HBK 2255 — prerequisites](device-controls/hbk2255/index.html#prerequisites). Clarify the difference from recording-only capture. |

## Results, analysis and export

| ID | Priority | Proposed filename(s) | What to show | Manual location / purpose |
|---|---|---|---|---|
| DF-28 | Core | df-28-measurement-pressure.png | Open stored Signal measurement with Category: Views and View: Pressure; include title, selectors, waveform and playback/export controls. | [Results — open](results-and-analysis/index.html#open). |
| DF-29 | Core | df-29-impulse-response-etc.png | A usable impulse response in ETC view, showing its direct arrival and decay. | [Results — signal views](results-and-analysis/index.html#views). |
| DF-30 | Supporting | df-30a-spectrum.png; df-30b-spectrogram.png | Spectrum and Spectrogram for the same representative recording, axes readable. | [Results — signal views](results-and-analysis/index.html#views). |
| DF-31 | Core | df-31a-t20-graph.png; df-31b-t20-table.png | The same reverberation parameter and measurement in Graph and Table representation. Use valid bands and readable units; include an unavailable band if naturally present. | [Results — parameters](results-and-analysis/index.html#parameters). |
| DF-32 | Supporting | df-32-stipa-result.png | A valid scalar STIPA result with category/parameter selection and its descriptive text. Record whether this is a direct STIPA capture or an IR calculation. | [Results — parameters](results-and-analysis/index.html#parameters). |
| DF-33 | Core | df-33-parameter-display.png | Parameter display dialog: resolution, representation, graph style, grid, trace width, frequency range and y-axis limits, including Apply/Close. Supply scrolling panels if necessary. | [Results — display options](results-and-analysis/index.html#display). |
| DF-34 | Core | df-34-export-format.png | Export action sheet offering Export for Dirac (.dmpx) and Export data. Use an ordinary non-developer build/state. | [Export — desktop DIRAC](export-and-desktop-dirac/index.html#dirac). |
| DF-35 | Supporting | df-35a-export-data-content.png; df-35b-export-result-format.png | Data content chooser (WAV / calculated results / both), then CSV/TXT chooser. | [Export — data](export-and-desktop-dirac/index.html#data). |
| DF-36 | Supporting | df-36a-system-save.png; df-36b-export-complete.png | Representative operating-system save picker and the app's successful export-complete message. Use a neutral folder and filename. | [Export — save](export-and-desktop-dirac/index.html#save). Platform-specific picker appearance will be identified in the caption. |

## Settings and maintenance

| ID | Priority | Proposed filename(s) | What to show | Manual location / purpose |
|---|---|---|---|---|
| DF-37 | Core | df-37-device-settings.png | Device settings for an AE device: top identity/header and section headings. ID expanded with the reported version. | [Device settings — open](device-settings/index.html#open). |
| DF-38 | Core | df-38-device-network-station.png | AE Network section expanded with SSID selection, Connect, Auto-reconnect and Save auto-reconnect setting for a saved network. Conceal passwords. | [Device settings — Network](device-settings/index.html#network). |
| DF-39 | Supporting | df-39a-ae-device-hotspot.png; df-39b-hbk2755-hotspot.png | Device access point editor for AE equipment, and HBK 2755's separate hotspot credential fields for comparison. | [Device settings — Network](device-settings/index.html#network). |
| DF-40 | Supporting | df-40-device-password.png | Unified Device password section showing masked/empty fields, Generate/Copy, and Change device password. | [Device settings — password](device-settings/index.html#password). |
| DF-41 | Core | df-41a-receiver-measurement-settings.png; df-41b-aether-led-settings.png | Aether Measurement section with default distance, Save and Calibrate; then LEDs with brightness, attention time and Save. An HBK 2255 distance-only comparison is optional. | [Device settings — Measurement and LEDs](device-settings/index.html#measurement). |
| DF-42 | Supporting | df-42a-update-available.png; df-42b-update-progress.png; df-42c-rollback-offer.png | Update available with Check/Install actions; an existing download/install progress example; and a retained rollback offer with target version where actually available. Do not install or roll back just to obtain images. | [Device settings — updates](device-settings/index.html#updates). Note device family for each image. |
| DF-43 | Core | df-43-app-filename-settings.png | App settings → Measurements with prefix choice, source/receiver options, preview and Save filename format. | [Application Settings](application-settings/index.html#open) and filename instructions. |
| DF-44 | Supporting | df-44-stored-password-management.png | Device Management with example device Clear actions and Clear All Stored Passwords. No actual passwords should be visible. | [Application Settings — passwords](application-settings/index.html#passwords). |
| DF-45 | Supporting | df-45-forgotten-devices.png | Forgotten Devices with one example device and its Unblock action. | [Application Settings — forgotten devices](application-settings/index.html#forgotten). |
| DF-46 | Supporting | df-46-about.png | About page showing DIRAC Field identity, app version and AE Field branding. | [Application Settings — About](application-settings/index.html#about), reused for support/version instructions. |

## Suggested first delivery

Provide the main control pages first: **DF-12, DF-13, DF-19, DF-20, DF-24 and DF-26**, followed by the configuration pages **DF-14, DF-21, DF-22 and DF-25**. These establish whether the device-specific text matches the actual app appearance. The remaining Core requests complete the shared workflow; Supporting requests can follow afterward.

One good screenshot can be reused wherever the same page is discussed. There is no need to repeat the project picker or the shared settings page for every device unless the visible controls differ.

## Items for text review alongside the screenshots

- Confirm that the source-triggered receiver set and HBK 2255 BZ-7351 explanation match the intended released product behaviour.
- Confirm the current detail-page limitation: the first successful receiver recording opens, with no receiver selector. The manual directs users to a full export for other receiver data.
- Supply an approved, versioned release history when available; the version chapter currently avoids inventing release dates or shipped-version claims.
