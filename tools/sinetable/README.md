# Sin wave table ROM生成用Pythonスクリプト

Sinの第一象限を1024サンプルでhexファイルに出力
分解能は24bit (Q1.23、値域 0〜2^23-1)

## 実行

```shell
uv run main.py
```

## 生成されるファイル

- sine_data.txt: sine_rom.verylの`SineRomData::TABLE`へコピーすること (`SineRomQuarter` / `SineRomQuarterDual`はこのテーブルを参照する)
