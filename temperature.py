#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 20:00:21 2020

@author: arch
"""

import time
import seeed_dht
def main():

    # for DHT11/DHT22
    sensor = seeed_dht.DHT("11", 12)
    # for DHT10
    # sensor = seeed_dht.DHT("10")

    while True:
        humi, temp = sensor.read()
        print('----------------------')
        print('temperature=',temp)
        print('humid=',humi)
        if not humi is None:
            print('DHT{0}, humidity {1:.1f}%, temperature {2:.1f}*'.format(sensor.dht_type, humi, temp))
        else:
            print('DHT{0}, humidity & temperature: {1}'.format(sensor.dht_type, temp))
        time.sleep(0.5)


if __name__ == '__main__':
    main()