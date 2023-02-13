# twitter-search30d-streamlit: Twitter30日間検索&CSV保存のクライアントアプリ
Twitter 30days Search Client deployed with Streamlit.

Twitter API v1.1のPremium Searchを利用して、特定のキーワードで検索できるWebアプリ。
検索結果をDataFrameとしてアプリ上で閲覧でき、CSVファイルとして保存することが可能です。
デプロイ先としてはStreamlit Cloudを想定しています。

## アプリケーションのスクリーンショット

![CleanShot 2023-02-13 at 18 44 55](https://user-images.githubusercontent.com/5616593/218425048-433c1c68-ebd6-4c9a-b4ab-05fac191f55b.png)

![CleanShot 2023-02-13 at 18 45 10](https://user-images.githubusercontent.com/5616593/218425060-367d7d1f-84c2-4c07-aa0e-143ce946a6e6.png)

## 使い方
### Premium Searchを利用できるアクセス権を取得。（無料で利用できるSandbox推奨）
30days Searchを利用するにはPremium Searchを利用できるアクセス権が必要です。
[Twitter API Sandboxの作成・申請方法。30日間検索と全期間検索を無料で実行](https://scr.marketing-wizard.biz/dev/twitter-api-sandbox-apply)

### Streamlit Cloudでデプロイ
本リポジトリのファイルをStreamlit Cloudへデプロイしてください。
デプロイ設定時、メインファイルのパスはstreamlit_30d.pyを指定します。

### 秘密鍵の設定
Tweepyを介してTwitter API検索を行う際に利用するAPI keyを秘密鍵としてStreamlitのSecret設定で保存してください。
- 参考: [Tweepyで自動ツイート・自動いいねを実装する](https://scr.marketing-wizard.biz/dev/tweepy-autotweet-apiv1)
- 参考: [TweepyをTwitter API v2経由で利用する](https://scr.marketing-wizard.biz/dev/tweepy-twitter-apiv2)

下記を参考に秘密鍵を保存・設定してください。
- [Secrets management - Streamlit Docs](https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management)

## 技術・構成
Python v3.8で確認済。
### 使用ライブラリ
- Pandas
- Streamlit
- Tweepy
### 想定デプロイ先
Streamlit Cloud
