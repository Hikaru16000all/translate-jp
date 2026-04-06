# translate-jp
How to Translate Vertical Japanese PDF Books (Step-by-Step Guide)

## dependency  
### ndlocr-lite
https://github.com/ndl-lab/ndlocr-lite
### pdf2image
https://github.com/Belval/pdf2image
### immersive translate
https://immersivetranslate.com/en/
### pdf 24 tools
https://tools.pdf24.org/zh/split-pdf
### openai (Optional)
https://github.com/openai/openai-python
### Others
an api key of LLM (e.g. Deepseek (most cost-effective), Claude (best performance), doubao (cheapest))  
python version >= 3.10 (I use 3.12)

## Tutorial
### Step0. Prepare
1. create a workdir ({workdir})
2. download your pdf file and put it in workdir
3. download all python scripts in this directory and put them in workdir ({workdir}/translate-jp)
4. create a conda environment of python >= 3.10
   ```python
   conda create -n translate-jp python=3.12
   ```
### Step1. Install ndlocr-lite
```
cd {wordir}
```
There are two ways to download ndlocr-lite
1. run
   ```
   git clone https://github.com/ndl-lab/ndlocr-lite
   ```
2. download .zip file (https://github.com/ndl-lab/ndlocr-lite/archive/refs/heads/master.zip) and then unzip and load it to your wrokdir.  
after downloading
```python
cd ndlocr-lite
conda activate translate-jp
pip install -r requirements.txt
cd src
```
there might be some dependency conflicts, but if running
```python
python ocr.py --help
```
successful, then it would not be a problem.
### Step2. Install pdf2image
```python
pip install pdf2image
```
### Step3. split pdf
We'll split your pdf file into small pdf files per page.  
Use pdf 24 tools (https://tools.pdf24.org/zh/split-pdf)  
You'll get a .zip dir file, unzip it and load it to your workdir ({workdir}/pdf).

### Step4. pdf to image
Because ndlocr-lite only recognize image file, we'll turn pdf into image.  
```python
python {workdir}/translate-jp/pdf2image.py
```

### Step5. image to text
```
cd {workdir}/ndlocr-lite/src
bash img2txt.sh
```

### Step6. merge txt
merge .txt file into a full .txt file


