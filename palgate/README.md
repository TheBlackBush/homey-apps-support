# PalGate Control for Homey

Open your PalGate gates and barriers from Homey Pro: from the device tile, from your phone, with your voice, or automatically in Homey Flows. Homey sends the open command through PalGate's servers, just like the PalGate app does.

- **Install:** [Homey App Store](https://homey.app/a/com.pal-es/)
- **Report a problem or ask for a feature:** [open an issue](https://github.com/TheBlackBush/homey-apps-support/issues/new/choose) and choose **PalGate Control**

> Unofficial community app. Not affiliated with, authorised by, or endorsed by PalGate (Pal Electronics Systems). "PalGate" is a trademark of its owner and is used here only to describe compatibility.

## What you can do

- **Open a gate** from Homey with one tap, just like the open button in the PalGate app.
- **Gates with several outputs** (for example a gate and a pedestrian door on one controller) become a separate Homey device for each output, so you can open each one on its own.
- **Automations:** open a gate from a Flow, for example when you arrive home, and start other Flows when a gate was opened from Homey.
- **Voice:** open a gate with a voice assistant connected to Homey, when that assistant supports garage doors (some ask for a PIN first).

**What it does not do:** PalGate does not report whether the gate is actually open or closed. Homey shows the gate as open for a few seconds after the open command, and then shows it as closed again. Openings from the PalGate app, a remote or a phone call are not seen by Homey.

## Before you start

- A Homey Pro with Homey 12.0.0 or newer. Homey Cloud is not supported.
- The PalGate app on your phone, signed in, with at least one gate you are allowed to open.
- Internet access for Homey: the open command goes through PalGate's servers.

## Connect your PalGate account

You connect once for the whole app; all your gates use the same connection. The app links to your account the same way the PalGate app links an extra phone, so you do not need to share your password or an SMS code.

1. In the Homey app, go to **Settings → Apps → PalGate Control → Configure**. Under **PalGate account** it says **Not connected**.
2. Tap **Link with PalGate app**. A QR code appears, with a countdown.
3. On your phone, open the PalGate app and go to **Device Linking → Link a Device**, then scan the QR code.
4. Within a few seconds the page shows **Connected**, with the last four digits of your phone number. The connection is saved by itself; there is nothing else to tap.

The QR code is valid for two minutes. When it expires, tap **Get a new code** and scan it right away.

Afterwards, Homey shows up as a linked device in the PalGate app. If you remove it there, Homey can no longer open your gates until you link again.

### Check, renew or remove the connection

When you are connected, the **PalGate account** section has three buttons:

- **Test connection:** asks PalGate whether the connection works and shows how many gates your account can open. Nothing is opened.
- **Link again:** shows a new QR code, for example after you removed Homey from the linked devices in the PalGate app.
- **Disconnect:** removes the connection from Homey after you confirm. Your gates stay in Homey but cannot be opened until you connect again.

### Connect with a session token

Only needed if you already have a PalGate session token, for example from another PalGate integration. Open **Connect with a session token** at the bottom of the settings page and fill in:

- **Phone number:** international format, digits only, without + or spaces, for example `972501234567`.
- **Account type:** **Linked device**, **Primary device** or **SMS login**, matching where the token comes from.
- **Session token:** 32 characters, digits 0 to 9 and letters a to f.

Tap **Check and save**. Homey first tests the details with PalGate and only saves them when PalGate accepts them.

## Add your gates

1. In the Homey app, go to **Devices → + → PalGate Control → PalGate Gate**.
2. Homey lists every gate your PalGate account can open. Pick the ones you want and add them.

Gates with several enabled outputs appear once for each output, named after the output in the PalGate app (or "Gate name - Output 2" when the output has no name). Outputs that are disabled in PalGate are not listed.

You can rename each gate and put it in a room as you like; this does not change anything in the PalGate app.

## Using your gates

Each gate is a garage door in Homey.

- **Open:** tap the tile, or open the gate's page and tap **Open**. The gate opens, Homey shows it as open, and after 5 seconds it shows closed again.
- **Close:** does nothing. PalGate only has an open command; your gate closes by itself as it always does.
- If the open command fails, the gate shows closed again right away. See [The gate does not open](#the-gate-does-not-open).

### How long the gate shows as open

In **Settings → Apps → PalGate Control → Configure**, under **Gate tile**, **Show the gate as open for** sets how long Homey shows the gate as open after the open command: from 2 to 60 seconds. The default is 5 seconds. The change is saved as soon as you pick a value.

This only changes what Homey shows. The real gate opens and closes the way it is set up in PalGate. A longer time is useful when you want "the gate is open" to stay true for a while in your Flows.

## Automations with Flows

The app uses Homey's standard garage door Flow cards; it adds no cards of its own. Choose your gate device and use:

| Card | Type | What it does with PalGate |
| --- | --- | --- |
| Open the garage door | Then | Opens the gate |
| Close the garage door | Then | Nothing (PalGate has no close command) |
| The garage door opened | When | Runs when the gate was opened from Homey |
| The garage door closed | When | Runs when Homey shows the gate as closed again, after the open time you set |
| The garage door is open / is closed | And | Checks what Homey shows, not the real gate |

"Opened from Homey" includes the tile, a Flow, a voice assistant and the Homey app. Openings from the PalGate app, a remote or a phone call do not start a Flow.

### Ideas

- **Open on arrival:** When someone comes home, Then open the parking gate.
- **One tap for everything:** create a Flow that you start from a Homey button or widget, Then open the gate And turn on the driveway lights.
- **Notification:** When the garage door opened, Then send a notification "The gate was opened from Homey".
- **Two outputs at once:** When someone comes home, Then open the car gate, And open the pedestrian door.

When you open a gate automatically, keep in mind who could be standing at it. Open on arrival works best with a reliable presence trigger, such as a geofence with a reasonable radius.

## Troubleshooting

### "Missing PalGate credentials in app settings" when adding gates

The app is not connected yet: the settings page shows **Not connected**. Follow [Connect your PalGate account](#connect-your-palgate-account).

### "Failed loading gates from PalGate API" when adding gates

PalGate refused the connection details.

- Tap **Link again** in the app settings and scan the new code. This fixes most cases, for example when Homey was removed from the linked devices in the PalGate app.
- If you connected with a session token, check the phone number (international format, digits only) and that the account type matches the token.
- Tap **Test connection** to see whether PalGate accepts the connection now.
- Check that Homey has internet access.

### Test connection says "PalGate refused the connection"

The link is no longer valid, usually because Homey was removed from the linked devices in the PalGate app, or the session token was entered wrong. Tap **Link again** and scan the new code. Also check Homey's date and time (**Settings → General**).

### The gate list is empty or a gate is missing

Homey only lists gates that your PalGate account is allowed to open. Check that the gate shows and opens in the PalGate app on the phone you linked. If you were given access to a new gate after adding your devices, add it with **Devices → + → PalGate Control** again.

### The gate does not open

The tile goes straight back to closed when the command fails.

- Check that you can open the same gate from the PalGate app.
- Check that Homey has internet access.
- If it stopped working for all gates at once, tap **Test connection** in the app settings. If PalGate refuses it, tap **Link again**: the link may have been removed in the PalGate app.
- Check that Homey's date and time are correct (**Settings → General**). The connection uses the current time, and a clock that is far off makes PalGate refuse the command.

### The QR code does not appear, or linking fails

- Check that Homey has internet access, then tap **Link with PalGate app** again.
- If the page says **This code has expired**, tap **Get a new code** and scan it right away. Codes are valid for two minutes.
- Restarting the app or Homey cancels a code that was not scanned yet. Get a new one.

### Homey shows the gate as open, but it is closed (or the other way around)

This is expected: PalGate does not report the real gate state. Homey shows open for the open time you set (5 seconds by default) after each open command, and closed the rest of the time.

## Questions

**Does it need the internet?**
Yes. The open command goes through PalGate's servers, like in the PalGate app.

**Can I keep using the PalGate app?**
Yes. Homey is added as an extra linked device and does not affect your phone.

**Can several people use it?**
Everyone who can use your Homey can open the gates you added. The PalGate account that was linked decides which gates are available.

## Reporting a problem

1. In the Homey app, go to **Settings → Apps → PalGate Control → Send diagnostics report** and copy the Log ID it shows.
2. [Open a PalGate bug report](https://github.com/TheBlackBush/homey-apps-support/issues/new?template=palgate_bug_report.yml) and add the Log ID, your app version and what happened.
3. Do not paste your phone number, the session token, gate IDs or the QR code: issues here are public.

## Privacy

The app connects only to PalGate's servers (to list and open your gates and to complete linking) and, while you link, to a public QR code service that draws the QR image. The QR code holds only a random one-time link ID, not your account details. Your phone number and session token are kept on your Homey and are sent only to PalGate. The app sends no telemetry or analytics to the developer or any third party.
