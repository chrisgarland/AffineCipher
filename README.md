# Fundamental Concepts of Cryptography
###### Assignment 1 – AffineCipher implementation

### 0. Refer to the [assignment specification](doc/Assignment_one_17.pdf) for details

### 1. Introduction:
This program makes use of python 2.7.\* and has been run on the lab machines.

### 2. Run/Usage:
<ul>
    <li>
        encrypt: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <code>python affine_cipher.py <b>existing_file e <i>KEY</i></b></code>
    </li>
    <li>
        decrypt: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <code>python affine_cipher.py <b>existing_file.encr d <i>KEY</i></b></code>
    </li>
</ul>

– Cannot encrypt a file that is currently encrypted (has extension .encr)<br>
– Cannot decrypt a file that is currently unencrypted (does not have ext .encr)<br>
– Both 'e' and 'd' are literal<br>
– In both cases (encr/decr), **_KEY_** needs to be replaced by a numeric (int) value
