# EasyOCR Japanese Text Extractor

このリポジトリは、日本語を含む画像からテキストを抽出し、信頼度付きで出力するシンプルな OCR（光学式文字認識）スクリプトです。  
[EasyOCR](https://github.com/JaidedAI/EasyOCR) を活用しており、CLI（コマンドラインインターフェース）から画像ファイルと出力先ファイルを指定できます。

## ✅ 特徴

- 日本語に対応したOCR（英語も簡単に追加可能）
- 認識結果と信頼度をファイルに保存
- コンソールにもリアルタイム出力
- シンプルなPythonスクリプト、カスタマイズ容易

---

## 📦 インストール

Python 3.7以上を推奨します。

```bash
pip install easyocr
```
---

## 🚀 使い方

### 以下のように実行します：

```bash
python ocr_script.py --input input.png --output output.txt
```

- `--input`: OCRを行う入力画像ファイル
- `--output`: 認識結果を保存するテキストファイル

---

##📄 出力例

```
こんにちは（信頼度: 0.95）
ようこそ（信頼度: 0.89）
```

---

##📁 ファイル構成
```bash
.
├── LICENSE
├── ocr_script.py      # メインスクリプト
├── README.md          # 本ファイル
├── requirements.txt
├── sample.png         # 入力サンプル
└── sample.txt         # 出力サンプル
```

---

## ⚖️ ライセンス
このリポジトリは MIT [License](./LICENSE) のもとで公開されています。

---

## ⚠️ 補足

おそらくあまり正誤率が高くないかもしれません、

その場合は、出力したテキストを ChatGPT などで校正を行ってください。
（結構まともになりますが、最後は人で確認して下さい）