python ../extract_test_result_line.py \
  --files ../../../ngc_results/vary_num_mem_tokens_transformer_xl_mem_tokens_simple_relative/1436629/nmt_*/test.csv \
  --file_var_regex "nmt_([0-9]+)" \
  --file_var_name num_mem_tokens \
  --sort_column num_mem_tokens \
  --cols test_loss test_perplexity \
  --row_index 0 \
  --output ../../../ngc_results/vary_num_mem_tokens_transformer_xl_mem_tokens_simple_relative/1436629/test_results.csv
