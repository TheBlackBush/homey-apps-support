# Switcher for Homey

Control your Switcher smart home devices from Homey Pro: water heater switches, the Smart Plug and Bath Heater, Runner shutter switches, Light switches and the Breeze air conditioner controller. The app talks to the devices directly over your home network, so control is instant and keeps working when the internet or the Switcher cloud is down.

- **Install:** [test version](https://homey.app/a/il.co.switcher.home/test/) (the Homey App Store version follows after certification)
- **Report a problem or ask for a feature:** [open an issue](https://github.com/TheBlackBush/homey-apps-support/issues/new/choose) and choose **Switcher**

> Unofficial community app. Not affiliated with, authorised by, or endorsed by Switcher. "Switcher" is a trademark of its owner and is used here only to describe compatibility.

## Features

- Local network only: the app listens to the status messages every Switcher device sends about once a second and sends commands straight to the device. No Switcher account login, no cloud.
- One Homey driver for each Switcher product, named as in the Switcher app.
- Water heaters: on/off, a timer on the device page (15, 30, 45, 60, 90 or 120 minutes), time left, auto shutdown (V2, Touch, Mini, Long), power in watts and energy in kWh, also in Homey Energy.
- Shutters: position, up, stop and down, and the child lock.
- Switches with several circuits (Runner S11 and S12, SL02, SL03, SL Mini 02) become one Homey device per light or shutter, so each can go in its own room and works with "turn off all lights" and voice assistants.
- Breeze: on/off, mode (auto, cool, heat, dry, fan), target temperature, fan speed, swing and the room temperature, with the IR codes of 259 air conditioner remotes built in.
- Changes made with the physical buttons or the Switcher app show up in Homey within a few seconds.
- A device that stops sending status messages for three minutes is shown as unavailable, and comes back by itself.

## Supported models

| Homey driver | Homey device | Account token | Status |
| --- | --- | --- | --- |
| V2 | Water heater | No | Same protocol as the Touch; not yet tested |
| Touch | Water heater | No | Tested daily |
| Mini | Water heater | No | Same protocol as the Touch; not yet tested |
| Long | Water heater | No | Same protocol as the Touch; not yet tested |
| Boiler S216 (onWall) | Water heater | Yes | Not yet tested; see the note below |
| Smart Plug | Socket | No | Same protocol as the Touch; not yet tested |
| Bath Heater | Heater | Yes | Not yet tested |
| Runner | Shutter | No | Not yet tested |
| Runner 55 | Shutter | No | Not yet tested |
| Runner S11 | 2 lights and 1 shutter | Yes | Not yet tested |
| Runner S12 | 1 light and 2 shutters | Yes | Not yet tested |
| Light SL01, SL02, SL03 | 1, 2 or 3 lights | Yes | Not yet tested |
| Light SL Mini 01, SL Mini 02 | 1 or 2 lights | Yes | Not yet tested |
| Breeze | Air conditioner | No | Not yet tested |

The untested models are built from the Switcher protocol and checked against recorded device data. Reports from owners are very welcome: open a **New device or model** issue or a bug report and say what worked.

**Boiler S216 (onWall):** other Switcher integrations report that this model currently refuses local commands on its present firmware, and Switcher is expected to fix this in a firmware update. Its status (on/off, power, time left) should still show in Homey; when a command is refused, the app says so. Reports from owners are very welcome.

### Not supported yet

- Light switch circuits that are set up as shutters in the Switcher app: they are added as lights for now.
- Device schedules: use Homey Flows instead.

## Before you start

- Set up the device in the Switcher app first (Wi-Fi, and for the Breeze, the air conditioner remote).
- Homey and the devices must be on the same network. The app listens on UDP ports 10002, 10003, 20002 and 20003.
- Homey Pro with Homey 12.9.0 or newer.
- **Account token** for the Boiler S216, Bath Heater, Runner S11 and S12 and the Light switches: request it at [switcher.co.il/GetKey](https://switcher.co.il/GetKey/) with the email address of your Switcher account; it arrives by email. The app asks for it once while pairing.
- **The older Switcher app** (il.co.switcher) cannot run at the same time: only one app can listen to the Switcher status messages. Disable or uninstall it first.

## Pairing

1. In Homey, go to **Devices → Add device → Switcher** and choose your model.
2. Enter the account token if Homey asks for it.
3. Pick the devices Homey found and add them.

Devices are found from their status messages. If the list is empty, check that the device is online in the Switcher app, wait a minute and try again. Devices follow IP address changes by themselves.

## Flow cards

Besides Homey's standard cards (turn on and off, power, temperature, mode, fan speed, shutter position, and so on):

### Actions

- Turn on for a set time (water heaters, Bath Heater)
- Set auto shutdown (V2, Touch, Mini, Long)
- Set child lock (shutters)
- Set the air conditioner: mode, temperature, fan and swing in one command (Breeze)
- Correct the known AC state: tells Homey what the air conditioner is doing, without sending anything to it (Breeze)

### Conditions

- Timer is running (water heaters, Bath Heater)
- Child lock is on (shutters)

### Triggers

- Time left changed, with the minutes left (water heaters, Bath Heater)

## Breeze

The Breeze sends infrared commands to your air conditioner with the remote you chose in the Switcher app; change the remote there. An air conditioner does not report back over infrared, so Homey shows the last state the Breeze sent: if you use the air conditioner's own remote, Homey does not see the change. Use **Correct the known AC state** to fix that. The room temperature always comes from the Breeze's own sensor.

If the device says the remote is not supported, it is not in the built-in list of 259 remotes; the room temperature still works. Open a **New device or model** issue with the remote's name as shown in the Switcher app.

## Troubleshooting

### No devices are found

- If pairing says another app is using the network ports, disable the older Switcher app, wait a minute and try again.
- Check that Homey and the device are on the same network and VLAN, and that the device is online in the Switcher app.

### A device is unavailable

Homey has not received its status messages for three minutes. Check its power and Wi-Fi; it becomes available again as soon as it is heard.

### "This device needs your Switcher account token"

Open the device and choose **Repair** to enter the token. Request a new one at [switcher.co.il/GetKey](https://switcher.co.il/GetKey/) if needed.

### "The device did not accept Homey's commands"

The device was probably set up with a different Switcher account than the one your token is from (for example, a device shared with you). Set it up again in the Switcher app with your own account, or request the token for the account that set it up. For the Boiler S216, see the note under Supported models.

### Commands fail or time out

Check that nothing blocks traffic from Homey to the device (TCP port 9957 for water heaters and the Smart Plug, 10000 for the other models), and that the device is reachable from the Switcher app on the same network.

## Reporting a problem

1. In the Homey app, go to **Settings → Apps → Switcher → Send diagnostics report** and copy the Log ID it shows.
2. [Open a bug report](https://github.com/TheBlackBush/homey-apps-support/issues/new/choose), choose **Switcher**, and add the Log ID, your device model and what happened.
3. Do not paste your email address, the account token, device IDs or IP addresses: issues here are public.

## Privacy

The app talks only to your Switcher devices on your local network. It does not log in to a Switcher account and does not connect to Switcher's servers. The account token you enter for newer models is kept on your Homey and sent only to your own devices. The app sends no telemetry or analytics to the developer, Switcher or any third party.
