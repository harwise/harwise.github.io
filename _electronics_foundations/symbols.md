---
layout: default
title: Symbols
---

{% include katex.html %}

# Metrics Prefixes

$G$ (giga) $M$ (mega) $k$ (kilo) $1$ $m$ (milli) $\mu$ (micro) $n$ (nano) $p$ (pico)

# Energy

Voltage  - Potential energy. Pressure.\
Current  - Kinetic energy. Flow.

Joule ($J$) - How much energy is transferred.\
Watt ($W$)  - Electric Power. The rate at which energy is transferred or transformed.

$$
1W = 1J \space per \space second
$$

$$
P = I \times V
$$

|Situation|Approximate Power|
|:-------:|:---------------:|
|Arduino Uno Micro-controller|0.25$W$|
|Cell Phone Transmitter|3$W$|
|Laptop Computer|65$W$|
|50-Inch LCD Television|150$W$|
|Microwave Oven|1000$W$|

# Battery

Nominal Voltage   - Output voltage after 50% discharge\
Capacity ($Ah$)   - Amp-hours. Amount of electrons. One amp of current for one hour at its rated voltage.

# Grounded vs. floating

GND (ground) - wall power outlets.\
COM (**own** common point) - batteries.

# Symbols

* DC Voltage Source
* AC Voltage Source
* Current Source
* Batteries
* Positive Voltage Nodes
* Negative Voltage Nodes
* Ground - Earth
* Ground - Common
* Ground - Chassis
* Resistor

# Prefix

* R - Resistor
* C - Capacitor
* L - Inductor
* S - Switch
* D - Diode
* Q - Transistor
* U - Integrated Circuit
* Y - Oscillator

# Voltage

* Working Voltage - maximum continuous voltage
* OverVoltage - maximum surge voltage

## Shift Voltage Levels

* Resistors for Voltage Dividers: use 1 $k\Omega$ - 10 $k\Omega$ resisitors.  
    Can only shift down.  
    Only use for low-current signals. ( a few $mAs$ )  
    Do not use for power supply output.  
* Voltage Regulator
* Switching Power Supply



# Components

## Wires

* 22 AWG - just fit in breadboard holes. Good for jumper wires.

## Resistors (passive)

### PTH

Plated-through hole

* normally 1/8 - 2 watts
* Power Resistors: 10s - 100s watts

### SMD

Surface-mount device

Smaller than PTHs

### Variable Resistors

* Potentiometers/Pots (3 terminals)
* Rheostat (2 terminals)

### Photoresistors / LDR (Light Dependent Resistor)

* More lights leads to less resistence

### Types

* Carbon Film (Cheapest, most common)
* Metal Film
* Wire Wound (most accurate and stable)

### Powering rating vs. working voltage

* Powering rating limits small resistors (< 250 $k\Omega$)
* Working voltage limits large resistors (> 250 $k\Omega$)

### Resistive Sensors

* Photoresistor changes based on light
* Strain Gauge changes based on physical strain
* Thermistor changes based on temperature

  For microcontrollers, measuring resistors is hard, but reading voltage is easy (e.g. Arduino A0 channel).  
  use Voltage Dividers.

