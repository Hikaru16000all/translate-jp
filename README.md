# translate-jp
How to Translate Vertical Japanese PDF Books (Step-by-Step Guide)

## dependency  
### ndlocr-lite
https://github.com/ndl-lab/ndlocr-lite
### pdf2image
https://github.com/Belval/pdf2image
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
   '''
   conda create -n translate-jp python=3.12
   '''
### Step1. Download ndlocr-lite
