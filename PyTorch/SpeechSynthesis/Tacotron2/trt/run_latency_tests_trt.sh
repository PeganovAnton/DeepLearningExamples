bash test_infer.sh --test trt/test_infer_trt.py \
     -bs 1 -il 128 -p fp16 --num-iters 1003 --encoder ./output/encoder_fp16.engine --decoder ./output/decoder_iter_fp16.engine --postnet ./output/postnet_fp16.engine  --waveglow ./output/waveglow_fp16.engine
bash test_infer.sh --test trt/test_infer_trt.py \
     -bs 1 -il 128 -p fp32 --num-iters 1003 --encoder ./output/encoder_fp32.engine --decoder ./output/decoder_iter_fp32.engine --postnet ./output/postnet_fp32.engine  --waveglow ./output/waveglow_fp32.engine
