# Check In BIPO automatic

This is a program that automates logging into BIPO and completing the clock-in process.

## How to use 

1. Intall requirement packages
  `pip install -r requirements.txt`
2. Prepare your credential information in **.env**, the content is like below. Your password should be encoded by Base64.
    ```
    USERNAME=MyName
    PASSWORD=eW91ciBwYXNzd29yZAo=
    ```
    How to use base64 decode in command line
    e.g: `echo 'your password' | base64`
3. Run check in
   `python checkin.py`
   