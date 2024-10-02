# Crypto

## Cryptanalysis of historical ciphers

- Shift cipher: [cryptanalysis/shift.py](shift.py)

## Indistinguishability experiments

- Private-key encryption schemes: [privk-eav/cipher.py](cipher.py)
- PrivK experiment driver: [privk-eav/privk-eav.py](privk-eav.py)
  - Adv randomly guessing: [privk-eav/mallory0.py](mallory0.py)
  - Adv for Shift cipher in ECB mode: [privk-eav/mallory1.py](mallory1.py)
  - Adv for Shift cipher with unbalanced keys: [privk-eav/mallory2.py](mallory2.py)
  - Adv for Vigenère cipher with unbalanced keys: [privk-eav/mallory3.py](mallory3.py)
  - Adv for OTP with computed last bit: [privk-eav/mallory4.py](mallory4.py)
  - Adv for two-time pad: [privk-eav/mallory5.py](mallory5.py)
  - Adv for quasi-OTP: [privk-eav/mallory6.py](mallory6.py)
