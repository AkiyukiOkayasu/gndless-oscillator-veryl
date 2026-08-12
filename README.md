# gndless_oscillator

NCOのphaseからsine、triangle、saw、square、white/pink noiseを生成します。公開APIは`SineWaveCore`、`SineWaveLerpCore`、`SineOscillator`、`SineOscillatorLerp`、`TriangleWaveCore`、`TriangleOscillator`、`SawWaveCore`、`SawOscillator`、`SquareWaveCore`、`PwmSquareOscillator`、`MultiWaveCore`、`MultiWaveOscillator`、`WhiteNoise`、`PinkNoise`、`WaveTypes`です。ROM moduleは内部APIです。

依存は`fixedpoint`と`nco`です。phase/phase stepは`gndless_nco::Phase`、波形出力は`gndless_fixedpoint::FixedPointValue::<gndless_fixedpoint::Q4_23>` interfaceです。サイン波ROMはQ1.23 (24bit) の第一象限テーブル (1024ワード) で、lerpの補間は27bit×18bit (Q1.17係数) 乗算です。内部演算はQ4.23ドメインのシフト・bit slice・加算のみで、`convert()`は使いません。oscillator wrapperは`gndless_nco::Phasor`の同期resetと`phase_rst`を使います。振幅、duty、noise seed/stateの契約は各module doc commentを正とします。

## レイテンシー契約 (phase入力 → audio出力)

各波形コアは自然なレイテンシーを持ち、遅延整列は行わない:

| module | レイテンシー |
|---|---|
| `SineWaveCore` / `SineOscillator` | 1クロック (BRAM読み出し) |
| `SineWaveLerpCore` / `SineOscillatorLerp` | 3クロック (ROM \| diff+係数 \| 乗算+加算のpipeline) |
| `TriangleWaveCore` / `TriangleOscillator` | 0クロック (組み合わせ) |
| `SawWaveCore` / `SawOscillator` | 0クロック (組み合わせ) |
| `SquareWaveCore` / `PwmSquareOscillator` | 0クロック (組み合わせ) |
| `WhiteNoise` / `PinkNoise` | 0クロック (更新と同時出力) |
| `MultiWaveCore` / `MultiWaveOscillator` | Sine: 3クロック、他: 0クロック (波形ごとに自然なレイテンシー) |

### 楽器用途ではレイテンシー差を気にする必要がない

本パッケージは連続的にオーディオを生成する楽器用オシレーターであり、レイテンシー差はすべて**定数遅延**として
現れる。定数遅延は音色に影響せず、波形切替時の位相ずれも最大3クロック分 (50MHz・20kHzで約0.4度、
440Hzで約0.01度) で可聴域外である。したがって:

- **全波形のレイテンシーを揃えるための遅延レジスタの追加は不要** (リソースの無駄になるだけ)
- 「レイテンシーが揃っていない」こと自体を修正対象にしないこと
- レイテンシーが意味を持つのはサンプル正確な外部同期が必要な用途のみで、その場合は利用側で明示的に遅延を挿入すること

```veryl
inst osc: oscillator::SineOscillator (...);
```

ROM生成ツールとchecked-in dataは`tools/sinetable/`にあります。検証: `veryl fmt --check && veryl check && veryl test && veryl build && veryl doc`。
