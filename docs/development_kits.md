# Developmemt Kits

## Standard Commercial Research Platforms

These are platforms that are currently commercially available for anybody to buy for their research.

### Copters

Holybro:

   - [PX4 Vision Dev Kit V1.5](https://holybro.com/collections/multicopter-kit/products/px4-vision-dev-kit-v1-5)

ModalAI:

   - [PX4 Autonomy Dev Kit](https://www.modalai.com/products/px4-autonomy-developer-kit?variant=46969885950256)
   - [Starling 2](https://www.modalai.com/products/starling-2?variant=48173890175280) and [Starling 2 Max](https://www.modalai.com/products/starling-2-max?variant=48172375310640)
- [PX4 Autonomy Developer Kit](https://www.modalai.com/collections/drones/products/px4-autonomy-developer-kit)

Duckietown:

- [Duckiedrone DD21](https://get.duckietown.com/products/duckiedrone-dd21)
- [Duckiedrone DD24](https://get.duckietown.com/products/autonomous-raspberrypi-quadcopter-duckiedrone-dd24)

Fly4Future:

- [Fly4Future Robofly](https://fly4future.com/robofly/)
- [FLy4Future custom drone designs](https://fly4future.com/custom-drones/)

Other:

- [NXP HoverGames Kit](https://www.nxp.com/design/designs/nxp-hovergames-drone-kit-including-rddrone-fmuk66-and-peripherals:KIT-HGDRONEK66) official hardware for the yearly [HoverGames Challenge](https://www.hovergames.com)
- [Clover by Coex](https://clover.coex.tech/en/)
- [Droneblocks DEXI 5](https://droneblocks.io/program/dexi-5-px4-stem-drone-kit/)
- [3DR Quad Zero Kit](https://store.3dr.com/3dr-quad-zero-kit/)
- [Crazyflie 2.1+ - Bitcraze](https://www.bitcraze.io/products/crazyflie-2-1-plus/)

### Flapping wing

- [Flapper Nimble+](https://flapper-drones.com/wp/nimbleplus/) insect-inspired UAV by Flapper Drones

## Industrial Platforms

- [Tricopter voliro AG](https://voliro.com/)
- [DJI M300](https://enterprise.dji.com/matrice-300)

## Inhouse-developed platforms

These are platforms that are standard within a lab or department, with information of what it contains provided with perhaps build instructions:

-  [OmniQuad - University of Naples Federico II](https://tilties2.github.io/omniquad-website/)
-  [Agilicous - University of Zurich](https://agilicious.readthedocs.io/en/latest/index.html)
-  [ModQuad - Lehigh University](http://swarmslab.com/projects/)
-  [RMF-Owl - Norwegian University of Science and Technology](https://ieeexplore.ieee.org/document/9836115)
-  [MiniHawk-VTOL](https://github.com/StephenCarlson/MiniHawk-VTOL)

### Reference Bill of Materials

#### Holybro S500v2

The [Holybro S500v2](https://holybro.com/collections/s500/products/s500-v2-development-kit) is a popular, relatively low-cost quadcopter. This is a list of the parts used with details of battery, motors, ESCs, and propellers with reference links to guide custom builds.


| S.No | Part Name                               | Part category           | Description                                               | Price (USD) | Qty         | Total Cost (USD) | Official/Reference Link                                                                                                                                                              |
| ---- | --------------------------------------- | ----------------------- | --------------------------------------------------------- | ----------- | ----------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | Holybro S500 frame                      | Frame                   | With landing gear, 385x385mm                              | 42          | 1           | 42               | [https://holybro.com/collections/s500/products/s500-v2-kit?variant=42724497391805](https://holybro.com/collections/s500/products/s500-v2-kit?variant=42724497391805)                 |
| 2    | Holybro Pixhawk 6C + GPS + Power module | FC + GPS + Power module | PM02 power module, M9N GPS                                | 290         | 1           | 290              | [https://holybro.com/products/pixhawk-6c?variant=43005243785405](https://holybro.com/products/pixhawk-6c?variant=43005243785405)                                                     |
| 3    | Holybro 2216 920KV CW                   | Motor                   | 19x19 mounting clockwise rotation                         | 20          | 2           | 40               | [https://holybro.com/products/spare-parts-s500-v2-kit?variant=41591094608061](https://holybro.com/products/spare-parts-s500-v2-kit?variant=41591094608061)                           |
| 4    | Holybro 2216 920KV CCW                  | Motor                   | 19x19 mounting counter-clockwise rotation                 | 20          | 2           | 40               | [https://holybro.com/products/spare-parts-s500-v2-kit?variant=41591094640829](https://holybro.com/products/spare-parts-s500-v2-kit?variant=41591094640829)                           |
| 5    | BLHeli S 20A ESC                        | ESC                     | Electronic Speed Controller to drive motors               | 14          | 4           | 56               | [https://holybro.com/products/spare-parts-s500-v2-kit?variant=41591094706365](https://holybro.com/products/spare-parts-s500-v2-kit?variant=41591094706365)                           |
| 6    | 1045 propellers                         | Props                   | 10x4.5" kit of 2 pairs                                    | 12          | 1           | 12               | [https://holybro.com/products/spare-parts-s500-v2-kit?variant=41591094313149](https://holybro.com/products/spare-parts-s500-v2-kit?variant=41591094313149)                           |
| 7    | Radiomaster R81 receiver                | Radio receiver          | Used for manually flying drone Line of Sight/testing\*    | 18          | 1           | 18               | [https://holybro.com/products/radiomaster-r81-receiver](https://holybro.com/products/radiomaster-r81-receiver)                                                                       |
| 8    | Holybro SiK telemetry radio v3          | Telemetry link radio    | 500mW, 433MHz variant, pair of transmitter + receiver\*\* | 63          | 1           | 63               | [https://holybro.com/products/sik-telemetry-radio-v3?variant=42801817485501](https://holybro.com/products/sik-telemetry-radio-v3?variant=42801817485501)                             |
| 9    | Tattu 5200mAh 4S                        | Battery                 | 4S1P XT60 plug 35C                                        | 63          | 1           | 63               | [https://genstattu.com/tattu-5200mah-14-8v-35c-4s1p-lipo-battery-pack-with-xt60-plug.html](https://genstattu.com/tattu-5200mah-14-8v-35c-4s1p-lipo-battery-pack-with-xt60-plug.html) |
|      |                                         |                         |                                                           |             | Grand Total | 624              |                                                   |             |             |                  |

**Notes**:

\*It can be used with Radiomaster Multiprotocol (4 in 1) or CC2500 based Radio Controller like FrSky Taranis X9D or similar<br>
\*\*Used for connecting to ground control station, 915MHz variant also available

**Useful tool for this page**:
<https://tabletomarkdown.com/convert-spreadsheet-to-markdown/>

This page was last updated: *{{ git_revision_date_localized }}*

--8<-- "docs/goatcounter.html"
