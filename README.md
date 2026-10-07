# Vanguard Raid Planner — standalone Linux edition

Includes the current planner, constraint builder, icons, roster editing, team generation,
parallel-team balancing, Discord message exports, and session JSON import/export.
No build step, npm installation, ChatGPT account, or Sites hosting is required.

## Hosted site

Live on GitHub Pages:

https://kidshuster.github.io/vanguard-raid-planner/

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
template libraries as standalone JSON (imports merge by template name).
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
