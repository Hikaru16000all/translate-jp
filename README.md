# translate-jp
How to Translate Vertical Japanese PDF Books (Step-by-Step Guide)

## dependency  
### ndlocr-lite
https://github.com/ndl-lab/ndlocr-lite
### pdf2image
https://github.com/Belval/pdf2image
### pdf 24 tools
https://tools.pdf24.org/zh/split-pdf
### openai (Optional)
https://github.com/openai/openai-python
### Api (Optional)
an api key of LLM (e.g. Deepseek (most cost-effective), Claude (best performance), doubao (cheapest))
### immersive translate (Optional)
https://immersivetranslate.com/en/
### Others
python version >= 3.10 (I use 3.12)

## Tutorial
### Step0. Prepare
1. create a workdir (in this tutorial, we'll refer your path to your workdir as '{workdir}')
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
```
python mergetxt.py
```

### Step7. translate
You can use your own translate method. Here we'll use immersive translate (https://immersivetranslate.com/en/).  
1. download google extension of immersive translate.
2. enter https://dash.immersivetranslate.com/#services
3. choose 'Add Custom Translation Service' adn confirm.
4. Add Custom Translation Service (depend on what api you use)
5. fill your api key and choose 'Paraphrase Expert' in 'You can designate an AI expert to provide translation strategies.：' option.
6. Verify sevice
7. enter https://app.immersivetranslate.com/ and choose Document Translation.
8. upload your .txt file and done!

### Step8. clean (Optional)
The translated document still contains many issues, such as disorganized formatting and extraneous margin text, making further cleaning necessary.
```
pip install openai
python {workdir}/translate-jp/clean.py
```


