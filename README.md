# today-google-calendar
GoogleCalendarから一日の予定を取得し、整形して表示するためのCLI

```md
$ today-google-calendar
## 【スケジュール】本日の予定
- 09:00 ~ 11:00 : お買い物
- 12:00 ~ 13:00 : ランチ
- 14:00 ~ 16:00 : 映画
- 19:00 ~ 21:30 : 友達とご飯
```

## Usage
```zsh
$ today-google-calendar -h
usage: today-google-calendar [-h] [-i CALENDARID] [-d TODAY]

Googleカレンダーから予定を取得する

options:
  -h, --help            show this help message and exit
  -i CALENDARID, --calendarId CALENDARID
                        取得したいGoogleカレンダーID
  -d TODAY, --today TODAY
                        予定の取得日 yyyy-mm-dd default:Today
```

## Install
### 環境変数設定
```zsh
$ cp src/config/.env.sample src/config/.env
$ vim .env
```
* .env内に必要な情報を記述する
  * SA_KEY_PATH: credentials.json のディレクトリパス(today_google_calendar.pyからの相対パス)
  * CALENDAR_ID: 取得するカレンダーのID(Googleアカウント)
    * -i オプションで直接指定することもできる

### サービスアカウントキーの作成
* [サービスアカウントの作成と管理](https://cloud.google.com/iam/docs/creating-managing-service-accounts?hl=ja#creating_a_service_account)
  * credentials.json をダウンロードし、上で指定したSA_KEY_PATHに保存
* カレンダーアクセスに使用するため、サービスアカウントに当該カレンダーの変更権限を与える
  * Google Calendar 設定 > マイカレンダーの設定 > 特定のユーザとの共有 > ユーザーを追加

### pipインストール
```
$ pip3 install -e .
```
