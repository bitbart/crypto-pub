# Crypto

## Cryptanalysis of historical ciphers

- Shift cipher: [shift.py](cryptanalysis/shift.py)

## Indistinguishability experiments

- Private-key encryption schemes: [cipher.py](privk-eav/cipher.py)
- PrivK experiment driver: [privk-eav.py](privk-eav/privk-eav.py)
  - Adv randomly guessing: [mallory0.py](privk-eav/mallory0.py)
  - Adv for Shift cipher in ECB mode: [mallory1.py](privk-eav/mallory1.py)
  - Adv for Shift cipher with unbalanced keys: [mallory2.py](privk-eav/mallory2.py)
  - Adv for Vigenère cipher with unbalanced keys: [mallory3.py](privk-eav/mallory3.py)
  - Adv for OTP with computed last bit: [mallory4.py](privk-eav/mallory4.py)
  - Adv for two-time pad: [mallory5.py](privk-eav/mallory5.py)
  - Adv for quasi-OTP: [mallory6.py](privk-eav/mallory6.py)
