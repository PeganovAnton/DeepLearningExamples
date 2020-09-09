for nmt in 0 1 2 3 4 6 9 13 19 28 42; do
    bash run_wt103_small_mem_tokens_simple_relative.sh train 8 \
        --config dgx1_8gpu_fp16 \
        --num_mem_tokens ${nmt} \
        --mem_len "$(expr 192 + ${nmt})"
done

