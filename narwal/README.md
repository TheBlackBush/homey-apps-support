# Narwal for Homey

Control your Narwal robot vacuum from Homey Pro. The app talks to the robot directly over your home network, so no Narwal account is needed; signing in with your Narwal account is optional (Cloud mode, cloud-only models and the camera).

- **Install:** [Homey App Store](https://homey.app/a/com.narwal.global/) ([test version](https://homey.app/a/com.narwal.global/test/))
- **Questions and news:** [Homey Community thread](https://community.homey.app/t/app-pro-narwal-control-for-narwal-robot-vacuums/160061)
- **Report a problem or ask for a feature:** [open an issue](https://github.com/TheBlackBush/homey-apps-support/issues/new/choose) and choose **Narwal**

> Unofficial community app. Not affiliated with, authorised by, or endorsed by Narwal. "Narwal" and "Freo" are trademarks of their respective owners and are used here only to describe compatibility.

## Features

- Local LAN connection to the robot, usually on WebSocket port `9002`.
- Optional Cloud mode: sign in with your Narwal account in the app settings to control the robot through the Narwal cloud, with the same features as Local. Choose the country your Narwal account is set to: Narwal keeps each account on its country's own server, and the app uses the same server as the Narwal app.
- Separate Homey drivers for each supported model.
- Start, pause, resume and stop cleaning.
- Return to dock and locate the robot. "Dock" in the app is the robot's Narwal base station.
- Live battery, charging, docked, connected, cleaning area/time, firmware, status and last error.
- Fan-speed control: `Quiet`, `Standard`, `Strong`, `Super Powerful`, `Ultra Powerful` (Freo Z10 Pro / Turbo: up to Super Powerful). A level chosen while docked is used for the next clean.
- Room cleaning with Flow autocomplete. Room names match the Narwal app (custom names in any language, and numbered types such as `Toilet1`, `Toilet2`).
- Cleaning mode settings (mode, water level, mop strength, passes, route) and a Clean with settings Flow card for one-off cleans.
- Station actions: empty the dustbin, wash the mop and dry the mop, from Flows.
- Robot settings read from the robot itself (child lock, pet mode, hot water mop wash, mop drying, obstacle avoidance, station light and more), in the app settings and in Flows. Each robot only shows the settings it supports.
- Robot camera (experimental, off by default): live video from the robot's camera in the device's camera view, for robots with remote view in the Narwal app. Needs a Narwal account. See [Camera](#camera-experimental).
- Flow actions, conditions and triggers for common automation scenarios.
- Narwal Map widget: the robot's map in the Narwal app's room colours, room names, dock, and the robot's live position and cleaning path, in Homey's light and dark theme.
- Narwal Consumables widget: what the robot asks you to clean or replace now, and (with a Narwal account) the life left for each part as in the Narwal app, with a Reset button per part. A Flow trigger and condition for parts that need attention.
- Diagnostics in the app settings: a read-only report to share, a status recording through a cleaning cycle, and command tests.
- In English, Dutch, German, French, Italian, Swedish and Spanish, following Homey's language.
- Resilient reconnect, heartbeat keep-alive and polling fallback.

## Supported models

Each model's pairing screen and its device settings (**Connection type**) show how it connects: **Local + Cloud** works over your network (the default) or through your Narwal account, **Cloud only** works only through your Narwal account, because the robot keeps its local port closed.

| Homey driver | Connection | Status |
| --- | --- | --- |
| Flow 2 | Local + Cloud | Tested daily, both modes |
| Flow | Local + Cloud | Local control confirmed by owners |
| Flow Compact | Local + Cloud | Same robot as the Flow with a smaller station; not yet tested |
| Freo 20 | Local + Cloud | Local control confirmed by owners |
| Freo 20 Edge | Local + Cloud | Local control and room cleaning reported by an owner |
| Freo Z10 Ultra | Local + Cloud | Local control confirmed by owners |
| Freo Z10 Pro / Turbo | Local + Cloud | Local control confirmed on the Pro; the Turbo is the same robot. No Ultra suction |
| Freo X10 Pro | Local + Cloud | Local control confirmed by owners |
| Freo Z Ultra | Local + Cloud | Added from your Narwal account list (it only answers with its cloud device ID). It never sends live updates, so Homey checks it every 15 seconds; its status can lag while it works |
| Freo Pro | Local + Cloud | Not yet tested. If it does not answer locally, use Cloud mode |
| Freo S | Local + Cloud | Not yet tested. If it does not answer locally, use Cloud mode |
| Freo X Ultra | Cloud | Local port closed on this model. No Ultra suction |
| Freo X Plus | Cloud | Local port closed on this model |
| Freo Z10 | Cloud | Local port closed on this model |
| Other Narwal robot | Depends on the model | Any other Narwal robot vacuum, such as the China-market 002/003, JX, J5 and J6 series and newer models. Named from Narwal's model list; not yet tested |

Cloud-only robots connect through your Narwal account even when the app's connection setting is Local, so you need to be signed in. Reports from owners of the untested models are very welcome.

### Not supported

- The original **Narwal Freo** (2021): it uses an older command set. Support may come once an owner can help test it.
- T10 / J1 and J2: an older protocol.
- Narwal S-series and F-series floor washers: not robot vacuums.

## Pairing

1. Make sure the robot is powered on and awake.
2. In Homey, go to **Devices → Add device → Narwal**.
3. Choose the exact model from the list, or **Other Narwal robot** for a model that is not listed. The cloud-only models (Freo X Ultra, Freo X Plus, Freo Z10) and the Freo Z Ultra are added from your Narwal account: sign in through the app settings first, then add the robot.
4. Pick your robot under **Robots found on your network**, or enter its IP address and port (default `9002`) if it is not listed.
5. When entering an IP, press **Continue**. The app validates the local connection and reads robot status.

Robots found on the network follow IP changes automatically; a DHCP reservation is still recommended.

## Flow cards

### Actions

- Start cleaning
- Pause cleaning
- Resume cleaning
- Stop cleaning
- Return to dock
- Locate robot
- Set fan speed
- Clean selected room
- Clean default rooms
- Clean with settings
- Empty the dustbin
- Wash the mop
- Dry the mop
- Reset a part
- Turn a robot setting on or off
- Change a robot setting
- Refresh robot status
- Refresh rooms and map

### Conditions

- Robot is cleaning
- Robot is docked
- Robot is charging
- Battery is above a percentage
- Robot is connected
- A part needs attention

### Triggers

- Robot started cleaning
- Robot paused
- Robot resumed
- Robot stopped
- Robot returned to dock
- Robot docked
- Robot undocked
- Battery level changed
- Charging state changed
- Cleaning completed
- Connection lost
- Connection restored
- A part needs attention

## Map, rooms and widget

- The app requests the robot's map when it connects and when the robot starts or stops working, and keeps it up to date from the robot's live map updates while it cleans. The last map is saved on Homey, so cleaning and the widget work right away after a restart.
- Rooms and their names come from the map and are used by the room Flow cards and the default rooms setting.
- The **Narwal Map** widget draws the map with the Narwal app's room colours (neighbouring rooms always differ), thin walls, room names that fit, the dock, and the robot with its heading. While the robot cleans, its position and path update live (pushed about every 2 seconds). The path stays visible after docking until the next clean starts.
- Widget settings: show status, show room names, and the refresh interval.
- If no map is available yet, run a full map-building clean in the official app, then press **Refresh** in the app settings (or run the Refresh rooms and map Flow card).

## Consumables

- The **Narwal Consumables** widget shows the parts the robot asks you to clean or replace now. The robot reports these itself, so this works in Local mode without an account.
- When you are signed in to your Narwal account (in either connection mode), it also shows the life left for each part in percent and hours, the same numbers as the Narwal app, plus the parts to clean regularly. The names come from Narwal in your Homey language when available.
- The app checks when the robot connects, after each clean and every hour, and keeps the last known values if the robot or the Narwal cloud does not answer.
- Flow: **A part needs attention** (tokens: part, action) fires once per part; the condition **A part needs attention** is true while anything is due.
- Widget settings: show hours left, show parts to clean regularly.

Core vacuum controls do not depend on the map, except starting a whole-home or room clean, which needs the map's room list.

## Camera (experimental)

- For robots with remote view in the Narwal app (the robot reports it in its own feature list, for example the Flow 2). Turn it on in the device settings under **Camera (experimental)**, and enter the robot's video code if you set one in the Narwal app. Remote view must be turned on for the robot in the Narwal app, and a Narwal account must be signed in to the app settings (in either connection mode).
- The video goes from the robot through Narwal's cloud to your phone or browser; nothing passes through or is stored on Homey.
- The robot sends H.265 video. It plays in the **Homey web app** (desktop browsers and Safari on the iPhone). The Homey phone apps cannot play H.265 yet: the camera view then says so, and the robot's camera is not started.
- A view ends when you close it, and the robot ends a view by itself after about two minutes; open it again to continue.
- Turning the setting off stops the camera at once; the camera view itself goes away the next time the app starts (Homey keeps it until then), and opening it says the camera is turned off.

## Troubleshooting

### Diagnostics

Open **Apps → Narwal → Configure**, pick the robot and press **Run diagnostics**. In about a minute it checks the network, the connection, the robot's model, firmware and features, its status messages, the map, consumables and the Narwal account, and shows a report to copy or share. It only reads information (the robot does not move) and leaves out IDs, addresses, room names and your account. Paste the report in a [bug report](https://github.com/TheBlackBush/homey-apps-support/issues/new/choose) or in the [Homey Community thread](https://community.homey.app/t/app-pro-narwal-control-for-narwal-robot-vacuums/160061) when asking for help or reporting a model that is not tested yet.

The app also writes what it does to its log, without IDs, addresses, emails or room names: pairing steps, the Narwal account's server and robot count, how each robot connects, a short summary once the robots have connected (and every hour after), and the diagnostics report when you run it. A Homey diagnostics report (**Settings → Apps → Narwal → Send diagnostics report**) therefore shows what went wrong.

### Pairing cannot reach the robot

- Verify the robot IP address and port.
- Make sure Homey and the robot are on the same LAN/VLAN.
- Wake the robot by opening the official app once, then close it and retry.
- Confirm another client is not holding the only local connection.

### Official app conflicts with Homey

Some robots appear to allow only one local client at a time. Close the official Narwal app while Homey is connected.

### Rooms or map are empty

- Build a map in the official app first.
- Press **Refresh** in the app settings.
- If the widget still has no map, the current local payload may not contain parsable map data yet.

### Signed in, but no robot is listed

Narwal keeps each account on its country's own server, and the robots are only listed there. Sign out in the app settings and sign in again with the country your Narwal app account is set to. (Before 1.4.2 the app sent many countries, such as Canada, Australia, the UK and Germany, to a shared server; signing in again fixes that.)

### Cloud mode is slow to answer

Over the Narwal cloud, the robot's replies take 20 to 30 seconds. The app waits for them, and commands succeed as soon as the robot's status shows the result, usually within a few seconds. If the official Narwal app shows a network error for the robot, Homey cannot reach it through the cloud either; restart the robot or check its internet access.

### Connection keeps dropping

- Use a static IP or DHCP reservation.
- Check Wi-Fi signal near the dock.
- Be aware that firmware updates can change local protocol behavior.

## Reporting a problem

1. Run the app's diagnostics: **Apps → Narwal → Configure → Diagnostics → Run diagnostics → Copy report**.
2. [Open a bug report](https://github.com/TheBlackBush/homey-apps-support/issues/new/choose), choose **Narwal**, and paste the report. Or send a Homey diagnostics report (**Settings → Apps → Narwal → Send diagnostics report**) and add its Log ID to the issue.
3. Do not paste your email address, passwords, video code, device IDs, IP addresses or room names: issues here are public. The app's report already leaves these out.

## Privacy

This app talks to your robot on your local network by default. Cloud mode is optional: only when you switch Connection to Cloud and sign in with your Narwal account in the app settings does the app connect to Narwal's servers, and then only to control your own robots. Your password is never stored; only the session from Narwal is kept on your Homey. The robot camera is off by default; when you turn it on and open the camera view, the video comes from the robot through Narwal's cloud, as in the Narwal app. The video code you enter for it is kept in the device settings. The app sends no telemetry or analytics to the developer, Narwal or any third party.
