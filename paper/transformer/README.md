# transformer

1. link
   * attention is all you need [arxiv-link](https://arxiv.org/abs/1706.03762)
2. encoder由两部分组成：
   * multi-head self-attention
   * position-wise fully connected feed-forward network
3. decoder由三部分组成
   * multi-head self-attention, `attn_mask`保证时序依赖
   * multi-head attention over the encoder output
   * position-wise fully connected feed-forward network
4. position encoding
5. multi-head attention的亮点
   * `output_j`完全不依赖与`input_i`当`j<i`时，由`attn_mask`保证
   * query, key, value
   * additive attention还是dot-product (multiplicative) attention，文章使用了后者，faster and more space efficient (for highly optimized matrix multiplication)
   * 因子`sqrt(head_dim)`是为了防止softmax的输入值过于极端，进而梯度消失
   * 所谓`multi-head`，即代码中`num_head=8`，一方面压缩了计算量，将矩阵乘替换为直和
6. `embedding_layer`那儿缺少一个因子`sqrt(emb_dim)`，这个因子不能收入到初始化里去，如果收到初始化里去，会导致梯度差一个因子，进而收敛效果很糟糕
7. maximum path length
8. byte pair encoding (BPE)
9. vocab size: 37000 tokens
10. adam optimizer, `beta1=0.9, beta2=0.98, eps=1e-9`
11. learning rate decay
12. dropout `p=0.1`
13. label smoothing
14. wmt2014, English-German, `bleu=28.4`, 8P100, 3.5day
15. beam search

网络结构图 [processon-link](https://www.processon.com/view/link/60e6cb05f346fb3713c8c451)
