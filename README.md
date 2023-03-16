Python script that reads an `.ods` (libreoffice calc) with an offset-file list and transform it to a `numpy` array in the following format:

```python
    N rows and [offset, file]
```

A typical ODS spreadsheet file might look like this:

| OFFSETS   | INDEX |
|-----------|-------|
| 111000000 | 54    |
|-----------|-------|
| 431003010 | 154    |

It will return an array like:
array([['111000000',
        '/lustre/ap/litv-exp/2021-05-00_E143_TwoPhotonDeday_ssanjari/NTCAP/iq/IQ_2021-05-10_00-14-45/0000054.iq.tdms'],
['431003010',
        '/lustre/ap/litv-exp/2021-05-00_E143_TwoPhotonDeday_ssanjari/NTCAP/iq/IQ_2021-05-10_00-14-45/0000154.iq.tdms']])


## Installation
Clone this repository with:
```bash
    git clone https://github.com/DFreireF/off2np.git
```
Then use `pip` for installing `off2np`.

```bash
  pip install -r requirements.txt
  pip install .
```

## Usage

Run it as a python module

    python -m off2np /your/path/with/thefile.ods

Or once installed, you can use from anywhere with:

    off2np /your/path/with/thefile.ods

Then it will return a numpy array.
