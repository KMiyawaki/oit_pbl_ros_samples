# oit_pbl_ros_samples

## Install

あらかじめ[oit_stage_ros](https://github.com/KMiyawaki/oit_stage_ros)の指示に従い、インストールしておくこと。

```shell
$ cd ~/catkin_ws/src
$ git clone https://github.com/KMiyawaki/oit_pbl_ros_samples.git
$ cd ~/catkin_ws && catkin_make
```

## 単純なナビゲーション

1. [oit_stage_ros](https://github.com/KMiyawaki/oit_stage_ros)のナビゲーションを起動する。
2. `rosrun oit_pbl_ros_samples simple_navigation.py`を実行すると、座標`(1.15, 2.42)`に向かい角度90度の方向を向いて停止する。

## Windows プログラムとの連携

### Windowsプログラムからロボットをコントロールする

[rosbridge_server](http://wiki.ros.org/rosbridge_server)を使い、WindowsからTCP/IPでROSトピックをパブリッシュする。  
ROSでそのトピックを受信し、データに応じてロボットの速度指令を送信する。  
[oit_stage_ros](https://github.com/KMiyawaki/oit_stage_ros)のマウステレオペを起動した状態で以下のコマンドを実行する。

```shell
rosrun oit_pbl_ros_samples control_from_win_sample_01.py
```

Windows側では次のリポジトリをクローンしておく。

- [win_rosclient_sample](https://github.com/KMiyawaki/win_rosclient_sample.git)

クローンした`win_rosclient_sample/win_rosclient_sample_01.py`を実行し、Windowsターミナルから`forward`、`back`、`left`、`right`などとコマンドを送るとロボットが動く。それ以外の文字列の場合は停止する。

### Windowsプログラムとメッセージを送受信する

WindowsからTCP/IPでROSトピックをパブリッシュする。また、ROSからパブリッシュしたトピックをWindowsで受信する。
Windows側では次のリポジトリをクローンしておく。

- [win_rosclient_sample](https://github.com/KMiyawaki/win_rosclient_sample.git)

[oit_stage_ros](https://github.com/KMiyawaki/oit_stage_ros)のナビゲーションを起動した状態で以下のコマンドを実行する。

```shell
rosrun oit_pbl_ros_samples communication_with_win_sample_01.py
```

5秒以内にWindowsターミナルから`win_rosclient_sample/communication_with_win_sample_01.py`を実行する。  
ロボットは座標`(1.15, 2.42)`に進んだ後、しばらくすると、Windows側ターミナルでROSからパブリッシュされたメッセージを受信する。

```shell
> python communication_with_ros_sample_01.py
{'topic': '/from_ros', 'msg': {'data': 'Hello! this is /communication_with_win_sample_01 0'}, 'op': 'publish'}
...
```

十回メッセージを送信するか20秒たつとWindowsからのメッセージ送信が始まり、ROS側で受信する。

```shell
$ ./communication_with_win_sample_01.py
[INFO] [1619573798.482099, 23.400000]: /communication_with_win_sample_01:Started
[INFO] [1619573814.455466, 39.400000]: Receive from win(0):Hello this is windows 2
[INFO] [1619573815.455155, 40.400000]: Receive from win(1):Hello this is windows 3
...
```

### 複数のWindowsプログラムとメッセージを送受信する

WindowsからTCP/IPでROSトピックをパブリッシュする。また、ROSからパブリッシュしたトピックをWindowsで受信する。  
ただし、Windows側ではプログラムを２つあらかじめ起動しておく。それぞれのWindowsプログラムとの通信に使うトピック名を個別に用意しておことでROS側からどのWindowsプログラムと通信するかを指定できる。
Windows側では次のリポジトリをクローンしておく。

- [win_rosclient_sample](https://github.com/KMiyawaki/win_rosclient_sample.git)

1. [oit_stage_ros](https://github.com/KMiyawaki/oit_stage_ros)のナビゲーションを起動する。
2. Windowsターミナル１で`win_rosclient_sample/play_with_ros_sample_01_rps.py`（じゃんけんの手を認識し、ロボットに結果を送信する）を実行する。
    - トピック`/from_windows_rps, /from_ros_rps`を使って通信する。
3. Windowsターミナル２で`win_rosclient_sample/play_with_ros_sample_01_b.py`（あっち向いてほいを模擬したもの）を実行する。
    - トピック`/from_windows_b, /from_ros_b`を使って通信する。
4. ROS側で`rosrun oit_pbl_ros_samples play_with_win_sample_01.py`を実行する。

ロボットは最初に`win_rosclient_sample/play_with_ros_sample_01_rps.py`とメッセージ通信し、じゃんけんを行う。  
その後座標`(1.15, 2.42)`に進んだ後、`win_rosclient_sample/play_with_ros_sample_01_b.py`とメッセージ通信し、あっち向いてほいを行う。  
最後に勝敗結果を表示して終了する。

#### 実行結果

- ROS側

```shell
$ rosrun oit_pbl_ros_samples play_with_win_sample_01.py
[INFO] [1620087276.042892, 105.700000]: /play_with_win_sample_01:Started
[INFO] [1620087276.205660, 105.800000]: /play_with_win_sample_01:The server move_base comes up
[INFO] [1620087276.629396, 106.300000]: /play_with_win_sample_01:Try to start game Rock, Paper, Scissors
[INFO] [1620087292.327971, 122.000000]: /play_with_win_sample_01:Receive from win:paper
[INFO] [1620087295.321705, 125.000000]: /play_with_win_sample_01:Robot selects 'paper'
[INFO] [1620087296.394480, 126.000000]: /play_with_win_sample_01:Receive from win:even
[INFO] [1620087297.324511, 127.000000]: Ouch!!
[INFO] [1620087297.327191, 127.000000]: /play_with_win_sample_01:Sending goal
[INFO] [1620087310.516897, 140.200000]: /play_with_win_sample_01:Finished: (3)
[INFO] [1620087310.520974, 140.200000]: /play_with_win_sample_01:Try to start game B
[INFO] [1620087319.585114, 149.200000]: /play_with_win_sample_01:Receive from win:up
[INFO] [1620087322.549679, 152.200000]: /play_with_win_sample_01:Robot selects 'left'
[INFO] [1620087323.644162, 153.300000]: /play_with_win_sample_01:Receive from win:lose
[INFO] [1620087324.660066, 154.300000]: Ouch!!
[INFO] [1620087324.662427, 154.300000]: /* GAME RESULTS */
[INFO] [1620087324.664652, 154.300000]: /* GAME (Rock, Paper, Scissors):Robot lose */
[INFO] [1620087324.666658, 154.300000]: /* GAME (B):Robot lose */
[INFO] [1620087324.669156, 154.300000]: /* ------------ */
[INFO] [1620087324.671986, 154.300000]: /play_with_win_sample_01:Exiting
```

- Windowsじゃんけんプログラム側

```shell
>python ./play_with_ros_sample_01_rps.py
Waiting ROS message...
Receive from ROS:Start your game!
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
finger 0-4: x o o o o | None
finger 0-4: x o o x x | scissors
finger 0-4: o o o o o | paper
[ WARN:0] global C:\Users\appveyor\AppData\Local\Temp\1\pip-req-build-wvn_it83\opencv\modules\videoio\src\cap_msmf.cpp (434) `anonymous-namespace'::SourceReaderCB::~SourceReaderCB terminating async callback
Sending ros message: {'op': 'publish', 'topic': '/from_windows_rps', 'msg': {'data': 'paper'}}
Sending ros message: {'op': 'publish', 'topic': '/from_windows_rps', 'msg': {'data': 'paper'}}
Sending ros message: {'op': 'publish', 'topic': '/from_windows_rps', 'msg': {'data': 'paper'}}
Sending ros message: {'op': 'publish', 'topic': '/from_windows_rps', 'msg': {'data': 'paper'}}
Receive from ROS:paper
Sending ros message: {'op': 'publish', 'topic': '/from_windows_rps', 'msg': {'data': 'even'}}
Sending ros message: {'op': 'publish', 'topic': '/from_windows_rps', 'msg': {'data': 'even'}}
Sending ros message: {'op': 'publish', 'topic': '/from_windows_rps', 'msg': {'data': 'even'}}
Sending ros message: {'op': 'publish', 'topic': '/from_windows_rps', 'msg': {'data': 'even'}}
```

- Windowsあっち向いてほいプログラム側

```shell
>python ./play_with_ros_sample_01_b.py
Receive from ROS:Start your game!
Sending ros message: {'op': 'publish', 'topic': '/from_windows_b', 'msg': {'data': 'down'}}
Sending ros message: {'op': 'publish', 'topic': '/from_windows_b', 'msg': {'data': 'down'}}
Sending ros message: {'op': 'publish', 'topic': '/from_windows_b', 'msg': {'data': 'down'}}
Receive from ROS:down
Sending ros message: {'op': 'publish', 'topic': '/from_windows_b', 'msg': {'data': 'win'}}
Sending ros message: {'op': 'publish', 'topic': '/from_windows_b', 'msg': {'data': 'win'}}
Sending ros message: {'op': 'publish', 'topic': '/from_windows_b', 'msg': {'data': 'win'}}
Sending ros message: {'op': 'publish', 'topic': '/from_windows_b', 'msg': {'data': 'win'}}
Sending ros message: {'op': 'publish', 'topic': '/from_windows_b', 'msg': {'data': 'win'}}
Sending ros message: {'op': 'publish', 'topic': '/from_windows_b', 'msg': {'data': 'win'}}
Sending ros message: {'op': 'publish', 'topic': '/from_windows_b', 'msg': {'data': 'win'}}
```
