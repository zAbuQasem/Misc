# SecretsConverter
A script to convert plain data into base64 encoded to use with  kubernetes secrets.yml
# Usage:
The tool takes a plain yml file:
```yml
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
type: Opaque
data:
  USER_NAME: zeyad
  PASSWORD: abuqasem@p@ssword!@
```
```bash
python3 SecretsConverter.py -f <FILE.yml> -o <OUTFILE.yml>
# Example
python3 SecretsConverter.py -f plain.yml -o secrets.yml
```
- Output
 ```yml
 apiVersion: v1
kind: Secret
metadata:
  name: mysecret
type: Opaque
data:
  USER_NAME: emV5YWQ=
  PASSWORD: YWJ1cWFzZW1AcEBzc3dvcmQhQA==
```
# Installation
```bash
pip3 install pyyaml
```
- Adding it to path
```bash
chmod +x SecretsConverter.py
sudo mv SecretsConverter.py /usr/bin
```
# Piping directly to clipboard
Install `xclip`
```bash
# Debian
apt install xclip
# Fedora/Centos
dnf install xclip
```
Then
```bash
python3 SecretsConverter.py -f plain.yml | xclip -selection c
```
