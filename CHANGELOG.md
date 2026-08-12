# Changelog

## [0.4.0]

- 破壊的変更: 各wave coreは自然なレイテンシーを持つ (sine LUT: 1クロック、lerp: 3クロック、他: 0クロック)。遅延整列は行わない (MultiWaveCoreの波形切替時はSineと他波形で位相が最大3クロックずれるが可聴域外)
- 破壊的変更: サイン波ROMをQ1.23 (1024×24bit) へ縮小。内部のQ1.31経由`convert()`を廃止し、全波形をQ4.23ドメインのシフト・bit sliceで直接生成
- 破壊的変更: lerpの補間乗算を27bit×18bit (Q1.17係数) へ縮小し、ROM | diff+係数 | 乗算+加算の3段pipeline化。90度端点のピーク平坦化 (10LSB) を解消
- fix: pink noiseの出力スケーリングを修正 (Q8.24→Q4.23変更時の`>>>16`を`>>>11`相当へ。設計比32倍の過減衰を解消)
- add: sine / multi_wave / noise のnative testを追加

## [0.3.0]

- 破壊的変更: 波形出力formatを`FixedPointValue::<Q8_24>`から`FixedPointValue::<Q4_23>`へ変更し、`gndless_sample_rate_conversion`等のmodule境界formatに統一
- 破壊的変更: `gndless_fixedpoint`依存を0.2.2 (Q4_23 preset追加) へ更新
- `gndless_nco`依存を0.2.0へ更新
- 公開moduleのparam/port doc commentを確認し、英語の公開説明を日本語へ整理
- doc commentの句点と体言止めの表記を整理
- 各testのdoc commentを検証目的が分かる表現へ統一

## [0.2.0]

- 破壊的変更: 公開moduleのQ8.24波形出力を`FixedPointValue::<Q8_24>` interfaceへ変更
- `gndless_fixedpoint`依存を0.2.0へ更新
- waveform/noise oscillatorを独立packageへ移動
- phase primitiveを`nco` packageへ移し、依存namespaceを明示
- fixedpoint format変換をflatなproject-scope `convert` APIへ移行
