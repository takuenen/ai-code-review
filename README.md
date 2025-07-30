# CodeSensei AI コードレビュー支援ツール（日本語）

📘 [🌐 English README is available here](./README_EN.md)

AIがコードの問題を発見し、品質を向上させます！


AIがコードの問題を発見し、品質を向上させます！  
Python と Java をサポートし、LangChain + Azure OpenAI を組み合わせて構築されています。

---

## ✨ 主な機能

* ✅ AIによるコードレビュー提案（日本語・中国語対応）
* ✅ 自動コメント生成
* ✅ 命名規則とコーディングスタイルのチェック（PEP8 / Java命名規則）
* ✅ 類似コードの推薦（RAG技術）
* ✅ 初心者モード（参考リンク + 練習問題付き）

---

## 🚀 クイックスタート

### 1️⃣ 依存ライブラリのインストール

Python バージョン：**3.11以上** を推奨

```bash
pip install -r requirements.txt
```

---

### 2️⃣ `.env` ファイルの設定

`.env.example` をコピーして `.env` にリネームし、以下の内容を記入：

```env
AZURE_OPENAI_API_KEY=あなたのAPIキー
AZURE_OPENAI_ENDPOINT=https://xxx.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT_CHAT=デプロイ名
AZURE_OPENAI_DEPLOYMENT_EMBEDDING=デプロイ名
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

---

### 3️⃣ アプリの起動

```bash
streamlit run main.py
```

ブラウザで `http://localhost:8501` にアクセスし、アプリを使用開始！

---

## 🗂️ プロジェクト構成

```plaintext
code-review-app/
├── main.py              # Streamlitアプリのメイン入口
├── utils.py             # ユーティリティ関数
├── review.py            # AIレビュー機能
├── comment_gen.py       # コメント自動生成機能
├── similar_code.py      # 類似コード推薦モジュール
├── vector_db.py         # ベクトルDB管理
├── requirements.txt     # 依存ライブラリ一覧
├── README.md            # 説明書
├── .env.example         # 環境変数テンプレート
├── revision_embedder.py # 埋め込み処理
└── style_check.py       # 命名とスタイルチェック機能
```

---

## 📚 参考リンク

* [LangChain 公式ドキュメント](https://python.langchain.com/)
* [Azure OpenAI 公式ドキュメント](https://learn.microsoft.com/azure/cognitive-services/openai/)
* [Streamlit 公式ドキュメント](https://docs.streamlit.io/)

---

## 🙋‍♀️ 作成者

プロジェクト責任者：タク
