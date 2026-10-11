# Red Alert Israel for Homey

Get Israeli Home Front Command alerts (Tzeva Adom, "Red Alert") in Homey Pro and act on them automatically: turn on the lights, announce the alert on your speakers, pause the TV, or send a notification with the time you have to reach a protected space.

- **Install:** [Homey App Store](https://homey.app/a/il.co.tzevaadom/)
- **Report a problem or ask for a feature:** [open an issue](https://github.com/TheBlackBush/homey-apps-support/issues/new/choose) and choose **Red Alert Israel**

> **Important:** this is an unofficial community app. It is not produced, endorsed or approved by the Home Front Command (Pikud HaOref), the Ministry of Defense or any government body. It does not replace official alert systems. Always keep the official Home Front Command app, sirens and other official channels active, and follow their instructions.

## What you can do

- **Run Flows when an alert arrives** for the cities you choose: rockets and missiles, hostile aircraft, terrorist infiltration, earthquakes, hazardous materials and the other Home Front Command alert types.
- **Early warnings and all-clear:** separate Flows for the early warning that comes before an alert ("alerts expected in your area soon") and for the end of the event ("you may leave the protected space").
- **Ready-made messages:** every alert comes with a written message (threat, areas, district, time to shelter, time and a link) that you can send as a notification or read out loud.
- **Dashboard widget** that shows whether the app is connected and whether an alert is active, with an on/off switch for monitoring.
- **Hebrew or English** for the alert text, area names and messages.

**What it does not do:**

- It adds no devices and makes no sound by itself. Homey only reacts to alerts through the Flows you create.
- Home Front Command drills are ignored.
- It does not tell you where the nearest shelter is or replace the instructions of the Home Front Command.

## Before you start

- A Homey Pro with Homey 12.3.0 or newer. Homey Cloud is not supported.
- Internet access for Homey. Alerts arrive over the internet, so a power or internet outage at home means Homey gets no alerts.

## Set up the app

All settings are on one page: in the Homey app, go to **Settings → Apps → Red Alert Israel → Configure**. Nothing is stored until you tap **Save** at the bottom of the page.

1. **Language:** tap **עברית** or **English** at the top. This sets the language of the settings page and of everything the app writes in your Flows: threat names, area names and messages.
2. **Monitoring enabled:** keep this on. When it is off, the app ignores all alerts.
3. **Cities:** tap **Choose cities**, search for your city (in Hebrew or English), tick it and tap **Apply**. Repeat for every city or area you care about, for example your home, your parents' city or your workplace. See [Choosing cities](#choosing-cities).
4. **Quiet hours** (optional): see [Quiet hours](#quiet-hours).
5. **Throttle** (optional): leave the default values unless you have a reason to change them. See [Throttle](#throttle).
6. Tap **Save**. The page shows **Saved.** and the new settings apply right away.

### Choosing cities

- Only alerts for the cities you selected start your Flows. The names are the official Home Front Command alert areas, so large cities are split into several areas (for example "Tel Aviv - City Center" and "Tel Aviv - South and Jaffa"). Select every area you need.
- **No cities selected means the whole country:** every alert anywhere in Israel starts your Flows. This is usually not what you want.
- Alerts for the whole country ("nationwide") always count as an alert for your cities.
- To remove a city, open **Choose cities** again, untick it, tap **Apply** and then **Save**. **Clear all** unticks everything.

### Quiet hours

Quiet hours only silence **early warnings**. Real alerts and all-clear messages always start your Flows, also during quiet hours.

Tick **Enable quiet hours** and choose a start and end time (24-hour clock, Israel time). A range that crosses midnight, such as 23:00 to 06:00, works as expected.

### Throttle

The same alert often arrives more than once (for example from both alert sources the app uses). The throttle values set, per alert type, how long the app ignores a repeat of an alert it already handled, in milliseconds: 60000 is one minute. The defaults are 2 minutes for alerts and all-clear messages, and 3 minutes for early warnings.

A value under one minute works like one minute. New alerts for other areas, or new alerts after the throttle time, always come through. Make the values longer only if your Flows run twice for the same alert.

## The dashboard widget

Add it from a Homey dashboard: **Edit → Add widget → Red Alert Israel → Red Alert Status**. It refreshes every 10 seconds.

| Row | What it shows |
| --- | --- |
| Switch (top right) | Monitoring on or off. Turning it off makes the app ignore all alerts until you turn it on again. |
| Connection | **Connected**: the live alert feed is working. **Reconnecting**: the connection dropped a moment ago and the app is reconnecting. **Disconnected**: no live connection. |
| Active alert | **Yes** from an alert for your cities until the all-clear, otherwise **No**. |
| Ingest source | Where alerts come from right now: **WebSocket** (the live feed, normal), **OREF Fallback** (the backup source, see [How alerts reach Homey](#how-alerts-reach-homey)) or **Idle**. |
| Event type | The type of the last alert: `primary` (an alert that needs shelter), `other` (other threats such as earthquake or hazardous materials), `pre-alert` (early warning) or `all-clear`. |
| Last update | When the last alert or message arrived. |

In the widget's settings, **Compact mode** makes it shorter.

## How alerts reach Homey

- **Normally**, the app keeps a live connection to the Tzeva Adom alert service, the same feed used by the Tzeva Adom app. Alerts arrive within seconds.
- **When the live connection is down**, the app reconnects by itself, and meanwhile checks the Home Front Command website for active alerts every 15 seconds. The widget then shows **OREF Fallback**.
- While the app runs on this backup source and an alert for your cities has not been seen for 3 minutes, the app assumes the event is over and starts your all-clear Flows. In the messages, this all-clear shows **Source: Inferred**.

## Automations with Flows

### When cards

| Card | Starts when |
| --- | --- |
| **Red alert received** | An alert arrives for one of your cities. This is any alert type: rockets and missiles, hostile aircraft, terrorist infiltration, chemical, earthquake, tsunami, hazardous materials, radiological and general Home Front Command alerts. Use the **Threat key equals** card to react only to some types. |
| **Early warning received** | An early warning arrives for one of your cities (alerts are expected soon). Not during [quiet hours](#quiet-hours), and not while a red alert for your cities is already active. |
| **All-clear notification received** | The event ends for one of your cities and you may leave the protected space. |

Each of these cards gives you these tags to use in the rest of the Flow:

| Tag | Example | Meaning |
| --- | --- | --- |
| Title / Threat name | Rockets and missiles | The alert type, in the app's language |
| Category | Primary | Primary (needs shelter), Pre-alert, All-clear or Other |
| Severity | Critical | Critical, Warning or Info (see below) |
| Areas | Tel Aviv - City Center, Ramat Gan - West | Your selected areas that are in the alert |
| Areas count | 2 | How many areas |
| Primary area | Tel Aviv - City Center | The first area |
| District | Dan | The district of the first area |
| Shelter time (sec) | 90 | Seconds to reach a protected space in the first area. Empty when not known. |
| Timestamp | 11.10.2026, 21:30:05 | Time of the alert, Israel time |
| Threat ID / Threat key | 0 / rockets_missiles | The alert type as a number and as a fixed English key (useful in logic cards) |
| Alert message | (see [Alert messages](#alert-messages)) | A full written message, ready to send |
| Alert link | https://www.tzevaadom.co.il/alerts/... | A link to the alert on the Tzeva Adom website |

**Severity:** Critical for rockets and missiles, hostile aircraft, terrorist infiltration and chemical alerts. Warning for early warnings and the other threat types. Info for all-clear.

### And cards

| Card | Checks |
| --- | --- |
| **Monitoring is enabled** | Whether monitoring is on |
| **Alert is currently active** | Whether an alert for your cities is active (between an alert and its all-clear) |
| **Threat key equals ...** | The type of the most recent alert: Rockets and missiles, Terrorist infiltration, Hostile aircraft, Chemical, Earthquake, Tsunami, Hazmat, Radiological, Home Front alerts, Pre-alert or All-clear |
| **Severity equals ...** | The severity of the most recent alert: Critical, Warning or Info |

### Then cards

| Card | What it does |
| --- | --- |
| **Set monitoring to ...** | Turns monitoring on or off |
| **Build ... message** | Rewrites the **Last alert message** tag for the most recent alert, in the **Full** or **Short** format |
| **Build alert link from ...** | Rewrites the **Last alert link** tag for the most recent alert: **Tzeva Adom** (the alert's page) or **Home Front Command** (the official alert history page) |

### Last alert message and Last alert link

Besides the tags of each card, the app keeps two tags you can use in **any** Flow, for example a Flow you start from a button: **Last alert message** and **Last alert link**. They always hold the most recent alert. After each new alert they are reset to the full message and the Tzeva Adom link; use the **Build** cards to switch to the short message or the Home Front Command link. The **Build** cards never fetch a new alert; before the first alert the message says "No alerts yet."

### Alert messages

The **Full** format (one item per line):

```text
🚨 Alert: Rockets and missiles
Areas: Tel Aviv - City Center
District: Dan
Category: Primary
Severity: Critical
Shelter time: 90s
Time: 10/11/2026, 21:30:05
Source: TzevaAdom (WebSocket)
Link: https://www.tzevaadom.co.il/alerts/...
```

The **Short** format puts everything on one line, which suits SMS and short notifications:

```text
🚨 Rockets and missiles | Primary | Tel Aviv - City Center (1) | Critical | Source: TzevaAdom (WebSocket) | 90s to shelter | District: Dan | Link: https://... | 10/11/2026, 21:30:05
```

### Ideas

- **Lights on:** When **Red alert received**, And **Severity equals Critical**, Then turn on the lights in the hallway and the protected space at full brightness.
- **Announce the alert:** When **Red alert received**, Then say on your speakers "Red alert, [Shelter time] seconds to the protected space".
- **Notification:** When **Red alert received**, Then send a push notification with the **Alert message** tag.
- **Prepare early:** When **Early warning received**, Then turn on the lights in the protected space and send a notification "Alerts expected soon".
- **Back to normal:** When **All-clear notification received**, Then send a notification and restore the lights.
- **Pause the TV:** When **Red alert received**, Then pause media on the TV and set the speakers to a low volume after the announcement.
- **Only some threats:** When **Red alert received**, And **Threat key equals Earthquake**, Then run your earthquake routine.

Your Flows are an addition to the official alerts, never a replacement. Do not build anything that delays you, for example a Flow that locks a door on the way to the protected space.

### Testing your Flows

The app has no test alert. To check a Flow, open it in the Flow editor and tap **Test**: the actions run, but tags from the alert are empty. To see a real alert end to end, wait for an all-clear or early warning in your area, or select a city that often has alerts for a short time.

## Troubleshooting

### My Flows did not start for an alert

- Check that monitoring is on (the widget switch, or **Monitoring enabled** in the settings).
- Open the settings and check that your city is selected and that you tapped **Save**. Large cities are split into several alert areas; the alert may have been for an area you did not select.
- Early warnings do not start Flows during quiet hours, or while a red alert for your cities is already active.
- Drills are ignored.
- Check that the Flow uses the right **When** card: rockets and other threats use **Red alert received**, not **Early warning received**.
- If you use **Threat key equals** or **Severity equals**, check that they match the alert type.

### My Flows started for an alert in another city

- With no cities selected, every alert in the country starts your Flows. Select your cities.
- Alerts for the whole country ("nationwide") always start your Flows.

### The widget shows Disconnected or Reconnecting

- Check that Homey has internet access.
- Wait a minute: the app reconnects by itself and uses the backup source meanwhile.
- Turn monitoring off and on again with the widget switch.
- If it stays disconnected, restart the app: **Settings → Apps → Red Alert Israel → Restart**.

### The widget shows OREF Fallback for a long time

The live connection is down and the app is using the Home Front Command website. Alerts still come in, but a few seconds later than usual. The Home Front Command website generally only answers connections from Israel; if your Homey is connected through a VPN or a connection abroad, the backup source may not work. Restart the app to retry the live connection.

### Active alert stays on Yes

The app sets **Active alert** back to **No** when the all-clear for your cities arrives. If the all-clear was missed (for example because Homey was offline at that moment), it stays **Yes** until the next all-clear for your cities. Restarting the app does not reset it.

### My Flows run twice for one alert

Increase the throttle values for that alert type (see [Throttle](#throttle)) and tap **Save**. Also check that you do not have two Flows reacting to the same card.

### My city is missing in the list

The city list is the official Home Front Command list of alert areas, and it is updated with app updates. Search for part of the name, in Hebrew or in English. If the area is still missing, [open an issue](https://github.com/TheBlackBush/homey-apps-support/issues/new?template=red_alert_bug_report.yml).

### The messages are in the wrong language

Pick the language at the top of the settings page and tap **Save**. New alerts use the new language; to rewrite the message of the last alert, run a **Build ... message** card.

### The link opens the Tzeva Adom home page instead of the alert

The app looks up the alert in the Tzeva Adom alert history. When it cannot find it in time, the link goes to the Tzeva Adom home page. The **Home Front Command** link from the **Build alert link** card always goes to the official alert history page.

### "Could not load cities list" in the settings

Close the settings page and open it again. If it keeps happening, restart the app.

## Questions

**Is this as fast as the official app?**
Alerts usually arrive within seconds, but there is no guarantee: they travel through the internet, an outside alert service and your Homey. Always rely on sirens and the official Home Front Command app.

**Does it work when the internet or power is down?**
No. Homey needs power and internet to receive alerts.

**Can I use it for more than one city?**
Yes. Select all the cities you want; the **Areas** tag tells you which of them are in the alert.

**Does the app need an account?**
No. There is nothing to sign in to.

## Reporting a problem

1. In the Homey app, go to **Settings → Apps → Red Alert Israel → Send diagnostics report** and copy the Log ID it shows.
2. [Open a Red Alert bug report](https://github.com/TheBlackBush/homey-apps-support/issues/new?template=red_alert_bug_report.yml) and add the Log ID, your app version, the time of the alert and what happened.
3. Issues are public. You do not need to share your home address; if you prefer not to name your city, name a nearby city or the district instead.

## Privacy

The app connects only to the Tzeva Adom alert service (live alerts and the alert history used for links) and to the Home Front Command website (backup source). It sends nothing about you or your home to these services: it receives the alerts for the whole country and filters them on your Homey. Your selected cities and settings stay on your Homey. The app sends no telemetry or analytics to the developer or any third party.
