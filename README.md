# translate-jp
How to Translate Vertical Japanese PDF Books (Step-by-Step Guide)

## Dependencies

### Required
- **ndlocr-lite**  
  https://github.com/ndl-lab/ndlocr-lite
- **pdf2image**  
  https://github.com/Belval/pdf2image
- **PDF24 Tools**  
  https://tools.pdf24.org/zh/split-pdf

### Optional
- **openai**  
  https://github.com/openai/openai-python
- **LLM API key**  
  An API key for an LLM service, such as:
  - DeepSeek (most cost-effective)
  - Claude (best performance)
  - Doubao (lowest cost)
- **Immersive Translate**  
  https://immersivetranslate.com/en/

### Environment
- Python >= 3.10  
  (This tutorial uses Python 3.12.)

---

## Tutorial

### Step 0. Preparation
1. Create a working directory. In this tutorial, the path to your working directory is referred to as `{workdir}`.
2. Download your PDF file and place it in `{workdir}`.
3. Download all Python scripts in this directory and place them in `{workdir}/translate-jp`.
4. Create a conda environment with Python >= 3.10:
   ```bash
   conda create -n translate-jp python=3.12

## Tutorial
### Step 0. Preparation
1. Create a working directory. In this tutorial, the path to your working directory is referred to as `{workdir}`.
2. Download your PDF file and place it in `{workdir}`.
3. Download all Python scripts in this directory and place them in `{workdir}/translate-jp`.
4. Create a conda environment with Python >= 3.10:
   ```bash
   conda create -n translate-jp python=3.12
   ```
   
### Step1. Install ndlocr-lite
First, go to your working directory:
```bash
cd {wordir}
```
There are two ways to get ndlocr-lite
1. Run the following command:
   ```
   git clone https://github.com/ndl-lab/ndlocr-lite
   ```
2. Download the .zip file (https://github.com/ndl-lab/ndlocr-lite/archive/refs/heads/master.zip), then unzip and extract it to your workdir.
After downloading:
```bash
cd ndlocr-lite
conda activate translate-jp
pip install -r requirements.txt
cd src
```
There might be some dependency conflicts, but if running the following command is successful, then it should not be a problem:
```bash
python ocr.py --help
```

### Step2. Install pdf2image
```bash
pip install pdf2image
```
### Step3. split pdf
We'll split your pdf file into small pdf files per page.  
Use pdf 24 tools (https://tools.pdf24.org/zh/split-pdf)  
You'll get a .zip dir file, unzip it and load it to your workdir ({workdir}/pdf).

### Step4. pdf to image
Because ndlocr-lite only recognizes image files, we need to convert the PDF pages into images.
```bash
python {workdir}/translate-jp/pdf2image.py
```

### Step5. image to text
```bash
cd {workdir}/ndlocr-lite/src
bash img2txt.sh
```

### Step6. merge txt
Merge the individual .txt files into a single, complete .txt file:
```bash
python mergetxt.py
```

### Step7. translate
You can use your own translate method. Here we'll use immersive translate (https://immersivetranslate.com/en/).  
1. Download the Immersive Translate extension for your browser.
2. Go to https://dash.immersivetranslate.com/#services
3. Choose 'Add Custom Translation Service' and confirm.
4. Add the Custom Translation Service (depending on the API you are using).
5. Fill in your API key and choose 'Paraphrase Expert' in the 'You can designate an AI expert to provide translation strategies:' option.
6. Click the 'verify service' button.
7. Go to https://app.immersivetranslate.com/ and choose Document Translation.
8. Upload your .txt file and you are done!

### Step8. clean (Optional)
The translated document may still contain issues, such as disorganized formatting and extraneous margin text, making further cleaning necessary.
```bash
pip install openai
python {workdir}/translate-jp/clean.py
```


