# Changelog

> 注: 0.5.0〜0.5.3の`SineWaveLerpCore`の誤差をcentで表していたが、これは波形の振幅誤差であり周波数誤差ではない。centは周波数比の単位なので、sine補間の誤差には使わない。正しくはLSB、フルスケール比、dBFSで評価する。以下の記述は訂正済み。dBFSはQ1.23フルスケール振幅2^23を0dBとしたピーク振幅比である。

## [0.5.3] - 2026-10-31

### Fixed

- `SineWaveLerpCore`の補間乗算を12bit×12bitへ戻した。`diff>>2`と`frac[19:8]`を使う
- GowinのMULT12X12はsigned 12×12のため、両オペランドから2048を引いて積を計算し、`2048*(a+b) - 2048^2`で補正することでunsigned 12×12を実現した
- 12bit unsignedを直接MULT12X12へ渡すと27×18へパディングされるが、signed primitive＋バイアス補正ならMULT12X12（0.5 DSPブロック）を維持できる
- Q4.23出力の最大振幅誤差は約5.5 LSB（フルスケール比 約0.66ppm、約-124dBFS）。公開ポート、レイテンシー、波形interfaceは変更なし

## [0.5.2] - 2026-10-31

### Fixed

- `SineWaveLerpCore`の補間乗算を11bit×11bitへ広げた。`diff>>3`と`frac[19:9]`を使い、Gowin GW5AでMULT12X12（0.5 DSPブロック）にマップされる
- 12bit×11bitおよび12bit×12bitは合成器が27×18へパディングするため、両オペランドを11bit以下にする必要があった
- Q4.23出力の最大振幅誤差は約11 LSB（フルスケール比 約1.3ppm、約-117dBFS）。公開ポート、レイテンシー、波形interfaceは変更なし

## [0.5.1] - 2026-10-31

### Fixed

- `SineWaveLerpCore`の補間乗算を11bit×10bitへ調整し、Gowin GW5AでMULT12X12（0.5 DSPブロック）にマップされるようにした。`diff>>3`と`frac[19:10]`を使う
- 0.5.0の12bit×12bitは合成器が27×18へパディングしており、DSP削減効果がなかった
- Q4.23出力の最大振幅誤差は約20 LSB（フルスケール比 約2.4ppm、約-112dBFS）。公開ポート、レイテンシー、波形interfaceは変更なし

## [0.5.0] - 2026-10-31

### Changed

- `SineWaveLerpCore`の補間乗算を27bit×18bitから12bit×12bitへ変更した。`diff>>2`と`frac[19:8]`を使う
- Gowin GW5Aの合成では12bit×12bitが27×18へパディングされ、DSP削減効果はなかった
- 12bit補間の最大振幅誤差は約6 LSB（フルスケール比 約0.7ppm、約-123dBFS）
- 12bit補間の期待値に合わせてnative testを更新した

## [0.4.3] - 2026-10-27

### Fixed

- `SineWaveLerpCore`のidx/fracをROM出力と同じ1段で遅延し、位相ジャンプ時に補間係数とROM addressがずれる問題を修正した
- `SuperSaw` exampleのQ4.23からQ8.24への変換を`$std::sign_extend`へ置き換え、native testでの符号拡張を修正した
- `SuperSaw` example内のLPF差分を1bit広く計算し、フルスケール符号反転時のwrapを修正した

### Added

- `SineWaveLerpCore`の位相ジャンプ時のpipeline整合testを追加した
- `examples/super_saw.veryl` とnative testを追加。7ボイスの非対称デチューンとLFSRジッターを含むSuperSAWのexample。ジッター用LPFはexample内の簡易実装

### Changed

- `PinkNoise`の行更新周期を実装に合わせて`2^(k+1)`サンプルごとと明記した
- `WhiteNoise`/`PinkNoise`のリセットなし動作とpower-up前提をdoc commentへ明記した

## [0.4.1] - 2026-10-09

### Changed

- 公開API・波形出力・latencyに変更なし（内部実装の整理のみ。ROM集約はGowin GW5A-25A合成でBSRAM数・INIT内容が集約前と一致することを確認済み）
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
