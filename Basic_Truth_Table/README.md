# Basic Truth Table

## Discrete Mathematics Lesson - Simple Logical Connectives

##### This program only accepts three characters namely;

1. Any character which will symbolizes **(p)**
2. Any of the following logical connective:
    - Negation **(¬)**
    - Conjunction **(^)**
    - Exclusive Or **(⊻)**
    - Disjunction **(v)**
    - Implication **(→)**
    - Biconditional **(<->)**
    
3. Any character which will symbolize **(q)**

**Format** :  (firstChar_connective_lastChar)
**(¬)** are MERGED WITH firstChar or lastChar to denote negation

Where:

  1. firstChar & lastChar = any alphabet 
  2. connective = (^) | (⊻) | (v) | (→) | <-> 
  3. (_) = spaces

Example :

    1. p ^ q  
    2. a v ¬b 
    3. ¬x → y 
    4. ¬i <-> ¬j

This program will only process simple propositions ONLY
