# Vanguard Raid Planner — standalone Linux edition

Includes the current planner, constraint builder, icons, roster editing, team generation,
parallel-team balancing, Discord message exports, and session JSON import/export.
No build step, npm installation, ChatGPT account, or Sites hosting is required.

## Hosted site

Live on GitHub Pages:

https://nayberhq.github.io/vanguard-raid-planner/

Pushes to `main` run CI (file/syntax/icon checks), then deploy the `public/` folder.
Pull requests run the same checks without deploying.

## Launch

Requirements: Python 3.7+ and unzip.

```bash
unzip vanguard-raid-planner.zip
cd vanguard-raid-planner
bash start.sh --port 8080
```

Open `http://YOUR_SERVER_IP:8080` in your browser. Allow TCP port 8080 in your
server firewall if you want to access it remotely. Press Ctrl+C to stop.
The default bind address is 0.0.0.0; for local-only access use:

```bash
bash start.sh --host 127.0.0.1 --port 8080
```

You can also serve the `public/` directory directly with an existing Nginx,
Apache, or other static web server. Use HTTPS on an internet-facing server.
The included Python server is a convenient launcher; use your usual web server
and access controls for a persistent production deployment. This standalone
edition has no built-in login.

## Sessions and imports

Roster and generated teams are kept in the open browser session. Export session
JSON to save them, then use Import → Restore saved session to resume. Constraint
and comp templates are saved in that browser's local storage; they are also
included in session JSON. On the Comp tab you can export or import just those
template libraries as standalone JSON (imports merge by template name). Full comp
templates and session JSON also include the Fellowship setup card: role coverage rules, role targeting defaults, class/spec
overrides and a separate Advanced placement section. Overrides take precedence
over role defaults and apply to every matching role rule. Team size steps through
6, 12, 18 and 24. Tank groups contain tanks; other groups with DPS are DPS groups.
If every group contains tanks, the most DPS-heavy groups also count as DPS groups.
Rules apply per matching group, supporting multiple tank/DPS groups in large raids.
An any-one-fellowship provider is assigned one target across all setup rules;
it cannot cover both groups simultaneously. Timed ability targets remain
configured separately in cooldown constraints. Required setup rules guide
class/spec selection and fellowship search; closest teams remain visible if
no valid placement is found.
Moving to a different hostname or browser does not automatically transfer data.
Export from the hosted planner and restore that JSON here to migrate your session.
There is no shared server database or automatic synchronization between users.

All app assets are bundled locally. Raid-Helper JSON file and paste imports and
team generation work without external requests. Loading events by Raid-Helper
link requires internet access and Raid-Helper to allow the request; file or paste
import remains available if that request is blocked. Use Load to replace the
roster from signups, or Append to add new players and roles without changing
existing schedules or preferences. Some browsers require HTTPS or localhost for
clipboard access; the export dialog lets you select and copy messages manually
as well.

Class artwork is credited to LOTRO Wiki via the collection referenced in the app.

## Files

- `public/`: complete static application and class icons
- `start.sh`: Linux launcher
- `server.py`: dependency-free Python static server
- `README.md`: these instructions
- `tests/planner.test.cjs`: planner regression checks (`node tests/planner.test.cjs`)

Role counts and recipients are now edited together in Roles & fellowship targets. Whole raid counts players once; each/tank/DPS targets apply per matching fellowship. Class/spec overrides can require or prefer physical tank/DPS fellowship placement independently of coverage. DPS concentration with buffers is a soft objective below Required rules. Older role totals migrate into Whole raid rows when opening Comp; templates and session exports preserve unified rules.

Role assignments now use a popup editor, with one slot per row, Required/Preferred importance, and a compact role-colored rough fellowship preview. Duplicate creates a second slot; matching assignments accumulate rather than reusing one provider. Targeting defaults and class/spec overrides are collapsed below the overview.

General assignments use Role (including Don’t care), Source (Each/Any/DPS/Tank), and Target (Same/Any/All). Specific class/spec rows inherit fields marked Don’t care; a Role wildcard matches all assigned roles. Explicit DPS/Tank sources constrain physical fellowship placement. Source Any is one slot total; Each/DPS/Tank apply per matching source. Older settings migrate when opening Comp.

Comp separates Team requirements (role minimum/preferred counts, physical presence versus coverage, source/target) from Class capabilities (role reach defaults and class/spec reach overrides). Legacy class placement specifics migrate to placement requirements. Capabilities do not request players. Raid-wide debuffers prefer tank fellowships below Required rules; targeting uses the label Raid.

Requirement editor uses one slot per selected scope (Per fellowship / Per tank group / Per DPS group / Per raid); duplicate to add slots. Prior count rows expand into equivalent assignments. No debuffer-specific or tank-specific grouping preference: unconstrained players move freely while DPS concentration and buffer proximity guide soft balancing.

Team preview now uses the fellowship optimizer on placeholder members, instead of hard-coded placement of raid-scoped roles. Role assignment class/spec controls are always visible, and the physical-presence switch is removed. Role template library saves/loads/deletes requirement and capability presets with JSON import/export and session backup. Actual rosters and additional constraints are not replaced when loading a role template.

Compatible coverage is resolved before staffing: wildcard-role class/spec rows with a different target override matching general coverage rather than adding slots. Class-presence rows can share a role slot; identical role duplicates accumulate. Preview shows provider alternatives and overlapping class requirements in raid/fellowship notes.

Bundled starter libraries include Heal cut and Default raid from supplied configuration. They appear once per browser without replacing matching saved templates, importing rosters, or activating rules. Deleting a starter template is respected on subsequent reloads.


## Background generation and schedule repair

Team generation runs in `planner-worker.js`, sharing `app.js`, `fellowship.js`, `constraints.js`, and `search.js` with the UI and tests. A modal spinner reports stages and offers Cancel; cancelling terminates the worker and preserves the last generated teams. Upload all JavaScript files along with index.html when deploying. Standard HTTP/HTTPS hosting (including GitHub Pages) supports the worker.

Schedule repair prioritizes required-rule deficits, player coverage, then role preferences/class variety/character repeats and even participation. It considers replacements and exchanges across runs, rejects unavailable or overlapping player assignments, and tries three alternate starts after the initial local improvement pass. Final candidates use the existing complete validation, including cooldown simulation. Candidate enumeration and repair passes are bounded; this improves search without guaranteeing a global optimum. Recommendation feasibility searches use the lighter original allocation to keep total work bounded.

Run `node tests/planner.test.cjs` and `node tests/background.test.cjs` for regressions.

Role priorities in Comp show selectable class/spec icons for every role: selected icons get first priority, unselected icons get second priority. They remain soft preferences and are included in comp templates and session exports. By default no icons are selected. Older first-choice settings remain selected; other tiers become unselected. Blue Lore-master is classified as Buffer; old roster and generated assignments are migrated on session import. See [SELECTION.md](SELECTION.md) for the search stages, objective and current weights.

Each selected class/spec receives its priority bonus only once per raid. Additional matching players use ordinary priority cost and retain the normal duplicate-class penalty. This cap applies to flow allocation, local improvements, parallel balancing and schedule repair.

Roster preferences use a star button per signed-up class. Starred classes share first choice; all unstarred classes share second choice. This applies to all playable specs of the class, and signup order no longer contributes a preference weight.
