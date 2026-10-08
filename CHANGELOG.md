# Changelog

## [Unreleased]

### Changed

- `gndless_fixedpoint` と `gndless_nco` の package をトップレベル import し、`FixedPointValue` / `Q4_23` / `Q1_23` / `Phase` / `Phasor` の完全修飾パスを短縮（Veryl 0.20.3 の namespace import 機能を使用）
- `gndless_fixedpoint` の project-scope function (`multiply` / `resize`) を import し、`sine` の補間乗算を全幅積と明示的な丸め (`resize`) へ整理。乗算・丸めを stage 2 の FF へ移動（Veryl 0.21 の project-scope function import 機能を使用）
- `SineRomQuarter` / `SineRomQuarterDual` に重複していたサイン波ROMテーブルを `SineRomData::TABLE` へ集約（Veryl 0.22 で simulator が package const 配列の初期化に対応したため）

## [0.4.0]

- 破壊的変更: 波形出力をQ4.23ドメインのシフト・bit slice・加算のみで直接生成する (Q1.31経由の`convert()`を廃止)
- 破壊的変更: サイン波ROMをQ1.23 (1024×24bit) へ縮小し、lerpの補間乗算を27bit×18bit (Q1.17係数) の3段パイプラインへ
- 破壊的変更: 各wave coreは自然なレイテンシー (sine LUT: 1クロック、lerp: 3クロック、他: 0クロック) を持ち、遅延整列は行わない
- fix: pink noiseの出力スケーリングを設計値 (÷8) に修正
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
