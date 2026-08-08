# Changelog

## [Unreleased]

- 破壊的変更: 波形出力formatを`FixedPointValue::<Q8_24>`から`FixedPointValue::<Q4_23>`へ変更し、`gndless_sample_rate_conversion`等のmodule境界formatに統一
- 破壊的変更: `gndless_fixedpoint`依存を0.2.2 (Q4_23 preset追加) へ更新
- 公開moduleのparam/port doc commentを確認し、英語の公開説明を日本語へ整理
- doc commentの句点と体言止めの表記を整理
- 各testのdoc commentを検証目的が分かる表現へ統一
### Changed

- 破壊的変更: 公開moduleのQ8.24波形出力を`FixedPointValue::<Q8_24>` interfaceへ変更
- `gndless_fixedpoint`依存を0.2.0へ更新
- waveform/noise oscillatorを独立packageへ移動
- phase primitiveを`nco` packageへ移し、依存namespaceを明示
- fixedpoint format変換をflatなproject-scope `convert` APIへ移行
