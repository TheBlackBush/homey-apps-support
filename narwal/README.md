# Narwal for Homey

Control your Narwal robot vacuum from Homey Pro: start and stop cleans, clean single rooms, send the robot back to its station, wash and dry the mop, and see its status, a live map and the state of its parts on your Homey dashboard. Homey talks to most robots directly over your home network, so they respond right away and keep working when the internet is down. Signing in with your Narwal account is optional, and needed only for a few models and features.

- **Install:** [Homey App Store](https://homey.app/a/com.narwal.global/) ([test version](https://homey.app/a/com.narwal.global/test/))
- **Questions and tips:** [Homey Community thread](https://community.homey.app/t/app-pro-narwal-control-for-narwal-robot-vacuums/160061)
- **Report a problem or ask for a feature:** [open an issue](https://github.com/TheBlackBush/homey-apps-support/issues/new/choose) and choose **Narwal**

> Unofficial community app. Not affiliated with, authorised by, or endorsed by Narwal. "Narwal" and "Freo" are trademarks of their respective owners and are used here only to describe compatibility.

## What you can do

- **Clean:** start, pause, resume and stop a clean, clean the whole home, your favourite rooms or a single room, and send the robot back to its station.
- **Choose how it cleans:** vacuum, mop or both, suction, water level, mop strength, number of passes and route, for every clean or just for one.
- **Use the station:** empty the dustbin, wash the mop and dry the mop.
- **See what it is doing:** battery, charging, docked, status (cleaning, returning, washing the mop and so on), the room it is in, the area and time of the clean, and its last error.
- **Map widget:** your home's map in the Narwal app's colours, with room names and the robot's live position and path while it cleans.
- **Parts widget:** what the robot asks you to clean or replace now, the life left for each part, and a Reset button per part.
- **Robot settings:** child lock, pet mode, hot water mop washing, mop drying, obstacle avoidance, the station light and more, as in the Narwal app.
- **Automations:** use all of the above in Homey Flows, for example clean when everyone has left, or get a message when a part needs attention.
- **Camera (experimental):** watch the robot's camera in Homey, on robots with remote view.
- **Languages:** English, Dutch, German, French, Italian, Swedish and Spanish, following your Homey's language.

## Which robots work

When you add a robot, choose its model in Homey. Each model's pairing screen also says how it connects.

| Narwal robot | Connection | Tested |
| --- | --- | --- |
| Flow 2 | Local or Cloud | Yes, daily |
| Flow 2 Compact (Flow 2 with the Compact Station) | Local or Cloud | Not yet (from version 1.4.5) |
| Flow | Local or Cloud | Yes, by owners |
| Flow Compact | Local or Cloud | Not yet |
| Freo 20 | Local or Cloud | Yes, by owners |
| Freo 20 Edge | Local or Cloud | Yes, by an owner |
| Freo Z10 Ultra | Local or Cloud | Yes, by owners |
| Freo Z10 Pro | Local or Cloud | Yes, by an owner |
| Freo Z10 Turbo | Local or Cloud | Not yet (from version 1.4.5) |
| Freo X10 Pro | Local or Cloud | Yes, by owners |
| Freo Z Ultra | Local or Cloud, added from your Narwal account | Yes, by an owner |
| Freo Pro | Local or Cloud | Not yet |
| Freo S | Local or Cloud | Not yet |
| Freo X Ultra | Cloud only | Not yet |
| Freo X Plus | Cloud only | Not yet |
| Freo Z10 | Cloud only | Not yet |
| Freo, the original from 2021 | Cloud only | Not yet (from version 1.4.5) |
| Other Narwal Robot (any other Narwal robot vacuum, for example the China-market models) | Depends on the model | Not yet |

- **Local or Cloud:** Homey talks to the robot over your home network (the default), or through your Narwal account if you choose Cloud.
- **Cloud only:** the robot keeps its local connection closed, so Homey always reaches it through your Narwal account. Sign in first (see [Connect your Narwal account](#connect-your-narwal-account)).
- Own a model that is not tested yet? Please tell us in the [Community thread](https://community.homey.app/t/app-pro-narwal-control-for-narwal-robot-vacuums/160061) whether it works, ideally with a diagnostics report (see [Diagnostics](#diagnostics)).

**Not supported:** T10, J1 and J2 (an older protocol), and the Narwal S and F series floor washers (they are not robot vacuums).

**Model notes:**
- **Freo Z10 Pro, Freo Z10 Turbo and Freo X Ultra:** up to Super Powerful suction (no Ultra Powerful).
- **Freo, the original:** three suction levels (Quiet, Standard, Strong). Its station washes and dries the mop in one step, so "Dry the mop" and "Empty the dustbin" are not offered for it.
- **Freo Z Ultra:** it never sends live updates, so Homey checks it every 15 seconds; its status can lag a little during a clean.

## Before you start

1. Set up the robot in the **Narwal app** first: connect it to your Wi-Fi and let it map your home once. Rooms, room cleaning and the map widget come from that map.
2. Keep Homey and the robot on the **same home network**.
3. Give the robot a **fixed IP address** in your router (a DHCP reservation). Homey follows a robot that moves to a new address, but a fixed address is the safest.
4. While you add the robot to Homey, **close the Narwal app** on your phone. Some robots accept only one local connection at a time.

## Choose how Homey connects

Open the app settings: in the Homey app go to **More → Apps → Narwal → Configure**. Under **Connection**, choose:

- **Local** (the default): Homey talks to the robot over your home network. No Narwal account needed. Fast, works without the internet, and uses the least memory on Homey.
- **Cloud:** Homey talks to the robot through your Narwal account, like the Narwal app does. Use this when the robot is on a different network, or when Local does not work for your robot.

Cloud-only models (Freo X Ultra, Freo X Plus, Freo Z10 and the original Freo) always connect through your Narwal account, whichever you choose here. The Freo Z Ultra is added from your account, but then connects locally when Local is chosen.

### Connect your Narwal account

You need this for Cloud mode, the cloud-only models, the Freo Z Ultra, the part life in the parts widget and the camera.

1. Open **More → Apps → Narwal → Configure**.
2. Under **Narwal account**, choose the **country of your Narwal account**: the country you chose in the Narwal app. Narwal keeps each account on its country's own server, so a wrong country means Homey finds no robots.
3. Enter the **email** of your Narwal account and tick **I am 14 or older** (Narwal asks this, as its own app does).
4. Choose how to sign in:
   - **Email code:** press **Email me a code**, enter the code from the email (check your spam folder), and press **Sign in**. Check the email address first: if no Narwal account uses it, Narwal creates a new, empty account.
   - **Password:** enter your Narwal password and press **Sign in**.
5. The page then shows **Signed in as** your email and country.

Your password is never stored on Homey; only the session from Narwal is kept. To sign out, press **Sign out** on the same page.

## Add your robot

1. In the Homey app, go to **Devices → + (Add device) → Narwal**.
2. Choose your robot's **model**. Not in the list? Choose **Other Narwal Robot**.
3. Add the robot. What you see depends on the model and the connection:

**Robots found on your network** (Local)
- Homey searches your network and lists the Narwal robots it finds. Press **Add** next to yours.
- Not listed? Press **Search again**, or use **Add by IP address**: enter the robot's IP address (from your router, or the Narwal app's device information), keep the port at **9002**, and press **Continue**. Homey checks the robot and adds it.

**Robots on your Narwal account** (Cloud, the cloud-only models and the Freo Z Ultra)
- Sign in to your Narwal account first (see above). The pairing screen then lists the robots on your account. Press **Add** next to yours.

**Good to know while pairing**
- **"Add it under ... instead":** the robot is a different model from the one you chose. Go back and choose the model it names.
- **"Not answering. Wake the robot, then retry":** wake the robot (press a button on it, or open the Narwal app once), close the Narwal app again, then press **Retry**.
- **"Already added":** this robot is already in Homey.
- **"No robots on this Narwal account":** the robot is on another account, or it is not added in the Narwal app yet. Also check the country in the app settings.

## Using the robot

Open the robot in Homey to see and control it:

- **Buttons:** Start cleaning, Pause, Resume, Stop, Return to dock and Locate (the robot plays a sound).
- **Fan speed:** Quiet, Standard, Strong, Super Powerful and Ultra Powerful. A level you choose while the robot is docked is used for its next clean.
- **Status:** Cleaning, Paused, Returning to dock, Docked, Charging, Washing mop, Drying mop, Emptying dust, Sleeping, Error and more.
- **Battery, Charging, Docked, Connected**, the **current room**, the **cleaned area and time** of the clean, the **last error** and the **firmware** version.

"Start cleaning" cleans the whole home, or your default rooms when you set them up (see [Rooms](#rooms)).

### Device settings

Open the robot, then the settings (gear icon):

- **Connection:** the robot's IP address and port (9002). The connection type shows whether the model works locally, through the cloud, or both.
- **Default cleaning:** the rooms "Start cleaning" and "Clean default rooms" use (see [Rooms](#rooms)).
- **Cleaning mode:** the mode (Vacuum and mop, Vacuum only, Mop only, Vacuum then mop), water level (Dry, Normal, Wet), mop strength (Normal, High), passes (1, 2, 3) and route (Robot default, Standard, Meticulous). They apply to every clean Homey starts.
- **Advanced:** how often Homey asks the robot for its status when no live updates arrive.
- **Camera (experimental):** see [Camera](#camera-experimental).

### App settings page

**More → Apps → Narwal → Configure** also shows, for the robot you pick at the top:

- **Status:** connection, battery, status, the dock, the clean's area and time, firmware, the last error and, on robots that report it, battery health.
- **Robot settings:** the settings stored on the robot itself, such as child lock, pet mode, hot water mop washing, mop drying, obstacle avoidance and the station light. Only the settings your robot supports are shown, and a change applies straight away.
- **Rooms:** your rooms, with a **Refresh** button that loads the rooms and map again.
- **Diagnostics:** see [Diagnostics](#diagnostics).

## Rooms

Homey reads your rooms from the robot's map, with the names you gave them in the Narwal app.

- **Clean one room:** use the Flow card "Clean selected room" and pick the room from the list.
- **Default rooms:** to make "Start cleaning" clean only some rooms, open the robot's settings, enter the room numbers under **Default room IDs** (for example 3,4,5; the **Discovered rooms** list shows each room's number) and tick **Use default rooms for Start cleaning**.
- **Rooms missing or renamed?** Change them in the Narwal app, then press **Refresh** under **Rooms** in the app settings, or run the Flow card "Refresh rooms and map".

## Widgets

Add them to a Homey dashboard: **Dashboards → edit → + → Narwal**.

**Narwal Map**
- Your home's map in the Narwal app's room colours, with room names, the station and the robot. While the robot cleans, its position and path update live.
- Options: show the status bar, show room names (optionally see-through), show the last clean's path, and how often to refresh.
- To save memory on Homey, the app keeps the full map only while a map widget is open (and for 10 minutes after). Opening the widget loads it within a few seconds.

**Narwal Consumables**
- The parts the robot asks you to clean or replace now. With a signed-in Narwal account it also shows the life left for each part in percent and hours, as in the Narwal app, plus the parts to clean regularly.
- Options: show hours left, show parts to clean regularly, and show the **Reset** buttons (press Reset after you cleaned or replaced a part).

## Camera (experimental)

Robots with remote view in the Narwal app (for example the Flow 2) can show their camera in the robot's camera view in Homey.

1. In the Narwal app, turn on **remote view** for the robot.
2. Sign in to your Narwal account in the app settings.
3. In the robot's device settings, tick **Show the robot's camera** under **Camera (experimental)**, and enter the **video code** if you set one in the Narwal app.

Good to know:
- The robot sends H.265 video. It plays in the **Homey web app** (in a desktop browser, and in Safari on an iPhone). The Homey phone apps cannot play it yet; the camera view then tells you so.
- The video goes from the robot through Narwal's cloud to your screen; nothing is recorded or stored on Homey.
- The robot ends a view after about two minutes; open it again to continue.
- Turned the camera off? The camera view goes away the next time the app restarts (**More → Apps → Narwal → Restart**).

## Automations with Flows

Find the cards under the robot when you create a Flow. Every card works with every Narwal robot, except where a model note says otherwise.

**When...** (triggers)

| Card | What it does |
| --- | --- |
| Robot started cleaning | The robot started a clean. |
| Robot paused | The clean was paused. |
| Robot resumed | A paused clean continues. |
| Robot stopped | The clean was stopped. |
| Cleaning completed | The clean finished. Tags: area (m²), duration (minutes) and the rooms it cleaned. |
| Robot returned to dock | The robot is back in its station. |
| Robot docked | The robot entered the station. |
| Robot undocked | The robot left the station. |
| Battery level changed | Tag: the battery level in percent. |
| Charging state changed | Tag: whether it is charging. |
| A part needs attention | The robot asks for a part to be cleaned or replaced, or a part's life runs out. Fires once per part. Tags: the part, and what to do. |
| Connection lost | Homey lost the connection to the robot. |
| Connection restored | Homey is connected to the robot again. |

**And...** (conditions; each can be inverted to "is not")

| Card | True when |
| --- | --- |
| Robot is cleaning | A clean is running. |
| Robot is docked | The robot is in its station. |
| Robot is charging | The robot is charging. |
| Battery is above ...% | The battery is above the level you set. |
| Robot is connected | Homey is connected to the robot. |
| A part needs attention | The robot asks for any part to be cleaned or replaced, or a part's life has run out. |

**Then...** (actions)

| Card | What it does |
| --- | --- |
| Start cleaning | Cleans the whole home, or your default rooms. |
| Clean default rooms | Cleans your default rooms. |
| Clean selected room | Cleans the room you pick from the list. |
| Clean with settings | One clean with its own settings: rooms, mode, suction, water level, mop strength, passes and route. Anything left on "Use device setting" takes the robot's settings. |
| Pause cleaning | Pauses the clean. |
| Resume cleaning | Continues a paused clean. |
| Stop cleaning | Ends the clean. |
| Return to dock | Sends the robot back to its station. |
| Locate robot | The robot plays a sound. |
| Set fan speed | Sets the suction for the current or next clean. |
| Empty the dustbin | Empties the robot's dustbin into the station (the robot must be in the station). |
| Wash the mop | Washes the mop in the station. When the robot is not cleaning, the station dries the mop afterwards, as in the Narwal app. |
| Dry the mop | Dries the mop in the station. |
| Reset a part | Resets a part's counter after you cleaned or replaced it. |
| Turn a robot setting on or off | For example child lock or emptying the dustbin after cleaning. The list shows your robot's settings. |
| Change a robot setting | Settings with several choices, such as mop drying or obstacle avoidance. |
| Refresh robot status | Asks the robot for its status now. |
| Refresh rooms and map | Loads the rooms and map again. |

### Ideas

- **Clean when everyone is out:** When the last person leaves home, And the robot is docked, And the battery is above 50%, Then Start cleaning.
- **Kitchen after dinner:** When it is 20:30, Then Clean with settings: the kitchen, Vacuum then mop, 2 passes.
- **Quiet while you are on a call:** When your work calendar starts a meeting, And the robot is cleaning, Then Pause cleaning; when the meeting ends, Then Resume cleaning.
- **Guests are coming:** When the doorbell rings, And the robot is cleaning, Then Return to dock.
- **Part reminders:** When A part needs attention, Then send a push notification with the part and what to do.
- **Report the clean:** When Cleaning completed, Then send a notification with the area, the time and the rooms.
- **Child lock at night:** When it is 21:00, Then Turn Child lock on; in the morning, turn it off.

## Troubleshooting

### Homey does not find the robot while pairing

- Check that the robot is on, connected to Wi-Fi, and on the same network as Homey. Robots on a guest network or another VLAN cannot be found.
- Wake the robot (press a button on it, or open the Narwal app once), then close the Narwal app and press **Search again**.
- Use **Add by IP address** with the robot's IP address and port 9002.
- Is your model **cloud only** (Freo X Ultra, Freo X Plus, Freo Z10, the original Freo) or the **Freo Z Ultra**? Sign in to your Narwal account in the app settings first; the robot is then listed under **Robots on your Narwal account**.

### Signed in, but no robot is listed

Narwal keeps each account on its country's own server, and the robots are only listed there. Sign out in the app settings and sign in again with the country your Narwal app account is set to. Also check that the robot is added to that account in the Narwal app.

### The robot shows as disconnected or unavailable

- Make sure the robot is on and has Wi-Fi. A robot in deep sleep may need a button press.
- Close the Narwal app on your phone: some robots accept only one local connection, and the Narwal app can take it.
- Did the robot get a new IP address? Homey usually follows it on its own; if not, enter the new address in the robot's device settings. A fixed address in your router prevents this.
- In Cloud mode: if the Narwal app also shows a network error for the robot, Homey cannot reach it either. Restart the robot or check its internet connection.

### Commands are slow or seem to do nothing

- In **Cloud** mode the robot's answers can take 20 to 30 seconds; Homey waits for them, and the status usually updates within a few seconds. **Local** mode is faster when your robot supports it.
- Station actions (empty the dustbin, wash and dry the mop) only work when the robot is in its station.
- "The robot is busy with a task": the robot is already doing something; try again when it is done.

### "Start cleaning" does not clean the rooms you expect

Check **Default cleaning** in the robot's device settings: with **Use default rooms for Start cleaning** ticked, it cleans only the rooms in **Default room IDs**. Untick it to clean the whole home.

### Rooms or map are missing

- Let the robot map your home in the Narwal app first.
- Press **Refresh** under **Rooms** in the app settings, or run "Refresh rooms and map".
- The map widget loads the full map when you open it; give it a few seconds.

### The parts widget shows no life left per part

The life of each part comes from your Narwal account. Sign in to your Narwal account in the app settings. Without an account, the widget still shows what the robot asks you to clean or replace now.

### The camera does not play

- In a Homey phone app, the camera view says it cannot play the robot's video: use the Homey web app (a desktop browser, or Safari on an iPhone).
- Check that remote view is on for the robot in the Narwal app, that your Narwal account is signed in, and that the video code is right.

### Homey is short on memory (for example a Homey Pro mini)

- Use **Local** mode if your robot supports it: it uses about 10 to 15 MB less than Cloud mode.
- Close the map widget when you do not need it: the app keeps the full map only while a map widget is open.
- Leave the camera turned off when you do not use it.

### The status or a setting does not match the Narwal app

Press **Refresh robot status** (Flow card) or reopen the app settings page. If it still differs, please run [Diagnostics](#diagnostics) and report it; it helps us support your model better.

## Diagnostics

The app has its own diagnostics that check how Homey reaches your robot.

1. Open **More → Apps → Narwal → Configure**, pick the robot at the top and press **Run diagnostics** under **Diagnostics**.
2. In about a minute it checks the network, the connection, the robot's model, firmware and features, its status messages, the map, the parts and your Narwal account. It only reads information; the robot does not move.
3. Press **Copy report** (or **Share**) and paste the report in a bug report or the Community thread.

The report leaves out IDs, IP addresses, room names and your account. Optional extras on the same page: **Record a cycle** records the robot's statuses while you run a clean from the Narwal app, and **Command tests** send one command at a time (the robot moves; each test asks you to confirm first).

## Questions

- **Do I need a Narwal account?** No, for most robots. You need one for Cloud mode, the cloud-only models (Freo X Ultra, Freo X Plus, Freo Z10, the original Freo), the Freo Z Ultra, the part life in the parts widget and the camera.
- **Does it work without the internet?** Yes, in Local mode, for the robots that support it.
- **Can I keep using the Narwal app?** Yes. Changes you make there show up in Homey. Only close it while you add the robot to Homey.
- **Why is my robot's model named differently?** Robots added under "Other Narwal Robot" are named from Narwal's model list.

## Reporting a problem

1. Run [Diagnostics](#diagnostics) and press **Copy report**.
2. [Open a bug report](https://github.com/TheBlackBush/homey-apps-support/issues/new/choose), choose **Narwal**, and paste the report. Or send a Homey diagnostics report (**More → Apps → Narwal → Send diagnostics report**) and add its Log ID to the issue.
3. Do not paste your email address, passwords, video code, device IDs, IP addresses or room names: issues here are public. The app's report already leaves these out.

## Privacy

The app talks to your robot on your home network by default. Only when you sign in with your Narwal account (for Cloud mode, cloud-only models, part life or the camera) does it connect to Narwal's servers, and then only for your own robots. Your password is never stored; only the session from Narwal is kept on your Homey. Camera video goes from the robot through Narwal's cloud to your screen and is not stored on Homey. The app sends no telemetry or analytics to the developer, Narwal or anyone else.
