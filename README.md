# gndless_oscillator

NCOのphaseからsine、triangle、saw、square、white/pink noiseを生成します。公開APIは`SineWaveCore`、`SineWaveLerpCore`、`SineOscillator`、`SineOscillatorLerp`、`TriangleWaveCore`、`TriangleOscillator`、`SawWaveCore`、`SawOscillator`、`SquareWaveCore`、`PwmSquareOscillator`、`MultiWaveCore`、`MultiWaveOscillator`、`WhiteNoise`、`PinkNoise`、`WaveTypes`です。ROM moduleは内部APIです。

依存は`fixedpoint`と`nco`です。phase/phase stepは`gndless_nco::Phase`、波形出力は`gndless_fixedpoint::FixedPointValue::<gndless_fixedpoint::Q4_23>` interfaceです。全wave coreはphase入力からaudio出力まで**3クロックのレイテンシーに統一**されています。サイン波ROMはQ1.23 (24bit) の第一象限テーブル (1024ワード) で、lerpの補間は27bit×18bit (Q1.17係数) 乗算です。内部演算はQ4.23ドメインのシフト・bit slice・加算のみで、`convert()`は使いません。oscillator wrapperは`gndless_nco::Phasor`の同期resetと`phase_rst`を使います。振幅、duty、noise seed/stateの契約は各module doc commentを正とします。

```veryl
inst osc: oscillator::SineOscillator (...);
```

ROM生成ツールとchecked-in dataは`tools/sinetable/`にあります。検証: `veryl fmt --check && veryl check && veryl test && veryl build && veryl doc`。
