# MCIGN

## Introduction
This PCB design is for a keyless motorcycle ignition controlled by a smartphone BLE app. The PCB is designed to be installed in a gutted ignition unit, resulting in a stock appearance. A BGM111 wireless modulecontrols the main board, and two relays are used to switch the power on and off. A auxillary relay board can be used for ignitions that require more than 2 relays.

The BGM111 module was chosen because it has already been FCC certified, which normally makes it much easier to sell the hardware without violating FCC regulations. However, this project is exempt from the required testing because it is "a digital device utilized exclusively in any transportation vehicle including motor vehicles." The project is now being ported to the nRF51822 chip for several reason:

 * It is about 1/3 the cost of a BGM111 module
 * Cheap generic breakout boards are available
 * Supports open source tools (gcc & make), which have less bugs, more documentation, and better integration with git than Simplicity Studio, which is required for the BGM111
 * An automotive grade (AEC-Q100) drop-in replacement is available (nRF51824), allowing the hardware to be built to automotive standards

## Usage
After assembly, the BGM111 module can be flashed with the MCIGN firmware via the exposed test pads. A 3d-printable programmer can be built using files in the cad/ directory and cheap [https://en.wikipedia.org/wiki/Pogo_pin](pogo pins) to flash PCBs without soldering wires to the test pads. Once flashed, the stock ignition switch should be closely examined to determine which wires are connected when the igition is in the "on" position. A wiring diagram from the service manual can also be helpful, but certain parts used to prevent hotwiring usually aren't shown on the diagram. A ground wire is usually not included in the connector, so another path to ground must be found. For a stock appearance, the body of the ignition itself can potentially be used as it is bolted to the frame, avoiding any extra wires coming out of the ignition housing.

## Contributing
This project is in its early stages, and all contributions are greatly appreciated. Features, bug fixes, documentation, etc can be submitted with a github pull request.

## Help
Please make a github issue for any technical questions, feature requests, etc.

## License
This project is released under GPLv3.
