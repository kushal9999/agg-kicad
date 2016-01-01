"""
iclib.py
Copyright 2016 Adam Greig

Generate symbols for generic black-box ICs etc.
"""

# Symbols configuration =======================================================
# Dictionary of dictionaries.
# Top keys are symbol names.
# Configuration format is:
# path: optional, sub-directory(s) to store the library in. Defaults to ".".
# designator: optional, default "IC", the default reference designator
# footprint: optional, an associated footprint to autofill
# datasheet: optional, a URL or path to a datasheet
# ordercodes: optional, dict of supplier:code for supplier order codes
# description: description of the part, placed in the .dcm file
# pins: list of lists of left and right pin groups
#           (blocks of related pins with a space in-between).
#       Each group contains a list of tuples of:
#           (pin name, pin number, electrical type).
#       Number and name may be given as a string or an integer.
#       Electrical type must be a string out of:
#           in, out, bidi, tri, passive, unspec, pwrin, pwrout, oc, oe, nc.
#       These correspond to input, output, bidirectional, tristate, passive,
#           unspecified, power_input, power_output, open_collector,
#           open_emitter, and not_connected. They should be given as strings.

config = {

    # STM32F1xxCxUx, in UFQFPN48 package
    "STM32F1xxCxUx": {
        "path": "ic/microcontroller",
        "footprint": "agg:QFN-48-EP-ST",
        "datasheet": "http://www.st.com/st-web-ui/static/active/en"
                     "/resource/technical/document/datasheet/CD00161566.pdf",
        "ordercodes": {
            "Farnell": "2060891",
        },
        "description": "STM32F1 48 pin UFQFPN package",
        "pins": [
            [
                [
                    ("VBAT", 1, "pwrin"),
                    ("VDD", 24, "pwrin"),
                    ("VDD", 48, "pwrin"),
                    ("VDDIO2", 36, "pwrin"),
                    ("VDDA", 9, "pwrin"),
                ], [
                    ("VSSA", 8, "pwrin"),
                    ("VSS", 23, "pwrin"),
                    ("VSS", 47, "pwrin"),
                    ("VSS", 35, "pwrin"),
                    ("VSS", "EP", "pwrin"),
                ], [
                    ("BOOT0", 44, "in"),
                    ("NRST", 7, "in"),
                ], [
                    ("PC13", 2, "bidi"),
                    ("PC14", 3, "bidi"),
                    ("PC15", 4, "bidi"),
                ], [
                    ("PF0", 5, "bidi"),
                    ("PF1", 6, "bidi"),
                ],
            ], [
                [
                    ("PA0", 10, "bidi"),
                    ("PA1", 11, "bidi"),
                    ("PA2", 12, "bidi"),
                    ("PA3", 13, "bidi"),
                    ("PA4", 14, "bidi"),
                    ("PA5", 15, "bidi"),
                    ("PA6", 16, "bidi"),
                    ("PA7", 17, "bidi"),
                ], [
                    ("PA8", 29, "bidi"),
                    ("PA9", 30, "bidi"),
                    ("PA10", 31, "bidi"),
                    ("PA11", 32, "bidi"),
                    ("PA12", 33, "bidi"),
                    ("PA13", 34, "bidi"),
                    ("PA14", 37, "bidi"),
                    ("PA15", 38, "bidi"),
                ], [
                    ("PB0", 18, "bidi"),
                    ("PB1", 19, "bidi"),
                    ("PB2", 20, "bidi"),
                    ("PB3", 39, "bidi"),
                    ("PB4", 40, "bidi"),
                    ("PB5", 41, "bidi"),
                    ("PB6", 42, "bidi"),
                    ("PB7", 43, "bidi"),
                ], [
                    ("PB8", 45, "bidi"),
                    ("PB9", 46, "bidi"),
                    ("PB10", 21, "bidi"),
                    ("PB11", 22, "bidi"),
                    ("PB12", 25, "bidi"),
                    ("PB13", 26, "bidi"),
                    ("PB14", 27, "bidi"),
                    ("PB15", 28, "bidi"),
                ],
            ],
        ],
    },

    # STM32F0xxCxTx, in LQFP48 package
    "STM32F0xxCxTx": {
        "path": "ic/microcontroller",
        "footprint": "agg:LQFP-48",
        "datasheet": "http://www.st.com/st-web-ui/static/active/en"
                     "/resource/technical/document/datasheet/DM00090510.pdf",
        "ordercodes": {
            "Farnell": "2432094",
        },
        "description": "STM32F0 48 pin LQFP package",
        "pins": [
            [
                [
                    ("VBAT", 1, "pwrin"),
                    ("VDD", 24, "pwrin"),
                    ("VDD", 48, "pwrin"),
                    ("VDDIO2", 36, "pwrin"),
                    ("VDDA", 9, "pwrin"),
                ], [
                    ("VSSA", 8, "pwrin"),
                    ("VSS", 23, "pwrin"),
                    ("VSS", 47, "pwrin"),
                    ("VSS", 35, "pwrin"),
                ], [
                    ("BOOT0", 44, "in"),
                    ("NRST", 7, "in"),
                ], [
                    ("PC13", 2, "bidi"),
                    ("PC14", 3, "bidi"),
                    ("PC15", 4, "bidi"),
                ], [
                    ("PF0", 5, "bidi"),
                    ("PF1", 6, "bidi"),
                ],
            ], [
                [
                    ("PA0", 10, "bidi"),
                    ("PA1", 11, "bidi"),
                    ("PA2", 12, "bidi"),
                    ("PA3", 13, "bidi"),
                    ("PA4", 14, "bidi"),
                    ("PA5", 15, "bidi"),
                    ("PA6", 16, "bidi"),
                    ("PA7", 17, "bidi"),
                ], [
                    ("PA8", 29, "bidi"),
                    ("PA9", 30, "bidi"),
                    ("PA10", 31, "bidi"),
                    ("PA11", 32, "bidi"),
                    ("PA12", 33, "bidi"),
                    ("PA13", 34, "bidi"),
                    ("PA14", 37, "bidi"),
                    ("PA15", 38, "bidi"),
                ], [
                    ("PB0", 18, "bidi"),
                    ("PB1", 19, "bidi"),
                    ("PB2", 20, "bidi"),
                    ("PB3", 39, "bidi"),
                    ("PB4", 40, "bidi"),
                    ("PB5", 41, "bidi"),
                    ("PB6", 42, "bidi"),
                    ("PB7", 43, "bidi"),
                ], [
                    ("PB8", 45, "bidi"),
                    ("PB9", 46, "bidi"),
                    ("PB10", 21, "bidi"),
                    ("PB11", 22, "bidi"),
                    ("PB12", 25, "bidi"),
                    ("PB13", 26, "bidi"),
                    ("PB14", 27, "bidi"),
                    ("PB15", 28, "bidi"),
                ],
            ],
        ],
    },

    # STM32F0xxRxHx, in UFBGA64 package
    "STM32F0xxRxHx": {
        "path": "ic/microcontroller",
        "footprint": "agg:UFBGA-64",
        "datasheet": "http://www.st.com/st-web-ui/static/active/en"
                     "/resource/technical/document/datasheet/DM00115237.pdf",
        "ordercodes": {
            "Farnell": "2503242",
        },
        "description": "STM32F0 64 pin UFBGA package",
        "pins": [
            [
                [
                    ("VBAT", "B2", "pwrin"),
                    ("VDD", "D2", "pwrin"),
                    ("VDD", "E4", "pwrin"),
                    ("VDD", "E5", "pwrin"),
                    ("VDDIO2", "E6", "pwrin"),
                    ("VDDA", "H1", "pwrin"),
                ], [
                    ("VSSA", "F1", "pwrin"),
                    ("VSS", "C2", "pwrin"),
                    ("VSS", "D4", "pwrin"),
                    ("VSS", "D5", "pwrin"),
                    ("VSS", "D6", "pwrin"),
                ], [
                    ("BOOT0", "B4", "in"),
                    ("NRST", "E1", "in"),
                ], [
                    ("PF0", "C1", "bidi"),
                    ("PF1", "D1", "bidi"),
                ], [
                    ("PA0", "G2", "bidi"),
                    ("PA1", "H2", "bidi"),
                    ("PA2", "F3", "bidi"),
                    ("PA3", "G3", "bidi"),
                    ("PA4", "H3", "bidi"),
                    ("PA5", "F4", "bidi"),
                    ("PA6", "G4", "bidi"),
                    ("PA7", "H4", "bidi"),
                ], [
                    ("PA8", "D7", "bidi"),
                    ("PA9", "C7", "bidi"),
                    ("PA10", "C6", "bidi"),
                    ("PA11", "C8", "bidi"),
                    ("PA12", "B8", "bidi"),
                    ("PA13", "A8", "bidi"),
                    ("PA14", "A7", "bidi"),
                    ("PA15", "A6", "bidi"),
                ],
            ], [
                [
                    ("PB0", "F5", "bidi"),
                    ("PB1", "G5", "bidi"),
                    ("PB2", "G6", "bidi"),
                    ("PB3", "A5", "bidi"),
                    ("PB4", "A4", "bidi"),
                    ("PB5", "C4", "bidi"),
                    ("PB6", "D3", "bidi"),
                    ("PB7", "C3", "bidi"),
                ], [
                    ("PB8", "B3", "bidi"),
                    ("PB9", "A3", "bidi"),
                    ("PB10", "G7", "bidi"),
                    ("PB11", "H7", "bidi"),
                    ("PB12", "H8", "bidi"),
                    ("PB13", "G8", "bidi"),
                    ("PB14", "F8", "bidi"),
                    ("PB15", "F7", "bidi"),
                ], [
                    ("PC0", "E3", "bidi"),
                    ("PC1", "E2", "bidi"),
                    ("PC2", "F2", "bidi"),
                    ("PC3", "G1", "bidi"),
                    ("PC4", "H5", "bidi"),
                    ("PC5", "H6", "bidi"),
                    ("PC6", "F6", "bidi"),
                    ("PC7", "E7", "bidi"),
                ], [
                    ("PC8", "E8", "bidi"),
                    ("PC9", "D8", "bidi"),
                    ("PC10", "B7", "bidi"),
                    ("PC11", "B6", "bidi"),
                    ("PC12", "C5", "bidi"),
                    ("PC13", "A2", "bidi"),
                    ("PC14", "A1", "bidi"),
                    ("PC15", "B1", "bidi"),
                ], [
                    ("PD2", "B5", "bidi"),
                ]
            ],
        ],
    },

    # STM32F3xxCxTx, in LQFP48 package
    "STM32F3xxCxTx": {
        "path": "ic/microcontroller",
        "footprint": "agg:LQFP-48",
        "datasheet": "http://www.st.com/st-web-ui/static/active/en"
                     "/resource/technical/document/datasheet/DM00058181.pdf",
        "ordercodes": {
            "Farnell": "2333254",
        },
        "description": "STM32F3 48 pin LQFP package",
        "pins": [
            [
                [
                    ("VBAT", 1, "pwrin"),
                    ("VDD", 24, "pwrin"),
                    ("VDD", 48, "pwrin"),
                    ("VDD", 36, "pwrin"),
                    ("VDDA", 9, "pwrin"),
                ], [
                    ("VSSA", 8, "pwrin"),
                    ("VSS", 23, "pwrin"),
                    ("VSS", 47, "pwrin"),
                    ("VSS", 35, "pwrin"),
                ], [
                    ("BOOT0", 44, "in"),
                    ("NRST", 7, "in"),
                ], [
                    ("PC13", 2, "bidi"),
                    ("PC14", 3, "bidi"),
                    ("PC15", 4, "bidi"),
                ], [
                    ("PF0", 5, "bidi"),
                    ("PF1", 6, "bidi"),
                ],
            ], [
                [
                    ("PA0", 10, "bidi"),
                    ("PA1", 11, "bidi"),
                    ("PA2", 12, "bidi"),
                    ("PA3", 13, "bidi"),
                    ("PA4", 14, "bidi"),
                    ("PA5", 15, "bidi"),
                    ("PA6", 16, "bidi"),
                    ("PA7", 17, "bidi"),
                ], [
                    ("PA8", 29, "bidi"),
                    ("PA9", 30, "bidi"),
                    ("PA10", 31, "bidi"),
                    ("PA11", 32, "bidi"),
                    ("PA12", 33, "bidi"),
                    ("PA13", 34, "bidi"),
                    ("PA14", 37, "bidi"),
                    ("PA15", 38, "bidi"),
                ], [
                    ("PB0", 18, "bidi"),
                    ("PB1", 19, "bidi"),
                    ("PB2", 20, "bidi"),
                    ("PB3", 39, "bidi"),
                    ("PB4", 40, "bidi"),
                    ("PB5", 41, "bidi"),
                    ("PB6", 42, "bidi"),
                    ("PB7", 43, "bidi"),
                ], [
                    ("PB8", 45, "bidi"),
                    ("PB9", 46, "bidi"),
                    ("PB10", 21, "bidi"),
                    ("PB11", 22, "bidi"),
                    ("PB12", 25, "bidi"),
                    ("PB13", 26, "bidi"),
                    ("PB14", 27, "bidi"),
                    ("PB15", 28, "bidi"),
                ],
            ],
        ],
    },

    # STM32F4xxVxTx, in LQFP100 package
    "STM32F4xxVxTx": {
        "path": "ic/microcontroller",
        "footprint": "agg:LQFP-100",
        "datasheet": "http://www.st.com/st-web-ui/static/active/en"
                     "/resource/technical/document/datasheet/DM00037051.pdf",
        "ordercodes": {
            "Farnell": "2215224",
        },
        "description": "STM32F4 100 pin LQFP package",
        "pins": [
            [
                [
                    ("VBAT", 6, "pwrin"),
                    ("VDD", 11, "pwrin"),
                    ("VDD", 19, "pwrin"),
                    ("VDD", 28, "pwrin"),
                    ("VDD", 50, "pwrin"),
                    ("VDD", 75, "pwrin"),
                    ("VDD", 100, "pwrin"),
                    ("VDDA", 22, "pwrin"),
                    ("VREF+", 21, "pwrin"),
                ], [
                    ("VCAP_1", 49, "passive"),
                    ("VCAP_2", 73, "passive"),
                ], [
                    ("VSSA", 20, "pwrin"),
                    ("VSS", 10, "pwrin"),
                    ("VSS", 27, "pwrin"),
                    ("VSS", 74, "pwrin"),
                    ("VSS", 99, "pwrin"),
                ], [
                    ("BOOT0", 94, "in"),
                    ("NRST", 14, "in"),
                ], [
                    ("PH0", 12, "bidi"),
                    ("PH1", 13, "bidi"),
                ], [
                    ("PA0", 23, "bidi"),
                    ("PA1", 24, "bidi"),
                    ("PA2", 25, "bidi"),
                    ("PA3", 26, "bidi"),
                    ("PA4", 29, "bidi"),
                    ("PA5", 30, "bidi"),
                    ("PA6", 31, "bidi"),
                    ("PA7", 32, "bidi"),
                ], [
                    ("PA8", 67, "bidi"),
                    ("PA9", 68, "bidi"),
                    ("PA10", 69, "bidi"),
                    ("PA11", 70, "bidi"),
                    ("PA12", 71, "bidi"),
                    ("PA13", 72, "bidi"),
                    ("PA14", 76, "bidi"),
                    ("PA15", 77, "bidi"),
                ], [
                    ("PB0", 35, "bidi"),
                    ("PB1", 36, "bidi"),
                    ("PB2", 37, "bidi"),
                    ("PB3", 89, "bidi"),
                    ("PB4", 90, "bidi"),
                    ("PB5", 91, "bidi"),
                    ("PB6", 92, "bidi"),
                    ("PB7", 93, "bidi"),
                ], [
                    ("PB8", 95, "bidi"),
                    ("PB9", 96, "bidi"),
                    ("PB10", 47, "bidi"),
                    ("PB11", 48, "bidi"),
                    ("PB12", 51, "bidi"),
                    ("PB13", 52, "bidi"),
                    ("PB14", 53, "bidi"),
                    ("PB15", 54, "bidi"),
                ],
            ], [
                [
                    ("PC0", 15, "bidi"),
                    ("PC1", 16, "bidi"),
                    ("PC2", 17, "bidi"),
                    ("PC3", 18, "bidi"),
                    ("PC4", 33, "bidi"),
                    ("PC5", 34, "bidi"),
                    ("PC6", 63, "bidi"),
                    ("PC7", 64, "bidi"),
                ], [
                    ("PC8", 65, "bidi"),
                    ("PC9", 66, "bidi"),
                    ("PC10", 78, "bidi"),
                    ("PC11", 79, "bidi"),
                    ("PC12", 80, "bidi"),
                    ("PC13", 7, "bidi"),
                    ("PC14", 8, "bidi"),
                    ("PC15", 9, "bidi"),
                ], [
                    ("PD0", 81, "bidi"),
                    ("PD1", 82, "bidi"),
                    ("PD2", 83, "bidi"),
                    ("PD3", 84, "bidi"),
                    ("PD4", 85, "bidi"),
                    ("PD5", 86, "bidi"),
                    ("PD6", 87, "bidi"),
                    ("PD7", 88, "bidi"),
                ], [
                    ("PD8", 55, "bidi"),
                    ("PD9", 56, "bidi"),
                    ("PD10", 57, "bidi"),
                    ("PD11", 58, "bidi"),
                    ("PD12", 59, "bidi"),
                    ("PD13", 60, "bidi"),
                    ("PD14", 61, "bidi"),
                    ("PD15", 62, "bidi"),
                ], [
                    ("PE0", 97, "bidi"),
                    ("PE1", 98, "bidi"),
                    ("PE2", 1, "bidi"),
                    ("PE3", 2, "bidi"),
                    ("PE4", 3, "bidi"),
                    ("PE5", 4, "bidi"),
                    ("PE6", 5, "bidi"),
                    ("PE7", 38, "bidi"),
                ], [
                    ("PE8", 39, "bidi"),
                    ("PE9", 40, "bidi"),
                    ("PE10", 41, "bidi"),
                    ("PE11", 42, "bidi"),
                    ("PE12", 43, "bidi"),
                    ("PE13", 44, "bidi"),
                    ("PE14", 45, "bidi"),
                    ("PE15", 46, "bidi"),
                ],
            ],
        ],
    },

}

# Other Constants =============================================================

# None yet.

# End Constants ===============================================================

import os
import sys


pin_types = {
    "in": "I",
    "out": "O",
    "bidi": "B",
    "tri": "T",
    "passive": "P",
    "unspec": "U",
    "pwrin": "W",
    "pwrout": "w",
    "oc": "C",
    "oe": "E",
    "nc": "N",
}


def geometry(conf):
    # width is twice the width required to accommodate the longest name
    longest_name = max(max(len(pin[0]) for pin in grp) for grp in conf['pins'])
    width = 2 * (longest_name + 3) * 50

    # height is the maximum required on either side
    left_pins = sum(len(x) for x in conf['pins'][0])
    right_pins = sum(len(x) for x in conf['pins'][1])
    left_groups = len(conf['pins'][0])
    right_groups = len(conf['pins'][1])

    height = 100 * max(
        left_pins + left_groups - 1, right_pins + right_groups - 1)

    # height must be an odd multiple of 0.1" or the grid breaks
    if (height // 100) % 2 == 0:
        height += 100

    return width, height, left_groups


def fields(conf):
    width, height, lgroups = geometry(conf)
    field_x = -width//2
    field_y = height//2 + 50
    out = []

    # Designator at top
    out.append("F0 \"{}\" {} {} 50 H V L CNN".format(
        conf.get('designator', 'IC'), field_x, field_y))

    # Value/name at bottom
    out.append("F1 \"{}\" {} {} 50 H V L CNN".format(
        conf['name'], field_x, -field_y))

    # Either specify a footprint or just set its size, position, invisibility
    if "footprint" in conf:
        out.append("F2 \"{}\" {} {} 50 H I L CNN".format(
            conf['footprint'], field_x, -field_y-100))
    else:
        out.append("F2 \"\" {} {} 50 H I L CNN".format(field_x, -field_y-100))

    # Specify a datasheet if given
    if "datasheet" in conf:
        out.append("F3 \"{}\" {} {} 50 H I L CNN".format(
            conf['datasheet'], field_x, -field_y-200))
    else:
        out.append("F3 \"\" {} {} 50 H I L CNN".format(field_x, -field_y-200))

    # Order codes
    for idx, (supplier, code) in enumerate(conf.get("ordercodes", {}).items()):
        out.append("F{} \"{}\" {} {} 50 H I L CNN \"{}\"".format(
            idx+4, code, field_x, -field_y-(300+idx*100), supplier))

    return out


def draw_pins(groups, x0, y0, direction):
    out = []
    pin_x = x0
    pin_y = y0
    for group in groups:
        for (name, num, t) in group:
            out.append("X {} {} {} {} 100 {} 50 50 0 0 {}".format(
                name, num, pin_x, pin_y, direction, pin_types[t]))
            pin_y -= 100
        pin_y -= 100
    return out


def draw(conf):
    width, height, lgroups = geometry(conf)
    out = []
    out.append("DRAW")

    # Containing box
    out.append("S {} {} {} {} 0 1 0 f".format(
        -width//2, height//2, width//2, -height//2))

    # Pins
    x0 = -width//2 - 100
    y0 = height//2 - 50
    out += draw_pins(conf['pins'][0], x0, y0, "R")
    out += draw_pins(conf['pins'][1], -x0, y0, "L")

    out.append("ENDDRAW")
    return out


def library(conf):
    out = []

    out.append("EESchema-LIBRARY Version 2.3")
    out.append("#encoding utf-8")
    out.append("#\n# {}\n#".format(conf['name']))
    out.append("DEF {} {} 0 40 Y Y 1 F N".format(
        conf['name'], conf.get('designator', 'IC')))

    out += fields(conf)
    out += draw(conf)

    out.append("ENDDEF\n#\n#End Library\n")
    return "\n".join(out)


def documentation(conf):
    out = []
    out.append("EESchema-DOCLIB\tVersion 2.0")
    out.append("$CMP {}".format(conf['name']))
    out.append("D {}".format(conf['description']))
    out.append("$ENDCMP\n")
    return "\n".join(out)


def main(libpath):
    for name, conf in config.items():
        conf['name'] = name
        path = os.path.join(libpath, conf.get("path", ""), name.lower()+".lib")
        dcmpath = os.path.splitext(path)[0] + ".dcm"

        lib = library(conf)
        dcm = documentation(conf)

        # Check if anything has changed
        if os.path.isfile(path):
            with open(path) as f:
                oldlib = f.read()
            if os.path.isfile(dcmpath):
                with open(dcmpath) as f:
                    olddcm = f.read()
            else:
                olddcm = ""
            if lib == oldlib and dcm == olddcm:
                continue

        # If we've made changes, write them
        with open(path, "w") as f:
            f.write(lib)
        with open(dcmpath, "w") as f:
            f.write(dcm)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        libpath = sys.argv[1]
        main(libpath)
    else:
        print("Usage: {} <lib path>".format(sys.argv[0]))
        sys.exit(1)
