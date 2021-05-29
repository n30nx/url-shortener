# url-shortener
Flask based url shortener

<p align="left" style="vertical-align: top;">
  <a target="_blank" href="https://www.python.org/downloads/" title="Written in"><img src="https://img.shields.io/badge/python->=_3.9.5-royalblue.svg"></a>
  <a target="_blank" href=https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html title="GPL V2 License"><img src="https://img.shields.io/badge/License-GPL%20v2-blue.svg"></a>
</p>

<p align="center">
  <a href="#installation">Installation</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#usage">Usage</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#customization">Customization</a>
</p>

## Installation

```console
$ git clone https://github.com/n30nx/url-shortener.git
$ cd url-shortener
$ pip install -r requirements.txt
```

## Usage

```console
$ python3 server.py
```
And that's it :)

## Customization

- You can write a css file and include it in the base.html
- You can change the port of the server: \
&nbsp;&nbsp;&nbsp;Just change the port option from the file
```python
if __name__ == "__main__":

    app.run(debug = True, port = 5000)
```
