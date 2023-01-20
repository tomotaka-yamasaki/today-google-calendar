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
$ today-google-calendar --help
Usage: today-google-calendar [OPTIONS]

Options:
  -i, --calendar-id TEXT          取得したいGoogleカレンダーID
  -d, --date [%Y-%m-%d|%Y/%m/%d]  予定の取得日 (yyyy-mm-dd or yyyy/mm/dd)
                                  default:Today
  -c, --copy-clipboard            クリップボードにコピーするかどうか
  --help                          Show this message and exit.
```

## Install
### 仮想環境構築
```zsh
$ pipenv install --dev
$ pipenv shell
```
### 環境変数設定
```zsh
$ cp src/today_google_calendar/config/.env.sample src/today_google_calendar/config/.env
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

## 実行
### Local
```zsh
$ python src/today_google_calendar/today_google_calendar.py
```

### pip install
```zsh
$ exit
$ pip install <path to pyproject.toml>
$ today-google-calendar
```
