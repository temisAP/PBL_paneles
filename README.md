# PBL Paneles

## File designation

A part will be designed as follows:
      
      NNN_NN

Where:

      the first number design the module 
        4 for solar panels
      the second number desgin the subset
        1 for panels per se
        2 for release mechanism
        3 for SADA mechanism
        4 for hinge joints
        5 for estructural subsets
      the third number desgin the product within the subset
            Subset 1:
            Subset 2:
            Subset 3:
            Subset 4:
              1 for hinges between panels
              2 for hinges between first panel and triangle support
      the two numbers after low bar enumerates the part within the product
  
## About parametrization

Every part will be parametrized independently and then all parameters will be set and linked in a single CATPart called 'PARAMETROS' which is a product that contains parameter parts named as their product
 

## Subsets, products, and parts 

### Subsets

      44: Hinge joints

### Products

Hinge joints

      441: Hinge between panels

### Parts

Hinge between panels

      441_01: Outter wing of the hinge
      441_02: Inner wing of the hinge
      441_03: Hinge spring
      441_04: Hinge axis
      441_05: Hinge axis nuts
      441_06: Hinge axis ball which blocks the hinge when it is opened
      441_07: Hinge axis spring which push the ball outside






      
   
