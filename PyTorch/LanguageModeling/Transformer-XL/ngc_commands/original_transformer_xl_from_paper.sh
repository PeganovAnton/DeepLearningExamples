cd DeepLearningExamples/PyTorch/LanguageModeling/Transformer-XL \
  && pip install -r requirements.txt \
  && pip install --no-cache-dir git+https://github.com/NVIDIA/dllogger.git#egg=dllogger \
  && mkdir -p data \
  && cd data \
  && wget --continue https://s3.amazonaws.com/research.metamind.io/wikitext/wikitext-103-v1.zip \
  && unzip -q wikitext-103-v1.zip \
  && cd wikitext-103 \
  && mv wiki.train.tokens train.txt \
  && mv wiki.valid.tokens valid.txt \
  && mv wiki.test.tokens test.txt \
  && cd ../.. \
  && cd pytorch \
  && bash run_wt103_orig_base.sh train 8 --config dgx1_8gpu_fp32 --work_dir /result 

