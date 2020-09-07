cd DeepLearningExamples/PyTorch/Transformer-XL \
  && pip install -r requirements.txt \
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
  && bash run_wt103_base_ngc.sh train 8 --config dgx1_8gpu_fp16  

