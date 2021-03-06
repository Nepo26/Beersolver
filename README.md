<p align="center">
<img src="images/logo.gif">
 
<p align="center">A script for solving vector mechanics Ferdinand P. Beer proposed exercises<br>
<code>pip3 install beersolver && beersolver</code>
</p>

# 🤔 Overview
Here are proposed solutions for the exercises listed on the end of the third
chapter of the book *"Vector Mechanics for Engineers 9° Edition, Ferdinand
P.Beer"*


The general recommendation for the script was that it needed at least
two types of input and at least 2 types of output.

Information about the solved exercises:
- [3C.6](exercises/ThirdChapter/README.md)

# 🔨 Installation
## Automatic
Issue

```
pip3 install search-that-hash
```

then:

```
beersolver
```

To run.
## Manual Installation
Create folder for the virtual env
```
mkdir beersolver
```

Create virtual env
```
python3 -m venv beersolver
```

Activate it:
- Linux
```
source beersolver/bin/activate
```
- Windows
```
call beersolver/bin/activate.bat
```

Install all the necessary packages:
```
pip3 install -r requirements.txt
```

Run beersolver to test it:
```
beersolver
```
# 📖 Documentation (How to use tutorial)
> OBS.:  Throughout this documentation whenever `beersolver` is referenced it means 
`python3 beersolver.py` for those who didn't install it or `beersolver` to the ones 
who installed it with setuptools.

## Configuration File 
To easily run you may just start by creating a skeleton config:

```bash
beersolver exercise-three-c-6 -g 
```

This will create a template with all parameters needed to solve called `example.ini`
as the one below.
```ini
[positions]
position_a_x = 0.0
position_a_y = 96.0
position_a_z = 4.0
position_e_x = 90.0
position_e_y = 52.0
position_e_z = 0.0
position_c_x = 120.0
position_c_y = 36.0
position_c_z = 100.0

[lambdas]
lambda_ab_x = 0.7777777777777778
lambda_ab_y = -0.4444444444444444
lambda_ab_z = 0.4444444444444444
lambda_cd_x = -0.7777777777777778
lambda_cd_y = 0.4444444444444444
lambda_cd_z = -0.4444444444444444

[range]
upper_range = 36.0
lower_range = 9.0
step = 1.0
```

With this created you can now just issue the command and see the result: 
```bash
beersolver exercise-three-c-6 -i example.ini
```

This now generates the response on the command prompt.
You can change the values from `example.ini` to change the exercise parameters.

## Inline
To solve the exercise using inline mode you may insert all the arguments as parameters,
or you wait for the prompt. The program detects if is there any missing argument. 

Supplying parameters:
```bash
beersolver  exercise-three-c-6 --position_a 0.0 96.0 4.0 --position_e 90.0 52.0 0.0 --position_c 120.0 36.0 100.0 --lambda_ab 7/9 -4/9 4/9 --lambda_cd -7/9 4/9 -4/9 --upper_range
 36 --lower_range 9 --step 1.0 
```

Waiting for the prompting:
```bash
beersolver  exercise-three-c-6

A[x]: 0.0
A[y]: 96.0
A[z]: 4.0
E[x]: 90.0
E[y]: 52.0
E[z]: 0.0
C[x]: 120.0
C[y]: 36.0
C[z]: 100.
Lambda_ab[x]: 7/9
Lambda_ab[y]: -4/9
Lambda_ab[z]: 4/9
Lambda_cd[x]: -7/9
Lambda_cd[y]: 4/9
Lambda_cd[z]: -4/9
upper_range: 36
lower_range: 9
step: 1.0
```