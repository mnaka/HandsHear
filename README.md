# Hands Hear

Hands Hear is a ASL to text converter using the Leap Motion. At the moment Hands Hear is a set of python scripts that interpret data streaming from the Leap, improve the signing model and tests the model correctness. 

## Installation instructions

To get started make sure you have the Leap Motion setup on your system and download the Leap Motion SDK. Our entire project is based on Python 2.7 and requires a few python libraries as dependencies. The python dependencies are:

-scikit-learn
-numpy
-matplotlib

Once you've downloaded Leap SDK you'll also need to drop all of the libraries shipped with it into the *lib* folder in the repository before you start. Once that libraries are in the *lib* folder and you've got the python dependencies you're ready to start

##The scripts

All scripts reside in the *src* folder. Open a terminal there to begin.

### stream.py

Stream.py interprets signs from the Leap in real-time and prints the results to the standard output. To run:

```bash
  >>> python stream.py
```  

### learn.py

learn.py adds to the model by machine learning from the learning database.

```bash
  >>>python learn.py
```
