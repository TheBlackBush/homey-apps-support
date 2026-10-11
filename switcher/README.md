# Switcher for Homey

Control your Switcher devices from Homey Pro: water heater switches, the Smart Plug, the Bath Heater, Runner shutter switches, Light switches and the Breeze air conditioner controller. Homey talks to them directly over your home network, so they respond right away and keep working when the internet is down.

- **Install:** [test version](https://homey.app/a/il.co.switcher.home/test/) (the Homey App Store version follows after certification)
- **Questions and tips:** [Homey Community thread](https://community.homey.app/t/app-pro-switcher-local-control-for-switcher-water-heaters-shutters-lights-and-breeze/160624)
- **Report a problem or ask for a feature:** [open an issue](https://github.com/TheBlackBush/homey-apps-support/issues/new/choose) and choose **Switcher**

> Unofficial community app. Not affiliated with, authorised by, or endorsed by Switcher. "Switcher" is a trademark of its owner and is used here only to describe compatibility.

## What you can do

- **Water heaters:** turn the heater on and off, start it for a set time, see how much time is left, set the auto shutdown, and see its power and energy use.
- **Shutters:** open, close or stop them, set an exact position, and turn the child lock on or off.
- **Lights:** turn each light on and off. A switch with two or three lights becomes two or three lights in Homey.
- **Breeze:** control your air conditioner: on and off, mode, temperature, fan speed and swing, and see the room temperature.
- **Automations:** use all of the above in Homey Flows, together with everything else in your home.
- Changes you make with the buttons on the device or in the Switcher app show up in Homey within a few seconds.

## Which devices work

| Switcher device | In Homey | Needs your account token | Tested |
| --- | --- | --- | --- |
| V2, Touch, Mini, Long | Water heater | No | Touch: yes. Others work the same way, not tested yet |
| Boiler S216 (onWall) | Water heater | Yes | Not yet, see [Boiler S216](#boiler-s216-onwall) |
| Smart Plug | Socket | No | Not yet |
| Bath Heater | Heater | Yes | Not yet |
| Runner, Runner 55 | Shutter | No | Not yet |
| Runner S11 | 2 lights and 1 shutter | Yes | Not yet |
| Runner S12 | 1 light and 2 shutters | Yes | Not yet |
| Light SL01, SL02, SL03 | 1, 2 or 3 lights | Yes | Not yet |
| Light SL Mini 01, SL Mini 02 | 1 or 2 lights | Yes | Not yet |
| Breeze | Air conditioner | No | Not yet |

Own a model that is not tested yet? Please tell us in the [Community thread](https://community.homey.app/t/app-pro-switcher-local-control-for-switcher-water-heaters-shutters-lights-and-breeze/160624) whether it works.

**Not available yet:**
- Light switch buttons that you set up as shutters in the Switcher app are added as lights.
- Schedules stored on the device. Use Homey Flows to switch at set times instead.

## Before you start

- A Homey Pro with Homey 12.9.0 or newer.
- Set up each device in the Switcher app first (Wi-Fi, and for the Breeze, your air conditioner's remote).
- Homey and the Switcher devices must be on the same home network. A separate guest or "smart home" Wi-Fi network that is cut off from Homey's network does not work.
- If you have the older **Switcher** app on your Homey, disable or uninstall it first. Only one Switcher app can work at a time.

### Get your account token (newer models only)

The Boiler S216, Bath Heater, Runner S11 and S12 and the Light switches only accept commands with your Switcher account token. You need it once:

1. Go to [switcher.co.il/GetKey](https://switcher.co.il/GetKey/).
2. Enter the email address you use to log in to the Switcher app.
3. The token arrives by email. Keep the email; Homey asks for the token when you add the first of these devices.

Use the token of the account that set up the device in the Switcher app. A device that someone else set up and shared with you does not accept your token.

## Add your devices

1. In the Homey app, go to **Devices → + → Switcher** and choose your model.
2. If Homey asks for the account token, paste it from the email and tap **Save token**. You only do this once for all your devices.
3. Pick the devices Homey found and add them.

Devices with several lights or shutters are added as one Homey device each, named after the device, for example "Living room light 1", "Living room light 2" and "Living room shutter 1". Put each one in its own room and rename it as you like.

If no devices are found, see [Troubleshooting](#no-devices-are-found).

## Using your devices

### Water heaters (V2, Touch, Mini, Long, Boiler S216)

On the device page:

- **On/off:** turns the heater on. When you turn it on this way, the device's own auto shutdown turns it off later.
- **Timer:** pick 15, 30, 45, 60, 90 or 120 minutes to turn the heater on for that time. Pick **Off** to turn it off. The timer shows **Off** again when the heater turns off, and also when the heater was turned on without a timer.
- **Time left:** minutes until the heater turns off.
- **Power:** what the heater uses right now, in watts.
- **Energy:** the total energy used, in kWh. It counts from the moment the device was added to Homey (or the app was updated), and only while Homey is running. You also find it in **Homey Energy** and **Insights**.

In the device settings (**⚙**):

- **Auto shutdown** (V2, Touch, Mini, Long): how long the heater stays on when it is turned on without a timer, as hours:minutes, from 1:01 to 23:59 (for example 1:30). This is the same setting as in the Switcher app; changing it in one place changes it in the other.
- **Model** and **IP address:** for information.

### Smart Plug

On/off, power and energy, like the water heaters. The Smart Plug has no timer or auto shutdown.

### Bath Heater

On/off, the timer list, time left, power and energy, like the water heaters. It has no auto shutdown setting in Homey.

### Shutters (Runner, Runner 55, and the shutters of the Runner S11 and S12)

- **Up, stop, down:** the buttons on the device page.
- **Position:** the slider, from closed (0%) to fully open (100%).
- **Child lock:** locks the buttons on the wall switch, so the shutter can only be moved from Homey or the Switcher app.

### Lights (Light SL series, and the lights of the Runner S11 and S12)

Each light is a normal Homey light with on and off. It works with Homey's "turn off all lights" in a room and with voice assistants.

### Breeze (air conditioner)

On the device page: on/off, the target temperature, the room temperature (measured by the Breeze), **Mode** (auto, cool, heat, dry, fan), **Fan speed** (auto, low, medium, high) and **Swing**. Only the modes, fan speeds and temperatures that your air conditioner's remote supports are offered.

When you change several things quickly, the Breeze waits a moment and then sends them together, so the air conditioner beeps once.

**Good to know:** the Breeze controls the air conditioner like its remote does, but the air conditioner never reports back. Homey shows what the Breeze last sent. If someone uses the air conditioner's own remote, Homey does not know. To fix what Homey shows without sending anything to the air conditioner, use the Flow card **Correct the known AC state** (see below).

To use a different remote, change it in the Switcher app; Homey picks it up by itself.

## Automations with Flows

All devices work with Homey's standard Flow cards (turn on and off, set the temperature, set the shutter position, and so on). The Switcher app adds these:

| Card | Type | For |
| --- | --- | --- |
| Turn on for a set time | Then | Water heaters, Bath Heater |
| Set auto shutdown | Then | V2, Touch, Mini, Long |
| Timer is running / is not running | And | Water heaters, Bath Heater |
| Time left changed (with the minutes left) | When | Water heaters, Bath Heater |
| Set child lock | Then | Shutters |
| Child lock is on / is not on | And | Shutters |
| Set the air conditioner (mode, temperature, fan and swing at once) | Then | Breeze |
| Correct the known AC state (nothing is sent to the air conditioner) | Then | Breeze |

### Ideas

- **Hot water for the morning:** When the time is 05:30 on weekdays, Then turn on the water heater for 30 minutes.
- **Use your solar power:** When the solar production is above 2 kW, And the timer is not running, Then turn on the water heater for 60 minutes.
- **Reminder:** When the time left changed, And the minutes left are 5, Then send a notification "Hot water: 5 minutes left".
- **Shutters at sunset:** When the sun sets, Then set the bedroom shutter to 0%.
- **Cool home on arrival:** When someone comes home, And the temperature outside is above 28 °C, Then set the air conditioner to cool, 24 °C, fan auto, swing off.

## Troubleshooting

### No devices are found

- Check that the device works in the Switcher app.
- Make sure Homey and the device are on the same home network (not a separate guest or smart home network).
- If adding a device says another app is using the network ports, disable the older Switcher app, wait a minute and try again.
- Wait a minute after the device is powered on, then try again.

### A device shows as unavailable

Homey has not heard from the device for three minutes. Check that it has power and Wi-Fi (does it work in the Switcher app?). It becomes available again by itself as soon as it is back.

### The device does not respond to commands

- Check that it works from the Switcher app on the same network.
- Turn the device's power off and on again, and restart your router if several devices are affected.
- If your router has a setting that isolates devices from each other (often called "AP isolation" or "client isolation"), turn it off for your home network.

### "This device needs your Switcher account token"

Open the device in Homey, go to **⚙ → Repair**, and enter the token from the email. Lost the email? Request the token again at [switcher.co.il/GetKey](https://switcher.co.il/GetKey/).

### "The device did not accept Homey's commands"

The device was set up with a different Switcher account than the one your token is from, for example a device someone shared with you. Either set the device up again in the Switcher app with your own account, or use the token of the account that set it up.

### Boiler S216 (onWall)

Other Switcher integrations report that the Boiler S216 currently refuses commands from home automation systems, and Switcher is expected to fix this in a firmware update. Its status (on/off, power, time left) should still show in Homey; when a command is refused, the app says so. Keep the device updated in the Switcher app.

### The timer shows Off while the heater is on

The heater was turned on without a timer (with on/off, the wall button or the Switcher app). It turns off by its auto shutdown; **Time left** shows when.

### Energy shows 0 or a low value

Energy is counted from when the device was added to Homey and only while Homey is running, so it starts at 0. Usage from before, or while Homey was off, is not included.

### The Breeze shows the wrong state

Someone probably used the air conditioner's own remote. Use the **Correct the known AC state** Flow card to tell Homey what the air conditioner is doing, or simply set the air conditioner from Homey again.

### The Breeze says the remote is not supported

The remote chosen in the Switcher app is not in the app's built-in list. The room temperature still works. Open a **New device or model** issue with the remote's name as shown in the Switcher app.

## Questions

**Does it need the internet or a Switcher account login?**
No. Homey talks to the devices on your home network. The account token is only needed for the newer models and is entered once.

**Can I keep using the Switcher app?**
Yes. Both work side by side, and changes in one show up in the other.

**What happens when Homey restarts?**
The devices keep working on their own (including timers and auto shutdown) and Homey picks up their status again when it is back.

## Reporting a problem

1. In the Homey app, go to **Settings → Apps → Switcher → Send diagnostics report** and copy the Log ID it shows.
2. [Open a bug report](https://github.com/TheBlackBush/homey-apps-support/issues/new/choose), choose **Switcher**, and add the Log ID, your device model and what happened. For questions, use the [Homey Community thread](https://community.homey.app/t/app-pro-switcher-local-control-for-switcher-water-heaters-shutters-lights-and-breeze/160624).
3. Do not paste your email address, the account token, device IDs or IP addresses: issues here are public.

## Privacy

The app talks only to your Switcher devices on your home network. It does not log in to a Switcher account and does not connect to Switcher's servers. The account token you enter for newer models is kept on your Homey and sent only to your own devices. The app sends no telemetry or analytics to the developer, Switcher or any third party.
