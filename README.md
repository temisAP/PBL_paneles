# PBL Paneles

## File designation

A part will be designed as follows:
      
      NNN_NN

Where:

      the first number design the module within the whole project

      the second number desgin the subset within the module

      the third number desgin the product within the subset

      the two numbers after low bar enumerates the part within the product
  
## About parametrization

Every part will be parametrized independently and then all parameters will be set and linked in a single CATPart called 'PARAMETROS' which is a product that contains parameter parts named as their product
 

## Subsets, products, and parts 

### Subsets

      4_GUI: Graphic User Interface
      40: Solar pannel assembly
      41: Solar panels 
      42: Release mechanism
      43: SADA mechanism
      44: Hinge joints
      45: Estructural subsets
      46: Solar cells
      47: Harness
      48: Hardware

### Products

Graphic User Interface

      GUI_PBL.mlapp
      Image

Solar panels assemly

      401: Solar panels

Solar panels

      411: Sandwich panel (right inserts in upper fiber)
      412: Aluminium panel
      413: Sandwich panel (left inserts in upper fiber) 

Release mechanism

      42: 421
      421: Satellite deployment 
      422: Sandwich Panels deployment 
      423: Aluminium Panels deployment
      424: Triangular support-panels
      

SADA mechanism

      43: 431, 432, 433, 434 and 435
      431: Motor (with its encoder), gear and support
      432: Output axis, gear and retaining rings
      433: Case
      434: T-shaped adapter
      435: Bolts & nuts

Hinge joints

      441: Hinge between panels
      442: Hinge between triangular support and panels

Estructural subsets
      
      451: Triangular support

Solar cells

      461: Solar cells module
      462: Solar cells (without aluminium base)

Harness

      471: Aluminium pannel harness #1
      472: Aluminium pannel harness #2
      473: 
      474: Composite panel harness #2
      475: Aluminium pannel connectors
      476: Aluminium pannel harness #3
      477: Aluminium pannel harness #4
      478: Composite panel harness #2

Hardware

      481: M3 Screw + Nut + Washer


### Parts

Solar panels

      401_01: Sandwich panel with cells (right inserts in upper fiber)
      401_02: Cupon with screws
      401_03: Aluminium panel with cupons
      401_04: Sandwich panel with cells (left inserts in upper fiber)


Solar panels

      411_01: Honeycomb core (right inserts in upper fiber)
      411_02: Upper Carbon Fiber (right inserts in upper fiber)
      411_03: Lower Carbon Fiber (right inserts in upper fiber)
      411_04: Insert Shur-Lok SL644
      411_05: Potting compound
      411_06: Release insert
      411_07: Release potting compound
      411_08: Release insert bolt
      411_09: Release potting compound bolt
      
      412_01: Aluminium panel
      
      413_01: Honeycomb core (left inserts in upper fiber)
      413_02: Upper Carbon Fiber (left inserts in upper fiber)
      413_03: Lower Carbon Fiber (left inserts in upper fiber)

      
Release mechanism between triangular support and satellite

      421_01: Base
      421_02: Claw
      421_03: Spring
      421_04: Spring2
      421_05: Parameters
      421_06: Bolts
      421_07: Helicoil
      421_08: Washer
      
Release mechanism between sandwich panels


      422_01: Base
      422_02: Claw
      422_03: Spring
      422_04: Spring2
      422_05: Parameters
      422_06: Bolts
      422_08: Washer
      
Release mechanism between aluminium panels deployment


      423_01: Base
      423_02: Claw
      423_03: Spring
      423_04: Spring2
      423_05: Parameters 
      423_06: Bolts
      423_07: Nuts
      423_08: Washer

Release mechanism between triangular support and panels

      424_01: Base
      424_02: Claw
      424_03: Spring
      424_04: Spring2
      424_05: Parameters 
      424_06: Bolts
      424_07: Nuts
      424_08: Washer
      
SADA mechanism

      431_01: Motor
      431_02: Gear
      431_03: Support
      
      432_01: Output axis
      432_02: Gear
      432_03: Retaining rings (DIN 471)
            
      433_01: Upper case
      433_02: Lower case
      433_03: Bearings
      433_04: Bolts & nuts
      
      434_01: T-shaped adapter
      434_02: Set screw (ISO 4026)

Hinge between panels

      441_01: Outter wing of the hinge
      441_02: Inner wing of the hinge
      441_03: Hinge spring
      441_04: Hinge axis
      441_05: Spring plunger (M3)

Hinge between triangular support and panels

      442_01: Outter wing of the hinge
      442_02: Inner wing of the hinge
      442_03: Hinge spring
      442_04: Hinge axis
      442_05: Spring plunger (M3)
 
Triangular support
 
      451_01: Triangular support

Solar cells

      461_01: Aluminium base
      461_02: Connecting plate
      461_03: Cell interconnectors
      461_04: Triple Junction solar Cell Assembly 3G30A
      461_05: Connectors base plate
      461_06: Molex Pico-Lock 1.50 mm pitch, right angle, 504050-0491

      462_01: Cell interconnectors
      462_02: Solar Cells

Harness

      471_GB: Geometrical Bundle
      471_01: Wire 1
      471_02: Wire 2
      471_03: Wire 3
      471_04: Wire 4
      471_05: Molex Pico-Lock 1.50 mm pitch, right angle, 504051-0401
      471_06: Clamp

      472_GB: Geometrical Bundle
      472_01: Wire 1
      472_02: Wire 2
      472_03: Wire 3
      472_04: Wire 4
      472_05: Molex Pico-Lock 1.50 mm pitch, right angle, 504051-0401
      472_06: Clamp




      473_01: Terminal block

      474_01: Composite panel harness #1

      475_01: Clamp
      475_02: https://www.harwin.com/products/G125-2240696F1/
      475_03: https://www.harwin.com/products/G125-324069600/

      47.._01: https://www.harwin.com/products/G125-FS10605F2R/
      47.._02: https://www.harwin.com/products/G125-3240696M3/


      476_01: Clamp
      476_GB: Geometrical Bundle
      476_02: Wire

      477_GB_1: Geometrical Bundle 1
      477_01: Wire 1
      477_02: Wire 2
      477_03: Wire 3
      477_04: Wire 4
      477_05: Molex Pico-Lock 1.50 mm pitch, right angle, 504051-0401
      477_06: Clamp
      477_07: Conection Box
      477_GB_2: Geometrical Bundle 2
      477_08: Wire 1
      477_09: Wire 2
      477_10: Wire 3
      477_11: Wire 4

      478_01: Composite panel harness #2



