# TODO

## 出力formatのQ4.23統一を検討する

`gndless_sample_rate_conversion`のmodule境界をQ4.23(±8.0、2^-23グリッド)へ統一したことに合わせ、`gndless_oscillator`の出力formatをQ8_24(±256、2^-24)からQ4.23へ変更するかを検討する。

- 変更する場合: 各wave coreの出力portとQ1.31→Q8.24変換をQ4.23へ変更し、既存testの期待値を更新する
- 判断材料: SRCチェーンとの境界変換コストと、Q8_24の±256レンジ(波形生成用headroom)が実際に必要か
