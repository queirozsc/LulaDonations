# Pytest vs UnitTest
Project to compare Pytest and Unittest test frameworks

## Comparison table

| Feature | Pytest | Unitest | Winner |
| --- | --- | --- | --- |
| Installation | Third party | Built in | Unitest |
| Basic infra | Can be only a function | Inheritance | Pytest |
| Basic assertion | Assert built in | TestCase instance methods| Pytest |
| Flat is better than nested | Function (1 level) | Method (2 level) | Pytest |
| Can run each other test | Yes | No | Pytest |
| Test results on console | Syntax highlight, Code snippet | Only line error | Pytest |
| Multi param test | Yes, Parametrize, Keep flat | Yes, Subtest, Increase nesting | Pytest |
| Test setup | Fixture: module, session, function | Template method: setup, tearDown | Pytest |