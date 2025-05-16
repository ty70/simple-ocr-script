# ==========================================================
# OCR Script using EasyOCR
#
# 概要:
#   日本語テキストを含む画像ファイルから文字を抽出し、
#   認識結果と信頼度を指定したテキストファイルに出力します。
#
# 入力:
#   コマンドライン引数で指定された画像ファイル (--input)
#
# 出力:
#   認識されたテキストとその信頼度を含むテキストファイル (--output)
#
# 使用例:
#   python ocr_script.py --input input.png --output output.txt
# ==========================================================

import easyocr
import argparse

def main():
    parser = argparse.ArgumentParser(description='OCR with EasyOCR')
    parser.add_argument('--input', required=True, help='Input image file (e.g., input.png)')
    parser.add_argument('--output', required=True, help='Output text file (e.g., output.txt)')
    args = parser.parse_args()

    reader = easyocr.Reader(['en','ja'])  # 英語＋日本語OCR
    results = reader.readtext(args.input)

    with open(args.output, 'w', encoding='utf-8') as f:
        for bbox, text, conf in results:
            line = f"{text}（信頼度: {conf:.2f}）\n"
            print(line, end='')  # コンソールにも出力
            text += '\n'
            f.write(text)

if __name__ == '__main__':
    main()
