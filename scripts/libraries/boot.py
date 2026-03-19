# -*- coding: utf-8 -*-
"""
File Name : boot.py
Project   : OpenMV N6 GPIO Self Test (Frozen Firmware Version)
Author    : Dino Cheng
Version   : v1.0
Date      : 2026-03-19
Platform  : OpenMV N6 / STM32N657X0
Python    : MicroPython (OpenMV)

Description:
    Frozen boot-time GPIO self-test script for OpenMV N6.
    This script runs automatically at boot, beeps 3 times, then exits.
"""

from pyb import Pin
import time

BUZZER_PIN = "P7"
BEEP_ON_MS = 200
BEEP_OFF_MS = 200
BEEP_TIMES = 3
STARTUP_DELAY_MS = 1000


def buzzer_on(pin):
    pin.low()   # low level trigger


def buzzer_off(pin):
    pin.high()  # low level trigger


def beep(pin, on_ms=BEEP_ON_MS, off_ms=BEEP_OFF_MS, times=BEEP_TIMES):
    for _ in range(times):
        buzzer_on(pin)
        time.sleep_ms(on_ms)
        buzzer_off(pin)
        time.sleep_ms(off_ms)


def main():
    buzzer = Pin(BUZZER_PIN, Pin.OUT_PP)
    buzzer_off(buzzer)

    print("Frozen GPIO self-test start")
    print("Pin         :", BUZZER_PIN)
    print("Trigger     : LOW")
    print("Beep times  :", BEEP_TIMES)

    time.sleep_ms(STARTUP_DELAY_MS)
    beep(buzzer)

    print("Frozen GPIO self-test done")


main()
