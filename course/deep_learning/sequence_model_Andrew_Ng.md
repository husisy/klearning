# Sequence model - Andrew Ng

## week1

1. reading material
   * [The Unreasonable Effectiveness of Recurrent Neural Networks - Andrej Karpathy](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
2. task
   * speech recognition
   * music generation
   * sentiment classification
   * DNA sequence analysis
   * machine translation
   * video activity recognition
   * name entity recognition
3. notation
   * $T_{x}^{\left( i \right)},\,\,T_{y}^{\left( i \right)}$
   * $x^{\left( i \right) \left< t \right>},\,\,y^{\left( i \right) \left< t \right>}$
   * $i$ denote index of all samples, $T$ denote length of each sample
4. vocabulary
   * size: ```30,0000~100,000```, more is also not uncommon
   * one-hot
   * ```<UNK>```
5. one-hot representation
   * inputs, outputs can be different lengths (useless padding)
   * doesn't share features learned across different position of texts
6. Recurrent Neural Networks
   * initial state
   * back propagation through time
   * $a^{\left< t \right>}=g\left( W_{aa}a^{\left< t-1 \right>}+W_{ax}x^{\left< t-1 \right>}+b_a \right)$
   * $y^{\left< t \right>}=h\left( W_{ya}a^{\left< t \right>}+b_y \right)$
7. RNN architectures
   * many to many (equal length): NER
   * many to many (equal length): machine translation
   * many to one: sentimental classification
   * one to many architecture: music generation
   * attention based architecture
8. Tokenize
   * ```<UNK>```
   * ```<EOS>```
   * punctuation
9. language model, generate sequence
10. character-level language model
    * no ```<UNK>```
    * long sequence
    * hard to catch long range dependence
11. RNN problem (vanish gradients)
    * hard to catch long range dependence. (从句). Mainly influenced by inputs that are close
12. exploding gradients (very deep neural networks): back-propagated gradients increase exponentially (using gradient clipping)
    * gradients vanishing tends to be the bigger problem, although exploding gradients happens in RNN
13. GRU [On the Properties of Neural Machine Translation: Encoder-Decoder Approaches](https://arxiv.org/abs/1409.1259)
    * relieve gradients vanishing problem
    * reset gate: $\Gamma_r=\sigma \left( W_r\left[ c^{\left< t-1 \right>},x^{\left< t \right>} \right] +b_r \right)$
    * update gate: $\Gamma_u=\sigma \left( W_u\left[ c^{\left< t-1 \right>},x^{\left< t \right>} \right] +b_u \right)$
    * candidate state: $\tilde{c}^{\left< t \right>}=\tanh \left( W_c\left[ \Gamma _r\ast c^{\left< t-1 \right>},x^{\left< t \right>} \right] +b_c \right)$
    * $c^{\left< t \right>}=\Gamma _u\ast \tilde{c}^{\left< t \right>}+\left( 1-\Gamma _u \right) \ast c^{\left< t-1 \right>}$
14. LSTM (Long Short Term Memory)
    * update gate: $\Gamma_u=\sigma \left( W_u\left[ c^{\left< t-1 \right>},x^{\left< t \right>} \right] +b_u \right)$
    * forget gate: $\Gamma_f=\sigma \left( W_f\left[ c^{\left< t-1 \right>},x^{\left< t \right>} \right] +b_f \right)$
    * output gate: $\Gamma_o=\sigma \left( W_o\left[ c^{\left< t-1 \right>},x^{\left< t \right>} \right] +b_o \right)$
    * candidate state: $\tilde{c}^{\left< t \right>}=\tanh \left( W_c\left[ c^{\left< t-1 \right>},x^{\left< t \right>} \right] +b_c \right)$
    * $c^{\left< t \right>}=\Gamma _u\ast \tilde{c}^{\left< t \right>}+\Gamma _f\ast c^{\left< t-1 \right>}$
    * peephole LSTM *TBA*
    * ```tf.nn.rnn_cell.LSTMCell``` *TBC*
15. bi-directional RNN v.s. unidirectional (forward directional) RNN
    * not suitable for speech recognition
16. deep RNN
    * three stacked RNN in common

## week2

1. one-hot representation
   * cannot generalize cross words
2. word embedding
3. t-SNE
4. transfer learning with word embedding from large unlabeled text corpus
5. word embedding suitable tasks
   * NER
   * text summarization
   * co-reference resolution
   * parsing
6. word embedding unsuitable tasks
   * language modeling
   * machine translation
   * word embedding from large unlabeled text corpus
7. relation to face encoding
   * Siamese networks: DeepFace: closing the gap to human level performance
8. word embedding property
   * word analogies: [Linguistic regularities in continuous space word representation](http://www.aclweb.org/anthology/N13-1090)
   * cosine similarity
9. context target pairs
   * language model: last 4 words
   * word embedding: 4 word on left & right; last 1 word; nearby 1 word (skip gram)
10. word2vec: [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781)
11. CBow (Continuous Bag Of Words)
12. sparse softmax
    * hierarchical softmax classifier
13. random sample context c: avoid frequently occurring words (cannot be uniformly at random)
14. negative sampling: [distributed representation of words and phrases and their compositionality](https://arxiv.org/abs/1310.4546)
    * k=5~20 for small dataset, 2~5 for larger dataset
    * (bad)sample according to token frequency: the, a, of, and
    * (bad)sample uniformly at random: non-representative of the distribution of English words
    * (heuristic) ```f^(3/4)```
15. Glove: [Global vectors for word representation](https://nlp.stanford.edu/projects/glove/)
16. sentiment analysis
17. debias word embedding: [Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings](https://arxiv.org/abs/1607.06520)

## week3

1. seq2seq
   * [sequence to sequence learning with neural networks](https://arxiv.org/abs/1409.3215)
   * [learning phrase representations using rnn encoder-decoder for statistical machine translation](https://arxiv.org/abs/1406.1078)
2. image caption
   * [deep captioning with multimodal recurrent neural networks](https://arxiv.org/abs/1412.6632)
   * [show and tell: neural image caption generator](https://arxiv.org/abs/1411.4555)
   * [deep visual semantic alignments for generating image descriptions](https://cs.stanford.edu/people/karpathy/cvpr2015.pdf)
3. machine translation: conditional language model
   * gready search
   * beam search
4. length normalization
   * $\frac{1}{T_{y}^{\alpha}}\sum_{t=1}^{T_y}{\log P\left( y^{\left< t \right>}|x,y^{\left< 1 \right>},...,y^{\left< t-1 \right>} \right)}$
   * B=1,3,10,100
   * error analysis: $P\left( y*|x \right) \,\,?\,\,P\left( \hat{y}|x \right) $
5. BLEU (bilingual evaluation understudy) score
   * [BLEU: a Method for Automatic Evaluation of Machine Translation](https://www.aclweb.org/anthology/P02-1040.pdf)
   * BP: brevity penalty
   * $P_n=\frac{\sum_{ngram\in \hat{y}}{count_{clip}\left( ngram \right)}}{\sum_{ngram\in \hat{y}}{count\left( ngram \right)}}$
   * $BLeu=BP\times \text{e}^{\left( p_1+p_2+p_3+p_4 \right) /4}$
6. attention: [neural machine translation by jointly learning to align and translate](https://arxiv.org/abs/1409.0473)
   * [show attend and tell neural image caption generation with visual attention](https://arxiv.org/abs/1502.03044)
7. speech recognition problem
   * phoneme
   * academic datasets: 300 hours
   * academia datasets: 3000 hours
   * commercial systems: 10000 hours - 100000 hours
   * CTC (Connectionist temporal classification) cost
   * [labelling unsegmented sequence data with recurrent neural networks](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.75.6306&rep=rep1&type=pdf)
8. trigger word detection
   * Amazon Echo (Alexa), Baidu DuerOS (xiaodunihao), Apple Siri (Hey Siri), Google Home (Okay Google)
